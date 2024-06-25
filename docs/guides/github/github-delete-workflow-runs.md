---
title: Delete GitHub workflow runs using the gh cli
date:
  created: 2022-09-22
  updated: 2024-06-25
#authors:
#  - rwaight
#slug: delete-workflow-runs
# from https://blog.oddbit.com/post/2022-09-22-delete-workflow-runs/
tags:
  - GitHub
---

From https://blog.oddbit.com/post/2022-09-22-delete-workflow-runs/

Hello, future me. This is for you next time you want to do this.

When setting up the CI for a project I will sometimes end up with a tremendous clutter of workflow runs. Sometimes they have embarrassing mistakes. Who wants to show that to people? I was trying to figure out how to bulk delete workflow runs from the CLI, and I came up with something that works:
```bash
gh run list --json databaseId  -q '.[].databaseId' |
  xargs -IID gh api \
    "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" \
    -X DELETE
```

This will delete _all_ (well, up to 20, or whatever you set in `--limit`) your workflow runs. You can add flags to `gh run list` to filter runs by workflow or by triggering user.
