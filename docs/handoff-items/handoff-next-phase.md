# Handoff — after the fixture runs and the first typed run

**Date:** 2026-09-05
**Phase finished:** plugin scaffold, three fixture runs, three fix rounds, a re-run of every fixture against the fixed templates, and the first run through `/kickoff` as typed
**Next phase:** apply the typed-run findings, the no-ECC smoke run, CI for this repo, and release preparation

## Where things stand

- `docs/DESIGN.md` is the confirmed design; section 13 lists what not to re-argue. `docs/question-bank.md` is reviewed; its "Review decisions" section records the outcomes.
- The whole plugin exists on branch `feature/skill-scaffold`, four commits, working tree clean: manifest and marketplace file, `skills/kickoff/SKILL.md`, six reference files, the blank form, seven document templates including the handoff one, nine task templates, `expected-files.md`, three fixtures, and the repo hygiene files.
- Every fixture has been run once by following `SKILL.md` literally, and re-run after the fixes. All three pass their expected-files lists. The runs found 24 template and skill defects, all fixed the same day. Each fixture directory holds a `run-2026-09-05.md` with the findings, the fixes, and the re-run result.
- The fixture runs were done by an agent following the skill in this session, not through an installed plugin.
- `/kickoff` has now been run once as typed, with the plugin loaded from this repo: Refuse mode in this directory, then a full walkthrough in an empty directory (`~/Documents/Projects/kickoff-test`, kept outside the repo), confirm, build with `ts-prisma-postgres`, one commit, and the defaults file written. Everything in `expected-files.md` came out. `fixtures/typed-run-2026-09-05.md` holds the log: eight findings, the worst being that the build leaves no `main` branch, so the runbook's first pull request has no target.
- All ten findings from the re-runs and the typed run are applied. The two design calls went: the scaffold commit lands on `main` and Task 01 opens the first branch; optional sections carry proposed answers so one word accepts them. The run logs record this. The fixture outputs on disk predate these changes; their expected-files lists do not.
- `~/.claude/kickoff/defaults.yaml` now exists on this machine, written by that run. The next walkthrough here will pre-select from it; the no-ECC smoke run must use a profile without it.
- `README.md` names the GitHub owner, `IBatsios`. The `claude-kickoff` repo does not exist there yet.

## What to do next, in order

1. **Re-check the three fixtures against the changed templates.** The git step now commits on `main`, the deploy templates gained a domain step, the skeletons start Task 01's branch, and the DECISIONS and PRD templates changed their rows. The expected-files lists are updated; regenerate the affected files and diff, as the earlier re-run did.
2. **Run a fixture through `/kickoff` as typed** to exercise the build-from-file path: `docs/intake.md` complete, no walkthrough, the skills list shown at confirm. Use `fixtures/ts-default`. The typed run so far covered only the walkthrough path.
3. **Smoke run without ECC and without a defaults file**: a profile with no `~/.claude/kickoff/defaults.yaml` and no `project-init` command anywhere. The runbook must have no ECC step and every task must read complete with no suggested-skills line. Use `fixtures/local-only`.
4. **CI for this repo**: a GitHub Actions workflow that runs a markdown linter, validates the frontmatter of the blank form and the three fixtures against the key list in `reference/checks.md`, and checks that every path `SKILL.md` names exists. No model calls.
5. **Hand-write this repo's own intake and docs** in the same shapes, as the reference example of the output. Optional; the fixture outputs already serve as examples and could be checked in under `fixtures/<name>/example/` instead.
6. **Create the `claude-kickoff` repo** under `IBatsios` on GitHub, push the branch, open the first pull request, tag `v0.1.0`, and add the version heading in `CHANGELOG.md`.
7. First live run on Yanni's next real app.

## Things to watch for when running

- Commands in `reference/hosts.md` for `glab` and `tea` were written from memory of those CLIs and have only been rendered, never executed. Verify the flags on a real host before release.
- `SKILL.md` asks for the structured question prompt for menu fields, which allows at most four options. The saved default goes first, the likeliest three follow, and any other value comes in through the free-text path. The typed run confirmed this works, including multi-select, at the cost of one extra exchange per section that mixes menu and prose fields.
- When the user defers a whole block ("I'll defer to you" on the stack), offering one recommended set and confirming it with a single structured question worked and still gave every field an explicit yes. `SKILL.md` section 2 now describes this path, along with proposed answers on optional sections.
- The build writes documents and configuration only; Task 01 writes the code. If a run produces `package.json` or `pyproject.toml`, the skill overstepped.
- `docs/question-bank.md` and `reference/checks.md` both describe the required fields and the contradiction checks. The runtime reads only `checks.md`. Keep them in step when a question changes.

## Decisions you must not reopen

See `docs/DESIGN.md` section 13, plus the review decisions in `docs/question-bank.md`.

## Suggested skills for the next session

- `writing-for-agents` when editing `SKILL.md` or any template.
- `grilling` if a run reveals a branch the design does not cover.
