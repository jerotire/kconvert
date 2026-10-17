# Tests

```
python -m pytest tests/
```

Needs `python-pytest` and `python-pyqt6`. Runs headless (offscreen Qt platform), no display required. These only exercise the argv builder; they never invoke `magick`.
