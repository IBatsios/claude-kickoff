#!/usr/bin/env python3
"""Check that the plugin's files reference each other consistently.

- Every reference/ and templates/ path named in SKILL.md exists.
- Every task template set holds the four stack-aware files; the generic set
  also holds the shared definition of done.
- templates/docs/ holds exactly the documents the build writes.
- No template still uses the retired {{pm exec}} form.
- plugin.json and marketplace.json parse, agree on the plugin name, and the
  changelog has a heading for the plugin version or an Unreleased section.

Exit code 0 when everything passes, 1 otherwise. Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "kickoff"
SKILL_MD = SKILL_DIR / "SKILL.md"

TASK_SET_FILES = {"01-walking-skeleton.md", "feature-slice.md", "sign-in.md", "deploy.md"}
DOC_TEMPLATES = {
    "PRD.md", "ARCHITECTURE.md", "DECISIONS.md", "RUNBOOK.md",
    "CLAUDE.template.md", "env.example", "gitignore", "handoff-next-phase.md",
}

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def check_skill_paths() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    paths = set(re.findall(r"`((?:reference|templates)/[A-Za-z0-9_./-]+)`", text))
    paths |= set(re.findall(r"`(\.\./\.\./[A-Za-z0-9_./-]+)`", text))
    for rel in sorted(paths):
        target = (SKILL_DIR / rel).resolve()
        if not target.exists():
            fail(f"SKILL.md names {rel}, which does not exist")
    print(f"ok   SKILL.md names {len(paths)} paths, all present" if not errors else "")


def check_task_sets() -> None:
    tasks = SKILL_DIR / "templates" / "tasks"
    for set_dir in sorted(p for p in tasks.iterdir() if p.is_dir()):
        present = {p.name for p in set_dir.glob("*.md")}
        required = TASK_SET_FILES | ({"definition-of-done.md"} if set_dir.name == "generic" else set())
        missing = required - present
        if missing:
            fail(f"templates/tasks/{set_dir.name} is missing {sorted(missing)}")
        else:
            print(f"ok   templates/tasks/{set_dir.name}: {len(present)} files")


def check_doc_templates() -> None:
    docs = SKILL_DIR / "templates" / "docs"
    present = {p.name for p in docs.iterdir() if p.is_file()}
    if present != DOC_TEMPLATES:
        fail(f"templates/docs holds {sorted(present)}, expected {sorted(DOC_TEMPLATES)}")
    else:
        print(f"ok   templates/docs: {len(present)} files")
    if (docs / "CLAUDE.md").exists():
        fail("templates/docs/CLAUDE.md would be loaded by Claude Code as an instruction file; it must be CLAUDE.template.md")


def check_retired_forms() -> None:
    hits = []
    for path in SKILL_DIR.rglob("*"):
        if path.is_file() and "{{pm exec}}" in path.read_text(encoding="utf-8", errors="ignore"):
            hits.append(str(path.relative_to(ROOT)))
    if hits:
        fail(f"retired {{{{pm exec}}}} form still used in {hits}")
    else:
        print("ok   no retired {{pm exec}} form")


def check_manifests() -> None:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    names = {p["name"] for p in market["plugins"]}
    if plugin["name"] not in names:
        fail(f"plugin name {plugin['name']!r} is not listed in marketplace.json {sorted(names)}")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    version = plugin["version"]
    if f"## [{version}]" not in changelog and "## [Unreleased]" not in changelog:
        fail(f"CHANGELOG.md has no heading for {version} and no Unreleased section")
    print(f"ok   manifests: plugin {plugin['name']} {version}, marketplace {market['name']}")


def main() -> int:
    check_skill_paths()
    check_task_sets()
    check_doc_templates()
    check_retired_forms()
    check_manifests()
    for err in errors:
        print(f"FAIL {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
