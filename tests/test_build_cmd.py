"""Smoke tests for ConvertDialog.build_cmd. Runs headless via QT_QPA_PLATFORM=offscreen."""
import importlib.util
import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_loader(
    "kconvert",
    importlib.machinery.SourceFileLoader("kconvert", os.path.join(HERE, "..", "bin", "kconvert")),
)
kconvert = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kconvert)

from PyQt6.QtWidgets import QApplication  # noqa: E402

app = QApplication.instance() or QApplication(sys.argv)


def pick(dlg, ext):
    dlg.fmt.setCurrentIndex(dlg.fmt.findData(ext))


def test_webp_default(tmp_path):
    src = str(tmp_path / "a.jpg")
    open(src, "w").close()
    dlg = kconvert.ConvertDialog([src])
    pick(dlg, "webp")
    cmd, dst, err = dlg.build_cmd(src)
    assert err is None
    assert dst == str(tmp_path / "a.webp")
    assert cmd == ["magick", src, "-strip", "-quality", "85", dst]


def test_same_format_gets_converted_suffix(tmp_path):
    src = str(tmp_path / "a.png")
    open(src, "w").close()
    dlg = kconvert.ConvertDialog([src])
    pick(dlg, "png")
    cmd, dst, err = dlg.build_cmd(src)
    assert dst == str(tmp_path / "a.converted.png")
    assert "-quality" not in cmd
    assert "png:compression-level=9" in cmd


def test_existing_target_skipped_unless_overwrite(tmp_path):
    src = str(tmp_path / "a.jpg")
    dst = str(tmp_path / "a.webp")
    open(src, "w").close()
    open(dst, "w").close()
    dlg = kconvert.ConvertDialog([src])
    pick(dlg, "webp")
    cmd, _, err = dlg.build_cmd(src)
    assert cmd is None and err == "target already exists"
    dlg.overwrite.setChecked(True)
    cmd, _, err = dlg.build_cmd(src)
    assert err is None and cmd[-1] == dst


def test_resize_and_max_width(tmp_path):
    src = str(tmp_path / "a.jpg")
    open(src, "w").close()
    dlg = kconvert.ConvertDialog([src])
    pick(dlg, "jpg")
    dlg.strip.setChecked(False)
    dlg.resize_pct.setValue(50)
    dlg.max_w.setValue(1200)
    cmd, _, _ = dlg.build_cmd(src)
    assert "-strip" not in cmd
    assert cmd[cmd.index("-resize") + 1] == "50%"
    assert "1200x>" in cmd
