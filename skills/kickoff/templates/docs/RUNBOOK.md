<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Every command in Phase 0 is rendered for git.host and environment.shell with the intake's real values, from reference/hosts.md, dev-database.md, and secrets-gate.md. A step that does not apply is omitted, not left as a note, except where a reference file says to render a one-line note. -->

# {{project.name}} — Runbook

Phase 0 is for a person: it needs accounts, passwords, and judgement. Phase 1 is for whoever builds, agent or human, one task at a time.

## Phase 0 — before any code

### 0.1 Create the remote

<!-- From reference/hosts.md. Local only: omit this step and renumber. Existing repo: only the remote-add and push lines. -->

### 0.2 Development database

<!-- From reference/dev-database.md. No database: omit. -->

### 0.3 Fill in `.env`

Copy `.env.example` to `.env` and fill every value. Where each one comes from:

<!-- One line per variable in .env.example: name, then where to get it (the provider console, the database step above, or "any long random string" for secrets you generate). Omit this whole step, and renumber, when .env.example has no variables. -->

- `{{VAR}}`: {{where to get it}}

`.env` is listed in `.gitignore`. Keep it there.

### 0.4 Scan for secrets

<!-- From reference/secrets-gate.md. -->

### 0.5 Install the ECC rules for this stack

<!-- Only when /project-init was detected on the machine. Otherwise omit and renumber. -->

Run `/project-init` in this directory and accept the plan it proposes.

### 0.6 Push

<!-- From "The push" section of reference/hosts.md: push main, the line saying Task 01 opens the first pull or merge request, and the protect-main line when the convention is on. This is the only place the runbook pushes. Local only: the one-line "no remote, Phase 1 can start now" note. -->

<!-- When conventions.db_backup_before_migrate is true and environments lack staging, add: -->
### 0.7 Before every migration from now on

There is no staging environment. Back up the database before each migration: {{one command appropriate to the database and dev_database mode, e.g. pg_dump for Postgres, or "take a snapshot in your provider's console" for hosted}}.

## Phase 1 — build

Pick the next task from the **frontier**: any task whose "Blocked by" list is entirely done. Finish it to its acceptance criteria before starting another. Each task lives in `docs/tasks/`. Every task starts on its own branch from `main` and ends in a {{pull request / merge request; for local only: a merge to main}}.

| # | Task | Blocked by | Delivers |
|---|---|---|---|
| 01 | Walking skeleton | none | {{4.4}} works end to end in the thinnest form, one test, CI green |
<!-- One row per task file, in number order. -->
| {{NN}} | {{title}} | {{numbers}} | {{one line}} |

## Done

v1 is done when the last task's acceptance criteria, which are the intake's definition of done, are all checked.
