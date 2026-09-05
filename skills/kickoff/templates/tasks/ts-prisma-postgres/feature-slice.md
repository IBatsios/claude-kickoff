<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. One file per must-have, written to docs/tasks/NN-<slug>.md in dependency order. Split a story into two tasks when it names more than one role or more than one screen. Same {{pm}} rendering as the skeleton. Keep the Next.js or the Express path lines, not both. -->

# {{NN}}: {{short title from the story}}

**What to build:** {{the story}}. From the user's side: {{one or two sentences of what they see and do}}.

**Blocked by:** 01{{, the sign-in task when the story needs a signed-in user}}{{, any earlier slice whose data this one reads}}.

**Status:** ready

## Steps, a vertical slice in this order

1. Schema: add or change {{entities}} in `prisma/schema.prisma`, then `{{pm exec}} prisma migrate dev --name {{slug}}`.
2. Data access: `src/lib/{{entity}}.ts` with the functions this story needs, and a Vitest test for each written first.
3. Interface: {{`src/app/api/{{resource}}/route.ts` and `src/app/{{path}}/page.tsx` / `src/routes/{{resource}}.ts`}}.
4. Walk the story as the {{role}} would. {{When Playwright is chosen: add the end-to-end test at `e2e/{{slug}}.spec.ts`.}}
5. Update `README.md` or `CLAUDE.md` if a command changed.

## Acceptance criteria

- [ ] As a {{role}}, I can {{do}}: demonstrated end to end.
- [ ] Vitest covers the data-access functions as a caller would observe them, and passes.
- [ ] {{When Playwright is chosen: The end-to-end test passes.}}
- [ ] The migration is committed under `prisma/migrations/`.
- [ ] Every earlier test still passes; CI is green. <!-- Drop the CI clause for local only. -->
- [ ] {{When 11.2 is WCAG 2.2 AA: every new control is reachable by keyboard, labeled, and readable at AA contrast.}}
- [ ] Any new environment variable is in `.env.example` with a placeholder.

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

<!-- Keep only on the first slice that needs the database in CI. -->
This is the first task that needs the database in CI. Add a service to the CI job: image `postgres:16`, environment `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` all set to `test`, port 5432, and `DATABASE_URL=postgresql://test:test@localhost:5432/test` in the job. Run `{{pm exec}} prisma migrate deploy` before the tests.
