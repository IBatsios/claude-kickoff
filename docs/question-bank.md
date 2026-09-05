# kickoff question bank — v0.1 draft for review

This is the product. Every question the intake asks, in order, with what the build does with the answer. Review this before any skill code is written. The blank form a person actually fills in is `skills/kickoff/templates/intake.md`; it is this document with the annotations stripped.

How to read this document:

- **Required** sections must be answered before a build runs. Blank optional answers become an "Open questions" section in the PRD.
- **(developer)** marks a section a non-developer collaborator can leave for the developer.
- **Key** is the frontmatter field, when the answer is a menu. Menu answers live only in the frontmatter; the body holds prose.
- **Defaults** marks answers eligible for `~/.claude/kickoff/defaults.yaml`.
- **Feeds** names the generated files that use the section.
- Answer types: `text`, `list` (one item per line), `single` (one option), `multi` (any options), `yes/no`.

Two rules that apply everywhere:

- **"I don't know" is an answer.** Any optional question accepts it. It is recorded in the PRD's open questions as *unknown*, distinct from a blank, which is recorded as *skipped*. Required questions do not accept it; the build needs a real answer.
- **"Other" is a free string, never a guess.** Every menu field accepts any text. Known values get the stack-aware templates. Anything else is recorded verbatim in the generated docs and gets the generic templates. The confirm step flags near-misses (for example "nextjs" against "Next.js") and asks, and never silently matches.

Rough size: 68 questions, 28 of them required. A developer filling only the required set takes about ten minutes; the full form is closer to twenty-five.

---

## Section 1 — Project identity (required)

Feeds: everything. This section names the thing.

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 1.1 | What is the project called? | text | `project.name` | |
| 1.2 | Short name for repo, package, and database (lowercase, hyphens). Leave blank to derive from 1.1. | text | `project.slug` | Used verbatim in commands. |
| 1.3 | One-line pitch: "<name> is a <thing> for <who> that <does what>." | text | | First line of the PRD, README, and CLAUDE.md. If this is hard to write, the project is not defined yet. |
| 1.4 | What kind of thing is it? | single: web app, API only, command-line tool, desktop app, mobile app, library, other | `project.type` | Decides whether there is a frontend and which task templates apply. |

## Section 2 — The problem (required)

Feeds: PRD.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 2.1 | What problem does this solve? Describe it from the point of view of the person who has it. | text | The PRD's problem statement. |
| 2.2 | Who has this problem today, and how do they cope now? | text | Reveals the incumbent: a spreadsheet, a competitor, doing nothing. |
| 2.3 | Why build it now? | text, optional, "I don't know" accepted | |
| 2.4 | What happens if it is never built? | text, optional, "I don't know" accepted | Cheap test of whether it matters. |

## Section 3 — Users and roles (required)

Feeds: PRD, ARCHITECTURE (permissions), tasks.

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 3.1 | Who uses it? One line per type of user: who they are and what they want from it. | list | | Every user story names one of these. |
| 3.2 | Do different users get to do different things? List the roles (for example admin, member, visitor), or write "one role". | list | | Checked against Section 6. |
| 3.3 | How many users at launch, and a year later? A rough guess is fine. | text, optional, "I don't know" accepted | | Sets sensible defaults for performance and hosting. |
| 3.4 | How technical are they? | single: not at all, comfortable with apps, developers | | Shapes error messages, onboarding, and the accessibility default. |

## Section 4 — Core features (required)

Feeds: PRD, tasks. Every must-have becomes at least one task.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 4.1 | Must have for v1. One per line, as "As a <role>, I can <do something>, so that <benefit>." | list | The task list is generated from this list. Vague lines make vague tasks. |
| 4.2 | Should have. Same shape. | list, optional | Built after the must-haves; first to be cut by the scope guard. |
| 4.3 | Could have. Same shape. | list, optional | Recorded in the PRD, not scheduled. |
| 4.4 | The single most important thing a user does with it. | text, required | Becomes the path the walking skeleton proves end to end. Required because the skeleton has nothing to aim at without it. |

## Section 5 — Data (optional)

Feeds: ARCHITECTURE (data model), tasks (schema), .env.example.

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 5.1 | The main things the app keeps track of. One per line: what it is and what it is connected to (for example "Invoice, belongs to a Customer, has many Line Items"). | list | | Seeds the data model. |
| 5.2 | What must never be lost or wrong? | list | | Decides backups, validation, and audit trails. |
| 5.3 | Does anything need to be deleted, or kept for a fixed time? | text | | Retention and privacy law. |
| 5.4 | Is any of it sensitive? | multi: personal details, payment data, health data, data about minors, none | `data.sensitive` | Drives the security and privacy sections and the secrets gate wording. |

## Section 6 — Sign-in and permissions (optional; answer 6.1, and skip the rest if the answer is no)

Feeds: ARCHITECTURE, tasks (the auth slice), .env.example (provider keys).

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 6.1 | Does anyone need to sign in? | yes/no | `features.auth` | Gates the rest of the section. |
| 6.2 | How? | multi: email and password, magic link, Google, GitHub, Apple, Microsoft, single sign-on (SAML or OIDC), other | `features.auth_methods` | Each provider is an env variable and a Phase 0 step. |
| 6.3 | Who can do what? A short table or list: role, then the things that role can do. | text | | Becomes the permission matrix. |
| 6.4 | Can visitors who are not signed in see anything? What? | text | | Public routes versus protected routes. |
| 6.5 | Is there an admin who manages other users? | yes/no | | Adds the admin slice. |

## Section 7 — Integrations (optional)

Feeds: ARCHITECTURE, .env.example, RUNBOOK Phase 0.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 7.1 | External services this depends on. One per line: name, what it is for, and whether you already have an account. Think payments, email, file storage, maps, analytics, AI, calendars. | list | Every one becomes an env variable and a Phase 0 "get the key" step. |
| 7.2 | Anything it must import from or export to? Files, other systems, formats. | text | |

## Section 8 — Stack (required) (developer)

Feeds: ARCHITECTURE, CLAUDE.md, tasks, .env.example, RUNBOOK. Defaults: every field in this section.

Menu answers go in the `stack` and `environment` blocks of the frontmatter. The body holds only 8.11. Saved defaults are pre-selected; every question is still asked.

| # | Question | Type | Key |
|---|---|---|---|
| 8.1 | Language | single: TypeScript, JavaScript, Python, Go, Rust, other | `stack.language` |
| 8.2 | Frontend | single: Next.js, React with Vite, Astro, Vue or Nuxt, SvelteKit, none, other | `stack.frontend` |
| 8.3 | Backend | single: Next.js route handlers, Express, Fastify, NestJS, FastAPI, Django, none, other | `stack.backend` |
| 8.4 | Database | single: PostgreSQL, SQLite, MySQL, MongoDB, none, other | `stack.database` |
| 8.5 | Data layer | single: Prisma, Drizzle, SQLAlchemy, Django ORM, raw driver, none, other | `stack.data_layer` |
| 8.6 | Styling | single: Tailwind, CSS Modules, plain CSS, styled-components, none, other | `stack.styling` |
| 8.7 | Tests | multi: Vitest, Jest, Playwright, pytest, Go test, other | `stack.tests` |
| 8.8 | Package manager | single: pnpm, npm, yarn, bun, uv, pip, cargo, Go modules, other | `stack.package_manager` |
| 8.9 | Your operating system | single: Windows, macOS, Linux | `environment.os` |
| 8.10 | Your shell | single: PowerShell, bash, zsh, fish | `environment.shell` |
| 8.11 | Anything the menus cannot capture: must-use libraries, must-avoid ones, pinned versions. | text, optional | |

Why 8.10 matters: every command in the runbook is rendered for this shell and no other.

First-class stack in v1: TypeScript, Next.js or Express, PostgreSQL, Prisma. Any other combination gets the generic task templates. A value not in a menu is written as-is (for example `frontend: SolidStart`), appears verbatim in the docs, and gets the generic templates. See the "other" rule at the top.

## Section 9 — Git host, visibility, and conventions (required) (developer)

Feeds: RUNBOOK Phase 0, the CI task, LICENSE, CLAUDE.md conventions section. Defaults: host, host URL, owner, and every conventions field.

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 9.1 | Where will the code live? | single: GitHub, GitLab, Gitea, other, nowhere yet (local only) | `git.host` | Picks the CLI and CI flavor. Local only skips every remote step. |
| 9.2 | Host URL, if not GitHub and not local only (for example `https://gitlab.example.com`). | text | `git.host_url` | Rendered into the login and create commands. |
| 9.3 | Owner: the user or group the repository is created under. | text | `git.owner` | Rendered into the create command and remote URL. |
| 9.4 | Public or private? | single: public, private | `git.visibility` | Public adds the license question. The secrets gate applies to both. |
| 9.5 | License, only if public. | single: MIT, Apache-2.0, GPL-3.0, Unlicense, other | `git.license` | Default MIT. Writes LICENSE. |
| 9.6 | Does the repository already exist? If so, its URL. | text, optional | `git.existing_repo_url` | Skips the create step. |

Conventions are asked in the walkthrough with the saved or shipped default pre-selected. Blank in a hand-filled form means "use the default".

| # | Question | Type | Key | Shipped default |
|---|---|---|---|---|
| 9.7 | Protect the default branch? Work on branches and merge via pull or merge request. | yes/no | `conventions.protect_default_branch` | yes |
| 9.8 | Branch name prefixes. | list | `conventions.branch_prefixes` | feature, fix, chore |
| 9.9 | Commit message style. | single: conventional, free | `conventions.commit_style` | conventional |
| 9.10 | Always keep a `.env.example` listing required variables? | yes/no | `conventions.env_example` | yes |
| 9.11 | Back up the database before every migration? | yes/no | `conventions.db_backup_before_migrate` | yes |
| 9.12 | Write a handoff document at the end of each phase? | yes/no | `conventions.handoff_docs` | no |

## Section 10 — Deployment, hosting, and dev environment (optional, except 10.3 when a database was chosen) (developer)

Feeds: ARCHITECTURE, RUNBOOK Phase 0, the deploy task. Defaults: target, dev database.

| # | Question | Type | Key | Why it matters |
|---|---|---|---|---|
| 10.1 | Where will it run? | single: Vercel, Netlify, Cloudflare, Fly.io, Railway, Docker on a server I control, desktop packaging (Tauri or Electron), nowhere yet (local only), other | `deployment.target` | "Local only" means no deploy task is generated. |
| 10.2 | Domain, if you have one. | text | `deployment.domain` | |
| 10.3 | Database for development. Required when 8.4 is not "none". | single: Docker Compose, already installed on localhost, hosted connection string | `environment.dev_database` | Phase 0 renders a compose file, a "use your local instance" note, or a "paste your connection string" step. |
| 10.4 | Which environments will exist? | multi: development, staging, production | `deployment.environments` | No staging changes the migration advice: back up before every migration. |
| 10.5 | Where do secrets live in production? | text | | Platform variables, a vault, a file on the server. Shapes the deploy task. |

## Section 11 — Non-functional needs (optional)

Feeds: PRD, ARCHITECTURE, acceptance criteria on UI tasks.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 11.1 | How many people use it at once, and how fast must it feel? | text | Turns into concrete performance criteria or an explicit "not a concern". |
| 11.2 | Accessibility target. | single: WCAG 2.2 AA, best effort, not a priority | Becomes an acceptance criterion on every UI task. |
| 11.3 | Devices and browsers that must work. | multi: desktop, phone, tablet, specific browsers (name them) | |
| 11.4 | Must it work offline? | yes/no | Changes the architecture substantially. |
| 11.5 | Languages the interface must support. | text, default English only | |
| 11.6 | Security or compliance requirements you know of (GDPR, HIPAA, SOC 2, none known). | text | |
| 11.7 | Uptime expectation. | single: hobby, business hours, always on | Sizes hosting and monitoring. |

## Section 12 — Constraints (optional)

Feeds: PRD, RUNBOOK ordering, the scope guard.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 12.1 | Deadline or first milestone. | text | |
| 12.2 | Budget for paid services. | single: free tiers only, some, not a concern | Filters integration and hosting suggestions. |
| 12.3 | Who is working on it? One per line: name, role, developer or not. | list | Names the people the runbook addresses. |
| 12.4 | Existing assets to reuse: designs, brand, domain, content, code. | list | |
| 12.5 | Must-use or must-avoid technology, vendors, or licenses. | text | |

## Section 13 — Out of scope (optional, strongly encouraged)

Feeds: PRD, the scope guard.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 13.1 | Things this will explicitly not do in v1. | list | The scope guard moves should and could items here; a pre-filled list makes those cuts faster. |
| 13.2 | Things people will ask for that you are saying no to, and why. | list | Saves the same argument later. |

## Section 14 — Definition of done for v1 (optional)

Feeds: PRD, the final task.

| # | Question | Type | Why it matters |
|---|---|---|---|
| 14.1 | What must be true to call v1 done? Checkable statements, one per line. | list | Becomes the acceptance criteria of the last task. |
| 14.2 | A month after launch, how will you know it worked? | text | |

---

## Contradiction checks run before build

The confirm step lists any of these it finds and asks the user to resolve them.

| Check | Sections |
|---|---|
| Roles listed, but nobody signs in | 3.2 vs 6.1 |
| A payments integration, but payment data not marked sensitive | 7.1 vs 5.4 |
| Project type is web app, but frontend is none | 1.4 vs 8.2 |
| A data layer chosen, but database is none, or the reverse | 8.4 vs 8.5 |
| Database chosen, but no dev database mode | 8.4 vs 10.3 |
| Deployment target is local only, but a domain or a production environment is given | 10.1 vs 10.2, 10.4 |
| Public, but no license | 9.4 vs 9.5 |
| Offline required, but every must-have depends on a server | 11.4 vs 4.1 |
| Shell is PowerShell on macOS or Linux, or bash on Windows | 8.9 vs 8.10 (possible, so warn, do not block) |
| More than twelve must-haves | 4.1 (early warning that the scope guard will fire) |

## Frontmatter schema

The exact YAML block is in the blank form. Keys, in order: `kickoff_version`, `project`, `data`, `features`, `stack`, `environment`, `git`, `deployment`, `conventions`. Menu fields accept any string; the listed options are the ones with stack-aware behavior. A blank `conventions` value means "use the skill's default or my saved default".

## Review decisions (2026-09-05)

Yanni reviewed the v0.1 draft. Outcomes, so they are not re-asked:

1. **Length.** No questions cut. Instead, optional questions accept "I don't know", recorded as *unknown* rather than *skipped*. 11.7 and 12.4 stay as they are.
2. **4.4 is required.** The walking skeleton targets it.
3. **Section 6 stays** before the stack, where a non-developer reaches it.
4. **Conventions are asked** in the walkthrough, as 9.7 to 9.12, with defaults pre-selected.
5. **"Other" is a free string, never a guess.** Recorded verbatim, generic templates, near-misses flagged at confirm time.
6. **Sensitive-data categories** stay as the four listed.
