---
title: Nested Virtualization with GitHub Actions
date:
  created: 2024-01-18
  updated: 2024-06-26
authors:
  - rwaight
#slug: github-actions-nested-virtualization
tags:
  - GitHub
  - GitHub/Actions
  - Virtualization
---

# Nested Virtualization with GitHub Actions



### Using KVM (Nested virtualization) in GitHub Actions

If you need to build specific images using GitHub Actions, you may need to leverage nested virtualization; which can be accomplished using KVM.

Review the following:

- https://github.blog/changelog/2023-02-23-hardware-accelerated-android-virtualization-on-actions-windows-and-linux-larger-hosted-runners/, **and**
- https://github.com/actions/runner-images/issues/183#issuecomment-1442154492
    - Migrated to https://github.com/actions/runner-images/discussions/7191

As well as:

- https://actuated.dev/blog/kvm-in-github-actions
- https://github.com/actions/runner-images/issues/183
    - Specifically, https://github.com/actions/runner-images/issues/183#issuecomment-1442154492, links to the GitHub changelog
