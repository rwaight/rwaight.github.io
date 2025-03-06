---
title: Random GitHub Notes
description: >
  This page has random GitHub notes that need to be organized.
#icon: octicons/repo-template-24
#status: new
# page metadata
draft: false
date:
  created: 2024-10-25
  updated: 2025-02-20
authors:
  - rwaight
categories:
  - GitHub
#slug: random-github-notes
tags:
  - GitHub
  - Random
  - Need to organize
---

<!---  # Random GitHub Notes  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

## References

this section is blank

## Show Git Commit Timeline for GitHub Repos

Template URL to list all commits of a specific committer on GitHub
```shell
https://github.com/search?q=committer:NAME&type=commits
https://github.com/search?q=committer-name:NAME&type=commits
```

Template URL to list all commits of a specific author on GitHub
```shell
https://github.com/search?q=author:NAME&type=commits
```

##### author, commiter, or committer-name

Template URL to list all commits of a specific (author, committer, or committer-name) on GitHub (this does not seem to work well)
```shell
https://github.com/search?q=%28committer:NAME%29+OR+%28author:NAME%29+OR+%28committer-name:NAME%29&type=commits
```
the query
```sql
(author:NAME) OR (committer:NAME) OR (committer-name:NAME)
```

reference: https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax

##### Links

- Searches
    - https://www.google.com/search?q=github+show+timeline+of+commits+in+a+chart
    - https://www.google.com/search?q=github+get+commit+timeline+for+myself
- Repos
    - https://github.com/jungbluth/git-commit-timeline
        - Utility to show histogram plot timelines of your github commits, organized by repository
    - https://github.com/izikeros/git-commits-graph
    - https://github.com/danielfleischer/git-commits-lines-graph
- Forums
    - https://stackoverflow.com/questions/33926874/in-github-is-there-a-way-to-see-all-recent-commits-on-all-branches
    - https://stackoverflow.com/questions/21699790/any-way-in-github-com-to-see-the-exact-time-for-a-commit-or-release


#### Commits on GitHub Profile Timeline

- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/troubleshooting-commits-on-your-timeline

#### Template URL to list all commits of a specific committer on GitHub

Template URL to list all commits of a specific committer on GitHub
```shell
https://github.com/search?q=committer-name:NAME&type=commits
```
→ Simply replace NAME with the specific committer name you are looking for.

the above is from https://stackoverflow.com/questions/33926874/in-github-is-there-a-way-to-see-all-recent-commits-on-all-branches

- https://stackoverflow.com/a/76342801


#### Show commits on a specific branch

Not exactly the asked for question (to see commits on all branches), but to see a commit on a specific branch of a github repository -
```shell
https://github.com/<repository_name>/commits/<branch_name>?author=<user_name>
```

eg.

- Repository: langchain-ai/langchain
- Branch: master
- Author: sepiatone
- https://github.com/langchain-ai/langchain/commits/master?author=sepiatone

the above is from https://stackoverflow.com/questions/33926874/in-github-is-there-a-way-to-see-all-recent-commits-on-all-branches

- https://stackoverflow.com/a/78091633
