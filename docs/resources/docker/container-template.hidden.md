---
title: TEMPLATE_REPLACEME container
description: >
  Notes on running TEMPLATE_REPLACEME in a container.
date:
  created: 2025-05-13
  updated: 2025-05-13
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

<!--- Configuring 'render_macros: true' in the frontmatter is needed when including external pages in files --->
<!--- Include external pages in files:  https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages --->

In order to run TEMPLATE_REPLACEME in a Docker container, you can use a [Dockerfile](#dockerfile) and a [docker-compose](#docker-compose) file.

### Dockerfile

```Dockerfile
{% include 'docker/TEMPLATE_DIR_REPLACEME/Dockerfile' %}
```

### docker-compose

```yaml
{% include 'docker/TEMPLATE_DIR_REPLACEME/docker-compose.yml' %}
```


## Reference list


<!--- #### Running TEMPLATE_REPLACEME in a container --->

Links found when looking up `Running TEMPLATE_REPLACEME in a container`:

- [https://github.com/topics/container](https://github.com/topics/container)
- [https://github.com/topics/docker-container](https://github.com/topics/docker-container)
- [https://gitlab.com/explore/projects/topics/containers](https://gitlab.com/explore/projects/topics/containers)
- [https://gitlab.com/explore/projects/topics/docker-containers](https://gitlab.com/explore/projects/topics/docker-containers)

