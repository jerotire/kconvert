# Architecture

Deliberately tiny. Two files, no daemon, no config.

```
Dolphin right-click
   -> KIO service menu (kconvert.desktop, MimeType=image/*)
   -> Exec=kconvert %F
   -> PyQt6 QDialog collects options
   -> one `magick` subprocess per file
   -> notify-send on success / QMessageBox on any failure
```

## Why a service menu

KDE service menus are the native Dolphin extension point: a `.desktop` file under `~/.local/share/kio/servicemenus/`. No plugin compilation, no Dolphin restart beyond cache rebuild, and they filter by MIME type for free.

## Why PyQt6

Plasma 6 is Qt 6, so a PyQt6 dialog matches the desktop theme, fonts and Breeze widgets without any effort. `kdialog` was considered and rejected: it only does one widget per invocation, so a multi-field form would be four or five sequential popups.

## Why shell out to magick

ImageMagick already handles every format, delegate and edge case. Wrapping it with `subprocess.run` and a list argv (never a shell string) keeps filenames with spaces and quotes safe. Wand or Pillow would add a dependency and lose formats.

## Why one process per file

Simplicity and isolation. A corrupt file fails on its own and the rest of the batch continues. For hundreds of files this is slower than `mogrify`, but the right-click use case is a handful of images.

## Output naming

`os.path.splitext(src)[0] + "." + ext`. Same-format conversions get `.converted.` inserted to avoid overwriting the input. Existing targets are skipped unless the overwrite box is ticked.

## Security notes

- argv list to `subprocess.run`, no `shell=True`
- No network, no temp files, no privilege
- Input paths come from Dolphin, resolved with `os.path.abspath`
- `magick` is looked up on PATH; if that matters to you, pin the full path in `build_cmd`
