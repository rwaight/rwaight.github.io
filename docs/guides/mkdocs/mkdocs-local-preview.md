---
title: Previewing as you write
description: How to preview MkDocs as you write
date:
  created: 2025-05-06
  updated: 2025-05-07
authors: [rwaight]
categories:
  - MkDocs
tags:
  - MkDocs
  - MkDocs/Examples
  - NeedToStandardizeTags
---

In order to [preview MkDocs as you write](#previewing-as-you-write), you will need to [run MkDocs locally with Docker](mkdocs-local-install.md#install-with-docker) first.


!!! warning

    As mentioned in the [Material for MkDocs "getting started with docker" guide](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker){:target="_blank"}, the Docker container is intended for local previewing purposes only and is not suitable for deployment. This is because the web server used by MkDocs for live previews is not designed for production use and may have security vulnerabilities.


## Previewing as you write

<!--- The content from this section is directly from 
 https://squidfunk.github.io/mkdocs-material/creating-your-site/#previewing-as-you-write
 --->

MkDocs includes a live preview server, so you can preview your changes as you
write your documentation. The server will automatically rebuild the site upon
saving. Start it with:

``` sh
mkdocs serve # (1)!
```

1.  If you have a large documentation project, it might take minutes until
    MkDocs has rebuilt all pages for you to preview. If you're only interested
    in the current page, the [`--dirtyreload`][--dirtyreload] flag will make
    rebuilds much faster:

    ```shell
    mkdocs serve --dirtyreload
    ```

If you're running Material for MkDocs from within Docker, use:

<!--- the original guide, from MkDocs, did not include using the `--detach` (`-d`) flag, but it is included below --->

=== "Unix, Powershell"

    ```shell
    docker run --rm -d -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

=== "Windows"

    ```shell
    docker run --rm -d -it -p 8000:8000 -v "%cd%":/docs squidfunk/mkdocs-material
    ```

Point your browser to [localhost:8000][live preview] and you should see:

[![Creating your site]][Creating your site]

  [--dirtyreload]: https://www.mkdocs.org/about/release-notes/#support-for-dirty-builds-990
  [live preview]: http://localhost:8000
  [Creating your site]: assets/screenshots/mkdocs-creating-your-site.png
