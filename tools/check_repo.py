"""Basic Nebula repository sanity checks."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

ignored = {".git", ".venv", "__pycache__"}
problems = []

for path in ROOT.rglob("*"):
    if any(part in ignored for part in path.parts):
        continue
    if path.is_file() and path.stat().st_size == 1:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if text.strip() == "":
            problems.append(f"empty placeholder file: {path.relative_to(ROOT)}")

required = [
    "README.md",
    "ARCHITECTURE.md",
    "NEBULA_SPEC.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/copilot-instructions.md",
]

for rel in required:
    if not (ROOT / rel).exists():
        problems.append(f"missing required file: {rel}")

if problems:
    print("\n".join(problems))
    sys.exit(1)

print("Nebula repository sanity checks passed.")
