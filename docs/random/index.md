---
title: Random pages index page
date:
  created: 2024-06-25
  updated: 2025-01-05
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

### Using SanDisk Sansa m260 with Windows 10

The old Sansa MP3 players had two different USB modes, `MSC` and `MTP`
- MSC mode requires using Windows Media Player to sync files
- MTP mode allows access to the music directory on the devices internal drive

On the Sansa m260, the internal drive was accessible in `MTP` mode.  The process to do this is:
1. Turn off the Sansa m260 MP3 player
2. Sliding the HOLD switch towards the headphone jack (orange showing)
3. Press and hold the rewind button `|<<` while connecting the USB cable into the bottom of the player


#### Old forum comments

##### Sansa e250 in MTP mode

From [https://forums.sandisk.com/t/my-computer-does-not-recognize-sansa-e250-in-msc-mode-but-will-in-mtp-mode/26263](https://forums.sandisk.com/t/my-computer-does-not-recognize-sansa-e250-in-msc-mode-but-will-in-mtp-mode/26263)

> I can’t access my microsd card unless my player is in msc mode, which won’t work.  I have googled several sites, but none have helped.  I have tried that thing where you lock up the player, hold the middle button while plugging it in.

**Response**:
> If you have a v1 model (firmware vserion starts with a V01 on the INFO screen) that is the way it works. The card can only be accessed in MSC mode. It cannot be ‘synced’ or accessed in MTP mode. That’s why many veteren Sansa owners who started out with these devices exclusively use MSC mode and drag & drop file transfer method for both internal & external memory. It greatly simplifies things and reduces confusion. Files put on using MTP cannot be seen or accessed via your computer while connected in MSC mode and vice-versa.
> 
> And you have the “force MSC mode” procedure slightly off . . . after sliding the HOLD switch towards the headphone jack (orange showing), you press and hold the REW |<< button while connecting the cable into the bottom of the player, not the middle button. Make sure your player is OFF to begin with and it also helps to already have Windows Explorer (My Computer) open beforehand.

##### Sansa e250 

From [https://forums.sandisk.com/t/my-sansa-e250-does-not-have-usb-mode-on-its-setting-menu/26494](https://forums.sandisk.com/t/my-sansa-e250-does-not-have-usb-mode-on-its-setting-menu/26494)

> my sansa e250 does not have usb mode on its setting menu… i’ve tried to look for usb mode on all menus but i can’t find it… and the computer cannot recognize the device… it also stops charging the battery even if the device displays it is connected to the computer…  how can i fix this?

**Response**:
> If your device isn’t being recognized in MTP mode, all you have to do is force an MSC connection:
> Turn off the sansa v2.
> Flip the LOCK / HOLD switch to the right (orange showing)
> Hold down the << button while connecting.  An MSC connection should be established within 15 seconds or so, at the most, if the PC’s never sen the device in this mode.  Keep the << button depressed until it shows “connected” on the display.
> 
> At this point, you should see the little lightning bolt.

