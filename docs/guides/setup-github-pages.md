---
title: Setup GitHub Pages
date:
  created: 2023-05-28
  updated: 2024-06-25
authors:
  - rwaight
#slug: setup-github-pages
tags:
  - GitHub
  - GitHub Pages
  - MkDocs
  - Jekyll
---


Resources:

* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)


## MkDocs

Resources:

* [Getting Started with MkDocs](https://www.mkdocs.org/getting-started/)
* [Deploying your docs to GitHub Pages](https://www.mkdocs.org/user-guide/deploying-your-docs/#github-pages)
* [`squidfunk/mkdocs-material` on GitHub](https://github.com/squidfunk/mkdocs-material)
    * the [`squidfunk/mkdocs-material` docker image](https://hub.docker.com/r/squidfunk/mkdocs-material)
* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)


### Install MkDocs Material with Docker

Here are the steps from the [installing with Docker](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker) guide:

```bash
# pull the image
docker pull squidfunk/mkdocs-material

# navigate to the root directory of the repo
cd /path/to/root/of/repo

# run the container and attach the current directory to /docs
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```


#### Adding plugins to the Docker image
From https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker

> Material for MkDocs only bundles selected plugins in order to keep the size of the official image small. If the plugin you want to use is not included, create a new `Dockerfile` and extend the official Docker image:
```bash
FROM squidfunk/mkdocs-material
RUN pip install ...
```
> Next, you can build the image with the following command:
```bash
docker build -t squidfunk/mkdocs-material .
```
> The new image can be used exactly like the official image.


### Creating a new site with Docker

After issuing the `docker run` command above, issue the following:
```bash
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
```


### Publish the site with GitHub Actions
From From https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker

> Using [GitHub Actions](https://github.com/features/actions) you can automate the deployment of your project documentation. At the root of your repository, create a new GitHub Actions workflow, e.g. .github/workflows/ci.yml, and copy and paste the following contents:
```yml
name: ci 
on:
  push:
    branches:
      - master 
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```
> Now, when a new commit is pushed to either the `master` or `main` branches, the static site is automatically built and deployed. Push your changes to see the workflow in action.


## Jekyll

Resources:
* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
* [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)
    * [Adding a theme to your GitHub Pages site using Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)


### Install Jekyll on macOS

Follow the [Jekyll on macOS](https://jekyllrb.com/docs/installation/macos/) guide:

1. Install Ruby using Homebrew
    1. Install Homebrew
    2. Install chruby and the latest Ruby with ruby-install
2. Install Jekyll


#### Supported macOS versions

Permalink: [Jekyll supported macOS versions](https://jekyllrb.com/docs/installation/macos/#supported-macos-versions)

* Ventura (macOS 13)
* Monterey (macOS 12)
* Big Sur (macOS 11)

> Older macOS versions might work, but we don’t officially support them.


#### 1. Install Ruby using Homebrew

Permalink: [Install Ruby](https://jekyllrb.com/docs/installation/macos/#install-ruby)

> To install Jekyll on macOS, you need a proper Ruby development environment. While macOS comes preinstalled with Ruby, we don’t recommend using that version to install Jekyll. This external article goes over the various reasons [why you shouldn’t use the system Ruby](https://www.moncefbelyamani.com/why-you-shouldn-t-use-the-system-ruby-to-install-gems-on-a-mac/).
> 
> Instead, you’ll need to install a separate and newer version of Ruby using a version manager such as [asdf](https://asdf-vm.com/), [chruby](https://github.com/postmodern/chruby), [rbenv](https://github.com/rbenv/rbenv), or [rvm](https://rvm.io/). Version managers allow you to easily install multiple versions of Ruby, and switch between them.
> 
> We recommend `chruby` because it’s the simplest and least likely to cause issues.
> 
> The instructions below are an excerpt from this detailed external guide to [install Ruby on Mac](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/). They work best if you’re setting up development tools for the first time on your Mac. If you’ve already tried to install Ruby or Jekyll on your Mac, or if you run into any issues, read that guide.


##### 1.1: Install Homebrew

Permalink: [Step 1: Install Homebrew](https://jekyllrb.com/docs/installation/macos/#step-1-install-homebrew)

> [Homebrew](https://brew.sh/) makes it easy to install development tools on a Mac.
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

##### 1.2: Install chruby and the latest Ruby with ruby-install


Permalink: [Step 2: Install chruby and the latest Ruby with ruby-install](https://jekyllrb.com/docs/installation/macos/#step-2-install-chruby-and-the-latest-ruby-with-ruby-install)

> Install `chruby` and `ruby-install` with Homebrew:
```bash
brew install chruby ruby-install xz
```

> Install the latest stable version of Ruby (supported by Jekyll):
```bash
ruby-install ruby 3.1.3
```

> This will take a few minutes, and once it’s done, configure your shell to automatically use `chruby`:
```bash
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.1.3" >> ~/.zshrc # run 'chruby' to see actual version
```

> If you’re using Bash, replace `.zshrc` with `.bash_profile`. If you’re not sure, read this external guide to [find out which shell you’re using](https://www.moncefbelyamani.com/which-shell-am-i-using-how-can-i-switch/).
> 
> Quit and relaunch Terminal, then check that everything is working:
```bash
ruby -v
```

> It should show ruby 3.1.3p185 (2022-11-24 revision 1a6b16756e) or a newer version.
> 
> Next, read that same external guide for important notes about [setting and switching between Ruby versions with chruby](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/#how-to-install-different-versions-of-ruby-and-switch-between-them).


#### 2. Install Jekyll


Permalink: [Install Jekyll](https://jekyllrb.com/docs/installation/macos/#install-jekyll)

> After installing Ruby with chruby, install the latest Jekyll gem:
```bash
gem install jekyll
```


#### Troubleshooting

Permalink: [Jekyll on macOS Troubleshooting](https://jekyllrb.com/docs/installation/macos/#troubleshooting)

> See [Troubleshooting](https://jekyllrb.com/docs/troubleshooting/) or [ask for help on our forum](https://talk.jekyllrb.com/).
