# Security check

Date: 2026-10-13 (Asia/Bangkok)
Reviewer: Phuc Loc, with Codex assistance
Branch: `phucloc`
Baseline: latest fetched `main`, commit `2a69fbd`
Scope: issues #14 and #15

## Summary

No credential leaks were detected by Gitleaks. Manual review did not identify
private student records or private individual contact data in the tracked
project content. Two environment-file handling gaps were fixed. The current
project is a Python starter with documentation and a UI mockup; there is no
implemented web framework or LLM integration to audit yet.

## Checks and results

| Check | What was checked | Result |
| --- | --- | --- |
| Tracked-file inventory | All 15 baseline files: source, scripts, tests, configuration, documentation, data directory and UI image | No tracked `.env`, private-key file or database dump found. The data README is empty; no student dataset is committed. |
| Manual secret review | Code, tests and text documents for hardcoded credentials, authentication headers, API keys, passwords and private keys | No credential values identified. Tests use synthetic office data. The environment checker prints system details, not credential values. |
| Manual personal-data review | Text files for emails, phone numbers, student IDs, grades, identity numbers and personal-record fields; visual inspection of `docs/ui.png` | No private student records identified. Team-member names in `docs/team.md` are public team credits. The UI mockup shows office contact information whose authenticity/public status is not established by the repository; do not reuse it as a verified data source. |
| Git history | Gitleaks 8.30.1 with built-in rules, all fetched refs (`--all`), redacted output | Exit code 0; 0 findings. |
| Working directory | Gitleaks 8.30.1 directory scan, including the new environment template and contribution rules | Exit code 0; 0 findings. |
| Ignore rules | `.env`, `.env.local` and `.env.production` at repository and project roots; `.env.example` at both roots | All 8 checks passed: local environment files are ignored, and example templates are allowed. |
| Environment template | `assistant-teamNN/.env.example` | `APP_MODE=dev`; `LLM_API_KEY` has no value. No actual credential is included. |

## Findings by severity

No critical, high or medium credential/personal-data findings were identified
within the reviewed scope.

### Low severity - fixed

1. **SEC-01: environment template excluded by ignore rules.** The existing
   `.env.*` rule would ignore `.env.example`, preventing the safe template from
   being tracked. Added the explicit exception in
   `assistant-teamNN/.gitignore:18`. Real environment files remain ignored
   by lines 16-17.
2. **SEC-02: repository-root environment files were not ignored.** The
   project-level ignore file only protected files inside `assistant-teamNN/`.
   Added `.gitignore:1-3` at the repository root to protect root environment
   files while permitting an example template.

### Informational

3. **SEC-03: UI contact details are unverified.** `docs/ui.png` is a mockup,
   rather than evidence of an official public contact source. Before these
   details become real assistant data, the data/UI owner should verify their
   public institutional source or replace them with clearly labelled
   synthetic examples.

## Reproduce

Run from the repository root with
[Gitleaks 8.30.1](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1):

```sh
gitleaks git . --log-opts="--all" --redact=100 --no-banner
gitleaks dir . --redact=100 --no-banner
```

To verify the project ignore rules:

```sh
git check-ignore assistant-teamNN/.env assistant-teamNN/.env.local
git check-ignore assistant-teamNN/.env.example
```

The first command should list both local files (exit 0). The second should
print nothing (exit 1), because the template is allowed. Equivalent checks
were made for root-level files and `.env.production`.

Gitleaks' JSON reports were kept in a temporary directory outside the repo.
The official Windows release archive was verified against its published
SHA-256 checksum before execution. No scan report containing credential
values was committed.

## Limits and follow-up

The history scan covers the refs fetched into this checkout, not inaccessible
or deleted history. Gitleaks checks secret patterns and does not establish
that all content is free of personal data; the image was inspected manually.
Git author identities are normal contribution metadata and were not treated
as student records. Re-run the checks when data or integrations are added.

Secret-handling and sample-data rules are in `../CONTRIBUTING.md`.
