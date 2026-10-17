# Extending

## Adding a format

Each format is one entry in the `FORMATS` dict near the top of `bin/kconvert`:

```python
"ext": ("Label", has_quality, default_quality, has_alpha, [extra, magick, args]),
```

1. `ext` is the output extension and what ImageMagick uses to pick the encoder.
2. `Label` is what shows in the combo box.
3. `has_quality` enables the slider.
4. `default_quality` is what the slider jumps to when this format is picked.
5. `has_alpha` controls whether Transparent is offered as a background.
6. Extra args are appended verbatim before the output path.

Examples:

```python
"jxl":  ("JPEG XL", True, 80, True, []),
"heic": ("HEIC", True, 70, True, []),
"pdf":  ("PDF", False, 0, True, []),
```

## Adding a background colour

One line in `BACKGROUNDS`: `"Label": "<any magick colour>"`, e.g. `"Drake": "#1a1612"`.

Check the encoder is available first: `magick -list format | grep -i jxl`.

## Adding a dial

Dials are plain Qt widgets added in `ConvertDialog.__init__` and read in `build_cmd`. Pattern:

1. Create the widget, add it with `form.addRow("Label", widget)`.
2. In `build_cmd`, read its value and append the matching `magick` args.
3. If it only applies to some formats, toggle `setEnabled` in `on_fmt`.

Ideas that fit the existing shape:

- Rotate / auto-orient: `-auto-orient`
- Colourspace: `-colorspace sRGB`
- Lossless WebP toggle: `-define webp:lossless=true`
- Output to a subfolder instead of beside the source

## Changing the menu

`share/kio/servicemenus/kconvert.desktop`:

- `MimeType=image/*;` controls when the entry shows. Narrow it (`image/jpeg;image/png;`) or add `application/pdf;` if you add a PDF path.
- `X-KDE-Priority=TopLevel` puts it in the main menu. Remove it to nest under **Actions**.
- `%F` passes all selected files as separate args. `%f` would pass only the first.

After editing, run `kbuildsycoca6` and restart Dolphin.

## Remembering last-used settings

Not implemented. If wanted, `QSettings("skycmd", "kconvert")` is the idiomatic route; read in `__init__`, write in `accept`.
