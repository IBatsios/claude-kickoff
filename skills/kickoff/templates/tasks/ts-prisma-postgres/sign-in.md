<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Only when features.auth is true. Written to docs/tasks/NN-sign-in.md, numbered before any slice that needs a signed-in user. Same {{pm}} rendering as the skeleton. Keep the Next.js or the Express lines, not both. -->

# {{NN}}: Sign-in and roles

**What to build:** A {{role}} can sign in with {{features.auth_methods}} and the app knows which role they hold. Visitors who are not signed in can {{6.4}}. {{When 6.5 is yes: An admin can change other users' roles.}}

**Blocked by:** 01.

**Status:** ready

## Steps, in order

1. Install Auth.js with the Prisma adapter: {{`{{pm add}} next-auth@beta @auth/prisma-adapter` / `{{pm add}} @auth/express @auth/prisma-adapter`}}.
2. Schema: add the Auth.js models (`User`, `Account`, `Session`, `VerificationToken`) to `prisma/schema.prisma`, plus a `role` enum on `User` with the values {{roles from 3.2}}. Then `{{pm bin}} prisma migrate dev --name auth`.
3. Secret: `{{pm dlx}} auth secret` writes `AUTH_SECRET` to `.env`; add the placeholder to `.env.example`.
4. Providers, one per method in {{features.auth_methods}}: OAuth providers take `{{PROVIDER}}_CLIENT_ID` and `{{PROVIDER}}_CLIENT_SECRET` from the provider's developer console; magic link takes an email sender and its key; email and password uses the Credentials provider with argon2 hashing (`{{pm add}} argon2`).
5. Guard: {{`src/middleware.ts` matching every protected path / a middleware on every protected route}} that reads the session and enforces the role matrix from `docs/PRD.md`.
6. Tests: a signed-out request to a protected {{page / route}} is redirected or refused; each role reaches exactly its allowed actions.

## Acceptance criteria

- [ ] Sign-in works with every method in {{features.auth_methods}}, and sign-out ends the session.
- [ ] Every row of the role matrix is enforced and has a test.
- [ ] `AUTH_SECRET` and every provider credential are in `.env` only, with placeholders in `.env.example`.
- [ ] The auth migration is committed under `prisma/migrations/`.
- [ ] Earlier tests still pass; CI is green. <!-- Drop the CI clause for local only. -->

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

Auth.js treats email and password as the least preferred method; keep it only if the intake asked for it, and never store a password without hashing.
