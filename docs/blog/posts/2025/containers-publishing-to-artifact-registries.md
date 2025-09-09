---
title: Publishing container images to artifact registries
#title: Publishing containers to the GitHub Container Registry
description: >
  Notes about publishing containers to ghcr.io, the GitHub Container Registry.
# icon: octicons/repo-template-24
# https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
status: new
# page metadata
draft: true
date:
  created: 2025-08-19
  updated: 2025-09-09
authors:
  - rwaight
categories:
  - Containers
#slug: publishing-containers-to-ghcr-dot-io
slug: publishing-container-images-to-artifact-registries
tags:
  - Image Builds
  - Docker
  - GitHub
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Publishing containers to the GitHub Container Registry  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

I wanted to find out how to publish a container to the GitHub Container Registry...

### Listing your local container images

```shell
$ docker images
```

### Authenticating to the GitHub Container registry

The [GitHub docs state]() you should export your token:

```shell
$ export CR_PAT=YOUR_TOKEN
$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
```

<!--- https://github.com/cli/cli/issues/5150#issuecomment-2574394995 --->
***however***, you can use the [GitHub CLI]() to login using:
```shell
gh auth token | docker login ghcr.io --username $(gh api user --jq '.login') --password-stdin
```

### Building a container and pushing to ghcr.io

```shell
# set variables for tagging the container
OWNER=rwaight
NAMESPACE=actions
IMAGE_NAME=ctfd
TAG=3.7.7
# set a variable for the ghcr.io tag
GHCR_TAG=ghcr.io/${OWNER}/${NAMESPACE}/${IMAGE_NAME}:${TAG}
GHCR_LATEST=ghcr.io/${OWNER}/${NAMESPACE}/${IMAGE_NAME}:latest
```


## Resources

- [GitHub Docs: Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [`gh` as Docker credential helper - GitHub `cli/cli#5150`](https://github.com/cli/cli/issues/5150)
    - [comment with one-liner for login](https://github.com/cli/cli/issues/5150#issuecomment-2574394995)
- asdf
