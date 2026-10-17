# Usage

## From Dolphin

1. Select one or more images.
2. Right-click, pick **Convert...**
3. Set your options, click **Convert**.

Output is written next to each source file with the new extension: `photo.jpg` becomes `photo.webp`. Converting to the same format as the source writes `photo.converted.jpg` so nothing is clobbered.

## From a terminal

```
kconvert photo1.jpg photo2.png
kconvert --version
```

Same dialog, same behaviour. Handy for testing.

## Options

| Option | What it does | Default |
|---|---|---|
| Target format | Output container | WebP |
| Quality | Lossy quality 1 to 100. Disabled for lossless formats | WebP 85, AVIF 60, JPEG 90 |
| Resize | Scale by percentage | 100 % |
| Max width | Cap width in px, keeps aspect, never upscales. 0 = off | off |
| Background | Transparent, White or Black. Transparent is greyed out for JPEG and BMP (no alpha) and falls back to White | Transparent |
| Strip metadata | Drops EXIF, ICC, XMP etc | on |
| Overwrite if target exists | Otherwise existing targets are skipped and reported | off |

## Multi-select

All selected files get the same settings. Failures do not stop the batch; you get a summary at the end listing which files failed and why.

## Exit codes

- `0` all converted, or dialog cancelled
- `1` one or more failures, or no files given, or `magick` not found

## Transparency

ImageMagick rasterises SVG and PDF onto white unless told otherwise, so kconvert always passes `-background` before the input. **Transparent** is the default for every format that supports alpha. Picking a colour flattens the image onto it, which is what you want when going to JPEG or when you need an opaque PNG.
