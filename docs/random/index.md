---
title: Random pages index page
date:
  created: 2024-06-25
  updated: 2024-09-05
---

# Random pages index page

### Dark mode in chromium browsers

#### Setting dark mode for everything

If you love dark mode for everything... you can enable **Auto Dark Mode for Web Contents** by setting `chrome://flags/#enable-force-dark`. If that does not work, then go to `chrome://flags/` and search for **Dark Mode**.

Referenced from [How do I set Google Calendar to Dark Mode?](https://support.google.com/calendar/thread/9762643?hl=en&msgid=37038653)
> turn on the flag **Force Dark Mode for Web Contents**
> you can do this by going to `chrome://flags/` and searching for it

#### Browser dark mode extensions

* [Dark Reader](https://darkreader.org/)
    * [`darkreader/darkreader` on GitHub](https://github.com/darkreader/darkreader)

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

### Reset a Cisco Switch

Here is a summary of the commands needed to [reset Cisco Catalyst Switches to factory defaults](https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/217969-reset-catalyst-switches-to-factory-defau.html):
```shell
# enter configuration mode
enable
# remove the startup configuration file
write erase
# remove the VLAN configuration
delete flash:vlan.dat
# then reboot the switch
reload
```

If there are other files that need to be deleted, run the following **before** issuing the `reload` command:
```shell
show file information flash:?
delete flash:config.text.backup
delete flash:config.text.old
delete flash:*.old
```
