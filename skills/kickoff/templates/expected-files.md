# Expected files after a build

The build is done when every applicable line exists. Fixtures carry their own resolved copy of this list.

Always:

- `docs/intake.md` (untouched by the build)
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/DECISIONS.md`
- `docs/RUNBOOK.md`
- `docs/tasks/01-walking-skeleton.md`
- `docs/tasks/NN-<slug>.md`, one per must-have
- `docs/tasks/NN-definition-of-done.md`, the highest number
- `CLAUDE.md` at the project root
- `.env.example` at the project root
- `.gitignore` at the project root, listing at least `.env`
- A git repository whose only commit is on `main`, with no other branch; Task 01 opens the first one

When `features.auth` is true:

- `docs/tasks/NN-sign-in.md`, numbered before any slice that needs a signed-in user

When `deployment.target` is not local only:

- `docs/tasks/NN-deploy.md`

When `git.visibility` is public:

- `LICENSE` at the project root, the license text verbatim; the one generated file with no header

When `environment.dev_database` is Docker Compose:

- `docker-compose.yml` at the project root

When `conventions.handoff_docs` is true:

- `docs/handoff-items/handoff-next-phase.md`, pointing at the runbook

Never written by the build:

- Any source code, package manifest, or CI file. Those are Task 01's job, so the first build is reviewable as documents alone.
- Any file under `docs/tasks/` from a previous build that no longer corresponds to a task: the regenerate step deletes those after confirmation.
