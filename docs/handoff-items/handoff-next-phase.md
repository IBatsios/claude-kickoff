# Handoff — after the plugin scaffold

**Date:** 2026-09-05
**Phase finished:** design, question bank review, and the full plugin scaffold
**Next phase:** first fixture run, fixes, then the no-ECC smoke run and CI

## Where things stand

- `docs/DESIGN.md` is the confirmed design; section 13 lists what not to re-argue. `docs/question-bank.md` is reviewed; its "Review decisions" section records the outcomes.
- The whole plugin exists as files on branch `feature/skill-scaffold`, uncommitted: manifest and marketplace file, `skills/kickoff/SKILL.md`, six reference files, the blank form, six document templates, nine task templates, `expected-files.md`, three fixtures, and the repo hygiene files.
- Nothing has been run. No fixture has been built, no command in the templates has been executed, and the README's install line still says `YOUR-GITHUB-USER`.

## What to do next, in order

1. **Commit the scaffold** on `feature/skill-scaffold` with `chore: kickoff plugin scaffold`. Yanni decides when; nothing is committed yet.
2. **Run the first fixture.** Copy `fixtures/ts-default/intake.md` into an empty directory as `docs/intake.md`, install the plugin locally (or symlink `skills/kickoff` into `~/.claude/skills/`), run `/kickoff`, and compare against `fixtures/ts-default/expected-files.txt`, including the comment lines at its end. Expect the templates to be wrong in places; fix the template, not the output.
3. **Run the other two fixtures** the same way. `local-only` is the one most likely to expose steps that assume a remote or a database.
4. **Fix what the runs found** in `SKILL.md`, the reference files, and the templates. Keep `docs/question-bank.md` and `skills/kickoff/reference/checks.md` in step if a question changes.
5. **Smoke run without ECC and without a defaults file**: a profile with no `~/.claude/kickoff/defaults.yaml` and no `~/.claude/commands/project-init.md`. The runbook must have no ECC step and every task must read complete with no suggested-skills line.
6. **CI for this repo**: a GitHub Actions workflow that runs a markdown linter, validates the frontmatter of the blank form and the three fixtures against the key list in `reference/checks.md`, and checks that every path `SKILL.md` names exists. No model calls.
7. **Hand-write this repo's own intake and docs** in the same shapes, as the reference example of the output. Optional until the templates have survived the fixtures.
8. **Fill in the GitHub owner** in `README.md`, push, tag `v0.1.0`, add the changelog heading.
9. First live run on Yanni's next real app.

## Things to watch for when running

- `SKILL.md` asks for the structured question prompt for menu fields, which allows at most four options. The saved default goes first, the likeliest three follow, and any other value comes in through the free-text path. If that feels wrong in practice, it is a `SKILL.md` change, not a design change.
- The build writes documents and configuration only; Task 01 writes the code. If a fixture run produces `package.json`, the skill overstepped.
- Commands in `reference/hosts.md` for `glab` and `tea` were written from memory of their CLIs. Verify the flags on a real run before the first release.

## Decisions you must not reopen

See `docs/DESIGN.md` section 13, plus the review decisions in `docs/question-bank.md`.

## Suggested skills for the next session

- `writing-for-agents` when editing `SKILL.md` or any template.
- `grilling` if a fixture run reveals a branch the design does not cover.
