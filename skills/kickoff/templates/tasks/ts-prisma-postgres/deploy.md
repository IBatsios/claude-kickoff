<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Only when deployment.target is not local only. Written to docs/tasks/NN-deploy.md after the skeleton and the sign-in task. Keep the block for the intake's target; for a target not listed, use the generic set's deploy template instead. Same {{pm}} rendering as the skeleton. -->

# {{NN}}: Deploy to {{deployment.target}}

**What to build:** The app runs at {{deployment.domain, or "the URL the target assigns"}} from the default branch, migrations run on every release, and a second deploy is one command or one merge.

**Blocked by:** 01{{, the sign-in task}}.

**Status:** ready

## Steps, in order

<!-- Vercel -->
1. Connect the repository in the Vercel dashboard, or run `{{pm dlx}} vercel link` in this directory. This is a human step: it needs the account.
2. Build command: `prisma generate && next build` (Next.js) or `prisma generate && tsc` (Express). Set it in the project settings.
3. Set every variable from `.env.example` in the project's environment variables, with a production `DATABASE_URL` that is not the development database.
4. Migrations on release: add `prisma migrate deploy` to the build command before the build, or run it from a release step.
5. Deploy from the default branch and walk "{{4.4}}" on the live URL.
<!-- Docker on a server I control -->
1. Add a multi-stage `Dockerfile` on `node:22-alpine`: install, `prisma generate`, build, then a runtime stage that runs `prisma migrate deploy` and starts the app.
2. Write `docker-compose.prod.yml` for the server: the app, and a `postgres:16` service with a named volume, both reading their environment from a `.env` on the server that is never committed. `docker-compose.yml`, when it exists, is the dev database's file and stays as it is.
3. Copy the project to the server, fill the server's `.env`, and run `docker compose -f docker-compose.prod.yml up -d --build`.
4. Put a reverse proxy with TLS in front of the app port ({{Caddy or nginx; confirm with the user}}) for {{deployment.domain}}.
5. Walk "{{4.4}}" on the live URL.
<!-- Fly.io or Railway -->
1. `fly launch` or `railway init` in this directory; accept the generated config. Human step: needs the account.
2. Set every variable from `.env.example` with `fly secrets set` or `railway variables`, with a production `DATABASE_URL`.
3. Add `prisma migrate deploy` as the release command.
4. Deploy and walk "{{4.4}}" on the live URL.
<!-- Netlify or Cloudflare -->
1. Next.js on this target needs the target's adapter; Express does not run here without a serverless wrapper. Confirm the approach with the user before building, and record it in `docs/DECISIONS.md`.
<!-- Desktop packaging -->
1. A web stack does not package as a desktop app by itself. Confirm with the user whether Tauri wraps the Next.js app, and record it in `docs/DECISIONS.md`.

6. Write the deploy procedure into `README.md`.

## Acceptance criteria

- [ ] Reachable at {{url}}.
- [ ] "{{4.4}}" works on the live URL.
- [ ] `prisma migrate deploy` runs on every release before traffic is served.
- [ ] No secret is in the repository; every one is in the target's settings or the server's `.env`.
- [ ] A deploy from the default branch is repeatable, and `README.md` says how.
- [ ] {{When conventions.db_backup_before_migrate is true: A backup step precedes the migration in the release procedure.}}

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->
