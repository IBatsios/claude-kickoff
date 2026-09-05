<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Only when deployment.target is not local only. Written to docs/tasks/NN-deploy.md, after the skeleton and the sign-in task when there is one. -->

# {{NN}}: Deploy to {{deployment.target}}

**What to build:** The app runs at {{deployment.domain, or "the URL the target assigns"}} from the default branch, and a second deploy is one command or one merge.

**Blocked by:** 01{{, the sign-in task}}.

**Status:** ready

## Steps, in order

1. Create the app or project on {{deployment.target}}. <!-- The command or console path when known for this target; otherwise "confirm with the user". This is a human step when it needs an account. For "Docker on a server I control", the server's compose file is docker-compose.prod.yml; docker-compose.yml is the dev database's file when one exists. -->
2. Set every variable from `.env.example` in the target's environment settings. Production secrets live in {{10.5, or "the target's environment settings"}}.
3. Point the deployment at a production database, separate from the development one.
4. {{When deployment.domain is set: Attach the domain to the app on the target and create the DNS record it shows.}}
5. Run migrations as part of each release, before the new version serves traffic.
6. Deploy once from the default branch and walk "{{4.4}}" on the live URL.
7. Write the deploy procedure into `README.md`.

## Acceptance criteria

- [ ] Reachable at {{url}}.
- [ ] "{{4.4}}" works on the live URL.
- [ ] No secret is in the repository; every one is in the target's settings.
- [ ] A deploy from the default branch is repeatable, and `README.md` says how.
- [ ] {{When conventions.db_backup_before_migrate is true: A backup step precedes the migration in the release procedure.}}

## Suggested skills

<!-- Only detected skills that fit. Omit when none. -->
