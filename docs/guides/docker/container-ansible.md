---
title: Ansible container
date:
  created: 2024-12-19
  updated: 2025-01-03
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

Test including external pages in files from https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages

### Dockerfile

```Dockerfile
{% include 'docker/ansible/Dockerfile' %}
```

### docker-compose

```yaml
{% include 'docker/ansible/docker-compose.yml' %}
```
