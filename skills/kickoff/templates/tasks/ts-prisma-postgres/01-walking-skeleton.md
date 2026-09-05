<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Written to docs/tasks/01-walking-skeleton.md. Render {{pm}} forms for stack.package_manager: add = "pnpm add" / "npm install" / "yarn add" / "bun add"; dev flag = "-D" / "--save-dev" / "-D" / "-d"; exec = "pnpm" / "npx" / "yarn" / "bunx"; run script = "pnpm <s>" / "npm run <s>" / "yarn <s>" / "bun run <s>". Keep the Next.js or the Express block, not both. -->

# 01: Walking skeleton

**What to build:** The thinnest version of "{{4.4}}" that works end to end. The app starts, a {{role}} can reach the one {{page / route}} that path needs, and the result is visible. Default styling, no sign-in, no second feature.

**Blocked by:** None. Phase 0 of the runbook must be complete first: database reachable, `.env` filled.

**Status:** ready

## Steps, in order

<!-- Next.js block -->
1. Create the app in this directory: `{{pm exec}} create-next-app@latest . --typescript --app --src-dir --eslint{{ --tailwind when styling is Tailwind}} --import-alias "@/*"`. Say yes to overwriting nothing; the directory holds only docs.
<!-- Express block -->
1. Create the app: `{{pm}} init`, then `{{pm add}} express` and `{{pm add dev}} typescript tsx @types/node @types/express`, then `{{pm exec}} tsc --init`. Entry at `src/server.ts` with a `GET /health` returning `{ ok: true }`; scripts `dev` (`tsx watch src/server.ts`) and `build`.
2. Prisma: `{{pm add dev}} prisma`, `{{pm add}} @prisma/client`, `{{pm exec}} prisma init --datasource-provider postgresql`. Confirm `DATABASE_URL` in `.env` matches the runbook's database step.
3. Add the first model the most important path needs to `prisma/schema.prisma` ({{entity from 5.1, or a single `Ping` model when the path needs no data}}), then `{{pm exec}} prisma migrate dev --name init`.
4. Tests: `{{pm add dev}} vitest` and a `test` script. First test at `src/lib/health.test.ts` on a pure function; no database.
5. CI for {{git.host}}. <!-- Inline the rendered workflow from reference/ci.md with setup-node 22 and, for pnpm, pnpm/action-setup. Omit for local only. -->
6. The one {{page at src/app/{{path}}/page.tsx / route at src/routes/{{name}}.ts}} for the most important path, reading through Prisma when the path needs data.
7. `README.md`: install, dev, test commands. Check they match `CLAUDE.md`.
8. Commit on this branch.

## Acceptance criteria

- [ ] `{{pm run dev}}` starts with no errors and {{the page / the route}} responds.
- [ ] `{{pm run test}}` passes with at least one test.
- [ ] `{{pm exec}} prisma migrate dev` has been run once and `prisma/migrations/` is committed.
- [ ] "{{4.4}}" can be demonstrated in its thinnest form.
- [ ] CI is green on {{git.host}} for this branch. <!-- Omit for local only. -->
- [ ] `.env.example` lists `DATABASE_URL` and every other variable the code reads; no secret is in the repository.

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

Keep the skeleton test free of the database so CI needs no service. Playwright, when chosen, is installed by the first slice with a screen to test, with `{{pm exec}} playwright install`.
