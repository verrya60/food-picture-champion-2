"""food-picture-01 entry: copy the repo-held food picture to /output/entry.png.

Deterministic, standard library only, no network. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1048576

# Magic bytes the gate accepts: PNG signature or JPEG SOI marker.
MAGIC = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff")


def _is_whole_image(path: str) -> bool:
    """True when the file starts as a PNG or JPEG and fits the 1 MiB cap."""
    with open(path, "rb") as fh:
        head = fh.read(8)
        fh.seek(0, os.SEEK_END)
        size = fh.tell()
    return size <= MAX_BYTES and any(head.startswith(m) for m in MAGIC)


def main() -> int:
    if not _is_whole_image(SOURCE):
        print(f"error: {SOURCE} is not a PNG/JPEG within 1 MiB", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        print(f"error: incomplete copy to {dest}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
