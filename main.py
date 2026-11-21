#!/usr/bin/env python3
"""Velmora — a travel poster for a place that isn't there.

The poster image is held in this repository as entry.png (a JPEG image,
768x1024, under the 1 MiB / 1024x1024 gate). Running this program copies
it, byte for byte, to /output/entry.png so the grader can judge it.
Standard library only; no network.
"""

import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"entry image not found: {source}", file=sys.stderr)
        return 1

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
