---
# page configuration
title: Conditionally authenticate to the GitHub CLI
description: >
  Using GitHub Actions to authenticate to the GitHub CLI as either a user or a bot
#icon: octicons/repo-template-24
status: new
# page metadata
draft: true
date:
  created: 2025-08-21
  updated: 2025-09-18
authors:
  - rwaight
categories:
  - GitHub
slug: github-auth-to-cli-conditionally
tags:
  - GitHub
links:
  # All relative links are resolved from the docs directory.
  - guides/github/overview.md
  - guides/github/github-use-gh-cli.md
---

<!---  # Conditionally authenticate to the GitHub CLI  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

Using GitHub Actions to authenticate to the GitHub CLI as either a user or a bot.

### References

- [`actions/create-github-app-token`](https://github.com/actions/create-github-app-token)
    - [Configure git CLI for an app's bot user](https://github.com/actions/create-github-app-token#configure-git-cli-for-an-apps-bot-user)
- [issues in `actions/create-github-app-token`](https://github.com/actions/create-github-app-token/issues)
    - [`#148` Return the GitHub App user id](https://github.com/actions/create-github-app-token/issues/148)
- [PRs in `actions/create-github-app-token`](https://github.com/actions/create-github-app-token/pulls)
    - [`#105` feat(outputs): app-slug and installation-id](https://github.com/actions/create-github-app-token/pull/105)
    - [`#145` docs(README): fix committer string example and add git config example](https://github.com/actions/create-github-app-token/pull/145)
- [Setup Git Credential Helper](https://github.com/jongio/gh-setup-git-credential-helper/blob/main/gh-setup-git-credential-helper)


### Configure git CLI for an app's bot user

<!--- https://github.com/actions/create-github-app-token#configure-git-cli-for-an-apps-bot-user --->

```yaml
on: [pull_request]

jobs:
  auto-format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/create-github-app-token@v2
        id: app-token
        with:
          # required
          app-id: ${{ vars.APP_ID }}
          private-key: ${{ secrets.PRIVATE_KEY }}
      - name: Get GitHub App User ID
        id: get-user-id
        run: echo "user-id=$(gh api "/users/${{ steps.app-token.outputs.app-slug }}[bot]" --jq .id)" >> "$GITHUB_OUTPUT"
        env:
          GH_TOKEN: ${{ steps.app-token.outputs.token }}
      - run: |
          git config --global user.name '${{ steps.app-token.outputs.app-slug }}[bot]'
          git config --global user.email '${{ steps.get-user-id.outputs.user-id }}+${{ steps.app-token.outputs.app-slug }}[bot]@users.noreply.github.com'
      # git commands like commit work using the bot user
      - run: |
          git add .
          git commit -m "Auto-generated changes"
          git push
```

> [!TIP]
> The `<BOT USER ID>` is the numeric user ID of the app's bot user, which can be found under `https://api.github.com/users/<app-slug>%5Bbot%5D`.
>
> For example, we can check at `https://api.github.com/users/dependabot[bot]` to see the user ID of Dependabot is 49699333.
>
> Alternatively, you can use the [octokit/request-action](https://github.com/octokit/request-action) to get the ID.



## Example section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
massa, nec semper lorem quam in massa.

<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
