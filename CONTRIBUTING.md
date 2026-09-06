# Contributing

Thanks for looking. The one contribution this project is built to receive is a new first-class stack. Everything else is welcome too, but start there if you are unsure.

## Ground rules

- Nothing in the skill may assume the maintainer's setup. A host name, a package manager, or a shell belongs in a default, never in a template.
- The skill makes no network calls and sends no telemetry. Every outbound action is a command the user pastes from the runbook.
- The skill never logs in, creates a remote, or pushes. It may `git init` and commit locally.
- Menu answers live only in the intake frontmatter. The body holds prose.
- Work on a branch and open a pull request. Commit messages follow conventional commits.

## Adding a first-class stack

A first-class stack gets stack-aware task templates: "run the Prisma migration" instead of "set up the database". Adding one is four steps.

1. **Name it.** Pick the frontmatter combination that selects it, for example `language: Python`, `backend: FastAPI`, `database: PostgreSQL`, `data_layer: SQLAlchemy`. Add the selector to the "Choose the template set" step in `skills/kickoff/SKILL.md`.
2. **Write the templates** in `skills/kickoff/templates/tasks/<stack-slug>/`. Copy the generic set and make every command concrete. Four files: `01-walking-skeleton.md`, `feature-slice.md`, `sign-in.md`, `deploy.md`. The definition-of-done task is shared from the generic set and needs no copy.
3. **Add a fixture** in `fixtures/<stack-slug>/` with a filled `intake.md` and an `expected-files.txt`. The fixture is how the next person knows they did not break your stack.
4. **Run it.** Copy the fixture intake into an empty directory, run `/kickoff`, and check every file in the expected list exists and every command in the runbook is real. Paste the file list into the pull request.

## Adding a question to the intake

1. Add it to `skills/kickoff/templates/intake.md` and, if it is a menu, to the frontmatter block.
2. Update `skills/kickoff/reference/checks.md` if it is required or takes part in a contradiction check.
3. List it under "Questions added" in `CHANGELOG.md` for the next version. The regenerate step reads that list to ask only the new questions of an older intake.
4. Update the three fixtures.

## Checks

CI runs three model-free checks on every pull request and every push to `main`; run the first two locally before opening a pull request:

```
pip install pyyaml
python scripts/check_frontmatter.py
python scripts/check_references.py
```

- `check_frontmatter.py` treats the blank form's frontmatter as the schema and validates every fixture against it: same keys, the plugin's version, the required-field rules from `skills/kickoff/reference/checks.md` (mirrored in the script; change both), every `conventions` field set, and a real answer on every required body question.
- `check_references.py` checks that every path `SKILL.md` names exists, that each task template set is complete, that `templates/docs/` holds exactly the build's documents, that no template uses a retired placeholder form, and that the manifests and changelog agree.
- Markdown lint runs in CI through `markdownlint-cli2`, configured in `.markdownlint-cli2.jsonc`. Rules the templates would trip by design are off there, with a reason each.

The skill itself is never run in CI; that is the fixture runs, by hand, above.

## Release checklist

- Bump `version` in `.claude-plugin/plugin.json` and add the version heading in `CHANGELOG.md`.
- Run all three fixtures by hand and compare against their expected file lists. Every fixture intake sets every `conventions` field explicitly, so a run never depends on the machine's `~/.claude/kickoff/defaults.yaml`; keep it that way when adding one.
- Run one fixture on a clean profile: set `CLAUDE_CONFIG_DIR` to an empty directory before starting Claude Code. The skill follows that variable, so it will see no skills, no commands, no plugins, and no defaults file. The runbook must have no ECC step and no task may carry a suggested-skills line.
- Tag the commit with the version.
