#!/usr/bin/env python3
"""Static quality checks for the public research portfolio.

Checks tracked Python source syntax, local Markdown links, expected files,
and basic credential patterns. This is not a full privacy or provenance audit.
"""
from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "docs/RESEARCH_OVERVIEW.md",
    "docs/GRIDWORLD_FINDINGS.md",
    "docs/RESEARCH_CLAIMS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/RESEARCH_ROADMAP.md",
    "evidence/gridworld/README.md",
    "evidence/gridworld/identifiability_enumeration.csv",
    "evidence/gridworld/table2_reaggregated.csv",
    "tools/verify_gridworld_enumeration.py",
    "tests/test_gridworld_evidence.py",
    ".github/workflows/gridworld-evidence.yml",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\n]+)\)")
CREDENTIAL_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,})\b"),
    "API token": re.compile(r"\bsk-[A-Za-z0-9_-]{30,}\b"),
}


def check() -> list[str]:
    problems: list[str] = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            problems.append(f"Required file missing: {name}")

    result = subprocess.run(
        ["git", "ls-files", "-z"], check=True, cwd=ROOT, capture_output=True
    )
    tracked = [ROOT / item.decode("utf-8")
               for item in result.stdout.split(b"\x00") if item]

    for path in tracked:
        rel = path.relative_to(ROOT)
        if not path.is_file():
            problems.append(f"Tracked file missing: {rel}")
            continue

        if path.suffix.lower() not in {".py", ".md", ".json", ".yaml", ".yml", ".txt", ".toml"}:
            continue

        try:
            contents = path.read_text(encoding="utf-8")
        except UnicodeError:
            problems.append(f"Text encoding error: {rel}")
            continue

        if path.suffix == ".py":
            try:
                ast.parse(contents, filename=str(rel))
            except SyntaxError as e:
                problems.append(f"Python syntax error in {rel}: {e}")

        for label, regex in CREDENTIAL_PATTERNS.items():
            if regex.search(contents):
                problems.append(f"Potential {label} in {rel}")

        if path.suffix != ".md":
            continue

        for match in LINK_RE.finditer(contents):
            url = match.group(1).strip().strip("<>").split(" ", 1)[0]
            if not url or url.startswith(("#", "https://", "http://", "mailto:")):
                continue
            relative_target = unquote(url.split("#", 1)[0].split("?", 1)[0])
            if relative_target and not (path.parent / relative_target).exists():
                problems.append(f"Broken Markdown link: {rel} -> {url}")

    print(f"Checked {len(tracked)} tracked files.")
    for issue in problems:
        print("FAIL:", issue)
    if not problems:
        print("PASS: required files, Python parsing, relative links, and common credential patterns.")
    print("Scope: static check only; not a historical privacy audit or simulator reproduction.")
    return problems


if __name__ == "__main__":
    sys.exit(bool(check()))
