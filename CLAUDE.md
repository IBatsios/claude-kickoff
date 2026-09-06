# CLAUDE.md — claude-kickoff

`kickoff` is a public Claude Code plugin. One command, `/kickoff`, turns an intake form into a Claude Code-ready project: PRD, architecture, decisions, a runbook, one file per task, a `CLAUDE.md`, and `.env.example`. Follows the global conventions in `~/Documents/Projects/CLAUDE.md`.

## Read first

- `docs/DESIGN.md` is the confirmed design. Anything not in it is undecided. Section 13 lists rejected alternatives; do not re-argue them.
- `docs/question-bank.md` is the intake, annotated. It is under review. Do not build the skill until Yanni has signed it off.
- `docs/handoff-items/` holds the newest handoff doc, which says where work stands.

## Rules specific to this repo

- Nothing in the skill may assume Yanni's setup. If you are writing `gitlab.featurama.com`, `pnpm`, or `PowerShell` into a template, it belongs in a default, not the template.
- The skill makes no network calls and sends no telemetry. Every outbound action is a command the user pastes.
- The skill never logs in, creates a remote, or pushes. It may `git init` and commit locally.
- Keep `SKILL.md` short and point at resource files. Load the `writing-for-agents` skill before editing it.
- Menu answers live only in the intake frontmatter; the body holds prose. One source of truth per answer.
- The source of truth for the public repo is GitHub. GitLab is a mirror.

## Layout

```
.claude-plugin/plugin.json, marketplace.json   plugin identity and one-command install
skills/kickoff/SKILL.md                        the skill: modes, walkthrough, confirm, build, regenerate
skills/kickoff/reference/                      checks, hosts, dev-database, secrets-gate, ci, defaults
skills/kickoff/templates/intake.md             the blank form
skills/kickoff/templates/docs/                 PRD, ARCHITECTURE, DECISIONS, RUNBOOK, CLAUDE.template.md, env.example, gitignore, handoff-next-phase
skills/kickoff/templates/tasks/generic/        walking skeleton, feature slice, sign-in, deploy, definition of done
skills/kickoff/templates/tasks/ts-prisma-postgres/   the first-class set (definition of done is shared from generic)
skills/kickoff/templates/expected-files.md     what a build must produce
fixtures/                                      ts-default, generic-python, local-only, each with expected-files.txt; typed-run-*.md logs
docs/DESIGN.md, docs/question-bank.md, docs/handoff-items/
```

## Status snapshot (2026-09-05)

Design confirmed, question bank reviewed, plugin scaffold complete on branch `feature/skill-scaffold`. All three fixtures run, 24 findings fixed, all three re-run and passing; each fixture directory has a `run-2026-09-05.md`. The first run through `/kickoff` as typed is done: a full walkthrough in an empty directory, build, commit, and defaults file, logged in `fixtures/typed-run-2026-09-05.md` with eight findings. All ten findings from the re-runs and the typed run are applied, and all three fixtures re-run against them and pass. Both invocation paths have been run as typed; every finding from every run is applied, and a confirming typed run showed the last six in effect. The no-ECC smoke run passes on a clean profile via `CLAUDE_CONFIG_DIR`, which the skill now follows. Fixture intakes no longer depend on the machine's defaults file. Not yet done: CI for this repo, creating the GitHub repo under `IBatsios`, the first live project.
