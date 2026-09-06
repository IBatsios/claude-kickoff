# kickoff — confirmed design

The record of what was decided for the `kickoff` Claude Code plugin, agreed on 2026-09-05 after a design interview. Anything not in this document is undecided, not implied. Written for developers and non-developers alike.

Three words used throughout:

- **intake**: the form. One Markdown file per project at `docs/intake.md`.
- **build**: the step that turns a completed intake into documents and tasks.
- **runbook**: the ordered "what to do next" document the build produces.

## 1. What it is

- A public Claude Code plugin named `kickoff`. Source repo `claude-kickoff` on GitHub, public. Optional mirror on `gitlab.featurama.com`. MIT licensed.
- One command, `/kickoff`, backed by one skill. The skill is human-invoked only (`disable-model-invocation: true`) because it runs `git init` and writes files.
- Audience is anyone with Claude Code. Yanni's own setup is never assumed; it lives in a learned defaults file (section 8).
- Releases use semver tags and a `CHANGELOG.md`. `CONTRIBUTING.md` has one main section: how to add a first-class stack.

## 2. Who it is for

- A developer starting a software project from an empty directory.
- Non-developer collaborators, who fill the intake in any editor. A developer runs the build. The collaborator gets the PRD back; it is written to be readable by them.
- Not for: existing codebases (v2), non-software projects.

## 3. How a run goes

### Command grammar: state detection, no flags

| Directory state | What `/kickoff` does |
|---|---|
| Empty | Starts the walkthrough |
| `docs/intake.md` exists, incomplete | Resumes at the next unanswered section |
| Intake complete, no generated docs | Builds, after the confirm step |
| Generated docs present | Offers to regenerate; overwrites after confirmation |
| Other files present | Refuses and says why |

`/kickoff form` writes a blank intake and stops. The skill always states which mode it picked and why before doing anything. Flags get added only if detection proves ambiguous in practice.

### The walkthrough

- One section per exchange, fourteen sections in a fixed order.
- Menu fields use structured multiple-choice prompts. Prose fields are free text.
- The intake is written to disk after every section, so abandoning and resuming costs nothing.
- The stack is asked every time, one menu per layer, with the user's saved defaults pre-selected.
- Installed skills are detected by reading the user and project skill directories. The ones that fit the stack are shown after Section 8 for the user to trim, with a count of the rest, since a machine may hold a couple of hundred.

### Confirm before build

The skill shows a short summary of what it understood and flags contradictions (for example, roles listed but "nobody signs in"), then waits for a yes. If the feature list implies more than about 25 tasks, it stops, says the scope is too big for a v1, and suggests moving should-have and could-have features to out of scope.

### Regenerate

Overwrites generated files after confirmation. Never touches the intake. Every generated file starts with a header: "Generated from docs/intake.md by kickoff vX.Y. Edit the intake, not this file." If the intake's version stamp is older than the skill, the skill warns, lists the questions added since, and asks only those.

## 4. The intake

- `docs/intake.md`: a YAML frontmatter holding the machine fields and a version stamp, then a Markdown body of fourteen sections.
- Menu answers live only in the frontmatter. The body holds prose. One source of truth per answer.
- Conditional sections are present and labeled ("answer only if..."), never hidden.
- Sections a non-developer cannot answer are marked **(developer)**.
- Required to build: identity, problem, users, core features including the single most important user path, stack, git host and visibility, shell. Everything else is optional; blank optional answers become an "Open questions" section in the PRD.
- "I don't know" is an accepted answer to any optional question, recorded as *unknown* rather than *skipped*.
- Menu fields accept any string. Known values get stack-aware templates; anything else is recorded verbatim and gets the generic templates. The confirm step flags near-misses and asks; it never silently matches.
- The full question list is in `docs/question-bank.md`.

## 5. What the build writes

| File | Contents |
|---|---|
| `docs/intake.md` | The form. Input only, never overwritten. |
| `docs/PRD.md` | Problem, users, user stories, must/should/could, out of scope, open questions. |
| `docs/ARCHITECTURE.md` | Stack, components, data model, integrations, deployment. |
| `docs/DECISIONS.md` | Decisions with a one-line rationale each. |
| `docs/RUNBOOK.md` | Phase 0 for a human, then the Phase 1 task index with blocking edges. |
| `docs/tasks/NN-slug.md` | One task per file. |
| `CLAUDE.md` | Six sections: project summary, stack, conventions in force, how to run and test, where docs and tasks live and how to pick the next task, installed skills to use. Nothing more. |
| `.env.example` | Derived from the stack and integrations sections. |

Then `git init -b main` and one commit on `main`, the only direct commit to it, since the scaffold is documents only; Task 01 opens the first branch and the first pull request. The skill never logs in, creates a remote, or pushes. Optional extras come from the defaults file, for example `handoff_docs: true` adds `docs/handoff-items/handoff-next-phase.md` pointing at the runbook.

## 6. The runbook

**Phase 0, for a human.** Every command is rendered for the chosen host and the user's shell, with the real host URL, owner, and repo name filled in. Tokens are never written anywhere; the CLI login prompts for them.

1. Create the remote. CLI path first (`gh` for GitHub, `glab` for GitLab, `tea` for Gitea), then "create it in the browser and `git remote add origin`" beneath as the fallback. Skipped for local-only projects, or when the repo already exists.
2. Set up the dev database, per the intake: a Docker Compose file and `docker compose up`, or "use your Postgres on localhost", or "paste your hosted connection string".
3. Fill `.env` from `.env.example`.
4. Secrets gate before the first push: `gitleaks detect` with an install pointer, and a grep for common key patterns as the fallback when gitleaks is missing. Applies to public and private repos alike.
5. If ECC is detected on the machine, run `/project-init`. Conditional; absent otherwise.
6. Push `main`, and protect it in the host's settings when the convention is on. The first merge request or pull request comes with Task 01.

**Phase 1, for an agent or a human.**

- Vertical-slice tasks, each cutting through every layer and demoable alone, sized to one session, with blocking edges and acceptance criteria.
- Task 01 is the walking skeleton: runs locally with one passing test and CI green on the host (GitHub Actions, GitLab CI, Gitea Actions; none for local-only).
- A deploy task exists only when a deployment target was chosen.
- Each task may carry a "Suggested skills" line, drawn only from skills detected on the machine. Tasks must be complete without any skill. ECC is recognized, never required.

## 7. Stacks

- First-class in v1: TypeScript with Next.js or Express, Prisma, PostgreSQL. This stack gets stack-aware task templates ("run the Prisma migration", not "set up the database").
- Everything else gets generic templates, which must be good enough to ship alone.
- Adding a stack means adding a template set and a fixture. That is the contributing doc's main section. Python is next, when someone asks.

## 8. Defaults and conventions

- Defaults file: `~/.claude/kickoff/defaults.yaml`, or under `$CLAUDE_CONFIG_DIR` when that variable is set, same keys as the intake frontmatter, so pre-filling the form is a plain merge. Cross-platform because every Claude Code user already has `~/.claude`. Skill detection follows the same directory, so a clean profile is one environment variable away.
- Learned: at the end of each run the skill shows which answers differed from the saved defaults and offers to save them. One prompt, never silent. The file is also hand-editable.
- Eligible to be saved: every `stack.*` field, `git.host`, `git.host_url`, `git.owner`, every `environment.*` field (OS, shell, dev database mode), `deployment.target`, every `conventions.*` field. Never saved: anything project-specific such as the problem, features, or data.
- Conventions ship with the skill as defaults and are asked in the walkthrough with the saved or shipped default pre-selected, so a project can differ from the defaults file: protect the default branch (work on branches, merge via MR/PR), branch prefixes `feature/` `fix/` `chore/`, conventional commit messages, always write `.env.example`, back up the database before migrations, handoff docs off.

## 9. Plugin internals

One skill with resource files beside it. `SKILL.md` stays short and points at the resources.

```
claude-kickoff/
  .claude-plugin/plugin.json
  skills/kickoff/SKILL.md
  skills/kickoff/templates/intake.md          blank form (the human-facing question bank)
  skills/kickoff/templates/docs/              one template per generated document
  skills/kickoff/templates/tasks/generic/     generic task templates
  skills/kickoff/templates/tasks/ts-prisma-postgres/
  fixtures/                                   three intakes with expected file lists
  docs/                                       this repo's own docs
```

Whether the question bank also needs a separate machine-readable file (for the contradiction checks and frontmatter schema) is decided during the build; `docs/question-bank.md` is the source for both.

## 10. Verification

- Three fixture intakes checked into the repo: the default TypeScript stack, a generic other-stack, and a local-only minimum. Each has an expected file list.
- One smoke run on a profile with no ECC and no defaults file. This is the run that proves the public claim.
- CI runs only model-free checks: markdown lint, frontmatter schema validation for the fixtures and the blank form, and a check that every template the skill references exists. Model-driven fixture runs are a release checklist, by hand.
- Dogfooding: a hand-written example of the output lives in this repo. The first live run is Yanni's next real app.

## 11. Commitments stated in the README

- No network calls and no telemetry.
- Every outbound action is a command the user pastes.
- English only in v1.
- A stated minimum Claude Code version, because the plugin format and structured prompts depend on it.

## 12. Deferred to v2

- Pushing tasks to a tracker as GitHub, GitLab, or Gitea issues.
- Existing-project intake.
- Diff-based regeneration that updates only affected docs.
- More first-class stacks.
- Non-English forms and output.

## 13. Rejected alternatives

Recorded so they are not re-argued.

- **A standalone web app.** A skill lives where the output is consumed and needs no hosting or accounts.
- **Composing the installed to-spec and to-tickets skills.** They assume an existing codebase and a configured tracker, and are not model-invocable, so a skill cannot chain them. Their templates were borrowed instead.
- **Runbook commands reading a project `.env`.** Loading one differs between bash and PowerShell, and it invites tokens into a file. Non-secret values are rendered into the commands directly.
- **Rendering every command for both shells.** Halves readability. The shell is asked once.
- **Asking the user to name a skill per task.** Tedious across fifteen to thirty tasks. Skills are detected and suggested instead.
- **A hard cap on task count.** A soft guard with a number on screen is what makes someone cut a feature.
- **Assuming the default stack with an override field.** Yanni wants the stack asked every time; defaults make that fast.
- **Coupling visibility to host.** Private GitHub repos and public Gitea repos both exist. Two answers, not one.
