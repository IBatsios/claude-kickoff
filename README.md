# kickoff

A Claude Code plugin. Run `/kickoff` in an empty directory, fill in a form (or hand it to a collaborator), and get a project an agent can start building: a PRD, an architecture doc, a decisions log, a runbook of what to do next, one file per task, a `CLAUDE.md`, and a `.env.example`.

It is built for the first hour of a project: the hour that usually goes to a blank page and a half-remembered checklist.

## Install

```
/plugin marketplace add YOUR-GITHUB-USER/claude-kickoff
/plugin install kickoff@claude-kickoff
```

Requires Claude Code 2.0 or later.

## Use

```
cd my-new-project
/kickoff
```

`/kickoff` looks at the directory and picks what to do:

| You have | It does |
|---|---|
| An empty directory | Walks you through the form, one section at a time |
| A half-filled `docs/intake.md` | Picks up where the form stops |
| A complete intake | Shows what it understood, waits for your yes, then builds |
| Generated docs already | Offers to regenerate from the intake |
| Other files | Refuses. kickoff starts from empty. |

`/kickoff form` writes a blank form and stops, so you can send it to someone who does not use Claude Code. They fill it in any editor; you run `/kickoff` when it comes back.

## What you get

```
docs/intake.md          the form, never overwritten
docs/PRD.md             problem, users, stories, must / should / could, open questions
docs/ARCHITECTURE.md    stack, components, data model, integrations, deployment
docs/DECISIONS.md       what was decided and why, one line each
docs/RUNBOOK.md         Phase 0 for you, Phase 1 for the agent
docs/tasks/NN-slug.md   one task per file, with acceptance criteria and blocking edges
CLAUDE.md               short and self-contained
.env.example
```

Phase 0 of the runbook is the human part: create the remote, set up the dev database, fill `.env`, scan for secrets, push. Every command is rendered for your git host and your shell, with your real values filled in. Phase 1 is vertical slices an agent can pick up in order, starting with a walking skeleton that runs locally with one passing test and green CI.

## Defaults that learn

The first run asks everything. At the end it offers to save the answers that rarely change (stack, host, shell, conventions) to `~/.claude/kickoff/defaults.yaml`. The next run pre-selects them. Edit the file by hand whenever you like.

## Stacks

Every stack works. One stack gets task templates with concrete commands rather than generic ones: TypeScript with Next.js or Express, Prisma, and PostgreSQL. Adding another is the main way to contribute; see `CONTRIBUTING.md`.

## Commitments

- No network calls. No telemetry.
- Every outbound action is a command you paste. The plugin never logs in, creates a remote, or pushes.
- It runs `git init` and makes one local commit on a feature branch. Nothing else touches git.
- English only, for now.

## License

MIT.
