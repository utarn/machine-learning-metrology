"""Tests for scripts/prebundle_offline.py (pure logic — no network).

Run: uv run python scripts/test_prebundle_offline.py
Follows the repo's smoke_test.py idiom (stdlib checks, pass/fail summary).
"""

import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prebundle_offline import (  # noqa: E402
    ESC50_MASTER,
    ESC50_ZIP_URL,
    esc50_done,
    esc50_extract,
    offline_env,
)

failures = []


def check(label, fn):
    try:
        fn()
        print(f"  OK   {label}")
    except Exception as exc:  # noqa: BLE001 - report any failure and continue
        failures.append((label, exc))
        print(f"  FAIL {label}: {exc}")


def test_esc50_done_false_on_empty(tmp):
    assert esc50_done(tmp) is False


def test_esc50_done_true_with_marker(tmp):
    marker = (tmp / "datasets" / "esc50" / ESC50_MASTER / "meta"
              / "esc50.csv")
    marker.parent.mkdir(parents=True)
    marker.write_text("filename,fold,target,src_file\n")
    assert esc50_done(tmp) is True


def test_esc50_extract_renames_inner_folder(tmp):
    # GitHub archive zips carry an inner "esc50-master/" folder; the
    # notebooks expect "ESC-50-master/" (with meta/esc50.csv) — the
    # extractor must lay it out at <root>/esc50/ESC-50-master/.
    inner = "esc50-master"
    zip_path = tmp / "master.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr(f"{inner}/meta/esc50.csv", "filename,fold,target\n")
        zf.writestr(f"{inner}/audio/1-100032-A-0.wav", "fake")
    esc50_extract(zip_path, tmp)
    assert (tmp / "datasets" / "esc50" / "ESC-50-master" / "meta"
            / "esc50.csv").exists()
    assert (tmp / "datasets" / "esc50" / "ESC-50-master" / "audio"
            / "1-100032-A-0.wav").exists()
    assert esc50_done(tmp) is True
    assert "github.com" in ESC50_ZIP_URL


def test_offline_env_points_into_datasets(tmp):
    env = offline_env(tmp)
    assert env["HF_HOME"] == str(tmp / "datasets" / "models" / "hf")
    assert env["EASYOCR_MODULE_PATH"] == str(
        tmp / "datasets" / "models" / "easyocr")
    assert env["MODEL_CACHE_DIR"] == str(
        tmp / "datasets" / "models" / "surya")
    assert env["TORCH_HOME"] == str(tmp / "datasets" / "models" / "torch")


def main():
    print("test_prebundle_offline.py")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        check("esc50_done false on empty root",
              lambda: test_esc50_done_false_on_empty(tmp))
        check("esc50_done true with meta/esc50.csv",
              lambda: test_esc50_done_true_with_marker(tmp))
        check("esc50_extract lays out ESC-50-master/",
              lambda: test_esc50_extract_renames_inner_folder(tmp))
        check("offline_env points into datasets/models/",
              lambda: test_offline_env_points_into_datasets(tmp))
    print()
    if failures:
        print(f"FAIL ({len(failures)}):")
        for label, exc in failures:
            print(f"  - {label}: {exc}")
        sys.exit(1)
    print("PASS — all prebundle logic checks passed")


if __name__ == "__main__":
    main()
