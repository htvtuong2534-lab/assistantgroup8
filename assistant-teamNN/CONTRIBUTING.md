# Contributing

Work on your assigned personal branch. Bring the latest `main` into that
branch before making changes, then commit and push to the same personal
branch for the team to review and merge.

## Secrets

- Keep passwords, API keys, access tokens and private keys out of source
  code, documents, screenshots, test fixtures and Git commits.
- Use environment variables for credentials. `.env.example` contains
  non-sensitive defaults and an empty `LLM_API_KEY` placeholder only.
- From `assistant-teamNN/`, copy the template to a local `.env` when
  configuration is needed:

  ```sh
  cp .env.example .env
  ```

  In PowerShell:

  ```powershell
  Copy-Item .env.example .env
  ```

- `.env` and `.env.*` are ignored at the repository root and inside the
  project. `.env.example` is the exception and must never contain a real
  credential. Do not force-add an ignored environment file.
- The current starter does not automatically load `.env`. When an LLM
  integration is added, read its key from the process environment or an
  explicit local configuration loader; keep the key out of logs and replies.
- Share credentials through a private credential manager. Do not put them
  in GitHub issues, PRs or chat screenshots. Use GitHub Actions secrets for
  CI credentials.
- Use public, synthetic or anonymised sample data. Do not commit private
  student records, grades, IDs, personal contact details or chat histories.
  Verify the public source before adding an institution's contact details.
- Before pushing, inspect the staged filenames and changes, then scan from
  the repository root:

  ```sh
  git diff --cached --name-only
  git diff --cached
  gitleaks git . --staged --redact=100 --no-banner
  ```

- If a real credential reaches Git, revoke or rotate it first and notify
  the team privately. Removing it in a later commit does not remove it
  from history. Coordinate any history cleanup with the repository owner.
