<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Written to docs/tasks/01-walking-skeleton.md. Render {{pm}} forms for stack.package_manager, in the order pnpm / npm / yarn / bun: {{pm add}} = "pnpm add" / "npm install" / "yarn add" / "bun add"; {{pm add dev}} = "pnpm add -D" / "npm install --save-dev" / "yarn add -D" / "bun add -d"; {{pm dlx}} runs a package that is not installed = "pnpm dlx" / "npx" / "yarn dlx" / "bunx"; {{pm bin}} runs a binary the project has installed = "pnpm" / "npx" / "yarn" / "bunx"; {{pm run}} = "pnpm <s>" / "npm run <s>" / "yarn <s>" / "bun run <s>". The same forms apply in every template of this set. Keep the Next.js or the Express block, not both. -->

# 01: Walking skeleton

**What to build:** The thinnest version of "{{4.4}}" that works end to end. The app starts, a {{role}} can reach the one {{page / route}} that path needs, and the result is visible. Default styling, no sign-in, no second feature.

**Blocked by:** None. Phase 0 of the runbook must be complete first: database reachable, `.env` filled.

**Status:** ready

## Steps, in order

<!-- Next.js block -->
1. Create the app in this directory: `{{pm dlx}} create-next-app@latest . --typescript --app --src-dir --eslint{{ --tailwind when styling is Tailwind}} --import-alias "@/*"{{ --use-pnpm / --use-npm / --use-yarn / --use-bun}}`. The directory holds only docs, so nothing is overwritten.
<!-- Express block -->
1. Create the app: `{{pm}} init`, then `{{pm add}} express` and `{{pm add dev}} typescript tsx @types/node @types/express`, then `{{pm bin}} tsc --init`. Entry at `src/server.ts` with a `GET /health` returning `{ ok: true }`; scripts `dev` (`tsx watch src/server.ts`) and `build`.
2. Prisma: `{{pm add dev}} prisma`, `{{pm add}} @prisma/client`, `{{pm bin}} prisma init --datasource-provider postgresql`. Confirm `DATABASE_URL` in `.env` matches the runbook's database step.
3. Add the first model the most important path needs to `prisma/schema.prisma` ({{entity from 5.1, or a single `Ping` model when the path needs no data}}), then `{{pm bin}} prisma migrate dev --name init`.
4. Tests: `{{pm add dev}} vitest` and a `test` script. First test at `src/lib/health.test.ts` on a pure function; no database.
5. CI for {{git.host}}. <!-- Inline the rendered workflow from reference/ci.md with setup-node 22 and, for pnpm, pnpm/action-setup. Omit for local only. --> {{For pnpm: `pnpm/action-setup@v4` needs a `packageManager` field in `package.json`; add `"packageManager": "pnpm@<installed version>"` when `create-next-app` did not write it.}}
6. The one {{page at src/app/{{path}}/page.tsx / route at src/routes/{{name}}.ts}} for the most important path, reading through Prisma when the path needs data.
7. `README.md`: install, dev, test commands. Check they match `CLAUDE.md`.
8. Before writing code, start the branch `{{first prefix}}/walking-skeleton` from `main`; commit there, and open the {{pull request / merge request}} when the criteria pass. Local only: merge to `main`.

## Acceptance criteria

- [ ] `{{pm run dev}}` starts with no errors and {{the page / the route}} responds.
- [ ] `{{pm run test}}` passes with at least one test.
- [ ] `{{pm bin}} prisma migrate dev` has been run once and `prisma/migrations/` is committed.
- [ ] "{{4.4}}" can be demonstrated in its thinnest form.
- [ ] CI is green on {{git.host}} for this branch. <!-- Omit for local only. -->
- [ ] `.env.example` lists `DATABASE_URL` and every other variable the code reads; no secret is in the repository.

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

Keep the skeleton test free of the database so CI needs no service. Playwright, when chosen, is installed by the first slice with a screen to test, with `{{pm bin}} playwright install`.

<!-- Keep the next paragraph only when the most important path needs a signed-in user. -->
The most important path needs a signed-in user and sign-in does not exist yet. Use one fixed placeholder identity, a constant in code and never a real account, and name it as such; the sign-in task replaces it with the Auth.js user.
