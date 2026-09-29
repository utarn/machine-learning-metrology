"""Make a learner ZIP snapshot from a git ref.

Usage:
    uv run python tools/make_learner_zip.py [--ref TAG_OR_SHA] [--out DIR]

Produces ``ml-metrology-learner-<ref>.zip`` per the packaging decision
(wayfinder #11 → #13): everything in the repo tree at <ref> EXCEPT

- all ``solution.ipynb`` files (instructor's answer key)
- the capstone exemplar ``day3/capstone/capstone_C_drift_predictor_solution.ipynb``
- ``docs/agents/`` (repo tooling docs, not learner material)
- ``tools/`` and ``smoke_test.py`` stay IN — learners verify their setup too.

The learner README is the repo's root ``README.md`` (committed, so it rides
in every ZIP automatically). Datasets, notebooks, environment files all stay.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

EXCLUDE_EXACT = {
    "day3/capstone/capstone_C_drift_predictor_solution.ipynb",
}
EXCLUDE_PREFIXES = ("docs/agents/", "tools/")
EXCLUDE_NAMES = {"solution.ipynb"}


def repo_files(ref: str) -> list[str]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "-z", ref],
        check=True, capture_output=True, text=True,
    ).stdout
    return [f for f in out.split("\0") if f]


def is_learner_file(path: str) -> bool:
    p = PurePosixPath(path)
    return (
        path not in EXCLUDE_EXACT
        and not any(path.startswith(pref) for pref in EXCLUDE_PREFIXES)
        and p.name not in EXCLUDE_NAMES
    )


def blob(ref: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "cat-file", "blob", f"{ref}:{path}"],
        check=True, capture_output=True,
    ).stdout


def make_zip(ref: str, out_dir: Path) -> tuple[Path, int]:
    files = [f for f in repo_files(ref) if is_learner_file(f)]
    out_path = out_dir / f"ml-metrology-learner-{ref}.zip"
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(files):
            z.writestr(f"ml-metrology/{f}", blob(ref, f))
    return out_path, len(files)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ref", default="HEAD", help="git tag or SHA to snapshot")
    ap.add_argument("--out", type=Path, default=Path.cwd(), help="output directory")
    args = ap.parse_args()

    # ยืนยันว่า ref มีอยู่จริงก่อนเขียนไฟล์
    subprocess.run(["git", "rev-parse", "--verify", args.ref], check=True,
                   capture_output=True)
    out_path, n = make_zip(args.ref, args.out)
    print(f"written: {out_path} ({n} files from {args.ref})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
