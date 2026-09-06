<!-- Generated from docs/intake.md by kickoff v{{version}}. Edit the intake, not this file. -->
<!-- Builder: comment lines like this one are instructions. Remove them from the output. Fill every {{value}} from the intake; section numbers refer to the form. A section whose every answer is blank is omitted from the body, and its questions go under "Open questions" as skipped. The one exception is "Definition of done for v1", which stays with the fallback line. Questions behind a closed gate (reference/checks.md lists them) appear nowhere. -->

# {{project.name}} — Product Requirements

{{1.3 pitch, verbatim}}

## Problem

{{2.1, as written, first person of the user who has it}}

**Today:** {{2.2}}

<!-- Include the next two lines only when answered with something other than "I don't know". -->
**Why now:** {{2.3}}

**If it is never built:** {{2.4}}

## Users

| User | Wants | Role |
|---|---|---|
<!-- One row per line of 3.1. Role from 3.2; "one role" when that was the answer. A role in 3.2, or the admin in 6.5, that no line of 3.1 mentions gets its own row, with what it wants taken from where it appears and marked "(inferred)". -->
| {{who}} | {{what they want}} | {{role}} |

Scale: {{3.3, or "unknown"}}. Technical comfort: {{3.4}}.

## User stories

<!-- Normalize every line of 4.1 to 4.3 into "As a <role>, I can <do>, so that <benefit>". Keep the user's wording where it already fits; add the missing clause where it does not, and mark an added clause with "(inferred)" so it can be corrected. Number continuously across the three lists. Work that only 7.2 or Section 14 mentions and no story covers becomes a must-have story here, marked "(inferred)", so it has a task, when it needs code. A manual one-off, such as an import the intake says is done by hand, is not a story; it becomes a step on the closest task. -->

### Must have for v1

1. As a {{role}}, I can {{do}}, so that {{benefit}}.

### Should have

<!-- Omit the heading when 4.2 is blank. -->

### Could have

<!-- Omit the heading when 4.3 is blank. -->

## The most important path

{{4.4}}

This is the path Task 01, the walking skeleton, proves end to end before any other feature is built.

## Data

<!-- From Section 5. Omit when the whole section is blank. -->

{{5.1 as a list: entity, what it connects to}}

Must never be lost or wrong: {{5.2}}. Retention: {{5.3}}. Sensitive categories: {{data.sensitive, or "none"}}.

## Sign-in and permissions

<!-- Only when features.auth is true. When false, one line: "Nobody signs in." followed by "Every visitor sees the same thing." for a web app or API, or "It runs as whoever runs it." for anything else. -->

Methods: {{features.auth_methods}}. Visitors who are not signed in can: {{6.4}}. Admin manages users: {{6.5}}.

| Role | Can |
|---|---|
| {{role}} | {{from 6.3}} |

## Integrations

<!-- From 7.1 and 7.2. Omit the section when both are blank. The table renders only when 7.1 has entries; the imports-and-exports line only when 7.2 is answered. -->

| Service | For | Account exists |
|---|---|---|
| {{name}} | {{purpose}} | {{yes / no}} |

Imports and exports: {{7.2}}

## Non-functional requirements

<!-- From Section 11. Write each answered item as a checkable statement. Unanswered ones go to Open questions. -->

- Load and speed: {{11.1}}
- Accessibility: {{11.2}}
- Devices and browsers: {{11.3}}
- Offline: {{11.4}}
- Languages: {{11.5}}
- Security and compliance: {{11.6}}
- Uptime: {{11.7}}

## Constraints

<!-- From Section 12. Omit blank items. -->

- Deadline: {{12.1}}
- Budget: {{12.2}}
- Team: {{12.3}}
- Existing assets: {{12.4}}
- Must use or avoid: {{12.5}}

## Out of scope

<!-- 13.1 and 13.2. Then anything the scope guard moved here at build time, each marked "(moved from should have at build)" or "(moved from could have at build)". -->

- {{item}}

## Definition of done for v1

<!-- 14.1 as checkboxes. 14.2 as the success signal line. When 14.1 is blank, replace the checkboxes with one line: "Not specified in the intake. Task {{NN}} falls back to: every must-have story demonstrated, and every task complete." Omit the success signal line when 14.2 is blank. -->

- [ ] {{statement}}

**Success signal, one month after launch:** {{14.2}}

## Open questions

<!-- Two lists. "Unknown" holds every optional question answered "I don't know"; "Skipped" holds every optional question left blank. Each item is the section number and the question in a few words. Omit an empty list. When both are empty, write "None." -->

**Unknown, to find out:**

- {{n.n question}}

**Skipped, never considered:**

- {{n.n question}}
