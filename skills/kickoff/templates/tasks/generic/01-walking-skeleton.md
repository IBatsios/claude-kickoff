<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Written to docs/tasks/01-walking-skeleton.md. This is the generic set: name the standard initializer and commands for the intake's stack where you know them, and write "confirm with the user" where you do not. Never invent a command. -->

# 01: Walking skeleton

**What to build:** The thinnest version of "{{4.4}}" that works end to end. The app starts, a {{role}} can reach the one {{screen / route / command}} that path needs, and the result is visible. No styling beyond defaults, no sign-in, no second feature.

**Blocked by:** None. Phase 0 of the runbook must be complete first: database reachable, `.env` filled.

**Status:** ready

## Steps, in order

1. Initialize the project with the standard tool for {{stack.language}} and {{stack.frontend / stack.backend}}: {{command, or "confirm the initializer with the user"}}.
2. Add the test runner ({{stack.tests}}) and one test that needs no database: a pure function, or a health route that returns a fixed value.
3. Add the CI file for {{git.host}}. <!-- Inline the rendered workflow from reference/ci.md, or omit this step for local only. -->
4. Wire the single {{screen / route / command}} the most important path needs. Read real data from the database when the path needs it; otherwise return static data.
5. Add the database connection and first migration when the path needs data: {{command, or "confirm with the user"}}. The runbook's `DATABASE_URL` uses the database's plain scheme; confirm the scheme the data layer expects (for example SQLAlchemy with psycopg 3 wants `postgresql+psycopg://`) and say in `README.md` where it is set.
6. Write the run and test commands into `README.md` and check they match `CLAUDE.md`.
7. Commit on this branch.

## Acceptance criteria

- [ ] `{{run command}}` starts the app with no errors.
- [ ] `{{test command}}` passes with at least one test.
- [ ] "{{4.4}}" can be demonstrated in its thinnest form.
- [ ] CI is green on {{git.host}} for this branch. <!-- Omit for local only. -->
- [ ] `.env.example` lists every variable the code reads, and no secret is in the repository.

## Suggested skills

<!-- Only skills detected on the machine that fit this task. Omit the section when none do. -->

## Notes

Keep the skeleton test free of the database so CI needs no service. The first slice that needs the database in CI adds a service container; the feature-slice tasks say how.

<!-- Keep the next paragraph only when the most important path needs a signed-in user. -->
The most important path needs a signed-in user and sign-in does not exist yet. Use one fixed placeholder identity, a constant in code and never a real account, and name it as such; the sign-in task replaces it.
