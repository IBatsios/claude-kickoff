<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. This file goes at the project root, not in docs/. Six sections, nothing more. It must stand alone: a reader with no other configuration should be able to work from it. -->

# CLAUDE.md — {{project.name}}

{{1.3 pitch}} Users: {{3.1 in one line}}. The most important path is {{4.4}}.

## Stack

{{one line: language, frontend, backend, database with data layer, styling, tests, package manager}}. Details in `docs/ARCHITECTURE.md`.

## Conventions

<!-- The resolved conventions, as rules. Include only the ones that are true. -->

- Work on a branch named `{{prefix}}/<short-description>`; merge to the default branch through a {{pull request / merge request}}.
- Commit messages: {{conventional commits with types feat, fix, chore, docs, test, refactor / free form}}.
- Every new environment variable is added to `.env.example` with a placeholder. Secrets never go in code or commits.
- Back up the database before running a migration.
- At the end of a phase, write a handoff doc in `docs/handoff-items/`.

## Run and test

<!-- Concrete commands from the template set. For the generic set, the commands the stack implies, marked "confirm" where unsure. -->

```
{{install}}
{{run in development}}
{{test}}
```

## Where things are

- `docs/PRD.md`: what and why. `docs/ARCHITECTURE.md`: how. `docs/DECISIONS.md`: what was decided and why; append new decisions there.
- `docs/RUNBOOK.md`: what to do next. Phase 0 is done by a person. Phase 1 is the task list.
- `docs/tasks/`: one file per task. Pick any task whose "Blocked by" list is entirely done. Finish it to its acceptance criteria before starting another.
- `docs/intake.md`: the source all of the above was generated from. Change the intake and run `/kickoff` to regenerate; edits to generated files are lost on regenerate.

## Skills to use

<!-- Only when skills were detected and kept in the walkthrough. Otherwise omit this section entirely. One line per skill: name and when. -->

- `{{skill}}`: {{when}}
