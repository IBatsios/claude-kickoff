# Handoff — after the fixture runs

**Date:** 2026-09-05
**Phase finished:** plugin scaffold, three fixture runs, three fix rounds, and a re-run of every fixture against the fixed templates
**Next phase:** the no-ECC smoke run, CI for this repo, and release preparation

## Where things stand

- `docs/DESIGN.md` is the confirmed design; section 13 lists what not to re-argue. `docs/question-bank.md` is reviewed; its "Review decisions" section records the outcomes.
- The whole plugin exists on branch `feature/skill-scaffold`, four commits, working tree clean: manifest and marketplace file, `skills/kickoff/SKILL.md`, six reference files, the blank form, seven document templates including the handoff one, nine task templates, `expected-files.md`, three fixtures, and the repo hygiene files.
- Every fixture has been run once by following `SKILL.md` literally, and re-run after the fixes. All three pass their expected-files lists. The runs found 24 template and skill defects, all fixed the same day. Each fixture directory holds a `run-2026-09-05.md` with the findings, the fixes, and the re-run result.
- The runs were done by an agent following the skill in this session, not through an installed plugin. Nothing has yet been run through `/kickoff` as a user would type it.
- Two candidate findings from the re-runs are logged and not applied: the uncovered-work rule turns a manual one-off import into a user story, and the scope guard counts stories rather than slices.
- `README.md` still says `YOUR-GITHUB-USER` in the install line.

## What to do next, in order

1. **Decide on the two candidate findings** in the ts-default and generic-python run logs, and apply them if agreed. Both are one-sentence changes to `SKILL.md`, `reference/checks.md`, and the PRD template.
2. **Install the plugin locally and run one fixture through `/kickoff`** as typed, rather than by an agent reading `SKILL.md`. This is the first test of mode detection, the structured prompts, and the defaults offer as a user meets them. Use `fixtures/ts-default`.
3. **Smoke run without ECC and without a defaults file**: a profile with no `~/.claude/kickoff/defaults.yaml` and no `project-init` command anywhere. The runbook must have no ECC step and every task must read complete with no suggested-skills line. Use `fixtures/local-only`.
4. **CI for this repo**: a GitHub Actions workflow that runs a markdown linter, validates the frontmatter of the blank form and the three fixtures against the key list in `reference/checks.md`, and checks that every path `SKILL.md` names exists. No model calls.
5. **Hand-write this repo's own intake and docs** in the same shapes, as the reference example of the output. Optional; the fixture outputs already serve as examples and could be checked in under `fixtures/<name>/example/` instead.
6. **Fill in the GitHub owner** in `README.md`, create the `claude-kickoff` repo on GitHub, push the branch, open the first pull request, tag `v0.1.0`, and add the version heading in `CHANGELOG.md`.
7. First live run on Yanni's next real app.

## Things to watch for when running

- Commands in `reference/hosts.md` for `glab` and `tea` were written from memory of those CLIs and have only been rendered, never executed. Verify the flags on a real host before release.
- `SKILL.md` asks for the structured question prompt for menu fields, which allows at most four options. The saved default goes first, the likeliest three follow, and any other value comes in through the free-text path. Step 2 above is where this is first felt.
- The build writes documents and configuration only; Task 01 writes the code. If a run produces `package.json` or `pyproject.toml`, the skill overstepped.
- `docs/question-bank.md` and `reference/checks.md` both describe the required fields and the contradiction checks. The runtime reads only `checks.md`. Keep them in step when a question changes.

## Decisions you must not reopen

See `docs/DESIGN.md` section 13, plus the review decisions in `docs/question-bank.md`.

## Suggested skills for the next session

- `writing-for-agents` when editing `SKILL.md` or any template.
- `grilling` if a run reveals a branch the design does not cover.
