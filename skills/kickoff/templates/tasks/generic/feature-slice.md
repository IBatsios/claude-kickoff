<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. One file per must-have, written to docs/tasks/NN-<slug>.md in dependency order. Split a story into two tasks when it names more than one role or more than one screen; each half is still a full vertical slice. -->

# {{NN}}: {{short title from the story}}

**What to build:** {{the story: As a role, I can do, so that benefit}}. From the user's side: {{one or two sentences of what they see and do}}.

**Blocked by:** 01{{, the sign-in task when the story needs a signed-in user}}{{, any earlier slice whose data this one reads}}.

**Status:** ready

## Steps, a vertical slice in this order

1. Data: add or change the entities this story needs ({{entities from 5.1}}), and write the migration.
2. Logic: the function or module that does the work, with its test written first.
3. Interface: the {{screen / route / command}} the {{role}} uses.
4. Walk the story the way the user would, end to end.
5. Update `README.md` or `CLAUDE.md` if a command changed.

## Acceptance criteria

- [ ] As a {{role}}, I can {{do}}: demonstrated end to end.
- [ ] Tests cover the behavior, as a user would observe it, and pass.
- [ ] Every earlier test still passes; CI is green. <!-- Drop the CI clause for local only. -->
- [ ] {{When 11.2 is WCAG 2.2 AA: every new control is reachable by keyboard, labeled, and readable at AA contrast.}}
- [ ] Any new environment variable is in `.env.example` with a placeholder.

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

<!-- When this is the first slice that needs the database in CI, keep this paragraph; otherwise remove it. -->
This is the first task that needs the database in CI. Add a database service to the CI workflow: for PostgreSQL, a service using image `postgres:16` with `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` set, port 5432, and set `DATABASE_URL` in the job to match. Run the migrations before the tests.
