---
title: GPG + Git SSH Authentication and Signing on Windows 10
date:
  created: 2025-01-08
  updated: 2025-01-08
# authors:
#   - rwaight
slug: gpg-plus-git-ssh-auth-and-sign-on-windows-10
tags:
  - Authentication
  - GPG
  - Git
  - SSH
  - Windows
---

From [https://gist.github.com/matusnovak/302c7b003043849337f94518a71df777](https://gist.github.com/matusnovak/302c7b003043849337f94518a71df777)

# GPG + Git SSH Authentication and Signing on Windows 10

## Introduction

This simple Gist will explain how to settup your GPG key to work for SSH authentication (with Git) and Git commit signing on Windows 10.
This may seem straightforward on Linux, but there are certain tweaks needed on Windows.

**No Cygwin, no MinGW, no Git Bash** or any other Linux emulated environment. This works in pure Windows 10.

## Software needed

* [Git for Windows](https://git-scm.com/download/win)
* [Gpg4win](https://www.gpg4win.org/)
* [OpenSSH Win64](https://github.com/PowerShell/Win32-OpenSSH/releases)
* [benpye/wsl-ssh-pageant](https://github.com/benpye/wsl-ssh-pageant/releases) (not on Chocolately)

If you prefer chocolately: `choco install git gpg4win openssh`

If you have the latest version of Windows 10, the OpenSSH is installed in `System32/OpenSSH` folder.

Make sure that your system's PATH environment variable contains `C:\Program Files (x86)\GnuPG\bin`.

## Create or import a key

You will have to create a new GPG key or import an existing one. There are plenty of tutorials to walk you through it on the internet.
You must make sure that your key has signing and authenticating subkeys!

You can import an existing key with `gpg --import key.gpg`

To list the keys use `gpg -k --with-keygrip`, example below.

```
> gpg -k --with-keygrip
C:/Users/Matus/AppData/Roaming/gnupg/pubring.kbx
------------------------------------------------
pub   rsa4096 2019-10-28 [SC] [expires: 2021-10-25]
      9B0069EA5619486EB2A7E44392FC071FF37A93E5
      Keygrip = 496F3C43AB7D195624832E0E3BF4FF9B531D2DB8
uid           [ultimate] Matus Novak <email@matusnovak.com>
sub   rsa4096 2019-10-28 [E] [expires: 2021-10-25]
      Keygrip = EE087ED74ED6F7843D397825CFB7D9EDD79F73BF
sub   rsa4096 2019-10-28 [A] [expires: 2021-10-25]
      Keygrip = 0B60893C664F965058DFDE93F34199566A12C39A
sub   rsa4096 2019-10-28 [S] [expires: 2021-10-25]
      Keygrip = BC0EC1D2E8E8B24405519823D51AFC4A05DF5E05
```

This key has three subkeys, one for \[A]authentication, one for \[S]igning, and one for \[E]ncryption. We will need the \[S] and \[A].

## Configure GPG

**WARNING:** Don't use CRLF newlines! You must switch to using LF only!

First, create a file `C:\Users\USER\AppData\Roaming\gnupg\gpg.conf` with the following contents. No new lines at the end.

```
> cat C:\Users\USER\AppData\Roaming\gnupg\gpg.conf
use-agent
```

Next, create another file `C:\Users\USER\AppData\Roaming\gnupg\gpg-agent.conf` with the following contents. No new lines at the end.

```
> cat C:\Users\USER\AppData\Roaming\gnupg\gpg-agent.conf
enable-ssh-support
enable-putty-support
```

## SSH control file

There is one more file, the `C:\Users\USER\AppData\Roaming\gnupg\sshcontrol`. This file may already exist in your `gnupg` folder. If not, create it.

Add your authenticating subkey (the keygrip ID) into this file. **There must be a single newline at the end! You must use LF line endings, not CRLF!.** Otherwise the key won't be recognised. Example below.

```
> cat C:\Users\USER\AppData\Roaming\gnupg\sshcontrol
0B60893C664F965058DFDE93F34199566A12C39A

```

## Restart the agent

Every time you change your configuration, you must restart the agent using the `gpg-connect-agent killagent /bye` and `gpg-connect-agent /bye`. Example below.

```
> gpg-connect-agent killagent /bye
OK closing connection

> gpg-connect-agent /bye
gpg-connect-agent: no running gpg-agent - starting 'C:\Program Files (x86)\Gpg4win\..\GnuPG\bin\gpg-agent.exe'
gpg-connect-agent: waiting for the agent to come up ... (5s)
gpg-connect-agent: connection to agent established
```

## Start the agent on startup

Make sure that the gpg agent starts on the startup. There are multiple ways to do that. The most simple solution is to create a shortcut of `C:\Program Files (x86)\GnuPG\bin\gpg-connect-agent.exe` inside of `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. Modify the shortcut, so that the "Target" ends with `/bye`, such as: `"C:\Program Files (x86)\GnuPG\bin\gpg-connect-agent.exe" /bye`.

The `/bye` is a necessary argument so that the command starts the agent and exits afterwards.

## Setup wsl-ssh-pageant

By default the Gpg4Win does not work with OpenSSH out of the box. It works with Putty, but if you want to use `ssh` command from your terminal, or use Visual Studio Code remote connection, you must do this step.

Download the `wsl-ssh-pageant-amd64-gui.exe` from [benpye/wsl-ssh-pageant releases](https://github.com/benpye/wsl-ssh-pageant/releases). (It's not a GUI, it only acts as one so you don't get a terminal window).

There is no install wizard for this application. Simply create a folder `C:\wsl-ssh-pageant` and put the `wsl-ssh-pageant-amd64-gui.exe` inside of it. The location does not matter.

Next, create a shortcut of `C:\wsl-ssh-pageant\wsl-ssh-pageant-amd64-gui.exe` inside of `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. Modify the shortcut, adding some command line arguments, so that the "Target" looks like the following: 

```
C:\wsl-ssh-pageant\wsl-ssh-pageant-amd64-gui.exe --wsl C:\wsl-ssh-pageant\ssh-agent.sock --winssh ssh-pageant --systray
```

The `--wsl` will create a socket for you to use inside of Windows Subsystem for Linux. The `--winssh` will create a named pipe for OpenSSH on your host (Windows).

**Finally, double click the shortcut.** You should see a new icon for wsl-ssh-pageant in your system tray.

## Check your SSH keys

Run the following command:

```
> ssh-add -L
ssh-rsa AAAAB3NzaC1yc2EA[...]
```

This will print out all of the available keys that can be used by your ssh. You need to double check that one of the printed keys is actually coming from the GPG. Use the `gpg --export-ssh-key YOUR_KEY_ID` command to print the public part of your ssh key from the GPG. The `YOUR_KEY_ID` is the ID of your key, not an ID of your subkey! Example below.

```
> gpg -k
C:/Users/Matus/AppData/Roaming/gnupg/pubring.kbx
------------------------------------------------
pub   rsa4096 2019-10-28 [SC] [expires: 2021-10-25]
      9B0069EA5619486EB2A7E44392FC071FF37A93E5
      [...]

> gpg --export-ssh-key 9B0069EA5619486EB2A7E44392FC071FF37A93E5
ssh-rsa AAAAB3NzaC1yc2EA[...]
```

If this matches your `ssh-add -L` then everything works fine for your OpenSSH!.

## Use with GitHub (Authentication)

Go to <https://github.com/settings/keys> and add the exported ssh key (the key from `gpg --export-ssh-key`).

Finally, test it out by connecting to `github.com` with `-T` using `ssh` as the `git` user. Example below.

```
> ssh -T git@github.com
Hi matusnovak! You've successfully authenticated, but GitHub does not provide shell access.
```

## Use with GitHub (Signing)

First, list your GPG key with the long format:

```
> gpg --list-secret-keys --keyid-format LONG
C:/Users/Matus/AppData/Roaming/gnupg/pubring.kbx
------------------------------------------------
sec#  rsa4096/92FC071FF37A93E5 2019-10-28 [SC] [expires: 2021-10-25]
      9B0069EA5619486EB2A7E44392FC071FF37A93E5
uid                 [ultimate] Matus Novak <email@matusnovak.com>
ssb   rsa4096/272F40FED5170F30 2019-10-28 [E] [expires: 2021-10-25]
ssb   rsa4096/FDB2A5741F89F17B 2019-10-28 [A] [expires: 2021-10-25]
ssb   rsa4096/8DDB99690FB73F0A 2019-10-28 [S] [expires: 2021-10-25]
```

Next, export the \[S]igning key in a readable format.

```
> gpg --armor --export 8DDB99690FB73F0A
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBF23fjMBEACy3dCCEIM9JxbIBhpciMPullyjiZAnWILbrB9jpLf1mUzo9l5U
[...]
-----END PGP PUBLIC KEY BLOCK-----
```

Copy the output, including the `-----BEGIN ...` until the very end. Go to <https://github.com/settings/keys> and add this public GPG key.


Finally, tell your Git about the signing key. Use the ID of the master secret key, the line that starts with `sec` (in the long format).

```
> git config --global user.signingkey 92FC071FF37A93E5
```

And configure git to auto-sign your commits.

```
> git config --global commit.gpgsign true
```

## Use with Windows Subsystem for Linux

All you have to do is to add `export SSH_AUTH_SOCK=/mnt/c/wsl-ssh-pageant/ssh-agent.sock` into your `~/.bashrc` file. As long as the `wsl-ssh-pageant` is running you can use this socket.

Running `ssh-add -L` will print out the same SSH key as on your host Windows.
