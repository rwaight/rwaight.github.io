---
title: Publishing container images to artifact registries
#title: Publishing containers to the GitHub Container Registry
description: >
  Notes about publishing container images to artifact registries.
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

I wanted to find out how to [publish container images to both][01] the GitHub Container Registry and to the Google Cloud Platform Artifact (Container) Registry using GitHub Actions.

### Listing your local container images

```shell
$ docker images
```

## GitHub Container Registry

The `ghcr.io` domain name is used for GitHub's built-in container registry, known as [GitHub Container Registry (GHCR)][11].


### Authenticating to the GitHub Container registry

The [GitHub docs state][12] you should export your token:

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

- [Docker Docs: Push to multiple registries with GitHub Actions][01]

**GitHub Container Registry**:

- [GitHub Docs: Working with the Container registry][11]
- [`gh` as Docker credential helper - GitHub `cli/cli#5150`](https://github.com/cli/cli/issues/5150)
    - [comment with one-liner for login](https://github.com/cli/cli/issues/5150#issuecomment-2574394995)
- [GitHub Docs: Creating a Docker container action][13]


**Google Cloud Platform Artifact (Container) Registry**:

- [Google Cloud Docs: Artifact Registry overview][21]
- [Building and Pushing to Artifact Registry with Github Actions][22]
- [Difference between Container Registry and Artifact Registry Google Cloud][23]


<!--- ## End --->

[01]: https://docs.docker.com/build/ci/github-actions/push-multi-registries/

[11]: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
[12]: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-in-a-github-actions-workflow
[13]: https://docs.github.com/en/actions/tutorials/use-containerized-services/create-a-docker-container-action

[21]: https://cloud.google.com/artifact-registry/docs/overview
[22]: https://medium.com/@sbkapelner/building-and-pushing-to-artifact-registry-with-github-actions-7027b3e443c1
[23]: https://medium.com/google-cloud/difference-between-container-registry-and-artifact-registry-google-cloud-deac2a3ac383


