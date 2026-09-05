---
# kickoff intake. Fill this in, then run /kickoff in the project folder.
# The block between the --- lines is for the developer. Everyone else: skip to "Section 1" below.
# Options are listed after each # sign. Write the option exactly as shown. Leave a field blank if you do not know.
# If your answer is not in the list, write your own. It is recorded as-is and gets the generic setup instead of a stack-specific one.

kickoff_version: 0.1.0

project:
  name: ""
  slug: ""                 # lowercase-with-hyphens; blank derives it from name
  type: ""                 # web app | API only | command-line tool | desktop app | mobile app | library | other

data:
  sensitive: []            # personal details | payment data | health data | data about minors | none

features:
  auth: false              # true if anyone signs in (Section 6)
  auth_methods: []         # email and password | magic link | Google | GitHub | Apple | Microsoft | single sign-on | other

stack:                     # (developer) Section 8
  language: ""             # TypeScript | JavaScript | Python | Go | Rust | other
  frontend: ""             # Next.js | React with Vite | Astro | Vue or Nuxt | SvelteKit | none | other
  backend: ""              # Next.js route handlers | Express | Fastify | NestJS | FastAPI | Django | none | other
  database: ""             # PostgreSQL | SQLite | MySQL | MongoDB | none | other
  data_layer: ""           # Prisma | Drizzle | SQLAlchemy | Django ORM | raw driver | none | other
  styling: ""              # Tailwind | CSS Modules | plain CSS | styled-components | none | other
  tests: []                # Vitest | Jest | Playwright | pytest | Go test | other
  package_manager: ""      # pnpm | npm | yarn | bun | uv | pip | cargo | Go modules | other

environment:               # (developer) Sections 8 and 10
  os: ""                   # Windows | macOS | Linux
  shell: ""                # PowerShell | bash | zsh | fish
  dev_database: ""         # Docker Compose | already installed on localhost | hosted connection string   (required if database is not none)

git:                       # (developer) Section 9
  host: ""                 # GitHub | GitLab | Gitea | other | local only
  host_url: ""             # only for GitLab, Gitea, other. Example: https://gitlab.example.com
  owner: ""                # the user or group the repository is created under
  visibility: ""           # public | private
  license: ""              # only if public: MIT | Apache-2.0 | GPL-3.0 | Unlicense | other
  existing_repo_url: ""    # only if the repository already exists

deployment:                # (developer) Section 10
  target: ""               # Vercel | Netlify | Cloudflare | Fly.io | Railway | Docker on a server I control | desktop packaging | local only | other
  domain: ""
  environments: []         # development | staging | production

conventions:               # (developer) Section 9. Asked in the walkthrough. Blank means "use kickoff's default, or my saved default".
  protect_default_branch:  # true | false     work on branches, merge via MR or PR
  branch_prefixes: []      # default: feature, fix, chore
  commit_style:            # conventional | free
  env_example:             # true | false
  db_backup_before_migrate:  # true | false
  handoff_docs:            # true | false
---

# Intake: <project name>

How to fill this in:

- Answer under each question, after the `>` mark. Write as much or as little as you like.
- "I don't know" is a real answer for any optional question. It is recorded as something to find out. A blank is recorded as something nobody considered. Prefer "I don't know".
- Sections marked **(developer)** can be left for the developer.
- Sections marked **required** must be answered before the build can run. Inside them, every question not marked (optional) is required. Everything else is optional; blanks become open questions in the plan.
- The build never edits this file. To change the plan later, change this file and run `/kickoff` again.

## Section 1 — Project identity (required)

Fill `project.name`, `project.slug`, and `project.type` at the top, then answer here.

### 1.3 One-line pitch: "<name> is a <thing> for <who> that <does what>."

_If this is hard to write, the project is not defined yet. That is worth knowing now._

>

## Section 2 — The problem (required)

### 2.1 What problem does this solve? Describe it from the point of view of the person who has it.

>

### 2.2 Who has this problem today, and how do they cope now?

_A spreadsheet, a competitor, doing nothing. Name the thing you are replacing._

>

### 2.3 Why build it now? (optional)

>

### 2.4 What happens if it is never built? (optional)

>

## Section 3 — Users and roles (required)

### 3.1 Who uses it? One line per type of user: who they are and what they want from it.

>

### 3.2 Do different users get to do different things? List the roles, or write "one role".

_For example: admin, member, visitor._

>

### 3.3 How many users at launch, and a year later? A rough guess is fine. (optional)

>

### 3.4 How technical are they? Choose one: not at all / comfortable with apps / developers.

>

## Section 4 — Core features (required)

### 4.1 Must have for v1. One per line: "As a <role>, I can <do something>, so that <benefit>."

_The task list is generated from this list. Vague lines make vague tasks._

>

### 4.2 Should have. Same shape. (optional)

_Built after the must-haves. First to be cut if the plan is too big._

>

### 4.3 Could have. Same shape. (optional)

_Recorded, not scheduled._

>

### 4.4 The single most important thing a user does with it.

_This is the first path that gets built end to end._

>

## Section 5 — Data (optional)

Fill `data.sensitive` at the top, then answer here.

### 5.1 The main things the app keeps track of. One per line: what it is and what it is connected to.

_For example: "Invoice, belongs to a Customer, has many Line Items."_

>

### 5.2 What must never be lost or wrong?

>

### 5.3 Does anything need to be deleted, or kept for a fixed time?

>

## Section 6 — Sign-in and permissions (optional)

Set `features.auth` at the top. If it is `false`, skip this section. If `true`, fill `features.auth_methods` and answer here.

### 6.3 Who can do what? A short list: the role, then the things that role can do.

>

### 6.4 Can visitors who are not signed in see anything? What?

>

### 6.5 Is there an admin who manages other users? yes / no

>

## Section 7 — Integrations (optional)

### 7.1 External services this depends on. One per line: name, what it is for, and whether you already have an account.

_Think payments, email, file storage, maps, analytics, AI, calendars. Each one becomes a setup step._

>

### 7.2 Anything it must import from or export to? Files, other systems, formats.

>

## Section 8 — Stack (required) (developer)

Fill the `stack` and `environment` blocks at the top. Every field is asked every time; saved defaults are only suggestions.

### 8.11 Anything the menus cannot capture: must-use libraries, must-avoid ones, pinned versions. (optional)

>

## Section 9 — Git host, visibility, and conventions (required) (developer)

Fill the `git` block at the top. Fill the `conventions` block too, or leave it blank to use the defaults. Nothing to answer here.

## Section 10 — Deployment, hosting, and dev environment (optional) (developer)

Fill the `deployment` block and `environment.dev_database` at the top. `dev_database` is required if a database was chosen.

### 10.5 Where do secrets live in production?

_Platform environment variables, a vault, a file on the server._

>

## Section 11 — Non-functional needs (optional)

### 11.1 How many people use it at once, and how fast must it feel?

>

### 11.2 Accessibility target. Choose one: WCAG 2.2 AA / best effort / not a priority.

>

### 11.3 Devices and browsers that must work.

>

### 11.4 Must it work offline? yes / no

>

### 11.5 Languages the interface must support. (default: English only)

>

### 11.6 Security or compliance requirements you know of. (GDPR, HIPAA, SOC 2, none known)

>

### 11.7 Uptime expectation. Choose one: hobby / business hours / always on.

>

## Section 12 — Constraints (optional)

### 12.1 Deadline or first milestone.

>

### 12.2 Budget for paid services. Choose one: free tiers only / some / not a concern.

>

### 12.3 Who is working on it? One per line: name, role, developer or not.

>

### 12.4 Existing assets to reuse: designs, brand, domain, content, code.

>

### 12.5 Must-use or must-avoid technology, vendors, or licenses.

>

## Section 13 — Out of scope (optional, strongly encouraged)

### 13.1 Things this will explicitly not do in v1.

>

### 13.2 Things people will ask for that you are saying no to, and why.

>

## Section 14 — Definition of done for v1 (optional)

### 14.1 What must be true to call v1 done? Checkable statements, one per line.

>

### 14.2 A month after launch, how will you know it worked?

>
