"""Pre-download all offline course material into datasets/.

Run (internet machine, once):
    uv run python scripts/prebundle_offline.py            # all steps
    uv run python scripts/prebundle_offline.py --only esc50
    uv run python scripts/prebundle_offline.py --force    # re-download

Everything lands under ``datasets/`` (gitignored — not tracked in the
repo because it is ~2.7 GB). Student machines get it by copying the
``datasets/`` folder from the instructor's machine (USB/LAN) or by
running this script themselves during prep. The notebooks point at
these paths themselves (they set HF_HOME / EASYOCR_MODULE_PATH /
MODEL_CACHE_DIR / TORCH_HOME in their setup cells when the datasets/
copies exist).

Steps (each is skipped if already present, idempotent otherwise):
    esc50         ESC-50 audio ~600 MB (CC BY-NC 3.0 — classroom use)
    fashion_mnist Fashion-MNIST ~60 MB via torchvision
    hf            thai-trocr ~0.4 GB + timm wide_resnet50_2 ~130 MB
    easyocr       EasyOCR craft + thai ~90 MB
    surya         Surya layout + table-rec ~0.5 GB (Datalab weights —
                  check their terms before redistributing further)
    torchhub      MobileNetV3-Small ImageNet weights ~10 MB

Cross-platform (Windows/macOS/Linux): stdlib download + lazy imports of
the heavy libraries, which must be installed first (uv sync).
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATASETS = BASE / "datasets"
MODELS = DATASETS / "models"

ESC50_ZIP_URL = "https://github.com/karoldvl/ESC-50/archive/master.zip"
ESC50_MASTER = "ESC-50-master"

LICENSE_NOTES = (
    "License notes:",
    "  - ESC-50 is CC BY-NC 3.0 — classroom use only, no commercial"
    " redistribution.",
    "  - Surya weights are hosted by Datalab — verify their terms"
    " before redistributing beyond this course.",
)


def offline_env(base: Path) -> dict[str, str]:
    """Env vars pointing every model library at datasets/models/."""
    return {
        "HF_HOME": str(base / "datasets" / "models" / "hf"),
        "EASYOCR_MODULE_PATH": str(base / "datasets" / "models" / "easyocr"),
        "MODEL_CACHE_DIR": str(base / "datasets" / "models" / "surya"),
        "TORCH_HOME": str(base / "datasets" / "models" / "torch"),
    }


def esc50_done(base: Path) -> bool:
    """True if datasets/esc50/ESC-50-master/meta/esc50.csv exists."""
    return (base / "datasets" / "esc50" / ESC50_MASTER / "meta"
            / "esc50.csv").is_file()


def esc50_extract(zip_path: Path, base: Path) -> None:
    """Extract a GitHub ESC-50 archive zip into datasets/esc50/.

    GitHub archive zips carry an inner folder named after the default
    branch (e.g. ``esc50-master/``); the notebooks expect
    ``ESC-50-master/`` — rename whatever single top-level folder the
    zip contains.
    """
    target = base / "datasets" / "esc50"
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target) as td:
        tmp = Path(td)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp)
        entries = [p for p in tmp.iterdir() if p.is_dir()]
        if len(entries) != 1:
            raise RuntimeError(
                f"expected exactly one top-level folder in the ESC-50"
                f" archive, found {[p.name for p in entries]}")
        src = entries[0]
        dst = target / ESC50_MASTER
        if dst.exists():
            shutil.rmtree(dst)
        src.rename(dst)


def step_esc50(base: Path, force: bool) -> str:
    if esc50_done(base) and not force:
        return "already present"
    zip_path = base / "datasets" / "esc50-master.zip"
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"    downloading {ESC50_ZIP_URL} (~600 MB) ...")
    urllib.request.urlretrieve(ESC50_ZIP_URL, zip_path)
    esc50_extract(zip_path, base)
    zip_path.unlink()
    return "downloaded"


def step_fashion_mnist(base: Path, force: bool) -> str:
    from torchvision.datasets import FashionMNIST

    root = base / "datasets" / "fashion_mnist"
    # download=True is idempotent: loads from disk when already present.
    train = FashionMNIST(root=root, train=True, download=True)
    FashionMNIST(root=root, train=False, download=True)
    return f"ready ({len(train)} train images)"


def step_hf(base: Path, force: bool) -> str:
    from huggingface_hub import snapshot_download
    from transformers import TrOCRProcessor, VisionEncoderDecoderModel

    snapshot_download("timm/wide_resnet50_2.racm_in1k")
    TrOCRProcessor.from_pretrained("openthaigpt/thai-trocr")
    VisionEncoderDecoderModel.from_pretrained("openthaigpt/thai-trocr")
    return "thai-trocr + wide_resnet50_2 cached"


def step_easyocr(base: Path, force: bool) -> str:
    import easyocr

    easyocr.Reader(["th", "en"], gpu=False, verbose=False)
    return "craft_mlt_25k + thai_g2 cached"


def step_surya(base: Path, force: bool) -> str:
    from surya.layout import LayoutPredictor
    from surya.table_rec import TableRecPredictor

    LayoutPredictor()
    TableRecPredictor()
    return "layout + table-rec cached"


def step_torchhub(base: Path, force: bool) -> str:
    import torchvision.models as tvm

    tvm.mobilenet_v3_small(
        weights=tvm.MobileNet_V3_Small_Weights.IMAGENET1K_V1)
    return "MobileNetV3-Small ImageNet weights cached"


STEPS = [
    ("esc50", step_esc50),
    ("fashion_mnist", step_fashion_mnist),
    ("hf", step_hf),
    ("easyocr", step_easyocr),
    ("surya", step_surya),
    ("torchhub", step_torchhub),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only", metavar="STEP", choices=[name for name, _ in STEPS],
        help="run a single step instead of all")
    parser.add_argument(
        "--force", action="store_true",
        help="re-run even if the material is already present")
    args = parser.parse_args()

    for key, value in offline_env(BASE).items():
        os.environ[key] = value

    failed: list[tuple[str, Exception]] = []
    for name, fn in STEPS:
        if args.only and name != args.only:
            continue
        print(f"[{name}]")
        try:
            print(f"    {fn(BASE, args.force)}")
        except Exception as exc:  # noqa: BLE001 - keep going, report all
            failed.append((name, exc))
            print(f"    FAILED: {exc}")

    print()
    for line in LICENSE_NOTES:
        print(line)
    if failed:
        print(f"\nDONE with {len(failed)} failure(s):")
        for name, exc in failed:
            print(f"  - {name}: {exc}")
        return 1
    print("\nDONE — datasets/ is pre-bundled for offline use.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
