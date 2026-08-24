# Mini Todo API

> Status: Merged from both main and feature branches

A deliberately tiny FastAPI project used to practice a full industry
git-to-deployment workflow: branching, PRs, CI, security practices, and CD.

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Visit http://127.0.0.1:8000/docs for interactive API docs.

## Run tests
```bash
pytest
```

## Roadmap
- [ ] Phase 1: Git basics (branch, merge, reset, revert, squash, cherry-pick, stash)
- [ ] Phase 2: Branch + PR workflow with protection rules
- [ ] Phase 3: CI with GitHub Actions
- [ ] Phase 4: Security practices (secrets, Dependabot, CODEOWNERS)
- [ ] Phase 5: CD to Render
WIP: working on something urgent
Feature A notes
