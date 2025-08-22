---
# page configuration
title: Create a bootable Win10 USB from Mac
description: >
  This is a template file for blog posts in MkDocs.
# icon: octicons/repo-template-24
# https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
status: new
# page metadata
draft: true
date:
  created: 2025-08-22
  updated: 2025-08-22
authors:
  - rwaight
categories:
  - Help Desk
slug: win10-bootable-usb-from-mac
tags:
  - Windows
  - System Recovery
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Blog post template  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

Resource: https://www.freecodecamp.org/news/how-make-a-windows-10-usb-using-your-mac-build-a-bootable-iso-from-your-macs-terminal/


```shell
brew install wimlib
```

```shell
win_usb=/dev/disk5
win_iso=~/Downloads/Win10_22H2_English_x64v1.iso
w10_vol=WIN10

diskutil eraseDisk MS-DOS "${w10_vol}" GPT ${win_usb}

hdiutil mount ~/Downloads/${win_iso}

rsync -vha --exclude=sources/install.wim /Volumes/CCCOMA_X64FRE_EN-US_DV9/* /Volumes/${w10_vol}

mkdir /Volumes/${w10_vol}/sources

wimlib-imagex split /Volumes/CCCOMA_X64FRE_EN-US_DV9/sources/install.wim /Volumes/${w10_vol}/sources/install.swm 3800
```

## Example section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
massa, nec semper lorem quam in massa.

<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
