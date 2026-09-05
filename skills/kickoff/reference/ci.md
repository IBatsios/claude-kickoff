# CI, per host

The walking skeleton (Task 01) is done only when CI is green on the host. Render the workflow file for `git.host` into the task's acceptance criteria and write the file itself as part of the skeleton task, with the install and test commands taken from the template set. Local only: no CI, and the task's criteria drop the CI line.

Replace `{{install}}` and `{{test}}` with the template set's commands. For `ts-prisma-postgres` they are `{{package manager}} install` and `{{package manager}} test`. For the generic set, use the commands the intake's stack implies and say in the task that the user should confirm them.

## GitHub Actions

`.github/workflows/ci.yml`:

```yaml
name: ci
on:
  push:
    branches-ignore: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        run: {{install}}
      - name: Test
        run: {{test}}
```

For the `ts-prisma-postgres` set, add `actions/setup-node@v4` with `node-version: 22` before Install, and `pnpm/action-setup@v4` when the package manager is pnpm.

## GitLab CI

`.gitlab-ci.yml`:

```yaml
stages: [test]
test:
  stage: test
  image: {{image}}
  script:
    - {{install}}
    - {{test}}
```

`{{image}}` is `node:22` for the `ts-prisma-postgres` set, and the closest official image for the intake's language otherwise (`python:3.12`, `golang:1.23`, `rust:1`), with a note in the task to confirm it.

## Gitea Actions

Same file shape as GitHub Actions, at `.gitea/workflows/ci.yml`. `actions/checkout@v4` and `actions/setup-node@v4` resolve on Gitea when the instance has Actions enabled; the task says to check the repository's Actions setting if the first run never starts.

## Other

No CI file. The skeleton's acceptance criteria say "tests pass locally" only, and the task notes that CI is set up by hand for this host.

## When Playwright is in the tests

The skeleton does not need it. The first slice that adds an end-to-end test adds a step before Test in the CI job: `{{pm bin}} playwright install --with-deps` (`pnpm playwright` / `npx playwright` / `yarn playwright` / `bunx playwright`). The feature-slice templates say so in their notes.

## When a database is needed in CI

The `ts-prisma-postgres` skeleton test does not need a database: it tests a pure function or a health route. Keep it that way, so CI has no service to provision. A later slice that needs one adds a Postgres service container to the workflow, and the feature-slice template says how.
