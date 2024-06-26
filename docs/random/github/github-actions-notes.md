---
title: Notes about GitHub Actions
date:
  created: 2023-10-02
  updated: 2024-06-25
authors:
  - rwaight
#slug: github-actions-notes
tags:
  - GitHub
  - GitHub/Actions
---

# Notes about GitHub Actions


### Add comment to pull request

- https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request
- third-party actions to check
    - https://github.com/marketplace/actions/comment-pr
    - https://github.com/marketplace/actions/create-or-update-comment
- get the PR number
    - https://www.google.com/search?q=github+script+variable+for+pull+request+number
    - https://stackoverflow.com/questions/59077079/how-to-get-pull-request-number-within-github-actions-workflow
- 2022 and newer blogs
    - https://github.blog/changelog/2023-04-11-commenting-on-files-in-a-pull-request-is-now-generally-available/
    - https://jacobtomlinson.dev/posts/2022/commenting-on-pull-requests-with-github-actions/
    - https://pet2cattle.com/2022/12/github-action-add-comment
    - https://ootips.org/yonat/add-pr-line-comment-from-github-actions/
    - https://www.google.com/search?q=github+script+add+comment+to+pull_request
- other links
    - https://stackoverflow.com/questions/59077079/how-to-get-pull-request-number-within-github-actions-workflow
    - https://stackoverflow.com/questions/70929443/how-to-create-an-automatic-github-comment-based-on-the-pull-request-title
    - https://dev.to/zirkelc/trigger-github-workflow-for-comment-on-pull-request-45l2
    - https://stackoverflow.com/questions/75079250/how-to-trigger-new-job-by-comment-in-pull-request-for-github-actions


### using conditionals in workflows

- https://samanpavel.medium.com/github-actions-conditional-job-execution-e6aa363d2867
- https://thomasthornton.cloud/2023/08/11/if-elseif-or-else-in-github-actions/


### Failing/preventing a pull request without checks being passed

- Use an `if` to check for a specific label (or wildcard label)
    - https://www.google.com/search?q=github+actions+fail+pull+request+check
    - https://stackoverflow.com/questions/58654530/how-to-auto-reject-a-pull-request-if-tests-are-failing-github-actions
    - Example using conditional from https://stackoverflow.com/questions/61770694/trigger-github-action-on-merge-of-pull-request-with-specific-tag
        - `if: contains(github.event.pull_request.labels.*.name, 'Update')`
        - https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#example-using-an-array
    - https://stackoverflow.com/questions/68554735/github-action-status-check-missing-from-the-list-of-checks-in-protected-branch-s/68613319#68613319


### Creating a composite action

- https://docs.github.com/en/actions/creating-actions/creating-a-composite-action


### Creating actions with Python

- https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
- https://www.google.com/search?q=run+github+action+with+python
- https://shipyard.build/blog/your-first-python-github-action/


### Creating a Docker container action

- https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action

