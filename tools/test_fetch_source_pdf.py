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
