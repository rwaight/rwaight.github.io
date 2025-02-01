---
title: Delete GitHub workflow runs using the gh cli
date:
  created: 2022-09-22
  updated: 2025-02-01
authors:
  - rwaight
categories:
  - GitHub
tags:
  - GitHub
  - GitHub/CLI
  - Automation
  - NeedToStandardizeTags
---

# Delete GitHub workflow runs using the gh cli

### Finding the workflow runs by ID

You can use the `gh` command line interface to list the workflow runs by ID:
```bash
gh run list --json databaseId -q '.[].databaseId'
```

#### Workflow runs by ID for a specific workflow
You can also filter the workflow runs to a specific workflow using the `-w myworkflow.yml`, which would only list the workflow runs for the `.github/workflows/myworkflow.yml` workflow:
```bash
gh run list --json databaseId -w myworkflow.yml -q '.[].databaseId'
```


## Using bash or zsh

From [https://blog.oddbit.com/post/2022-09-22-delete-workflow-runs/](https://blog.oddbit.com/post/2022-09-22-delete-workflow-runs/)

Hello, future me. This is for you next time you want to do this.

When setting up the CI for a project I will sometimes end up with a tremendous clutter of workflow runs. Sometimes they have embarrassing mistakes. Who wants to show that to people? I was trying to figure out how to bulk delete workflow runs from the CLI, and I came up with something that works:
```bash
gh run list --json databaseId -q '.[].databaseId' |
  xargs -IID gh api \
    "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" \
    -X DELETE
```

This will delete _all_ (well, up to 20, or whatever you set in `--limit`) your workflow runs. You can add flags to `gh run list` to filter runs by workflow or by triggering user.

## Using PowerShell

The same command as above, but in PowerShell

```powershell
gh run list --json databaseId -q '.[].databaseId' | ForEach-Object { gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/$_" -X DELETE }
```

