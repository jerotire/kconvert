# ImageConvert (kconvert)

Right-click any image in Dolphin, pick **Convert...**, choose a target format and a few dials, done.

Small PyQt6 dialog in front of ImageMagick. Nothing clever, nothing resident. Works on multi-select: one dialog, same settings applied to every file.

## Features

- Formats: WebP, AVIF, JPEG, PNG, GIF, TIFF, BMP, ICO
- Quality slider, only enabled for lossy formats, with per-format defaults
- Resize by percentage
- Max width cap (never upscales)
- Strip metadata (on by default)
- Overwrite toggle (off by default; existing targets are skipped and reported)
- Desktop notification on success, summary dialog on any failure

## Requirements

CachyOS / Arch, KDE Plasma 6, Dolphin.

```
sudo pacman -S --needed python-pyqt6 imagemagick libnotify
```

AVIF and WebP need `libavif` and `libwebp`; the Arch `imagemagick` package already depends on them.

## Install

```
./install.sh
```

Then restart Dolphin. See [docs/INSTALL.md](docs/INSTALL.md) for the manual steps and troubleshooting.

## Uninstall

```
./uninstall.sh
```

## Layout

```
bin/kconvert                          the script (PyQt6 dialog + magick runner)
share/kio/servicemenus/kconvert.desktop   Dolphin service menu entry
install.sh / uninstall.sh             user-level install into ~/.local
docs/                                 install, usage, extending, architecture notes
tests/                                smoke test for the magick command builder
```

## Docs

- [Install and troubleshooting](docs/INSTALL.md)
- [Usage](docs/USAGE.md)
- [Adding formats and dials](docs/EXTENDING.md)
- [Architecture](docs/ARCHITECTURE.md)

## Licence

MIT. See [LICENSE](LICENSE).
