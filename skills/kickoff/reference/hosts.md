# Remote creation, per host

Render Phase 0 step 1 of the runbook from this file. Fill every `{{value}}` from the intake before writing; the user pastes the result as-is. Skip the step entirely when `git.host` is local only, and skip the create-repo command when `git.existing_repo_url` is set (render only the remote-add line with that URL).

No block here pushes. The push is step 0.6, rendered from "The push" at the bottom of this file, so that the secrets gate in step 0.4 always runs first.

Every host gets the CLI path first, then the browser fallback under a heading "If the CLI is not installed". The login command is where the token is entered; it is never written into a file.

## GitHub

```
gh auth login
gh repo create {{owner}}/{{slug}} --{{visibility}} --source=. --remote=origin
```

Browser fallback: create the repository at `https://github.com/new` with the name `{{slug}}`, visibility {{visibility}}, no README, then:

```
git remote add origin https://github.com/{{owner}}/{{slug}}.git
```

## GitLab (gitlab.com or self-hosted)

`{{host_url}}` is `https://gitlab.com` when the intake left it blank.

```
glab auth login --hostname {{host_url without scheme}}
glab repo create {{owner}}/{{slug}} --{{visibility}}
git remote add origin {{host_url}}/{{owner}}/{{slug}}.git
```

Browser fallback: create the project at `{{host_url}}/projects/new`, blank project, name `{{slug}}`, under `{{owner}}`, visibility {{visibility}}, no README, then the same `git remote add` line.

## Gitea

```
tea login add --url {{host_url}} --name {{slug}}-host
tea repo create --name {{slug}} --{{visibility}}
git remote add origin {{host_url}}/{{owner}}/{{slug}}.git
```

Add `--owner {{owner}}` to `tea repo create` when the owner is an organization rather than the logged-in user. `tea login add` prompts for the token.

Browser fallback: create the repository at `{{host_url}}/repo/create`, name `{{slug}}`, owner `{{owner}}`, visibility {{visibility}}, no README, then the same `git remote add` line.

## Other

No CLI. Render only the browser path: "Create an empty repository named `{{slug}}` under `{{owner}}` on `{{host_url}}`, with no README, then:"

```
git remote add origin {{host_url}}/{{owner}}/{{slug}}.git
```

## Shell notes

The commands above are identical in PowerShell, bash, zsh, and fish. Shell matters in the other Phase 0 steps: quoting, environment variables, and line continuation. Render those steps for `environment.shell` only, from `dev-database.md` and `secrets-gate.md`.

## The push (step 0.6)

The build committed on `main`. Render this after the secrets gate, for every host except local only:

```
git push -u origin main
```

Then one line: the first pull request or merge request comes with Task 01, from its branch to `main`, using the host's word for it: pull request on GitHub and Gitea, merge request on GitLab. When `conventions.protect_default_branch` is true, one more line: protect `main` in the host's repository settings now that it exists. Local only: one line saying there is no remote and Phase 1 can start now.
