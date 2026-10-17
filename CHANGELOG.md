# Changelog

## 0.2.0 - 2026-10-17

- Fix: SVG and other transparent sources were rasterised onto white. `-background none` is now passed before the input.
- Add Background option: Transparent (default), White, Black. Transparent is disabled for JPEG and BMP.

## 0.1.0 - 2026-10-17

- Initial release
- Dolphin service menu for `image/*`
- PyQt6 dialog: format, quality, resize %, max width, strip metadata, overwrite
- Formats: WebP, AVIF, JPEG, PNG, GIF, TIFF, BMP, ICO
- `install.sh` / `uninstall.sh` for user-level install
