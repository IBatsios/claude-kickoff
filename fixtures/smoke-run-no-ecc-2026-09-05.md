# Smoke run without ECC and without a defaults file, 2026-09-05

The run that proves the public claim: kickoff v0.1.0 on a profile with nothing in it. `CLAUDE_CONFIG_DIR` pointed at an empty directory, `~/Documents/Projects/kickoff-smoke-profile`, so Claude Code had no skills, commands, plugins, settings, or sign-in, and the skill, which now follows the same variable, saw none of the 204 skills on this machine and no defaults file. Plugin loaded with `--plugin-dir` from this repo. Test folder `~/Documents/Projects/kickoff-test-4` holding the local-only intake. Yanni at the keyboard, in auto mode.

Prerequisite change made the same day: the skill and `reference/defaults.md` read `$CLAUDE_CONFIG_DIR` when set and `~/.claude` otherwise. Before that, a clean Claude Code profile would not have been a clean profile for the skill.

**Status:** passes. No defects. Two candidate improvements logged and not applied.

## Result

Mode line: "Confirm then Build, `C:\Users\ibats\Documents\Projects\kickoff-test-4` has a complete `docs/intake.md` and no `docs/PRD.md`". The confirm summary reported no defaults file, the shipped conventions, the generic template set, four projected tasks, no checks fired, and "Skills detected: none", with the reason: the config directory has no skills, commands, or plugin cache. It added one note of its own: the intake says macOS and zsh while the machine is Windows, and it would follow the intake unless told otherwise.

Build: every fixed-name file in `fixtures/local-only/expected-files.txt`, four task files, headers on everything, no leftovers. No `LICENSE`, no compose file, no handoff doc, no source or module file. Not one task carries a "Suggested skills" line. The runbook has two Phase 0 steps, the secrets scan and the no-remote note, and no ECC step. Conventions are the shipped defaults. DECISIONS has the 8.11 row as D2. One commit on `main`, no other branch, working tree clean.

Defaults offer: a structured prompt with three options, "Save all of them", "Save all except os and shell", "Don't save". The middle option was the skill's own addition for the OS mismatch. The file was written to `kickoff-smoke-profile/kickoff/defaults.yaml` with a header comment, the eligible keys only, and `environment.os` and `environment.shell` deliberately left unset, which the comment says.

After the build, Yanni asked the skill to continue into the runbook. It ran the secrets scan with the zsh fallback, noted there is no remote, then found Go is not installed, said Task 01 could be written but not demonstrated, and asked how to proceed with "Stop here" as the first option. Stopped there. The skill itself had ended correctly after the defaults offer; the continuation was requested.

## Candidate improvements, not applied

1. **OS differs from the machine.** `reference/checks.md` warns when an intake contradicts itself about OS and shell, not when it contradicts the machine running the build. The run noticed on its own and said what it would do. A row in the contradictions table would make that the rule: when `environment.os` differs from the machine, warn, and follow the intake.
2. **Defaults offer on an OS mismatch.** The run's "Save all except os and shell" option is the right one in that case and is not in `reference/defaults.md`. Adding it as the recommended option whenever `environment.os` differs from the machine would codify it.

## What this run settles

The plugin works with nothing else installed: no ECC, no other skills, no defaults file, no prior sign-in. Every task reads complete on its own. The config-directory rule makes a clean profile reproducible with one environment variable, which is how the release checklist should describe the smoke run from now on.
