---
title: Using the GitHub CLI
draft: false 
date:
  created: 2025-01-02
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

The [GitHub CLI](https://cli.github.com/), or `gh`, is a command-line interface to GitHub for use in your terminal or your scripts.
- [View the GitHub CLI installation instructions](https://github.com/cli/cli#installation)

#### Configuration

Run [`gh auth login`](https://cli.github.com/manual/gh_auth_login) to authenticate with your GitHub account. Alternatively, `gh` will respect the `GITHUB_TOKEN` [environment variable](https://cli.github.com/manual/gh_help_environment).

To set your preferred editor, use `gh config set editor <editor>`. Read more about [`gh config`](https://cli.github.com/manual/gh_config) and [environment variables](https://cli.github.com/manual/gh_help_environment).

Declare your aliases for often-used commands with [`gh alias set`](https://cli.github.com/manual/gh_alias_set).


### Sign in to GitHub

Follow these steps once you have followed [the GitHub CLI installation instructions](https://github.com/cli/cli#installation)

1. In your terminal, issue `gh auth login` and follow the prompts
```bash
gh auth status
```


### Verify you are signed in to GitHub

Ensure you are signed in to GitHub with the CLI using `gh auth status`

1. Check the GH authentication status with
```bash
gh auth status
```

2. Ensure the output shows
```bash
github.com
  ✓ Logged in to github.com as GH_USERNAME (/home/USER/.config/gh/hosts.yml)
  ✓ Git operations for github.com configured to use https protocol.
  ✓ Token: *******************
```

3. If needed, login to GitHub with `gh auth login` and follow the prompts


## Next steps

Read through the [GitHub CLI manual](https://cli.github.com/manual/) to learn more.
- [Available commands](https://cli.github.com/manual/gh)
- [Usage examples](https://cli.github.com/manual/examples)
- [Community extensions](https://github.com/topics/gh-extension)

