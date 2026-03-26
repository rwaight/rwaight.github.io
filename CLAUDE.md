# Claude Code Instructions — rwaight/rwaight.github.io

This file is automatically loaded by Claude Code when working in this repository.

---

## Git Branch Policy

**NEVER commit directly to `main`.** This is a hard rule with no exceptions, including for agents operating autonomously.

Required workflow for all changes:
1. Verify you are NOT on main: `git branch --show-current`
2. If on main, create a branch first: `git checkout -b <type>/<description>`
3. Make commits on the feature branch
4. Push: `git push -u origin <branch-name>`
5. Open a PR: `gh pr create --base main`

Never run `git push origin main` or `git push origin HEAD:main`.

---

## Commit Message Convention

Commits follow **Conventional Commits** format: `<type>(<optional-scope>): <description>`

Common types: `feat`, `fix`, `docs`, `chore`, `ci`, `refactor`
