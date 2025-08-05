---
title: References in GitHub workflows and composite actions
description: >
  Enabling a GitHub composite action to call another action in the same repo.
icon: simple/githubactions
# https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
status: new
# page metadata
draft: false
date:
  created: 2025-08-05
  updated: 2025-08-05
authors:
  - rwaight
categories:
  - GitHub
slug: github-reusable-workflow-references
tags:
  - GitHub
  - Workflows
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Blog post template  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

Enabling a GitHub [composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) to call another action in the same repo.

This **can be done** with [reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows), but 
not yet composite actions: [github.blog/changelog/2022-01-25-github-actions-reusable-workflows-can-be-referenced-locally](https://github.blog/changelog/2022-01-25-github-actions-reusable-workflows-can-be-referenced-locally/)

### The problem

When running a [composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) 
(even in a [reusable workflow](https://docs.github.com/en/actions/using-workflows/reusing-workflows)), I want to be 
able to use the same GitHub `ref` for the actions that exist within the remote repo. For instance, I have 
an [actions monorepo](https://github.com/rwaight/actions) and would like to have some of my composite actions 
be able to call another action within the actions monorepo using the version (`ref`) that the action is using.

For example, the `check-semver-labels` action calls the `label-checker` action:

```yml
    - name: Check for semantic version labels
      uses: rwaight/actions/github/label-checker@main  # can use version specific or main
      #uses: rwaight/actions/github/label-checker@v1
      id: semver-labels-check
      with:
        prefix_mode: true
        one_of: ${{ inputs.semver-prefix }}
        #none_of: "skip-changelog"
        allow_failure: ${{ inputs.allow-failure }}
        repo_token: ${{ inputs.gh-token }}
```



### References

- GitHub `actions/toolkit`
    - [`#1264` make reference accessible in reusable workflow](https://github.com/actions/toolkit/issues/1264)
- GitHub `actions/runner`
    - [`#2417` Property job_workflow_sha in context github is not available](https://github.com/actions/runner/issues/2417)
- GitHub Community Discussions
    - [`#18601` Accessing Composite Action within Reusable Workflow from called workflow repo](https://github.com/orgs/community/discussions/18601)
    - [`#41927` Calling a sibling composite action using the same ref](https://github.com/orgs/community/discussions/41927)
    - [`#111928` Calling a composite action from an external workflow using the same ref used in the caller workflow](https://github.com/orgs/community/discussions/111928)



### Potential solutions

Here are some potential solutions:

- **Get reusable workflow version** action
    - [`canonical/get-workflow-version-action`](https://github.com/canonical/get-workflow-version-action)
    > GitHub composite action to get commit SHA that GitHub Actions reusable workflow was called with
    > Workaround for [`actions/toolkit#1264`](https://github.com/actions/toolkit/issues/1264)




<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
