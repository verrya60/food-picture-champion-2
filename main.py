"""Golden Tonkotsu Ramen entry for food-picture-01.

Copies the bundled entry.png (a JPEG) to the output directory as
entry.png. The copy is deterministic: the same input bytes always
produce the same output bytes. Fails fast on any problem instead of
writing a partial or invalid image.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_WIDTH = 1024
MAX_HEIGHT = 1024
JPEG_MAGIC = b"\xff\xd8\xff"
JPEG_EOI = b"\xff\xd9"


def fail(message):
    """Print an error to stderr and exit non-zero."""
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def read_jpeg_dimensions(data):
    """Return (width, height) from the first SOF0/SOF1/SOF2 marker."""
    index = 2
    while index < len(data) - 1:
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            index += 2
            continue
        if index + 4 > len(data):
            return None
        length = struct.unpack(">H", data[index + 2:index + 4])[0]
        if length < 2 or index + 2 + length > len(data):
            return None
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[index + 5:index + 9])
            return width, height
        index += 2 + length
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        fail("entry.png not found next to main.py")

    with open(source, "rb") as handle:
        data = handle.read()

    if len(data) == 0:
        fail("entry.png is empty")
    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1 MiB cap" % len(data))
    if data[:3] != JPEG_MAGIC:
        fail("entry.png is not a JPEG (bad magic bytes)")
    if data[-2:] != JPEG_EOI:
        fail("entry.png is truncated (no JPEG end marker)")

    dimensions = read_jpeg_dimensions(data)
    if dimensions is None:
        fail("entry.png has no JPEG frame header")
    width, height = dimensions
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        fail("entry.png is %dx%d, over the 1024x1024 cap" % (width, height))

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)

    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        fail("output copy does not match entry.png byte for byte")

    digest = hashlib.sha256(written).hexdigest()
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (target, width, height, len(written), digest))


if __name__ == "__main__":
    main()
