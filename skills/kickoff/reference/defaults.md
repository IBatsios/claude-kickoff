# Defaults file

`~/.claude/kickoff/defaults.yaml`. Same keys as the intake frontmatter, only the eligible ones. Missing file means no defaults; ask everything with the shipped conventions pre-selected.

## Eligible keys

Every `stack.*` field, `git.host`, `git.host_url`, `git.owner`, every `environment.*` field, `deployment.target`, every `conventions.*` field. Nothing else is ever written to this file: no project name, problem, features, data, integrations, domain, or visibility.

## Shipped conventions

Used when neither the defaults file nor the intake sets a value.

```yaml
conventions:
  protect_default_branch: true
  branch_prefixes: [feature, fix, chore]
  commit_style: conventional
  env_example: true
  db_backup_before_migrate: true
  handoff_docs: false
```

## Pre-fill at the start of a walkthrough

Read the file. For each eligible field, the saved value is the first option offered in its prompt, marked as the saved default. The intake always wins: whatever the user answers is what gets written, and every field is still asked.

## The offer at the end of a build

Compare the intake's eligible fields to the file (or to nothing, when there is no file). When any differ, send a message of its own, separate from the build report: a table of the differing fields, saved value beside intake value, then the structured prompt with two options, save these as my defaults or keep my saved defaults. When any differing value looks like a placeholder (an owner or domain containing `example`, a fixture's name), keep-my-saved-defaults is the first option and the message says why. Saving writes the file, merging over what was there. Keeping leaves it untouched. Ask once; never write without the answer. When the user corrects a wrong answer in the next message ("I meant no"), restore the previous values exactly and say so.

## Hand edits

The file is plain YAML the user may edit at any time. Unknown keys are ignored and left in place.
