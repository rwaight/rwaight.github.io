---
title: Local installation
description: Local installation of MkDocs
date:
  created: 2024-05-28
  updated: 2026-08-19
authors: [rwaight]
categories:
  - MkDocs
tags:
  - MkDocs
  - MkDocs/Examples
  - NeedToStandardizeTags
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

In order to [preview MkDocs as you write](mkdocs-local-preview.md#previewing-as-you-write), you will first need to [run MkDocs locally with Docker](#install-with-docker).


???+ warning

    The Docker container is intended for [local previewing purposes only and is **not suitable for deployment**](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker){:target="_blank"}. This is because the web server used by MkDocs for live previews is not designed for production use and may have security vulnerabilities.

<!--- The Docker container warning is from:
 https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker
 --->

## Install with docker

<!--- The content from this section is directly from 
 https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/docs/getting-started.md
 --->


This repository publishes an image that already includes the plugins used by the site. After a production tag, and after the GHCR package is set to Public, pull without logging in:

=== "Latest"

    ```shell
    docker pull ghcr.io/rwaight/rwaight.github.io/mkdocs-material:latest
    ```

=== "0.x"

    ```shell
    docker pull ghcr.io/rwaight/rwaight.github.io/mkdocs-material:v0.1
    ```

The `mkdocs` executable is the entrypoint and `serve` is the default command. See the [container README](https://github.com/rwaight/rwaight.github.io/blob/main/container/README.md) for the full tag policy. While the image is in the `0.x` series, there is no moving `v0` tag.

The image includes:

- mkdocs-material
- mkdocs-awesome-nav
- mkdocs-macros-plugin
- mkdocs-git-revision-date-localized-plugin
- mkdocs-git-committers-plugin-2

  [Docker image]: https://github.com/rwaight/rwaight.github.io/pkgs/container/rwaight.github.io%2Fmkdocs-material

???+ warning

    The Docker container is intended for local previewing purposes only and
    is not suitable for deployment. This is because the web server used by
    MkDocs for live previews is not designed for production use and may have
    security vulnerabilities.

### Verify required plugins

The published image is pinned in [`container/requirements.txt`](https://github.com/rwaight/rwaight.github.io/blob/main/container/requirements.txt). Site deploy in `.github/workflows/publish-pages.yml` still installs packages with `pip` and does not use this image.

### Add plugins to the image

If you need extra plugins beyond what this repository publishes, extend the public image:

```Dockerfile title="Dockerfile"
{% include 'docker/mkdocs/Dockerfile' %}
RUN pip install mkdocs-glightbox
```

### Build an extended image

```shell
docker build -t mkdocs-material-local .
```



<!--- 
    === "Material for MkDocs"

  --- the below code block is from the MkDocs guide ---
  --- 
        ``` Dockerfile title="Dockerfile"
        FROM squidfunk/mkdocs-material
        RUN pip install mkdocs-macros-plugin
        RUN pip install mkdocs-glightbox
        ```
 ---
  --- the below code block is from this repo ---
  --- the below 'include' code block is from this repo ---
  ---         
        ```Dockerfile title="Dockerfile"
        {% include 'docker/mkdocs/Dockerfile' %}
        ```
 ---
  --- the below code block is from this repo ---
  ---         
        ```Dockerfile title="Dockerfile"
        FROM ghcr.io/rwaight/rwaight.github.io/mkdocs-material
        # be sure to include the plugins that are installed in the 'publish-pages' workflow
        #     check the '.github/workflows/publish-pages.yml' file
        RUN pip install mkdocs-awesome-nav
        RUN pip install mkdocs-macros-plugin
        RUN pip install mkdocs-git-revision-date-localized-plugin
        RUN pip install mkdocs-git-committers-plugin-2
        ```
 ---        
 --->
