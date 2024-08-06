---
title: Setup a GPG key to use with git
draft: true
date:
  created: 2019-05-28
  updated: 2024-08-06
authors:
  - rwaight
#slug: setup-gpg-key
tags:
  - GPG
  - git
---


#### WIP Links and info

* Unlock GnuPG keys on login: https://github.com/cruegge/pam-gnupg
* Quick'n easy gpg cheatsheet: https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/
* Setting Up GPG on Windows (The Easy Way): https://www.git-tower.com/blog/setting-up-gpg-windows/
* https://stackoverflow.com/questions/50332885/how-do-i-install-and-use-gpg-agent-on-windows
* GPG + Git SSH Authentication and Signing on Windows 10: https://gist.github.com/matusnovak/302c7b003043849337f94518a71df777
* https://stackoverflow.com/questions/63440623/no-gpg-passphrase-prompt-in-visual-studio-code-on-windows-10-for-signed-git-comm


##### gpg-agent

* https://petrmanek.cz/blog/2022/unlocking-gpg-agent/
* https://stackoverflow.com/questions/50332885/how-do-i-install-and-use-gpg-agent-on-windows
* https://superuser.com/questions/739215/gpg-with-gpg-agent-never-asks-for-passphrase


##### Keyring

* https://pypi.org/project/gnome-keyring-gpg-unlock/
* https://wiki.archlinux.org/title/GNOME/Keyring
* https://stackoverflow.com/questions/14756352/how-is-python-keyring-implemented-on-windows
* https://dev.gnupg.org/T2135
* https://superuser.com/questions/1661377/can-i-leverage-windows-authentication-to-use-my-private-gpg-key
* https://stackoverflow.com/questions/63440623/no-gpg-passphrase-prompt-in-visual-studio-code-on-windows-10-for-signed-git-comm

##### GPG and YubiKey

* https://github.com/drduh/YubiKey-Guide#github
* https://support.yubico.com/hc/en-us/articles/360013790259-Using-Your-YubiKey-with-OpenPGP
* https://developers.yubico.com/PGP/Importing_keys.html
* https://google.com/search?q=add+gpg+key+to+yubikey&source=desktop


#### References

* [GnuPG Documentation](https://www.gnupg.org/documentation/index.html)


### Download and install GPG

Download and install the applicable OS-specific [GPG command line tools](https://www.gnupg.org/download/) from [https://www.gnupg.org/download/](https://www.gnupg.org/download/).

