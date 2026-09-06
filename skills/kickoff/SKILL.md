---
name: kickoff
description: Turn an intake form into a Claude Code-ready project: PRD, architecture, decisions, runbook, one file per task, CLAUDE.md, .env.example.
argument-hint: "[form]"
disable-model-invocation: true
---

# kickoff

The current directory becomes the project. The **intake** is `docs/intake.md`: a YAML frontmatter of machine fields and a Markdown body of fourteen sections. A **build** turns a complete intake into documents and tasks. The **runbook** is the ordered what-to-do-next the build writes.

Three rules hold in every mode:

- The intake is the single source of truth. Generated files are derived from it and say so in their first line, except `LICENSE`, which is the license text verbatim. The build never edits the intake.
- Every outbound action is a command the user pastes from the runbook. You run `git init` and one local commit. You never log in, create a remote, or push, and you never write a token anywhere.
- Menu answers live only in the frontmatter, the body holds prose, and a value outside a menu is written verbatim. The confirm step catches near-misses; nothing is silently matched.

## 1. Pick the mode

Look at the directory and the argument, choose exactly one mode, and tell the user which one and why in one line that names the directory's absolute path, before doing anything else. A session started in the wrong folder is then obvious at a glance.

| Condition | Mode |
|---|---|
| Argument is `form` | **Form**: copy `templates/intake.md` to `docs/intake.md`, say where it is and that it can be filled in any editor, stop. |
| No `docs/intake.md`, and the directory holds nothing but `.git/` and `docs/` | **Walkthrough** (section 2) |
| `docs/intake.md` exists and any required field in `reference/checks.md` is blank | **Walkthrough**, resuming at the first section with a blank required field |
| Intake complete, no `docs/PRD.md` | **Confirm** (section 3), then **Build** (section 4) |
| `docs/PRD.md` exists | **Regenerate** (section 5) |
| Anything else in the directory | **Refuse**: list the files, say kickoff only starts from an empty directory, stop. |

Done when the mode is stated and the user can see the reason.

## 2. Walkthrough

Before the first section: load `reference/defaults.md` to read the defaults file if it exists, and detect installed skills (section 6). One section per exchange, in the form's order, fourteen sections. A section that mixes menu and prose fields takes two exchanges, the prompt and then the chat; that is the cost of the structured prompt, not a defect. For each section:

- Ask menu fields with the structured question prompt when it is available: the saved default first, then the likeliest three, and the free-text option is where any other value goes, written verbatim. Ask prose fields in plain chat, all of a section's prose questions in one message. Write prose exactly as typed, correcting only an obvious typo and saying so in the same message.
- When the user defers a whole block ("I'll defer to you" on the stack), offer one complete set with a one-line reason per field and confirm it with a single structured question; every field still passes through an explicit yes.
- On an optional section, propose an answer for each question that earlier sections imply, so that one word accepts the lot; an accepted proposal is written as the answer. A question with nothing to propose stays blank unless the user answers it.
- After Section 8, show the detected skills that fit the stack and the project type (section 6) and let the user trim the list.
- Present conditional sections only when their gate is open: Section 6 after `features.auth` is true, the license after `visibility` is public, the dev database after a database is chosen. In the file they stay present and labeled.
- Accept "I don't know" on any optional question and write it as the answer. Required questions need a real answer; ask again with one sentence on why it is needed.
- Write `docs/intake.md` after every section, frontmatter and body, so abandoning costs nothing.

Done when every required field in `reference/checks.md` holds a real answer. Then go to section 3.

## 3. Confirm

Run every check in `reference/checks.md`: required fields, contradictions, near-misses, and the scope guard. Show the user one summary of at most fifteen lines: pitch, users, count of must-haves, the stack on one line, host and visibility, dev database, the projected task count, and every check that fired. When no walkthrough ran in this session, the same message also shows the detected skills that fit the stack (section 6) for the user to trim, since the walkthrough is where that otherwise happens. If the scope guard fired, stop here and ask which should-have or could-have features move to out of scope. Wait for a yes; on anything else, amend the intake as instructed and re-run the checks.

Done when the user has said yes to a summary with no open checks.

## 4. Build

1. **Choose the template set.** `templates/tasks/ts-prisma-postgres/` when `language` is TypeScript, `backend` is Next.js route handlers or Express, `database` is PostgreSQL, and `data_layer` is Prisma. Otherwise `templates/tasks/generic/`. Say which.
2. **Write the documents** from `templates/docs/`, in this order: `PRD.md`, `ARCHITECTURE.md`, `DECISIONS.md`, the task files, `RUNBOOK.md`, `CLAUDE.md` at the project root from `templates/docs/CLAUDE.template.md`, `.env.example` and `.gitignore` at the root, `LICENSE` when visibility is public, `docker-compose.yml` when the dev database is Docker Compose, and `docs/handoff-items/handoff-next-phase.md` when `conventions.handoff_docs` is true. Each starts with the header line the template shows, carrying the version from `../../.claude-plugin/plugin.json`. The build writes documents and configuration only; source code, package manifests, and CI files are Task 01's job. Write each generated file with the file-writing tool, one file per call; shell heredocs fail on these files' quoting. The shell is for git and checks.
3. **Write the tasks** into `docs/tasks/`, numbered from `01` in dependency order. `01` is the walking skeleton and targets the most important user path (4.4). One feature slice per must-have, split when one would not fit a single session. An auth slice when `features.auth` is true, before any slice that needs a signed-in user. A deploy task only when `deployment.target` is not local only. The last task is the definition of done, always from `templates/tasks/generic/definition-of-done.md`, since it is stack-independent. Work that only 7.2 (imports and exports) or Section 14 (definition of done) mentions, and no must-have covers, is attached to the closest slice or gets a slice of its own, and the PRD gains the story marked "(inferred)", when it needs code. A manual one-off, such as a one-time import the intake says is done by hand, becomes a step on the closest task, or a Phase 0 step when it must precede code, and no story. Every task names what blocks it, and carries a "Suggested skills" line only when a detected skill fits; a task reads complete without any skill, and the definition of done never carries one.
4. **Write the runbook.** Phase 0 from `reference/hosts.md`, `reference/dev-database.md`, and `reference/secrets-gate.md`, every command rendered for `git.host`, `environment.shell`, and the intake's real values. The ECC step appears only when `/project-init` was detected. Phase 1 is the task index with blocking edges.
5. **Init git.** If the directory is not a repository: `git init -b main`, then one commit of everything on `main` with the message `chore: kickoff scaffold`. The scaffold is documents only, so it is the one direct commit to `main`; Task 01 opens the first branch and the first pull request. When git has no `user.name` or `user.email`, show the two `git config --global` commands, skip the commit, and say so; the user commits after configuring.
6. **Offer defaults.** Follow `reference/defaults.md`: in a message of its own, show the eligible fields that differ from the saved defaults as a table, then ask once with the structured prompt whether to save them. When any differing value looks like a placeholder, such as an owner or domain containing `example`, the first option is to keep the saved defaults.

Done when every applicable file in `templates/expected-files.md` exists, the commit exists, and the user has answered the defaults question.

## 5. Regenerate

Compare the intake's `kickoff_version` with the plugin version. When the intake is older, list the questions added since from the "Questions added" sections of `../../CHANGELOG.md`, ask only those, and append the answers to the intake. Then say which files will be overwritten and wait for a yes. Run section 4 with the intake as it stands; step 5 commits on a branch named `<first branch prefix>/kickoff-regenerate` with the message `chore: kickoff regenerate`, since `main` may hold real work by now.

Done when the user has said yes and section 4 has completed.

## 6. Detecting installed skills

Claude Code's config directory is `$CLAUDE_CONFIG_DIR` when that variable is set and `~/.claude` otherwise; call it `<config>`. Read only names and descriptions from `<config>/skills/*/SKILL.md`, `.claude/skills/*/SKILL.md`, `<config>/commands/*.md`, and `<config>/plugins/cache/*/*/*/skills/*/SKILL.md`. A machine may hold a couple of hundred skills, most for other stacks, so show only the ones whose name or description fits the stack, the project type, or an answered need in Section 11 (accessibility, offline, performance, security), grouped, with a count of the rest and a note that any of them can be added by name. Show that list once, after Section 8 of the walkthrough or else in the confirm step, and let the user trim it. ECC is present when a `project-init.md` command exists under `<config>/commands/` or under `<config>/plugins/cache/*/*/*/commands/`. Nothing detected means every task simply has no suggested-skills line.
