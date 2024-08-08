---
title: Random pages index page
date:
  created: 2024-06-25
  updated: 2024-08-08
---

# Random pages index page


### Difference between 'git pull' and 'git fetch' 

From [https://stackoverflow.com/a/292359](https://stackoverflow.com/a/292359):
> In the simplest terms, [`git pull`](http://git-scm.com/docs/git-pull) does a [`git fetch`](http://git-scm.com/docs/git-fetch) followed by a [`git merge`](http://git-scm.com/docs/git-merge).
> 
> `git fetch` updates your remote-tracking branches under `refs/remotes/<remote>/`. This operation is safe to run at any time since it never changes any of your local branches under `refs/heads`.
> 
> `git pull` brings a local branch up-to-date with its remote version, while also updating your other remote-tracking branches.
> 
> From the Git documentation for [`git pull`](http://git-scm.com/docs/git-pull):
> > `git pull` runs `git fetch` with the given parameters and then depending on configuration options or command line flags, will call either `git rebase` or `git merge` to reconcile diverging branches.


### Random GitHub Notes

See the [random GitHub notes page](github/random-github-notes.md) for some random info.


### Running an Ubuntu container to test bash commands

If you want to use a specific version of Linux to run `bash`, you can create a container (for example, ubuntu) using:
```bash
docker run -dt --name ubuntu-temp ubuntu:22.04
```

Then you can access `bash` in the ubuntu container using:
```bash
docker exec -it ubuntu-temp /bin/bash
```
