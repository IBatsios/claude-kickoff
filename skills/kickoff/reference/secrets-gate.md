# Secrets gate

Render Phase 0 step 4 from this file, for public and private repositories alike. The gate sits immediately before the first push. Render the gitleaks block for `environment.os`, then the fallback block for `environment.shell` under the heading "If gitleaks is not installed".

## gitleaks

Install, one line per OS, render only the user's:

- Windows: `winget install gitleaks` (or download the release binary from `https://github.com/gitleaks/gitleaks/releases`)
- macOS: `brew install gitleaks`
- Linux: download the release binary from `https://github.com/gitleaks/gitleaks/releases` and put it on the PATH; many distributions also package it.

Run, identical in every shell:

```
gitleaks detect --source . --no-banner
```

Then: "No leaks found" means push. Anything else means remove the value from the file, rotate it with the provider that issued it, and run the scan again. Rotation matters even though nothing was pushed, because the value has been in a file on disk.

## Fallback without gitleaks

Weaker, no install. It looks for the most common key shapes and a few telltale words.

bash, zsh, fish:

```
grep -rInE --exclude-dir=.git --exclude-dir=node_modules -e 'AKIA[0-9A-Z]{16}' -e 'sk-[A-Za-z0-9]{20,}' -e 'ghp_[A-Za-z0-9]{36}' -e 'glpat-[A-Za-z0-9_-]{20,}' -e 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY' -e '(password|secret|token|api_key)\s*[=:]\s*["'"'"'][^"'"'"']{8,}' .
```

PowerShell:

```
Get-ChildItem -Recurse -File -Exclude *.lock | Where-Object { $_.FullName -notmatch '\\(\.git|node_modules)\\' } | Select-String -Pattern 'AKIA[0-9A-Z]{16}', 'sk-[A-Za-z0-9]{20,}', 'ghp_[A-Za-z0-9]{36}', 'glpat-[A-Za-z0-9_-]{20,}', 'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY', '(password|secret|token|api_key)\s*[=:]\s*["''][^"'']{8,}'
```

Then: "No output means nothing matched. A match in `.env.example` with a placeholder value is fine; a match anywhere else is not."

## Also render

One line reminding the user that `.env` is in `.gitignore` and must stay there, and that `.env.example` holds names and placeholder values only.
