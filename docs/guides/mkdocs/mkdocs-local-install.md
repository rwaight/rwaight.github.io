---
title: Local installation
description: Local installation of MkDocs
date:
  created: 2024-05-28
  updated: 2025-05-07
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

In order to [preview MkDocs as you write](mkdocs-local-preview.md#previewing-as-you-write), you will need to [run MkDocs locally with Docker](#install-with-docker) first.


???+ warning

    As mentioned in the [Material for MkDocs "getting started with docker" guide](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker){:target="_blank"}, the Docker container is intended for local previewing purposes only and is not suitable for deployment. This is because the web server used by MkDocs for live previews is not designed for production use and may have security vulnerabilities.


## Install with docker

<!--- The content from this section is directly from 
 https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/docs/getting-started.md
 --->

The official [Docker image] is a great way to get up and running in a few
minutes, as it comes with all dependencies pre-installed. Open up a terminal
and pull the image with:

=== "Latest"

    ```shell
    docker pull squidfunk/mkdocs-material
    ```

=== "9.x"

    ```shell
    docker pull squidfunk/mkdocs-material:9
    ```

The `mkdocs` executable is provided as an entry point and `serve` is the
default command. If you're not familiar with Docker don't worry, we have you
covered in the following sections.

The following plugins are bundled with the Docker image:

- [mkdocs-minify-plugin]
- [mkdocs-redirects]

  [Docker image]: https://hub.docker.com/r/squidfunk/mkdocs-material/
  [mkdocs-minify-plugin]: https://github.com/byrnereese/mkdocs-minify-plugin
  [mkdocs-redirects]: https://github.com/datarobot/mkdocs-redirects

???+ warning

    The Docker container is intended for local previewing purposes only and
    is not suitable for deployment. This is because the web server used by
    MkDocs for live previews is not designed for production use and may have
    security vulnerabilities.

???+ question "How to add plugins to the Docker image?"

    Material for MkDocs only bundles selected plugins in order to keep the size
    of the official image small. If the plugin you want to use is not included,
    you can add them easily following the [add plugins to the Docker image](#add-plugins-to-the-docker-image) section below.

### Add plugins to the Docker image

Material for MkDocs only bundles selected plugins in order to keep the size
of the official image small. If the plugin you want to use is not included,
you can add them easily:

=== "Material for MkDocs"

    Create a `Dockerfile` and extend the official image:

    ```Dockerfile title="Dockerfile"
    FROM squidfunk/mkdocs-material
    RUN pip install mkdocs-awesome-nav
    RUN pip install mkdocs-macros-plugin
    RUN pip install mkdocs-git-revision-date-localized-plugin
    RUN pip install mkdocs-git-committers-plugin-2
    ```

=== "Insiders"

    Clone or fork the Insiders repository, and create a file called
    `user-requirements.txt` in the root of the repository. Then, add the
    plugins that should be installed to the file, e.g.:

    ``` txt title="user-requirements.txt"
    mkdocs-awesome-nav
    mkdocs-macros-plugin
    mkdocs-git-revision-date-localized-plugin
    mkdocs-git-committers-plugin-2
    ```

!!! tip "Verify correct list of plugins"

    Be sure to include the plugins that are installed in the 'publish-pages' 
    workflow. Look in the repos `.github/workflows/publish-pages.yml` file
    for commands starting with `pip install` for needed MkDocs plugins.

Next, build the image with the following command:

```shell
docker build -t squidfunk/mkdocs-material .
```

The new image will have additional packages installed and can be used
exactly like the official image.



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
        FROM squidfunk/mkdocs-material
        # be sure to include the plugins that are installed in the 'publish-pages' workflow
        #     check the '.github/workflows/publish-pages.yml' file
        RUN pip install mkdocs-awesome-nav
        RUN pip install mkdocs-macros-plugin
        RUN pip install mkdocs-git-revision-date-localized-plugin
        RUN pip install mkdocs-git-committers-plugin-2
        ```
 ---        
 --->

