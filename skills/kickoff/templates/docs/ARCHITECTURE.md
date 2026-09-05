<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Describe only what the intake states or directly implies. Where the intake is silent, say "not specified" rather than choosing. -->

# {{project.name}} — Architecture

## Stack

| Layer | Choice |
|---|---|
| Language | {{stack.language}} |
| Frontend | {{stack.frontend}} |
| Backend | {{stack.backend}} |
| Database | {{stack.database}} |
| Data layer | {{stack.data_layer}} |
| Styling | {{stack.styling}} |
| Tests | {{stack.tests}} |
| Package manager | {{stack.package_manager}} |

<!-- One line: "Task templates: ts-prisma-postgres" or "Task templates: generic". Then 8.11 verbatim when answered. -->

Task templates: {{set}}. Notes from the intake: {{8.11}}

## Components

<!-- Derive from project.type and the stack. A web app with a backend and database has three: the frontend, the API, the database. Add a "background jobs" component only when an integration or a must-have implies work outside a request (email sending, imports, scheduled tasks). A CLI or library has one. One short paragraph each: what it owns, what it talks to. -->

### {{component}}

{{what it owns and what it talks to}}

## Data model

<!-- From 5.1. When there are two or more entities, draw them: -->

```mermaid
erDiagram
    {{ENTITY_A}} ||--o{ {{ENTITY_B}} : has
```

<!-- Then one line per entity: name, the fields the intake mentions, and any "must never be lost or wrong" rule from 5.2 attached to the entity it protects. Sensitive categories from data.sensitive are named on the entities that hold them. -->

## Sign-in and permissions

<!-- Only when features.auth is true. Name the methods, where sessions live (as implied by the template set: Auth.js with the Prisma adapter for ts-prisma-postgres, "not specified" for generic), and reproduce the role matrix from the PRD. -->

## Integrations

| Service | Purpose | Environment variables | Account |
|---|---|---|---|
| {{name}} | {{purpose}} | {{VAR_NAMES}} | {{exists / needed}} |

<!-- Variable names here are the same ones written to .env.example. -->

## Environments and deployment

- Deployment target: {{deployment.target}}
- Domain: {{deployment.domain, or "none yet"}}
- Environments: {{deployment.environments}}
- Development database: {{environment.dev_database}}
- Production secrets live in: {{10.5, or "not specified"}}

<!-- When environments lack staging and conventions.db_backup_before_migrate is true, add one line: migrations run against production directly, so every migration is preceded by a backup. -->

## Non-functional design notes

<!-- Only the answered items from Section 11, each with what it implies for the design in one line. Examples: WCAG 2.2 AA implies an accessibility check in every UI task's acceptance criteria; offline implies a local store and a sync strategy, which is not specified. -->

## Conventions in force

<!-- The resolved conventions block: intake value, else defaults file, else shipped default. One line each. -->

- Default branch protected: {{value}}
- Branch prefixes: {{value}}
- Commit style: {{value}}
- `.env.example` maintained: {{value}}
- Database backup before every migration: {{value}}
- Handoff docs: {{value}}
