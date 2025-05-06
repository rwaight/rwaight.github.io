---
title: MkDocs container
date:
  created: 2025-05-06
  updated: 2025-05-06
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

<!--- Include external pages in files from https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages --->

???+ warning

    The Docker container is intended for local previewing purposes only and
    is not suitable for deployment. This is because the web server used by
    MkDocs for live previews is not designed for production use and may have
    security vulnerabilities.


### Dockerfile

```Dockerfile
{% include 'docker/mkdocs/Dockerfile' %}
```

