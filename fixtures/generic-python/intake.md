---
kickoff_version: 0.1.0

project:
  name: "Pantry"
  slug: "pantry"
  type: "API only"

data:
  sensitive: ["none"]

features:
  auth: true
  auth_methods: ["email and password"]

stack:
  language: "Python"
  frontend: "none"
  backend: "FastAPI"
  database: "PostgreSQL"
  data_layer: "SQLAlchemy"
  styling: "none"
  tests: ["pytest"]
  package_manager: "uv"

environment:
  os: "Linux"
  shell: "bash"
  dev_database: "already installed on localhost"

git:
  host: "Gitea"
  host_url: "https://git.example.org"
  owner: "kitchen"
  visibility: "private"
  license: ""
  existing_repo_url: ""

deployment:
  target: "Docker on a server I control"
  domain: "pantry.example.org"
  environments: ["development", "production"]

conventions:
  protect_default_branch: true
  branch_prefixes: ["feat", "fix"]
  commit_style: "conventional"
  env_example: true
  db_backup_before_migrate: true
  handoff_docs: true
---

# Intake: Pantry

## Section 1 — Project identity (required)

### 1.3 One-line pitch

> Pantry is a stock-tracking API for a small restaurant kitchen that tells the cooks what is running low.

## Section 2 — The problem (required)

### 2.1 What problem does this solve?

> We find out we are out of something when a cook opens the walk-in during service. Orders go in late and we 86 dishes we should not have to.

### 2.2 Who has this problem today, and how do they cope now?

> One restaurant, six cooks, one manager. A clipboard on the walk-in door that gets updated when someone remembers.

### 2.3 Why build it now? (optional)

> I don't know

### 2.4 What happens if it is never built? (optional)

> The clipboard continues. It mostly works, it just costs us a few dishes a week.

## Section 3 — Users and roles (required)

### 3.1 Who uses it?

> Cooks: record what they used during prep and service, from a phone, fast.
> Manager: sees what is low and places orders.

### 3.2 Roles

> cook, manager

### 3.3 How many users at launch, and a year later? (optional)

> Seven. Same in a year.

### 3.4 How technical are they?

> not at all

## Section 4 — Core features (required)

### 4.1 Must have for v1

> As a cook, I can record that I used a quantity of an item, so that the stock count stays true.
> As a manager, I can see every item below its reorder level, so that I order before we run out.
> As a manager, I can record a delivery, so that the count goes back up.

### 4.2 Should have (optional)

> As a manager, I can set the reorder level per item, so that the low list matches how fast each thing moves.

### 4.3 Could have (optional)

> I don't know

### 4.4 The single most important thing a user does with it

> A cook records that an item was used.

## Section 5 — Data (optional)

### 5.1 The main things the app keeps track of

> Item, has a unit, a current quantity, and a reorder level.
> Movement, belongs to an Item and a User, is a use or a delivery, has a quantity and a time.

### 5.2 What must never be lost or wrong?

> Movements. The count is derived from them, so a lost movement is a wrong count.

### 5.3 Does anything need to be deleted, or kept for a fixed time?

> Keep movements for a year for the accountant.

## Section 6 — Sign-in and permissions (optional)

### 6.3 Who can do what?

> cook: record a use, see the item list
> manager: everything a cook can, plus record deliveries, see the low list, manage items and users

### 6.4 Can visitors who are not signed in see anything?

> No.

### 6.5 Is there an admin who manages other users?

> yes, the manager

## Section 7 — Integrations (optional)

### 7.1 External services this depends on

>

### 7.2 Anything it must import from or export to?

> Export movements as CSV for the accountant.

## Section 8 — Stack (required) (developer)

### 8.11 Anything the menus cannot capture

> Python 3.12. Alembic for migrations. The phone client is a later project; this is the API only.

## Section 9 — Git host, visibility, and conventions (required) (developer)

## Section 10 — Deployment, hosting, and dev environment (optional) (developer)

### 10.5 Where do secrets live in production?

> A .env file on the server, readable only by the service user.

## Section 11 — Non-functional needs (optional)

### 11.1 How many people use it at once, and how fast must it feel?

> Six cooks during a rush. A use must be recorded in under a second or nobody will bother.

### 11.2 Accessibility target

> not a priority

### 11.3 Devices and browsers that must work

>

### 11.4 Must it work offline?

> I don't know

### 11.5 Languages the interface must support

>

### 11.6 Security or compliance requirements you know of

> none known

### 11.7 Uptime expectation

> business hours

## Section 12 — Constraints (optional)

### 12.1 Deadline or first milestone

>

### 12.2 Budget for paid services

> free tiers only

### 12.3 Who is working on it?

> One developer, part time.

### 12.4 Existing assets to reuse

> A server already running Docker with a reverse proxy.

### 12.5 Must-use or must-avoid technology, vendors, or licenses

> Must run on our own server. No cloud database.

## Section 13 — Out of scope (optional)

### 13.1 Things this will explicitly not do in v1

> Ordering from suppliers.
> Recipes or menu costing.
> Any user interface beyond the API.

### 13.2 Things people will ask for that you are saying no to, and why

>

## Section 14 — Definition of done for v1 (optional)

### 14.1 What must be true to call v1 done?

> A cook can record a use from a phone browser hitting the API in under a second.
> The low list matched the walk-in on three consecutive mornings.
> The accountant received a CSV of last month's movements.

### 14.2 A month after launch, how will you know it worked?

> Fewer than two 86s a week caused by running out.
