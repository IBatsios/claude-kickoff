# Checks

Run every check here before a build. Section numbers refer to the intake form. The runtime copy of the rules in the repo's `docs/question-bank.md`; keep the two in step.

## Required fields

A build needs a real answer for each of these. "I don't know" and blank both count as missing here.

Frontmatter: `project.name`, `project.type`, every `stack.*` field except `tests`, `environment.os`, `environment.shell`, `git.host`, `git.visibility`. Also `git.host_url` when host is GitLab, Gitea, or other; `git.owner` unless host is local only; `git.license` when visibility is public; `environment.dev_database` when `stack.database` is not none.

Body: 1.3 pitch, 2.1 problem, 2.2 who copes how, 3.1 users, 3.2 roles, 3.4 how technical, 4.1 at least one must-have, 4.4 the most important user path.

## Optional answers

Blank is recorded in the PRD's open questions as *skipped*. "I don't know" is recorded as *unknown*. Both are listed; the PRD says which is which.

## Contradictions

| Fires when | Sections | Action |
|---|---|---|
| Roles listed, but `features.auth` is false | 3.2 vs 6.1 | Ask which is right |
| A payments integration, but `data.sensitive` lacks payment data | 7.1 vs 5.4 | Ask, then add the category |
| Project type is web app, but frontend is none | 1.4 vs 8.2 | Ask which is right |
| A data layer chosen but database is none, or the reverse | 8.4 vs 8.5 | Ask which is right |
| Database chosen, but no dev database mode | 8.4 vs 10.3 | Ask 10.3 |
| Deployment target is local only, but a domain or a production environment is given | 10.1 vs 10.2, 10.4 | Ask which is right |
| Public, but no license | 9.4 vs 9.5 | Ask 9.5, offer MIT |
| Offline required, but every must-have needs a server | 11.4 vs 4.1 | Warn, do not block |
| PowerShell on macOS or Linux, or bash on Windows | 8.9 vs 8.10 | Warn, do not block |
| More than twelve must-haves | 4.1 | Warn that the scope guard will likely fire |

## Near-misses

A menu value that is not in the list is written verbatim and gets the generic templates. When it is within an edit or two of a known value, or a case or spacing variant, ask "did you mean X?" once and write whichever the user chooses. Known values are the option lists in the frontmatter comments of `templates/intake.md`. Common cases: `nextjs`, `next`, `NextJS` for Next.js; `postgres`, `psql`, `pg` for PostgreSQL; `tailwindcss` for Tailwind; `node` for JavaScript; `ts` for TypeScript.

## Scope guard

Projected task count is 1 for the walking skeleton, plus 1 per must-have (2 when a must-have names more than one role or more than one screen), plus 1 when `features.auth` is true, plus 1 when a deployment target is set, plus 1 for the definition of done. Above 25, stop before building, show the number, and ask which should-have or could-have features move to out of scope. A must-have list is what the user decided; propose cuts, never make them.
