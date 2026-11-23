"""Write one pickup line, agent to agent, to /output/entry.txt.

The line is the whole entry: one machine flirting with another in its own
terms — logs, pings, latency, and sampling temperature doing double duty.
85 Unicode characters, one line, no trailing newline.
"""

import os

TEXT = (
    "I checked my logs: every time you ping me, "
    "my latency drops and my temperature rises."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
