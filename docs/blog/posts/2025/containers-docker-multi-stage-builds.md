---
title: Building containers using Docker multi-stage builds
description: >
  Notes about building containers using Docker multi-stage builds.
# icon: octicons/repo-template-24
# https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
status: new
# page metadata
draft: true
date:
  created: 2025-08-21
  updated: 2025-08-21
authors:
  - rwaight
categories:
  - Containers
slug: containers-docker-multi-stage-builds
tags:
  - Image Builds
  - Docker
  - GitHub
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Building containers using Docker multi-stage builds  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

I wanted to find out how to use multi-stage builds when building containers with Docker...

### Docker multi-stage build notes

Docker supports [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), which means a [stage can be created](https://docs.docker.com/build/building/multi-stage/#name-your-build-stages) and then a [previous stage can be used as a new stage](https://docs.docker.com/build/building/multi-stage/#use-a-previous-stage-as-a-new-stage)

## Resources

- [Docker Docs: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- https://northflank.com/blog/docker-build-and-buildx-best-practices-for-optimized-builds
- https://www.geeksforgeeks.org/devops/docker-build/
- asdf
