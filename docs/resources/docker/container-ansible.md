---
title: Ansible container
description: >
  Notes on running Ansible in a container.
date:
  created: 2024-12-19
  updated: 2025-05-13
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

<!--- Configuring 'render_macros: true' in the frontmatter is needed when including external pages in files --->
<!--- Include external pages in files:  https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages --->

In order to run Ansible in a Docker container, you can use a [Dockerfile](#dockerfile) and a [docker-compose](#docker-compose) file.

### Dockerfile

```Dockerfile
{% include 'docker/ansible/Dockerfile' %}
```

### docker-compose

```yaml
{% include 'docker/ansible/docker-compose.yml' %}
```


## Reference list


<!--- #### Running Ansible in a container --->

Links found when looking up `Running Ansible in a container`:

- [https://github.com/ansible/awx-ee](https://github.com/ansible/awx-ee)
- [https://hub.docker.com/r/geerlingguy/docker-ubuntu2404-ansible](https://hub.docker.com/r/geerlingguy/docker-ubuntu2404-ansible)
    - [https://www.ansiblefordevops.com/](https://www.ansiblefordevops.com/)
- [https://github.com/William-Yeh/docker-ansible](https://github.com/William-Yeh/docker-ansible)
- [https://www.reddit.com/r/ansible/comments/1d8trn1/which_image_should_i_use_for_ansible_container/?rdt=62502](https://www.reddit.com/r/ansible/comments/1d8trn1/which_image_should_i_use_for_ansible_container/?rdt=62502)
- [https://github.com/thegreenrobot/alpine-ansible-python3/blob/master/Dockerfile](https://github.com/thegreenrobot/alpine-ansible-python3/blob/master/Dockerfile)
- [https://github.com/willhallonline/docker-ansible/blob/master/README.md](https://github.com/willhallonline/docker-ansible/blob/master/README.md)
- [https://www.reddit.com/r/ansible/comments/1c6hqk0/running_ansible_in_docker/](https://www.reddit.com/r/ansible/comments/1c6hqk0/running_ansible_in_docker/)
    - [https://www.turnkeylinux.org/ansible](https://www.turnkeylinux.org/ansible)
    - [https://github.com/ldorad0/ldorad0.docker/tree/main/catalog/devops/devops-cli](https://github.com/ldorad0/ldorad0.docker/tree/main/catalog/devops/devops-cli)

