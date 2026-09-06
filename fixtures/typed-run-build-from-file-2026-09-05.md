# Typed run, build-from-file path, 2026-09-05

The second run of `/kickoff` as a user types it, kickoff v0.1.0, plugin loaded with `--plugin-dir` from this repo, in `~/Documents/Projects/kickoff-test-2` holding only `docs/intake.md`, a copy of `fixtures/ts-default/intake.md`. Yanni at the keyboard; two answers given: yes to the confirm summary, and a mistaken yes to the defaults offer, corrected a message later.

A first attempt was launched from this repo's directory instead of the test folder and hit Refuse mode, correctly. The skill looks only at the directory the session started in.

**Status:** all six findings applied the same day. The ts-default and local-only fixture intakes now set every `conventions` field; a re-run of ts-default on this machine should no longer produce the handoff doc.

## Result

Mode detection said "Confirm, then Build" and asked no intake question. Confirm took about three minutes, mostly reading every reference file and template; the summary was twelve numbered lines plus the skills list. Skill detection counted 204 entries and showed 14 that fit the stack, grouped, with the count of the rest and a note that any can be added by name. The new contradiction check for an admin without an admin role reasoned that the organizer is that role, which is right. The summary also flagged, unprompted, that `example-owner` and `shelfmate.example.com` look like placeholders and that the intake never says how a member joins a club.

Build took about ten minutes. The first write attempt used a shell heredoc and failed on quoting; the skill switched to the file-writing tool and continued. Every fixed-name file in `fixtures/ts-default/expected-files.txt` exists, eight task files, headers on every generated file, no unrendered placeholders. One commit on `main`, no other branch. The runbook pushes `main` at step 0.6 after the gitleaks gate and carries the protect-`main` line; the skeleton starts `feature/walking-skeleton` from `main` and notes the `packageManager` field; the Vercel task has the domain step. The 8.11 row is present in DECISIONS.

The defaults offer showed a two-row table, `git.owner` and `deployment.target`, and recommended no. The answer was yes by reflex; the skill wrote both values into `~/.claude/kickoff/defaults.yaml`, was interrupted, and on "I meant no" restored both. The file is as it was.

One line of the expected list failed: `docs/handoff-items/handoff-next-phase.md` exists. The fixture leaves every `conventions` field blank, so they resolved from the machine's defaults file, which the first typed run wrote with `handoff_docs: true`. The skill did what the design says; the fixture assumed no defaults file.

## Findings, in order of severity

1. **Fixture output depends on the machine's defaults file.** Blank `conventions` in a fixture intake resolve from `~/.claude/kickoff/defaults.yaml` when one exists, so the same fixture produces different files on different machines, and the ts-default and local-only expected lists are wrong on any machine with `handoff_docs: true` saved. Fix: every fixture intake spells out every `conventions` field (ts-default and local-only get the shipped defaults written in; generic-python already sets them), and the release checklist in `CONTRIBUTING.md` says fixtures must not depend on the defaults file.
2. **The defaults offer invites a reflex answer.** It came as a plain chat question at the tail of a long build report, and was answered yes when no was meant. The skill then wrote the file before the correction. Fix: `SKILL.md` step 6 and `reference/defaults.md` make the offer its own message, use the structured prompt with "No, keep my saved defaults" as the first option whenever any differing value looks like a placeholder (an `example` owner or domain), and put the table above the prompt. Name the correction path too: on "I meant no", restore the previous values, as this run did.
3. **Shell heredocs fail on generated files.** The first write attempt was a heredoc that tripped on quoting, the same failure the fixture runs hit in this repo. Fix: `SKILL.md` section 4 says to write generated files with the file-writing tool, one file per call, and to use the shell only for git and checks.
4. **The mode line does not name the directory.** The first attempt refused because the session had started in this repo; the refusal described the contents but never printed the path. Fix: `SKILL.md` section 1 says the mode line names the absolute directory.
5. **Skills filter ignores Section 11.** The intake asks for WCAG 2.2 AA and `front-a11y` is installed, but the filter keyed on stack and project type and left it out. Fix: `SKILL.md` section 6 says the filter also considers the answered non-functional needs.
6. **8.11 row position.** The template places the "Must use" row right after D1; the run put it at D6. The template's comment says "one row when 8.11 is answered" beside D1 but does not say the row is D2. Fix: say so.

## What worked without adjustment

Mode detection on a complete intake with no questions asked. The filtered skills list with a count of the rest. The confirm summary shape, including notes the template did not ask for that a user wants: placeholder values and an intake gap. The admin-without-role check. The build from templates with `pnpm dlx` and `pnpm` forms, the placeholder-identity paragraph, the domain step, the `packageManager` note. `git init -b main` with one commit and no other branch. The runbook's push after the gate with the protect line. The DECISIONS row for a convention that came from the defaults file, labeled with its source. The defaults offer's diff table and its restore on correction.

## Observations that are not defects

- Confirm at three minutes and build at ten are long for a form that was already filled. Almost all of it is reading every reference and template in full, one Bash call each. A future version could read only the template set it needs, but the reads are what make the output faithful.
- The run's DECISIONS labeled the defaults-sourced convention row "intake left blank; from defaults". The template does not say to; it is better than "chosen in intake" and could become the rule.
