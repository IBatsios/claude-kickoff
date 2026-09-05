<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Only when features.auth is true. Written to docs/tasks/NN-sign-in.md, numbered before any slice that needs a signed-in user. -->

# {{NN}}: Sign-in and roles

**What to build:** A {{role}} can sign in with {{features.auth_methods}} and the app knows which role they hold. Visitors who are not signed in can {{6.4}}. {{When 6.5 is yes: An admin can manage other users' roles.}}

**Blocked by:** 01.

**Status:** ready

## Steps, in order

1. Choose the sign-in library the {{stack.backend / stack.frontend}} community uses for {{features.auth_methods}}: {{name it when known for this stack, otherwise "confirm with the user"}}.
2. Add the user and role to the data model, and write the migration.
3. Sign in, sign out, and a session that survives a page reload or a second command.
4. A guard that enforces the role matrix from `docs/PRD.md` on every protected {{screen / route / command}}.
5. Tests: a signed-out visitor is refused or redirected from a protected place; each role sees exactly its allowed actions.

## Acceptance criteria

- [ ] Sign-in works with every method in {{features.auth_methods}}.
- [ ] Every row of the role matrix is enforced and has a test.
- [ ] Provider credentials live in `.env` only; `.env.example` carries placeholders for each.
- [ ] Earlier tests still pass; CI is green. <!-- Drop the CI clause for local only. -->

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->

## Notes

Email and password sign-in means storing password hashes; use the library's recommended hashing and never roll your own. Magic links need an email sender, which is an integration with its own key in `.env.example`.
