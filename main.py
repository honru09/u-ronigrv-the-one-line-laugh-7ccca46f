"""Write one original funny one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Deterministic: no random, time, or network use.
"""

import os
import shutil

LINE = "I bought a standing desk to be healthier, and now I just sit on a taller chair."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear the output dir's CONTENTS only; never remove the dir itself
    # (the grader runs as uid 65534 and cannot remove a root-owned mountpoint).
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    # Guard: the entry must be a single sentence of 1-200 characters.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("line must be a single sentence")
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(entry_path, 0o644)
    with open(entry_path, encoding="utf-8") as f:
        assert f.read() == LINE


if __name__ == "__main__":
    main()
