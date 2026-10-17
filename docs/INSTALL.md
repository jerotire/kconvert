# Install

## Quick

```
sudo pacman -S --needed python-pyqt6 imagemagick libnotify
./install.sh
```

Restart Dolphin.

## Manual steps

1. `mkdir -p ~/.local/bin ~/.local/share/kio/servicemenus`
2. `cp bin/kconvert ~/.local/bin/kconvert`
3. `chmod +x ~/.local/bin/kconvert`
4. `cp share/kio/servicemenus/kconvert.desktop ~/.local/share/kio/servicemenus/`
5. `chmod +x ~/.local/share/kio/servicemenus/kconvert.desktop`
6. `kbuildsycoca6`
7. Restart Dolphin

## Troubleshooting

### Convert... does not appear in the menu

1. Service menu file must be executable. Plasma 6 silently ignores non-executable ones.
   `chmod +x ~/.local/share/kio/servicemenus/kconvert.desktop`
2. Rebuild the cache: `kbuildsycoca6`
3. Fully quit Dolphin (not just close the window): `pkill dolphin`
4. Check it is registered: `kbuildsycoca6 --noincremental 2>&1 | grep -i kconvert`

### Menu appears, nothing happens on click

1. Dolphin launches `kconvert` via `$PATH`. Check `~/.local/bin` is on the PATH that Plasma sees, not just your fish session.
   Fish: `set -Ua fish_user_paths ~/.local/bin` then log out and in.
   Or hardcode the path in the `.desktop` file: `Exec=/home/YOU/.local/bin/kconvert %F`
2. Run it from a terminal to see errors: `kconvert ~/Pictures/some.jpg`

### "No module named PyQt6"

`sudo pacman -S python-pyqt6`. If you use mise or pyenv, make sure the shebang resolves to the system Python: `head -1 ~/.local/bin/kconvert` should give `/usr/bin/env python3` and `which python3` in a plain login shell should be `/usr/bin/python3`. If it points at a mise shim, change the shebang to `#!/usr/bin/python3`.

### AVIF or WebP conversion fails

Check the delegates are compiled in:

```
magick -list format | grep -iE 'avif|webp|heic'
```

Arch's `imagemagick` includes them. If not, install `libavif` and `libwebp`.

### Wayland dialog placement

The dialog is a plain top-level window so KWin places it per your window rules. If you want it centred on the active screen, add a window rule in System Settings for window class `kconvert`.
