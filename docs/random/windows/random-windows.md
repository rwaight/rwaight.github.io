---
title: Random Windows Notes
date:
  created: 2024-10-24
  updated: 2024-10-24
authors:
  - rwaight
slug: random-windows-notes
tags:
  - Windows
---

# Random Windows Notes

### Creating a symbolic link

#### Creating a symbolic link with PowerShell


**Note**: These commands require administrative privileges

Create a symbolic link named `my_symbolic_link` to the `C:\Users\myuser\Documents\test\asdf1234` directory, the symbolic link will be in the `~\my_target_dir` directory:
```shell
cd my_target_dir
New-Item -ItemType SymbolicLink -Path .\my_symbolic_link -Target C:\Users\myuser\Documents\test\asdf1234
```

Reference: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.4#example-7-create-a-symbolic-link-to-a-file-or-folder


### Creating a symbolic link with command prompt

**Note**: These commands require administrative privileges

Create a symbolic link named `my_symbolic_link` to the `C:\Users\myuser\Documents\test\asdf1234` directory, the symbolic link will be in the `~\my_target_dir` directory:
```shell
cd my_target_dir
mklink /d \my_symbolic_link C:\Users\myuser\Documents\test\asdf1234
```

# end of page
