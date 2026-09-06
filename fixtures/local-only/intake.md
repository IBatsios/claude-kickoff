---
kickoff_version: 0.1.0

project:
  name: "tidy"
  slug: "tidy"
  type: "command-line tool"

data:
  sensitive: ["none"]

features:
  auth: false
  auth_methods: []

stack:
  language: "Go"
  frontend: "none"
  backend: "none"
  database: "none"
  data_layer: "none"
  styling: "none"
  tests: ["Go test"]
  package_manager: "Go modules"

environment:
  os: "macOS"
  shell: "zsh"
  dev_database: ""

git:
  host: "local only"
  host_url: ""
  owner: ""
  visibility: "private"
  license: ""
  existing_repo_url: ""

deployment:
  target: "local only"
  domain: ""
  environments: []

conventions:                 # set explicitly so the fixture does not depend on the machine's defaults file
  protect_default_branch: true
  branch_prefixes: ["feature", "fix", "chore"]
  commit_style: "conventional"
  env_example: true
  db_backup_before_migrate: true
  handoff_docs: false
---

# Intake: tidy

## Section 1 — Project identity (required)

### 1.3 One-line pitch

> tidy is a command-line tool for me that moves screenshots and downloads into dated folders.

## Section 2 — The problem (required)

### 2.1 What problem does this solve?

> My desktop and downloads folder fill up with screenshots and PDFs I never file. Finding last week's screenshot means scrolling through hundreds.

### 2.2 Who has this problem today, and how do they cope now?

> Me. I select all and drag into a folder called "old" every few weeks.

### 2.3 Why build it now? (optional)

> I don't know

### 2.4 What happens if it is never built? (optional)

> I don't know

## Section 3 — Users and roles (required)

### 3.1 Who uses it?

> Me, on my own laptop.

### 3.2 Roles

> one role

### 3.3 How many users at launch, and a year later? (optional)

> One.

### 3.4 How technical are they?

> developers

## Section 4 — Core features (required)

### 4.1 Must have for v1

> As the user, I can run tidy on a folder and have every screenshot moved into a subfolder named by its month, so that the folder is empty of screenshots.
> As the user, I can run tidy with a dry-run flag and see what would move without moving it, so that I trust it before it touches anything.

### 4.2 Should have (optional)

>

### 4.3 Could have (optional)

>

### 4.4 The single most important thing a user does with it

> Run tidy on the desktop and watch the screenshots disappear into month folders.

## Section 5 — Data (optional)

### 5.1 The main things the app keeps track of

>

### 5.2 What must never be lost or wrong?

> A file. It must move, never copy-and-delete halfway, and never overwrite one with the same name.

### 5.3 Does anything need to be deleted, or kept for a fixed time?

>

## Section 6 — Sign-in and permissions (optional)

## Section 7 — Integrations (optional)

### 7.1 External services this depends on

>

### 7.2 Anything it must import from or export to?

>

## Section 8 — Stack (required) (developer)

### 8.11 Anything the menus cannot capture

> Standard library only if possible.

## Section 9 — Git host, visibility, and conventions (required) (developer)

## Section 10 — Deployment, hosting, and dev environment (optional) (developer)

### 10.5 Where do secrets live in production?

>

## Section 11 — Non-functional needs (optional)

### 11.1 How many people use it at once, and how fast must it feel?

>

### 11.2 Accessibility target

>

### 11.3 Devices and browsers that must work

>

### 11.4 Must it work offline?

> yes

### 11.5 Languages the interface must support

>

### 11.6 Security or compliance requirements you know of

>

### 11.7 Uptime expectation

>

## Section 12 — Constraints (optional)

### 12.1 Deadline or first milestone

>

### 12.2 Budget for paid services

>

### 12.3 Who is working on it?

>

### 12.4 Existing assets to reuse

>

### 12.5 Must-use or must-avoid technology, vendors, or licenses

>

## Section 13 — Out of scope (optional)

### 13.1 Things this will explicitly not do in v1

> Watching folders continuously. It runs when I run it.

### 13.2 Things people will ask for that you are saying no to, and why

>

## Section 14 — Definition of done for v1 (optional)

### 14.1 What must be true to call v1 done?

>

### 14.2 A month after launch, how will you know it worked?

>
