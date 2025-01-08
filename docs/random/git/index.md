---
title: Random Git Notes
date:
  created: 2023-10-02
  updated: 2025-01-08
authors:
  - rwaight
#slug: random-git-notes
tags:
  - Git
---

# Random Git Notes

- [Learn Git Branching](https://learngitbranching.js.org/)
    - [https://learngitbranching.js.org/](https://learngitbranching.js.org/)

## References

#### Git Basics - Tagging
- https://git-scm.com/book/en/v2/Git-Basics-Tagging


#### Git Branching - Rebasing
- https://git-scm.com/book/en/v2/Git-Branching-Rebasing


## Clean up commits

This section is related to commands used to clean up commits.
<!--- review the following links as well:

* https://stackoverflow.com/questions/8225125/remove-last-commit-from-remote-git-repository
* https://stackoverflow.com/questions/3882583/how-to-discard-local-commits-in-git
* https://stackoverflow.com/questions/5097456/throw-away-local-commits-in-git


--->

### Uncommit but keep changes

[credit to this gist from `CrookedNumber`](https://gist.github.com/CrookedNumber/8964442).

To "uncommit" the last commit from git, but keep the changes, run:
```shell
git reset HEAD^
```

This command will "evict" the commits from the branch and from the index, but leave the working tree around.

If you want to save the commits on a new branch name, then run `git branch newbranchname` before doing the git reset.

### Remove the last commit

To remove the last commit from git, run:
```shell
git reset --hard HEAD^
```

### Remove the last n commits

If you are removing multiple commits from the top, run:
```shell
git reset --hard HEAD~n
```

> Where `n` is the number of commits to remove.

Example to remove the last two commits:
```shell
git reset --hard HEAD~2
```

### Remove the last n commits on local and remote

To remove the last commit from git, run:
```shell
git reset --hard HEAD~n
git push origin -f
```

> Where `n` is the number of commits to remove.

Example to remove the last two commits on local **and remote**:
```shell
git reset --hard HEAD~2
git push origin -f
```

## Releases and Tags

### GitHub Tagging
- https://www.google.com/search?q=github+create+tag+without+release
- https://stackoverflow.com/questions/18216991/create-a-tag-in-a-github-repository

### Show latest releases with git
- https://unix.stackexchange.com/questions/502939/how-to-show-latest-releases-git-tag-with-message
- https://stackoverflow.com/questions/1404796/how-can-i-get-the-latest-tag-name-in-current-branch-in-git
- https://github.com/orgs/community/discussions/25199
- https://www.google.com/search?q=github+actions+workflow+to+checkout+latest+release

