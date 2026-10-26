# Publish to GitHub

The packaged repository is ready for a first commit, but GitHub repository creation, visibility, and distribution permissions require the owner's account and an authorised write interface.

## Review first

- Decide **private vs public** before creating the repository.
- Decide if/when to add an explicit `LICENSE` (see [Licensing](licensing.md)).
- Run both local validation commands from README.
- Confirm `git status` includes no secrets or personal data.

## Publish into an existing empty repository

Confirm the remote repository exists, belongs to the expected owner, and is empty. From the package directory:

```bash
git init -b main
git add .
git commit -m "feat: introduce undercut agent skill pack"
git remote add origin https://github.com/Lelekhoa1812/undercut.git
git push -u origin main
```

Do not force-push if the remote contains commits. If the remote has content, fetch and reconcile its history before pushing. Credentials must be provided by your normal GitHub login or credential helper, **never embedded in files or remote URLs**.

If a GitHub integration supports creating blobs, trees and commits but not repository creation, create the repository through GitHub first, then publish the tree using the authenticated connection. Verify the final `main` SHA and inspect the rendered README and CI workflow after pushing.

### New repository, only when needed

```bash
# Example private repository; confirm visibility and licensing first.
gh repo create Lelekhoa1812/undercut --private --source . --remote origin --push
```

The owner decides whether to make a repository public or grant reuse via a LICENSE file. A public repository without a license is **not** automatically open source.
