---
title: "13.0.0 (2026-10-16)"
url: https://pillow.readthedocs.io/en/stable/releasenotes/13.0.0.html
hostname: readthedocs.io
description: "Security: CVE identifiers will be added to these entries as they are assigned. Critical: CVE 2026-96639, GHSA-v9pv-5gc8-w2m6: Stale native image storage reused after mode transitions, GHSA-5x8w-8jj..."
sitename: Pillow (PIL Fork)
date: "2026-07-01"
fingerprint: "1b8b98700d309ac9"
---
# 13.0.0 (2026-10-16)[¶](https://pillow.readthedocs.io#id1)

## Security[¶](https://pillow.readthedocs.io#security)

CVE identifiers will be added to these entries as they are assigned.

### Critical[¶](https://pillow.readthedocs.io#critical)

- [**CVE 2026-96639**](https://www.cve.org/CVERecord?id=CVE-2026-96639), [GHSA-v9pv-5gc8-w2m6](https://github.com/python-pillow/Pillow/security/advisories/GHSA-v9pv-5gc8-w2m6): Stale native image storage reused after mode transitions
- [GHSA-5x8w-8jj5-q52h](https://github.com/python-pillow/Pillow/security/advisories/GHSA-5x8w-8jj5-q52h), [GHSA-8g5g-8vmr-9782](https://github.com/python-pillow/Pillow/security/advisories/GHSA-8g5g-8vmr-9782): JPEG decoder buffer overflow from scanlines wider than tile extents

### High[¶](https://pillow.readthedocs.io#high)

- [**CVE 2026-96644**](https://www.cve.org/CVERecord?id=CVE-2026-96644), [GHSA-9v9v-9qvf-h2hj](https://github.com/python-pillow/Pillow/security/advisories/GHSA-9v9v-9qvf-h2hj): WMF/EMF heap out-of-bounds read from dimension truncation
- [**CVE 2026-96637**](https://www.cve.org/CVERecord?id=CVE-2026-96637), [GHSA-g842-9rc4-69pw](https://github.com/python-pillow/Pillow/security/advisories/GHSA-g842-9rc4-69pw): SPIDER decompression bomb bypass via seek()
- [**CVE 2026-96643**](https://www.cve.org/CVERecord?id=CVE-2026-96643), [GHSA-g4qv-2jxx-769h](https://github.com/python-pillow/Pillow/security/advisories/GHSA-g4qv-2jxx-769h): Unbounded Exif header replacement loop
- [**CVE 2026-96778**](https://www.cve.org/CVERecord?id=CVE-2026-96778), [GHSA-g7cr-3p24-7wf7](https://github.com/python-pillow/Pillow/security/advisories/GHSA-g7cr-3p24-7wf7): JPEG comment write after ICC profile fills encoder buffer
- [GHSA-462x-pgg6-55fp](https://github.com/python-pillow/Pillow/security/advisories/GHSA-462x-pgg6-55fp), [GHSA-c6hw-5grf-ff96](https://github.com/python-pillow/Pillow/security/advisories/GHSA-c6hw-5grf-ff96): TIFF tile and YCbCr decoding out-of-bounds read from undersized libtiff buffers
- [GHSA-p4wg-p73j-c528](https://github.com/python-pillow/Pillow/security/advisories/GHSA-p4wg-p73j-c528): PDF parsing stack exhaustion from long trailer chains and deep or cyclic page trees
- [**CVE 2026-96640**](https://www.cve.org/CVERecord?id=CVE-2026-96640), [GHSA-mrfp-p49p-3hf2](https://github.com/python-pillow/Pillow/security/advisories/GHSA-mrfp-p49p-3hf2): PDF append resource exhaustion from repeated page tree references
- [GHSA-pchr-8j38-3x4p](https://github.com/python-pillow/Pillow/security/advisories/GHSA-pchr-8j38-3x4p): TIFF encoder accepted an incorrectly sized Colormap for non-8-bit images
- [GHSA-332p-7hrc-92wf](https://github.com/python-pillow/Pillow/security/advisories/GHSA-332p-7hrc-92wf): TIFF encoder heap buffer overflow when saving to a file object
- [GHSA-xcvg-w56q-r89m](https://github.com/python-pillow/Pillow/security/advisories/GHSA-xcvg-w56q-r89m): TIFF encoder heap buffer overflow when tags override the image size
- [GHSA-xvh5-g6gv-559v](https://github.com/python-pillow/Pillow/security/advisories/GHSA-xvh5-g6gv-559v): TIFF encoder memory disclosure and crash from mismatched tag values
- [GHSA-q45j-58j2-45rg](https://github.com/python-pillow/Pillow/security/advisories/GHSA-q45j-58j2-45rg): TIFF decoding returned uninitialized memory for short JPEG strips
- [GHSA-78g4-xqwv-q3g8](https://github.com/python-pillow/Pillow/security/advisories/GHSA-78g4-xqwv-q3g8): Bundled OpenJPEG heap buffer overflow when reading tile-part data

### Medium[¶](https://pillow.readthedocs.io#medium)

- [GHSA-4rr5-89j8-mwwm](https://github.com/python-pillow/Pillow/security/advisories/GHSA-4rr5-89j8-mwwm): TIFF encoder use-after-free write
- [**CVE 2026-96636**](https://www.cve.org/CVERecord?id=CVE-2026-96636), [GHSA-p8hx-v2p6-rp84](https://github.com/python-pillow/Pillow/security/advisories/GHSA-p8hx-v2p6-rp84): MPO, DCX and MIC decompression bomb bypass via seek()
- [GHSA-f2g6-542v-9j58](https://github.com/python-pillow/Pillow/security/advisories/GHSA-f2g6-542v-9j58): PDF page tree stack exhaustion via cyclic `/Kids` reference
- [GHSA-5xm2-6676-qcp9](https://github.com/python-pillow/Pillow/security/advisories/GHSA-5xm2-6676-qcp9): APNG decompression bomb bypass via delayed disposal-frame sizing
- [**CVE 2026-96642**](https://www.cve.org/CVERecord?id=CVE-2026-96642), [GHSA-3j72-p6qg-6xp7](https://github.com/python-pillow/Pillow/security/advisories/GHSA-3j72-p6qg-6xp7): TarIO negative size field causes infinite CPU-spin loop
- [**CVE 2026-96638**](https://www.cve.org/CVERecord?id=CVE-2026-96638), [GHSA-24rc-8hj2-v98c](https://github.com/python-pillow/Pillow/security/advisories/GHSA-24rc-8hj2-v98c): BMP RLE decoder memory-amplification denial of service
- [GHSA-gg2r-wvfm-q9rx](https://github.com/python-pillow/Pillow/security/advisories/GHSA-gg2r-wvfm-q9rx): MSP RLE decoder expands a tiny file into unbounded memory
- [GHSA-wqgw-9xfh-qf2g](https://github.com/python-pillow/Pillow/security/advisories/GHSA-wqgw-9xfh-qf2g): TIFF and Exif IFD parsing memory and CPU amplification from shared tag data
- [GHSA-jg86-v3jv-hrpm](https://github.com/python-pillow/Pillow/security/advisories/GHSA-jg86-v3jv-hrpm): Quadratic time when writing many objects to a PDF
- [GHSA-254f-3936-288h](https://github.com/python-pillow/Pillow/security/advisories/GHSA-254f-3936-288h): PdfParser unbounded recursion via deeply nested objects
- [GHSA-rfgq-q3w2-pmv2](https://github.com/python-pillow/Pillow/security/advisories/GHSA-rfgq-q3w2-pmv2): Image.quantize() crash from an empty target palette
- [GHSA-xgh8-jp6q-p5x8](https://github.com/python-pillow/Pillow/security/advisories/GHSA-xgh8-jp6q-p5x8): XBM header parsing regular expression denial of service
- [GHSA-22hg-r758-rrw9](https://github.com/python-pillow/Pillow/security/advisories/GHSA-22hg-r758-rrw9), [GHSA-74r2-7ff9-mjj2](https://github.com/python-pillow/Pillow/security/advisories/GHSA-74r2-7ff9-mjj2), [GHSA-fc9g-5qg7-mf45](https://github.com/python-pillow/Pillow/security/advisories/GHSA-fc9g-5qg7-mf45): GIF comment handling quadratic-time blowup from repeated concatenation
- [GHSA-27h8-gf7j-v5hc](https://github.com/python-pillow/Pillow/security/advisories/GHSA-27h8-gf7j-v5hc): Out-of-bounds read in rank-based filters for zero-dimension images
- [**CVE 2026-96641**](https://www.cve.org/CVERecord?id=CVE-2026-96641), [GHSA-4rm8-3hmm-39fg](https://github.com/python-pillow/Pillow/security/advisories/GHSA-4rm8-3hmm-39fg): Integer underflow in PILfont text width calculation
- [GHSA-cp9v-662q-vvx9](https://github.com/python-pillow/Pillow/security/advisories/GHSA-cp9v-662q-vvx9): Image.merge() buffer overflow when merging 32-bit images as narrower bands
- [GHSA-j4m9-6w36-pw47](https://github.com/python-pillow/Pillow/security/advisories/GHSA-j4m9-6w36-pw47): Uninitialized glyph pointer freed on font rendering error path
- [GHSA-7mwm-ghpf-9vrm](https://github.com/python-pillow/Pillow/security/advisories/GHSA-7mwm-ghpf-9vrm): Double free in `Image.transform()` after an allocation failure
- [GHSA-4558-3h8r-v8xp](https://github.com/python-pillow/Pillow/security/advisories/GHSA-4558-3h8r-v8xp): `P;2L` and `P;4L` raw mode decoders read past the end of their input
- [GHSA-w889-685w-c8fh](https://github.com/python-pillow/Pillow/security/advisories/GHSA-w889-685w-c8fh): EPS filename argument injection into Ghostscript

### Low[¶](https://pillow.readthedocs.io#low)

- [GHSA-65qm-jvmh-6pqg](https://github.com/python-pillow/Pillow/security/advisories/GHSA-65qm-jvmh-6pqg): GIF decompression bomb check used a size discarded on failure
- [GHSA-vx6w-vv9f-6gvg](https://github.com/python-pillow/Pillow/security/advisories/GHSA-vx6w-vv9f-6gvg): EPS decompression bomb bypass via Ghostscript rendering
- [GHSA-58r4-6rv3-gfh8](https://github.com/python-pillow/Pillow/security/advisories/GHSA-58r4-6rv3-gfh8): ImageMorph.MorphOp.apply() out-of-bounds write on zero-width images

## Backwards incompatible changes[¶](https://pillow.readthedocs.io#backwards-incompatible-changes)

### Python 3.10[¶](https://pillow.readthedocs.io#python-3-10)

Pillow has dropped support for Python 3.10, which reached end-of-life in October 2026.

### Saving I mode images as PNG[¶](https://pillow.readthedocs.io#saving-i-mode-images-as-png)

In order to fit the 32 bits of I mode images into PNG, when PNG images can only contain at most 16 bits for a channel, Pillow has been clipping the values. Rather than quietly changing the data, this is now removed. Instead, the image can be converted to another mode before saving:

```
from PIL import Image
im = Image.new("I", (1, 1))
im.convert("I;16").save("out.png")
```
### Image.fromarray mode parameter[¶](https://pillow.readthedocs.io#image-fromarray-mode-parameter)

Using the `mode` parameter in [`fromarray()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.fromarray) was deprecated in
Pillow 11.3.0. In Pillow 12.0.0, this was partially reverted, and now the only
functionality removed is when the mode changes data types. Since pixel values do not
contain information about palettes or color spaces, the parameter can still be used to
place grayscale L mode data within a P mode image, or read RGB data as YCbCr for
example. If omitted, the mode will be automatically determined from the object’s shape
and type.

### Image.Image.get\_child\_images()[¶](https://pillow.readthedocs.io#image-image-get-child-images)

`Image.Image.get_child_images()` has been moved to
`ImageFile.ImageFile.get_child_images()`. The method uses an image’s file pointer,
and so child images could only be retrieved from an [`PIL.ImageFile.ImageFile`](https://pillow.readthedocs.io/reference/ImageFile.html#PIL.ImageFile.ImageFile)
instance.

### Image.\_show[¶](https://pillow.readthedocs.io#image-show)

`Image._show` has been removed. Use [`show()`](https://pillow.readthedocs.io/reference/ImageShow.html#PIL.ImageShow.show) instead.

### ImageCms.ImageCmsProfile.product\_name and .product\_info[¶](https://pillow.readthedocs.io#imagecms-imagecmsprofile-product-name-and-product-info)

`ImageCms.ImageCmsProfile.product_name` and the corresponding
`.product_info` attributes have been removed. They were set to `None` since Pillow
2.3.0.

## Deprecations[¶](https://pillow.readthedocs.io#deprecations)

### IM image format[¶](https://pillow.readthedocs.io#im-image-format)

The IM image format has been deprecated and removal is planned in Pillow 15.0.0 (2028-10-15). If you are using this format and would like to continue doing so, open an issue about what other software uses it.

### JpegImageFile.load\_djpeg[¶](https://pillow.readthedocs.io#jpegimagefile-load-djpeg)

`JpegImageFile.load_djpeg` has been deprecated, and will be removed in Pillow 14
(2027-10-15).

Use the built-in JPEG decoder instead, or call `djpeg` directly and decode the
resulting image with Pillow.

### ImageQt align8to32()[¶](https://pillow.readthedocs.io#imageqt-align8to32)

`ImageQt.align8to32()` has been deprecated. This was an undocumented helper function
intended for internal use, so there is no replacement.

## API changes[¶](https://pillow.readthedocs.io#api-changes)

### ImageColor.getcolor() with premultiplied alpha modes[¶](https://pillow.readthedocs.io#imagecolor-getcolor-with-premultiplied-alpha-modes)

When `mode` is `RGBa` or `La`, [`getcolor()`](https://pillow.readthedocs.io/reference/ImageColor.html#PIL.ImageColor.getcolor) now returns
color values premultiplied by the alpha channel, matching how pixels are stored in
those modes. Previously, the unmultiplied values were returned.

### Saving small ICO images[¶](https://pillow.readthedocs.io#saving-small-ico-images)

When saving an image smaller than 16x16 pixels as an ICO without a `sizes`
argument, the image’s own size is now used. Previously, none of the default sizes
matched, and an ICO containing no images was written. If no size in `sizes` fits
within the image, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError) is now raised.

## API additions[¶](https://pillow.readthedocs.io#api-additions)

### New resizing filters[¶](https://pillow.readthedocs.io#new-resizing-filters)

Two new filters are available for [`resize()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.resize) and
[`thumbnail()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.thumbnail): `Image.Resampling.MKS2013` and
`Image.Resampling.MKS2021`. These are versions of the Magic Kernel Sharp filter.

### Added `strip_namespaces` argument to `Image.getxmp()`[¶](https://pillow.readthedocs.io#added-strip-namespaces-argument-to-image-getxmp)

[`getxmp()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.getxmp) now accepts an optional keyword argument of
`strip_namespaces`. It is set to `True` by default, stripping each tag’s XML
namespace URI prefix as before. If set to `False`, each tag’s full
`{namespace-uri}local-name` form is kept instead, avoiding collisions between tags
that share a local name across different namespaces.

### Added `escape` argument to `PSDraw.text()`[¶](https://pillow.readthedocs.io#added-escape-argument-to-psdraw-text)

[`text()`](https://pillow.readthedocs.io/reference/PSDraw.html#PIL.PSDraw.PSDraw.text) now accepts a keyword-only boolean argument,
`escape`. Set it to `True` to escape backslashes, for example in Windows paths.
The default, `False`, preserves the existing handling of backslashes and PostScript
escape sequences.

### ImageOps invert, posterize and solarize of P images[¶](https://pillow.readthedocs.io#imageops-invert-posterize-and-solarize-of-p-images)

[`invert()`](https://pillow.readthedocs.io/reference/ImageOps.html#PIL.ImageOps.invert), [`posterize()`](https://pillow.readthedocs.io/reference/ImageOps.html#PIL.ImageOps.posterize) and
[`solarize()`](https://pillow.readthedocs.io/reference/ImageOps.html#PIL.ImageOps.solarize) now support P mode images. The operation is applied
to the palette colors, leaving any alpha values in the palette unchanged. Previously,
these functions raised [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError) for P mode.

### Path-like objects for font files[¶](https://pillow.readthedocs.io#path-like-objects-for-font-files)

[`load()`](https://pillow.readthedocs.io/reference/ImageFont.html#PIL.ImageFont.load), [`load_path()`](https://pillow.readthedocs.io/reference/ImageFont.html#PIL.ImageFont.load_path) and
[`save()`](https://pillow.readthedocs.io/PIL.html#PIL.FontFile.FontFile.save) now accept [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) objects,
such as [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path), in addition to strings.

## Other changes[¶](https://pillow.readthedocs.io#other-changes)

### Python 3.15[¶](https://pillow.readthedocs.io#python-3-15)

Pillow 12.3.0 had wheels built against Python 3.15 beta, available as a preview
to help projects prepare for 3.15, and to ensure Pillow could be used
immediately at the release of 3.15.0 final (2026-10-01, [**PEP 790**](https://peps.python.org/pep-0790/)).

Pillow 13.0.0 now officially supports Python 3.15.

### Faster import[¶](https://pillow.readthedocs.io#faster-import)

Importing Pillow takes around half the time it did in Pillow 12.3.0. `PIL.Image` no
longer imports `logging`, modules that are only needed for some operations, such as
`tempfile`, are now imported on first use, and on Python 3.15 Pillow also declares
`__lazy_modules__` to defer its remaining standard library imports ([**PEP 810**](https://peps.python.org/pep-0810/)). On an
Apple Silicon Mac, `from PIL import Image` took 24 ms on Python 3.14 and 23 ms on
Python 3.15 with Pillow 12.3.0, and now takes 12 ms and 10 ms.

### PyPy 3.12[¶](https://pillow.readthedocs.io#pypy-3-12)

Wheels are now also built for PyPy 3.12, in addition to PyPy 3.11.

### Faster JPEG 2000, TIFF, FreeType and LittleCMS in macOS and Linux wheels[¶](https://pillow.readthedocs.io#faster-jpeg-2000-tiff-freetype-and-littlecms-in-macos-and-linux-wheels)

Several of the libraries bundled in the macOS and Linux wheels were built without compiler optimisation. The Windows wheels were not affected.

These libraries are now compiled with `-O2`. Compared to Pillow 12.3.0, the wheels

- decode JPEG 2000 images 2 to 3 times faster and encode them about twice as fast,
- read and write LZW-compressed TIFF images about twice as fast,
- render text with [`ImageFont`](https://pillow.readthedocs.io/reference/ImageFont.html#module-PIL.ImageFont) up to 3 times faster, and
- apply [`ImageCms`](https://pillow.readthedocs.io/reference/ImageCms.html#module-PIL.ImageCms) transforms up to 3 times faster.

PNG, JPEG, WebP and AVIF are unaffected, as those libraries were already built with optimisation.

### Performance improvements[¶](https://pillow.readthedocs.io#performance-improvements)

Building on the optimizations in Pillow 12.3.0, more of the C code has been
restructured so that compilers can vectorize it. Compared to Pillow 12.3.0,
[`offset()`](https://pillow.readthedocs.io/reference/ImageChops.html#PIL.ImageChops.offset) is up to 46 times faster,
[`getbbox()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.getbbox) up to 24 times faster,
flipping and rotating by 180 degrees with
[`transpose()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.transpose) up to 10 times faster,
[`filter()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.filter) up to 3.5 times faster,
[`difference()`](https://pillow.readthedocs.io/reference/ImageChops.html#PIL.ImageChops.difference) up to 3 times faster, and converting P and PA
images to RGB and RGBA up to 2.5 times faster. Saving an optimized GIF with a shared
palette is around 6 times faster and uses less memory.

### Wheels now use HarfBuzz for hinting[¶](https://pillow.readthedocs.io#wheels-now-use-harfbuzz-for-hinting)

FreeType can use HarfBuzz to work out which glyphs a script covers, so that its auto-hinter can derive hinting “Blue Zones” for scripts such as Arabic.

Only the Windows wheels were actually built with this support.
The macOS wheels disabled HarfBuzz interoperability outright,
and the Linux wheels left it up to FreeType’s `configure`,
which in turn fell back to loading HarfBuzz by its unversioned name at
runtime.

Since the bundled copy of HarfBuzz is renamed when the wheel is audited and repaired
for distribution, that lookup only succeeded if a separate copy happened to be
installed on the system with the expected name (e.g. `libharfbuzz.so.0`).

All wheels are now linked against the HarfBuzz that Pillow ships, which may slightly change how text is rendered in scripts that rely on the auto-hinter.

### Thread safety for free-threaded Python[¶](https://pillow.readthedocs.io#thread-safety-for-free-threaded-python)

Critical sections now protect most operations on core image objects, such as conversion, pasting, filtering and pixel access, improving thread safety in the free-threaded build of Python. AVIF decoding also no longer blocks other threads.

### Resizing images with alpha[¶](https://pillow.readthedocs.io#resizing-images-with-alpha)

The `reducing_gap` argument to [`resize()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.resize) is now
applied to RGBA and LA images. Previously, these modes ignored the argument,
including when called by [`thumbnail()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.thumbnail), which uses
`reducing_gap=2.0` by default.

### Preserved transparency when padding or expanding images in ImageOps[¶](https://pillow.readthedocs.io#preserved-transparency-when-padding-or-expanding-images-in-imageops)

[`pad()`](https://pillow.readthedocs.io/reference/ImageOps.html#PIL.ImageOps.pad) and [`expand()`](https://pillow.readthedocs.io/reference/ImageOps.html#PIL.ImageOps.expand) now preserve the
`transparency` value from the source image’s `info` dictionary. Transparent
pixels in L, P and RGB images previously became opaque when a border was added.
New palette colors are allocated without using reserved transparency entries.

### Fixed reading FITS images with more than 8 bits per pixel[¶](https://pillow.readthedocs.io#fixed-reading-fits-images-with-more-than-8-bits-per-pixel)

FITS data is big-endian, but Pillow was reading 16-bit and 32-bit integer data, and 32-bit and 64-bit floating point data, in the native byte order. These images now load with the correct pixel values.

### Fixed accuracy of 16-bit image filters and conversions[¶](https://pillow.readthedocs.io#fixed-accuracy-of-16-bit-image-filters-and-conversions)

Applying a kernel filter to an `I;16` image gave incorrect results for pixel values
above 255, and converting an `I;16N` image to `I` or `F` clipped values to 255.
Both now preserve the full 16-bit range.

### Saving APNG frames with different palettes[¶](https://pillow.readthedocs.io#saving-apng-frames-with-different-palettes)

An APNG file can only contain a single palette. When saving P mode frames with different palettes, the image is now saved as RGB, or RGBA if any palette contains alpha, instead of writing the later frames with the wrong colors.

### Fixed ImageStat variance rounding[¶](https://pillow.readthedocs.io#fixed-imagestat-variance-rounding)

Fixed a floating-point rounding error that may have produced a negative variance in
[`var`](https://pillow.readthedocs.io/reference/ImageStat.html#PIL.ImageStat.Stat.var).

### Fixed ImageChops.offset() for 16-bit images[¶](https://pillow.readthedocs.io#fixed-imagechops-offset-for-16-bit-images)

[`offset()`](https://pillow.readthedocs.io/reference/ImageChops.html#PIL.ImageChops.offset) now works correctly for 16-bit-per-channel images.

### Fixed drawing on I;16B images[¶](https://pillow.readthedocs.io#fixed-drawing-on-i-16b-images)

When drawing on an `I;16B` image, some drawing methods wrote in the wrong byte order.
All drawing operations now use the byte order of the image mode.

### Fixed histograms for masked LA, La and PA images[¶](https://pillow.readthedocs.io#fixed-histograms-for-masked-la-la-and-pa-images)

When [`histogram()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.histogram) was given a mask for a two-band image (LA,
La or PA), the second band was incorrectly derived from the first band of the input
image, rather than the alpha band.

### Fixed exporting Arrow arrays from images with non-contiguous rows[¶](https://pillow.readthedocs.io#fixed-exporting-arrow-arrays-from-images-with-non-contiguous-rows)

Exporting an image as an Arrow array assumed that its rows were contiguous. However, this was not the case for

- images whose rows were padded to an alignment returned incorrect data,
- empty images,
- images created by [`frombuffer()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.frombuffer), and
- images memory-mapped from uncompressed files.

These images crashed instead.

Images with rows that are not contiguous now raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError), and the
others are exported correctly.

### Fixed combining GIF frames with missing durations[¶](https://pillow.readthedocs.io#fixed-combining-gif-frames-with-missing-durations)

Saving identical consecutive GIF frames no longer raises a `KeyError` when an earlier
frame has no duration and a later frame does.

### PNG palettes are no longer padded when saving with the `bits` argument[¶](https://pillow.readthedocs.io#png-palettes-are-no-longer-padded-when-saving-with-the-bits-argument)

When saving a `P` mode image as a PNG with the `bits` argument, Pillow used to pad
the `PLTE` chunk with zeroes up to `2 ** bits` entries. The `PLTE` chunk now only
contains as many entries as the image’s palette actually has, matching the behavior
already used when `bits` is not specified.

### Restore image position if ImageSequence.all\_frames() fails[¶](https://pillow.readthedocs.io#restore-image-position-if-imagesequence-all-frames-fails)

If processing a frame in [`all_frames()`](https://pillow.readthedocs.io/reference/ImageSequence.html#PIL.ImageSequence.all_frames) raises an exception,
the given image will now seek back to its original frame.

### Clean up TIFF encoders before closing their output files[¶](https://pillow.readthedocs.io#clean-up-tiff-encoders-before-closing-their-output-files)

TIFF saving now explicitly cleans up the libtiff encoder, including when saving raises an exception. Previously, delayed encoder destruction could access a closed file descriptor after it had been reused for another file, disturbing that file’s position or contents.

[`tobytes()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.tobytes) also now explicitly cleans up its encoder on
both success and failure, rather than relying on object destruction.

### Fixed reading PSD layers at the wrong file offset[¶](https://pillow.readthedocs.io#fixed-reading-psd-layers-at-the-wrong-file-offset)

When seeking to a layer of a PSD image, the pixel data was read from the wrong
position in the file, so [`seek()`](https://pillow.readthedocs.io/reference/Image.html#PIL.Image.Image.seek) returned unrelated
bytes reinterpreted as image data instead of that layer’s actual content.

### Fixed opening XBM images with comments[¶](https://pillow.readthedocs.io#fixed-opening-xbm-images-with-comments)

XBM images with C-style `/* ... */` comments in the header could not be identified.
Comments on separate lines before the bits declaration are now skipped.

### Clarified FriBiDi shim license[¶](https://pillow.readthedocs.io#clarified-fribidi-shim-license)

The SBOM published with Pillow 12.3.0 listed the vendored FriBiDi shim
(`src/thirdparty/fribidi-shim/`) as LGPL-2.1-or-later. The shim was written for
Pillow and is covered by Pillow’s MIT-CMU license. Its header declares the parts of
FriBiDi’s public API needed to load FriBiDi at runtime, and contains no FriBiDi code.
FriBiDi itself is not included in Pillow’s wheels.

The shim’s source files now include SPDX license identifiers, and the SBOM has been corrected.

### ImagePath.Path.compact() on an empty path[¶](https://pillow.readthedocs.io#imagepath-path-compact-on-an-empty-path)

[`compact()`](https://pillow.readthedocs.io/reference/ImagePath.html#PIL.ImagePath.Path.compact) is documented to return the number of
points removed. On a path with no points, it instead added a point whose
y coordinate was read from uninitialized memory, and returned `-1`.
`compact()` now leaves an empty path unchanged and returns `0`.
