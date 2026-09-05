<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines are instructions; remove them. Record only decisions the intake actually made. When the intake gives no reason, the "Why" column says "chosen in intake", never an invented rationale. Later decisions are appended by hand below the generated rows; the regenerate step keeps the hand-written rows. -->

# {{project.name}} — Decisions

One line per decision. Newest at the bottom. Reasons come from the intake; where it gave none, the reason is "chosen in intake" and can be filled in later.

| # | Decision | Why | Source |
|---|---|---|---|
| D1 | Stack: {{language}}, {{frontend}}, {{backend}}, {{database}} with {{data_layer}}, {{styling}}, tests with {{tests}}, {{package_manager}} | chosen in intake | Section 8 |
<!-- One row when 8.11 is answered; it holds must-use and must-avoid notes, not a reason for D1. -->
| D{{n}} | Must use: {{8.11}} | chosen in intake | Section 8 |
<!-- D2 for local only reads "Code lives locally, no remote yet, {{visibility}}". D3 for local only reads "Runs locally only; no deployment". D4 only when stack.database is not none. -->
| D2 | Code lives on {{git.host}}{{, at host_url}}, {{visibility}}{{, licensed license}} | {{"chosen in intake"}} | Section 9 |
| D3 | Runs on {{deployment.target}}{{; environments: ...}} | {{"chosen in intake"}} | Section 10 |
| D4 | Development database: {{environment.dev_database}} | {{"chosen in intake"}} | Section 10 |
<!-- D5 only when features.auth is true. -->
| D5 | Sign-in via {{auth_methods}}; roles: {{roles}} | {{"chosen in intake"}} | Sections 3, 6 |
<!-- One row per convention that differs from the shipped default. -->
| D{{n}} | {{convention}}: {{value}} (differs from the default {{default}}) | {{"chosen in intake"}} | Section 9 |
<!-- One row per must-use or must-avoid item in 12.5. -->
| D{{n}} | {{must use / must avoid}}: {{item}} | {{reason from 12.5 or "chosen in intake"}} | Section 12 |
<!-- One row per feature the scope guard moved out of scope at build time. -->
| D{{n}} | Out of scope for v1: {{feature}} | Scope guard: projected {{count}} tasks | Build |

<!-- Hand-written decisions go below this line. The regenerate step preserves everything after it. -->

---

## Added after the build
