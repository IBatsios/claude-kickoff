#!/usr/bin/env python3
"""Validate the intake frontmatter of the blank form and every fixture.

The blank form at skills/kickoff/templates/intake.md is the schema: its
frontmatter defines the key structure. Every fixture must have exactly the
same keys, carry the plugin's version, satisfy the required-field rules from
skills/kickoff/reference/checks.md (mirrored here; keep them in step), and set
every conventions field so no fixture depends on a machine's defaults file.

Exit code 0 when everything passes, 1 otherwise. Needs PyYAML.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "skills" / "kickoff" / "templates" / "intake.md"
FIXTURES = sorted((ROOT / "fixtures").glob("*/intake.md"))
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"

# Body questions that must carry a real answer before a build (checks.md).
REQUIRED_BODY = ["1.3", "2.1", "2.2", "3.1", "3.2", "3.4", "4.1", "4.4"]

NONE_VALUES = {"", "none", None}
LOCAL_ONLY = {"local only", "none"}


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError("no frontmatter block")
    return match.group(1), match.group(2)


def key_shape(obj, prefix: str = "") -> set[str]:
    """Every dotted key path in a nested mapping, leaves included."""
    keys: set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            path = f"{prefix}{k}"
            keys.add(path)
            keys |= key_shape(v, path + ".")
    return keys


def body_answer(body: str, number: str) -> str:
    """Text of the blockquote answer under the heading numbered `number`."""
    pattern = re.compile(rf"^### {re.escape(number)} .*$", re.M)
    match = pattern.search(body)
    if not match:
        return ""
    rest = body[match.end():]
    end = re.search(r"^##", rest, re.M)
    section = rest[: end.start()] if end else rest
    lines = [ln[1:].strip() for ln in section.splitlines() if ln.startswith(">")]
    return " ".join(ln for ln in lines if ln)


def check_fixture(path: Path, schema_keys: set[str], version: str) -> list[str]:
    errors: list[str] = []
    front, body = split_frontmatter(path.read_text(encoding="utf-8"))
    data = yaml.safe_load(front)

    keys = key_shape(data)
    missing = schema_keys - keys
    extra = keys - schema_keys
    if missing:
        errors.append(f"missing keys: {sorted(missing)}")
    if extra:
        errors.append(f"unknown keys: {sorted(extra)}")

    if data.get("kickoff_version") != version:
        errors.append(f"kickoff_version {data.get('kickoff_version')!r} != plugin {version!r}")

    project = data.get("project", {})
    stack = data.get("stack", {})
    env = data.get("environment", {})
    git = data.get("git", {})
    conv = data.get("conventions", {})

    def require(cond: bool, msg: str) -> None:
        if not cond:
            errors.append(msg)

    require(bool(project.get("name")), "project.name is required")
    require(bool(project.get("type")), "project.type is required")
    for field in ("language", "frontend", "backend", "database", "data_layer", "styling", "package_manager"):
        require(bool(stack.get(field)), f"stack.{field} is required")
    require(bool(env.get("os")), "environment.os is required")
    require(bool(env.get("shell")), "environment.shell is required")

    host = (git.get("host") or "").strip().lower()
    require(bool(host), "git.host is required")
    require(bool(git.get("visibility")), "git.visibility is required")
    if host in {"gitlab", "gitea", "other"}:
        require(bool(git.get("host_url")), f"git.host_url is required when host is {host}")
    if host and host not in LOCAL_ONLY:
        require(bool(git.get("owner")), "git.owner is required unless host is local only")
    if (git.get("visibility") or "").lower() == "public":
        require(bool(git.get("license")), "git.license is required when visibility is public")

    database = (stack.get("database") or "").strip().lower()
    if database not in NONE_VALUES:
        require(bool(env.get("dev_database")), "environment.dev_database is required when a database is chosen")

    for field, value in conv.items():
        require(value is not None and value != "" and value != [],
                f"conventions.{field} must be set explicitly in a fixture")

    for number in REQUIRED_BODY:
        answer = body_answer(body, number)
        require(bool(answer), f"body question {number} needs a real answer")
        require(answer.lower() != "i don't know", f"body question {number} does not accept \"I don't know\"")

    return errors


def main() -> int:
    version = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))["version"]
    front, _ = split_frontmatter(TEMPLATE.read_text(encoding="utf-8"))
    template = yaml.safe_load(front)
    schema_keys = key_shape(template)
    failures = 0

    if template.get("kickoff_version") != version:
        print(f"FAIL {TEMPLATE.relative_to(ROOT)}: kickoff_version != plugin version {version}")
        failures += 1
    else:
        print(f"ok   {TEMPLATE.relative_to(ROOT)}: schema with {len(schema_keys)} keys, version {version}")

    for path in FIXTURES:
        errors = check_fixture(path, schema_keys, version)
        rel = path.relative_to(ROOT)
        if errors:
            failures += 1
            print(f"FAIL {rel}")
            for err in errors:
                print(f"     - {err}")
        else:
            print(f"ok   {rel}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
