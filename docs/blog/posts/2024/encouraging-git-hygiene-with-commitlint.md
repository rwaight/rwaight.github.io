---
title: Encouraging git hygine with commitlint
description: >
  Using commitlint 
date:
  created: 2024-03-20
  updated: 2025-07-07
authors:
  - rwaight
categories:
  - coding
  - Git
  - GitHub
links:
  # All relative links are resolved from the docs directory.
  - references/version-control/index.md
  - resources/version-control/index.md
---

<!--- This page was moved from the 'rwaight/actions' repo --->
<!--- original file: https://github.com/rwaight/actions/blob/main/docs/adding-commitlint.md --->


I added a [GitHub Action that uses commitlint](https://github.com/rwaight/actions/blob/v0.2/.github/workflows/check-commits.yml) to my [GitHub Actions Monorepo](https://github.com/rwaight/actions).  The GitHub Action is based off of [**commitlint**](https://commitlint.js.org/) ([commitlint GitHub](https://github.com/conventional-changelog/commitlint)) and has been added in an effort to encourage (enforce?) good **git hygiene**.  _Note_: The original [`actions-ci` workflow](https://github.com/rwaight/actions/blob/v0.1.12/.github/workflows/actions-ci.yml) was added in the [`v0.1.12` release](https://github.com/rwaight/actions/releases/tag/v0.1.12).


The workflow originated from [the _CI setup_ **GitHub Actions** section](https://commitlint.js.org/guides/ci-setup.html#github-actions) of the [commitlint guides](https://commitlint.js.org/guides/ci-setup.html).  The example workflow needed to be updated in order to run, but it should be working now.

The default commitlint configuration:
```js
module.exports = {
    extends: [
        "@commitlint/config-conventional"
    ],
}
```

#### Enforcing good git hygiene

Part of ensuring proper commit messages (and pull requests) will help with automating releases.  For example, the [semantic release](https://github.com/semantic-release/semantic-release) tool can be used in a GitHub action, via [this semantic-release-action](https://github.com/cycjimmy/semantic-release-action).

Here are some other write-ups on the topic:

- https://www.vantage-ai.com/blog/how-to-enforce-good-pull-requests-on-github
- https://hugooodias.medium.com/the-anatomy-of-a-perfect-pull-request-567382bb6067



#### Resources

commitlint guide links:

- [Guide: Getting started](https://commitlint.js.org/guides/getting-started.html)
- [Guide: Local setup](https://commitlint.js.org/guides/local-setup.html)
- [Guide: CI Setup](https://commitlint.js.org/guides/ci-setup.html)

Actions that can be used with `commitlint`:

- https://github.com/webiny/action-conventional-commits
- https://github.com/wagoid/commitlint-github-action
- https://github.com/commitizen/conventional-commit-types
- https://github.com/amannn/action-semantic-pull-request
- (deprecated) https://github.com/squash-commit-app/squash-commit-app
- (deprecated) https://github.com/zeke/semantic-pull-requests


Examples with a `semantic.yml` file within a GitHub repo:

- https://github.com/GoogleChrome/lighthouse-ci/blob/main/.github/semantic.yml
- https://github.com/minecrafthome/minecrafthome/blob/master/semantic.yml
- https://github.com/meltano/sdk/blob/main/.github/semantic.yml
- https://github.com/vectordotdev/vector/blob/master/.github/semantic.yml


Here are links to other resources:

- https://github.blog/changelog/2022-05-11-default-to-pr-titles-for-squash-merge-commit-messages/
- https://semantic-release.gitbook.io/semantic-release/recipes/ci-configurations/github-actions
- https://jamiewen00.medium.com/integrate-commitlint-to-your-repository-67d6524d0d24
- https://ajcwebdev.com/semantic-github/

