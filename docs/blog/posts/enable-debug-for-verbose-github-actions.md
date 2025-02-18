---
title: Enable debug for verbose GitHub Actions
draft: false 
date:
  created: 2024-06-25
  updated: 2025-02-16
authors:
  - rwaight
categories:
  - GitHub
slug: enable-debug-for-verbose-github-actions
tags:
  - GitHub
  - GitHub/Actions
  - Automation
  - NeedToStandardizeTags
---

**This post is incomplete and will be updated in the future**

If you are using composite actions that support their own **verbose mode**, you may find you only want to enable **verbose mode** when the GitHub runner is in **debug mode**.  The variable we need to know is `runner.debug`, which is also stored as `RUNNER_DEBUG`.

### Understanding when variables are available

In a GitHub workflow there are three different situations where different environmental variables are available, GitHub calls this "context".  There is `workflow` context, `job` context, and `step` context.  The `runner.*` and `RUNNER_*` variables are available in the `STEP` environmental context, **but not** in the `workflow` or `job` environmental context.

### Example workflow using debug mode

What this means is that in order to find out what the `runner.debug` variable is set to, you **must** check for the variable in a `step`.  Here is an example workflow that will run **only** when the GitHub runner is in **debug mode**:
```yml
name: Print information only in runner debug

on:
  push:
    branches:
      - 'main'
    # ignore changes to .md files and the entire .github directory
    paths-ignore:
      - '**.md'
      - '.github/**'

jobs:

  runner-debug:
    runs-on: ubuntu-latest
    name: Print info in runner debug mode
    steps:

      - name: GitHub Runner Debug Mode
        if: ${{ runner.debug == '1' }}
        # to do:  run this if either the verbose input is true or the runner.debug is true
        id: runner-debug-mode
        ## The 'runner.*' and 'RUNNER_*' variables are not available in the WORKFLOW env context or the top-level JOB context, but are available in the STEP env context
        shell: bash
        env:
            EVAL_GH_VAR_RUNNER_DEBUG_EQ0: ${{ runner.debug == '0' }}
            EVAL_GH_VAR_RUNNER_DEBUG_EQ1: ${{ runner.debug == '1' }}
            FOOBAR: ${{ runner.debug == '1' && 'foo' || 'bar' }}
            # https://github.com/actions/runner/issues/2204#issuecomment-1287947031
            # https://github.com/orgs/community/discussions/27627#discussioncomment-3302259
            GH_RUNNER_LOG: "${{ runner.debug == '1' && 'INFO' || 'ERROR' }}"
            GH_VAR_RUNNER_DEBUG1: ${{ runner.debug }}
            GH_VAR_RUNNER_DEBUG2: ${{ env.RUNNER_DEBUG }}
        run: |
            echo "::group::starting the 'print-runner-context' step... "
            echo ""
            echo "NOTE: The 'runner.*' and 'RUNNER_*' variables are not available in the WORKFLOW env context or the top-level JOB context, but are available in the STEP env context "
            echo ""
            echo "eval if the 'runner.debug' is set to either '0' or '1' "
            echo "     runner.debug equal 0:  ${EVAL_GH_VAR_RUNNER_DEBUG_EQ0} "
            echo "     runner.debug equal 1:  ${EVAL_GH_VAR_RUNNER_DEBUG_EQ1} "
            echo ""
            echo "set FOOBAR to 'foo' if 'runner.debug' is '1'; otherwise set FOOBAR to 'bar' "
            echo "    FOOBAR:  ${FOOBAR} "
            echo ""
            echo "set GH_RUNNER_LOG to 'INFO' if 'runner.debug' is '1'; otherwise set GH_RUNNER_LOG to 'ERROR' "
            echo "    GH_RUNNER_LOG:  ${GH_RUNNER_LOG} "
            echo ""
            echo "the values of 'runner.debug' and 'env.RUNNER_DEBUG': "
            echo "    GH_VAR_RUNNER_DEBUG1:  ${GH_VAR_RUNNER_DEBUG1} "
            echo "    GH_VAR_RUNNER_DEBUG2:  ${GH_VAR_RUNNER_DEBUG2} "
            echo ""
            echo "finishing the 'print-runner-context' step... "
            ##
            echo "::endgroup::"
        ## The 'runner.*' and 'RUNNER_*' variables are not available in the WORKFLOW env context or the top-level JOB context, but are available in the STEP env context
```

