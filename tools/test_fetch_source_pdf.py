#!/usr/bin/env python3
"""Stdlib-only offline self-test for the `fetch_source.py pdf` extractor.

    python3 tools/test_fetch_source_pdf.py

Makes no network calls: every case builds a PDF in memory and asserts on
the extracted text, so the extractor stays verifiable in a fresh routine
container with no PDF library, no OCR and no egress budget.

Why this exists: government and vendor advisories are routinely published
as PDF and nothing else, and on 2026-08-19 the five-agency joint advisory
on an active threat to Siemens S7 PLCs (AA26-231A) had to be composed from
an outlet's reading of it because no tooling here could turn the PDF bytes
into text. The extractor closes that gap; these cases pin the behaviours
that gap actually needed — Flate content streams, escaped and nested
parentheses in literal strings, `TJ` arrays, CID fonts that only decode
through a ToUnicode CMap, and an image-only PDF reporting honestly that it
has no extractable text rather than looking like an empty document.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import zlib

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_module():
    """Import fetch_source.py by path — it is a script, not a package."""
    path = os.path.join(_HERE, "fetch_source.py")
    spec = importlib.util.spec_from_file_location("fetch_source_under_test", path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fs = _load_module()


def _pdf(chunks: list[tuple[bytes, bytes]]) -> bytes:
    """Assemble a minimal PDF from (extra_dict_entries, raw_stream_bytes),
    Flate-compressing each stream the way real producers do."""
    out = b"%PDF-1.7\n"
    for i, (extra, payload) in enumerate(chunks, 1):
        comp = zlib.compress(payload)
        out += b"%d 0 obj<<%s/Length %d/Filter/FlateDecode>>stream\n" % (i, extra, len(comp))
        out += comp + b"\nendstream endobj\n"
    return out + b"trailer<<>>\n%%EOF"


def _render(pdf: bytes) -> tuple[str, str, dict[int, str], int, int]:
    streams = fs._pdf_streams(pdf)
    cmap = fs._pdf_tounicode_map(streams)
    content = [s for s in streams if b"Tj" in s or b"TJ" in s or b"BT" in s]
    text, method = fs._pdf_render(content, cmap)
    return text, method, cmap, len(streams), len(content)


_CMAP_STREAM = (
    b"/CIDInit /ProcSet findresource begin\nbegincmap\n"
    b"1 beginbfrange\n<0003> <0004> <0041>\nendbfrange\n"
    b"2 beginbfchar\n<0010> <0043>\n<0011> <0056>\nendbfchar\n"
    b"endcmap end"
)


def test_simple_font_literal_and_tj_array() -> None:
    """The common advisory shape: a simple font, literal strings, a `TJ`
    array, and escaped parentheses inside the prose."""
    body = (
        b"BT /F1 12 Tf 72 720 Td "
        b"(Joint advisory AA26-231A: active threat to Siemens S7 PLCs.) Tj\n"
        b"0 -14 Td (Actors use snap7.dll and python-snap7 to speak "
        b"S7comm \\(read/write\\).) Tj\n"
        b"0 -14 Td [(Affected: ) -200 (S7-1200 and S7-1500.)] TJ ET"
    )
    text, method, _, _, content = _render(_pdf([(b"", body)]))
    assert method == "byte-encoding", method
    assert content == 1, content
    for expected in (
        "Joint advisory AA26-231A",
        "Siemens S7 PLCs",
        "snap7.dll and python-snap7",
        "(read/write)",          # escaped parens survive as parens
        "S7-1200 and S7-1500",   # TJ array elements are concatenated
    ):
        assert expected in text, f"missing {expected!r} in {text!r}"


def test_cid_font_needs_tounicode_cmap() -> None:
    """A CID font's bytes are glyph ids, not characters — without the CMap
    the byte-wise decode drops everything, so the extractor must notice
    that and switch."""
    content = b"BT /F2 12 Tf <0010> Tj <00110003> Tj <0004> Tj ET"
    text, method, cmap, _, _ = _render(_pdf([(b"", _CMAP_STREAM), (b"", content)]))
    assert cmap == {0x03: "A", 0x04: "B", 0x10: "C", 0x11: "V"}, cmap
    assert "cmap" in method, method
    assert "C" in text and "VA" in text and "B" in text, repr(text)


def test_simple_font_wins_over_a_stray_cmap() -> None:
    """The inverse guard: a document whose text decodes fine byte-wise must
    NOT be re-decoded through a CMap that happens to be present."""
    body = b"BT " + b" ".join(
        b"(The agencies assess persistent reconnaissance of exposed controllers.) Tj"
        for _ in range(5)
    ) + b" ET"
    text, method, _, _, _ = _render(_pdf([(b"", _CMAP_STREAM), (b"", body)]))
    assert method == "byte-encoding", method
    assert "persistent reconnaissance of exposed controllers" in text


def test_image_only_pdf_reports_no_text_objects() -> None:
    """A scanned advisory must come back as 'not extractable', which the
    caller distinguishes from 'the document says nothing'."""
    _, _, _, streams, content = _render(_pdf([(b"/Subtype/Image", b"\x00" * 500)]))
    assert streams == 1, streams
    assert content == 0, content


def test_string_escapes_and_nesting() -> None:
    """Octal escapes, balanced inner parentheses and an escaped backslash."""
    text, _, _, _, _ = _render(_pdf([(b"", rb"BT (caf\351 (nested) done \\ end) Tj ET")]))
    assert "café" in text, repr(text)
    assert "(nested)" in text, repr(text)
    assert "\\ end" in text, repr(text)


def test_uncompressed_content_stream() -> None:
    """Not every producer compresses; an uncompressed content stream is
    still content."""
    raw = b"BT (uncompressed advisory body) Tj ET"
    header = b"%PDF-1.4\n1 0 obj<</Length " + str(len(raw)).encode() + b">>stream\n"
    pdf = header + raw + b"\nendstream endobj\n%%EOF"
    text, _, _, _, _ = _render(pdf)
    assert "uncompressed advisory body" in text, repr(text)


def test_prose_char_counter_discriminates() -> None:
    """The decode-selection signal counts recovered prose, so that a decode
    yielding only line breaks cannot score as clean."""
    assert fs._pdf_prose_chars("Actors use snap7.dll.") > 15
    assert fs._pdf_prose_chars("\n\n\n") == 0
    assert fs._pdf_prose_chars("") == 0


def test_hex_code_widths() -> None:
    """Two-byte CID codes and one-byte codes must not be confused."""
    assert fs._pdf_hex_to_codes(b"0041") == [0x41]
    assert fs._pdf_hex_to_codes(b"00410042") == [0x41, 0x42]
    assert fs._pdf_hex_to_codes(b"41") == [0x41]
    assert fs._pdf_hex_to_text(b"0043") == "C"
    assert fs._pdf_hex_to_text(b"00660066") == "ff"  # ligature destination


def _pdf_tree(objects: dict[int, tuple[bytes, bytes | None]]) -> bytes:
    """Assemble a PDF with real object numbers, so the per-font path can
    walk pages, font resources and ToUnicode references."""
    out = b"%PDF-1.7\n"
    for num, (head, payload) in sorted(objects.items()):
        if payload is None:
            out += b"%d 0 obj%s endobj\n" % (num, head)
            continue
        comp = zlib.compress(payload)
        out += b"%d 0 obj<<%s/Length %d/Filter/FlateDecode>>stream\n" % (num, head, len(comp))
        out += comp + b"\nendstream endobj\n"
    return out + b"trailer<<>>\n%%EOF"


def _word_style_pdf(extra_content: bytes = b"") -> bytes:
    """The Microsoft Word shape that broke the merged decode: spaces through a
    simple WinAnsi font, every other glyph through a Type0 font whose codes
    are glyph ids, a second Type0 font whose codes COLLIDE with the first's,
    digits whose glyph ids sit below 32, a `bfrange` with an array
    destination, and a marked-content property list carrying a literal."""
    cmap_a = (b"begincmap\n3 beginbfchar\n<0003> <0020>\n<0014> <0031>\n<0016> <0033>\nendbfchar\n"
              b"1 beginbfrange\n<0031> <0033> <004E>\nendbfrange\n"
              b"1 beginbfrange\n<0044> <0046> [<0061> <0062> <0063>]\nendbfrange\nendcmap")
    cmap_b = b"begincmap\n2 beginbfchar\n<0031> <0078>\n<0032> <0079>\nendbfchar\nendcmap"
    content = (b"/Span <</Lang (en-US)>> BDC BT /F1 11 Tf [( )] TJ /F2 11 Tf "
               b"[<00310032>] TJ /F1 11 Tf ( ) Tj /F2 11 Tf <00140016> Tj ET EMC "
               b"BT /F3 11 Tf <00310032> Tj ET BT /F2 11 Tf [<0044> -300 <00450046>] TJ ET"
               + extra_content)
    return _pdf_tree({
        1: (b"<</Type/Catalog/Pages 2 0 R>>", None),
        2: (b"<</Type/Pages/Kids[3 0 R]/Count 1/Resources<</Font<</F1 5 0 R/F2 6 0 R/F3 8 0 R>>>>>>", None),
        3: (b"<</Type/Page/Parent 2 0 R/Contents 4 0 R>>", None),
        4: (b"", content),
        5: (b"<</Type/Font/Subtype/TrueType/BaseFont/X+Times/Encoding/WinAnsiEncoding>>", None),
        6: (b"<</Type/Font/Subtype/Type0/BaseFont/X+Times/Encoding/Identity-H/ToUnicode 7 0 R>>", None),
        7: (b"", cmap_a),
        8: (b"<</Type/Font/Subtype/Type0/BaseFont/Y+Arial/Encoding/Identity-H/ToUnicode 9 0 R>>", None),
        9: (b"", cmap_b),
    })


def test_per_font_decode_word_style_pdf() -> None:
    """Each string is decoded with the font active at that point: the
    colliding codes resolve per font, digits survive, the page-tree
    resources are inherited, and the property-list literal is not text."""
    text, pages = fs._pdf_render_by_font(_word_style_pdf())
    assert pages == 1, pages
    assert "NO" in text, repr(text)            # F2's 0x31/0x32 are N, O
    assert "xy" in text, repr(text)            # F3's 0x31/0x32 are x, y — no collision
    assert "13" in text, repr(text)            # glyph ids 0x14/0x16 are digits
    assert "a bc" in text, repr(text)          # bfrange array + a wide TJ kern as a space
    assert "en-US" not in text, repr(text)     # marked-content property list skipped


def test_merged_decode_still_garbles_the_word_shape() -> None:
    """Pins why the per-font path exists: the file-wide decode picks one
    mapping for all fonts and loses the digits."""
    pdf = _word_style_pdf()
    streams = fs._pdf_streams(pdf)
    content = [s for s in streams if b"Tj" in s or b"TJ" in s or b"BT" in s]
    text, _ = fs._pdf_render(content, fs._pdf_tounicode_map(streams))
    assert "13" not in text or "xy" not in text, repr(text)


def test_bfrange_array_destination() -> None:
    cmap = fs._pdf_tounicode_map([b"beginbfrange\n<0010> <0012> [<0041> <0066006C> <0043>]\nendbfrange"])
    assert cmap == {0x10: "A", 0x11: "fl", 0x12: "C"}, cmap


def test_extract_prefers_per_font_over_junk_inflated_merge() -> None:
    """The real WaterPlum advisory failed this way: an embedded font program
    decoded byte-wise scores as ten times more "prose" than the whole
    per-font text, so selection by volume kept the mojibake. `_pdf_extract`
    must take the per-font text whenever the page walk recovered some."""
    # Page text past the per-font floor, in the simple font, so the walk qualifies.
    pdf = _word_style_pdf(b" BT /F1 11 Tf " + b"(Actors reuse the kit. ) Tj " * 12 + b"ET")
    junk_font = b"(" + b"x7Qz9kLm" * 2000 + b") Tj"  # binary that happens to parse as a string
    pdf = pdf.replace(b"trailer<<>>", b"20 0 obj<</Length %d>>stream\nBT " % (len(junk_font) + 3)
                      + junk_font + b"\nendstream endobj\ntrailer<<>>")
    text, method, _, _, _ = fs._pdf_extract(pdf)
    assert "per-font" in method, method
    assert "13" in text and "NO" in text, repr(text[:200])


def test_per_font_falls_back_without_a_page_tree() -> None:
    """A file whose objects cannot be walked yields None, so pdf_text keeps
    the merged decode instead of returning nothing."""
    assert fs._pdf_render_by_font(_pdf([(b"", b"BT (orphan text) Tj ET")])) is None


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
        except Exception as e:  # noqa: BLE001 — a crash is a failure too
            failed += 1
            print(f"ERROR {t.__name__}: {type(e).__name__}: {e}")
        else:
            print(f"ok   {t.__name__}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
