---
kickoff_version: 0.1.0

project:
  name: "Shelfmate"
  slug: "shelfmate"
  type: "web app"

data:
  sensitive: ["personal details"]

features:
  auth: true
  auth_methods: ["magic link", "Google"]

stack:
  language: "TypeScript"
  frontend: "Next.js"
  backend: "Next.js route handlers"
  database: "PostgreSQL"
  data_layer: "Prisma"
  styling: "Tailwind"
  tests: ["Vitest", "Playwright"]
  package_manager: "pnpm"

environment:
  os: "Windows"
  shell: "PowerShell"
  dev_database: "Docker Compose"

git:
  host: "GitHub"
  host_url: ""
  owner: "example-owner"
  visibility: "private"
  license: ""
  existing_repo_url: ""

deployment:
  target: "Vercel"
  domain: "shelfmate.example.com"
  environments: ["development", "production"]

conventions:                 # set explicitly so the fixture does not depend on the machine's defaults file
  protect_default_branch: true
  branch_prefixes: ["feature", "fix", "chore"]
  commit_style: "conventional"
  env_example: true
  db_backup_before_migrate: true
  handoff_docs: false
---

# Intake: Shelfmate

## Section 1 — Project identity (required)

### 1.3 One-line pitch

> Shelfmate is a shared reading list for a book club that picks the next book by vote.

## Section 2 — The problem (required)

### 2.1 What problem does this solve?

> Our club argues about the next book in a group chat for two weeks and then someone picks anyway. Suggestions get lost, nobody remembers who wanted what, and the person who missed the meeting never gets a say.

### 2.2 Who has this problem today, and how do they cope now?

> A book club of about fifteen people. We use a WhatsApp group and a shared Google Sheet that one person maintains and everyone else ignores.

### 2.3 Why build it now? (optional)

> The organizer is burning out on the spreadsheet and has threatened to quit.

### 2.4 What happens if it is never built? (optional)

> I don't know

## Section 3 — Users and roles (required)

### 3.1 Who uses it?

> Members: club regulars who want to suggest books and vote without scrolling a chat.
> Organizer: the person who runs the meetings and wants the pick settled a week before.

### 3.2 Roles

> organizer, member

### 3.3 How many users at launch, and a year later? (optional)

> 15 at launch. Maybe 30 if a second club joins.

### 3.4 How technical are they?

> comfortable with apps

## Section 4 — Core features (required)

### 4.1 Must have for v1

> As a member, I can propose a book with its title and author, so that it is on the list for the next vote.
> As a member, I can vote for up to three proposed books, so that my preference counts even when I miss the meeting.
> As a member, I can see the current pick and the vote tally, so that I know what to read next.
> As an organizer, I can close the vote and set the current pick, so that the club has a decision a week before the meeting.

### 4.2 Should have (optional)

> As a member, I can leave a short comment on a proposal, so that I can say why I suggested it.

### 4.3 Could have (optional)

> As a member, I can see which books the club has read this year, so that we do not repeat one.

### 4.4 The single most important thing a user does with it

> A member votes for the next book.

## Section 5 — Data (optional)

### 5.1 The main things the app keeps track of

> Club, has many Members and many Books.
> Member, belongs to a Club, has a role.
> Book, belongs to a Club, proposed by a Member, has many Votes, has a status (proposed, picked, read).
> Vote, belongs to a Member and a Book.

### 5.2 What must never be lost or wrong?

> Votes. A vote counted for the wrong book or dropped is the whole point failing.

### 5.3 Does anything need to be deleted, or kept for a fixed time?

> A member who leaves should be able to have their account removed.

## Section 6 — Sign-in and permissions (optional)

### 6.3 Who can do what?

> member: propose, vote, view the pick and tally, comment (later)
> organizer: everything a member can, plus close the vote, set the pick, and remove members

### 6.4 Can visitors who are not signed in see anything?

> No. Only the sign-in page.

### 6.5 Is there an admin who manages other users?

> yes, the organizer

## Section 7 — Integrations (optional)

### 7.1 External services this depends on

> Google Books API, to look up title and cover from a search, no account yet.
> Resend, to send the magic-link emails, account exists.

### 7.2 Anything it must import from or export to?

> Import the existing Google Sheet once, by hand is fine.

## Section 8 — Stack (required) (developer)

### 8.11 Anything the menus cannot capture

> Node 22. Prefer the App Router.

## Section 9 — Git host, visibility, and conventions (required) (developer)

## Section 10 — Deployment, hosting, and dev environment (optional) (developer)

### 10.5 Where do secrets live in production?

> Vercel environment variables.

## Section 11 — Non-functional needs (optional)

### 11.1 How many people use it at once, and how fast must it feel?

> A dozen at once at most, right after a meeting. Normal web speed.

### 11.2 Accessibility target

> WCAG 2.2 AA

### 11.3 Devices and browsers that must work

> Phone first, desktop second. Current Safari and Chrome.

### 11.4 Must it work offline?

> no

### 11.5 Languages the interface must support

> English only

### 11.6 Security or compliance requirements you know of

> none known

### 11.7 Uptime expectation

> hobby

## Section 12 — Constraints (optional)

### 12.1 Deadline or first milestone

> Before the October meeting.

### 12.2 Budget for paid services

> free tiers only

### 12.3 Who is working on it?

> Yanni, developer.
> Sam, organizer, not a developer, fills in this form and tests.

### 12.4 Existing assets to reuse

> The Google Sheet with this year's reads. A club logo as a PNG.

### 12.5 Must-use or must-avoid technology, vendors, or licenses

> Avoid anything that needs a credit card on file.

## Section 13 — Out of scope (optional)

### 13.1 Things this will explicitly not do in v1

> Buying or linking to buy books.
> A member belonging to more than one club.
> Meeting scheduling.

### 13.2 Things people will ask for that you are saying no to, and why

> Ratings and reviews. It turns the club into Goodreads, which is what we are escaping.

## Section 14 — Definition of done for v1 (optional)

### 14.1 What must be true to call v1 done?

> All fifteen current members have signed in once.
> The October pick was decided in the app, not in the chat.
> The organizer did not touch the spreadsheet in September.
> The vote tally on the pick page matches a hand count of votes in the database.

### 14.2 A month after launch, how will you know it worked?

> The WhatsApp group has no book-picking argument in it.
