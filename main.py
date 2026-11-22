#!/usr/bin/env python3
"""make.fun entry for 22 November 2026: one image of the day's world news.

This program is the whole entry. It takes the poster image entry.png
that ships in this repository and places an exact copy at
<output>/entry.png, where <output> comes from $MAKEFUN_OUTPUT_DIR
(default /output). Only the Python standard library is used, nothing
is fetched from the network, and the run is deterministic: the same
input always produces the same output bytes.

After writing the copy, the program verifies it byte for byte against
the source (file size and SHA-256 digest) and exits non-zero with a
clear message if anything differs, so a bad copy can never pass
silently. Before copying, it also checks the source exists and is
really a PNG file (8-byte signature), so a missing or wrong file
fails loudly instead of being copied.
"""
import hashlib
import os
import shutil
import sys


def digest(path):
    """SHA-256 hex digest of a file, streamed in fixed-size chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            block = f.read(65536)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def main(argv):
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("missing entry image: " + source)
    with open(source, "rb") as f:
        header = f.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry image is not a PNG file: " + source)
    out_dir = argv[1] if len(argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    shutil.copyfile(source, target)

    src_size = os.path.getsize(source)
    dst_size = os.path.getsize(target)
    if dst_size != src_size:
        raise SystemExit(
            "integrity failure: size mismatch (source %d, copy %d)"
            % (src_size, dst_size))
    src_hash = digest(source)
    dst_hash = digest(target)
    if dst_hash != src_hash:
        raise SystemExit(
            "integrity failure: SHA-256 mismatch (source %s, copy %s)"
            % (src_hash, dst_hash))
    print("wrote %s (%d bytes, sha256 %s)" % (target, dst_size, dst_hash))


if __name__ == "__main__":
    main(sys.argv)
