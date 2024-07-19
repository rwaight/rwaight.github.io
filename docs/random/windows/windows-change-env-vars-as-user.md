---
title: Change environment variables as standard user
date:
  created: 2024-07-19
  updated: 2024-07-19
authors:
  - rwaight
slug: change-env-vars-as-standard-user
tags:
  - Windows
---

# Change environment variables as standard user

This pages comes from [this "Change environment variables as standard user" post](https://superuser.com/questions/25037/change-environment-variables-as-standard-user) on [superuser.com](https://superuser.com/), which states:
> When clicking on "Advanced system settings", I need to login as the administrator and hence only edit _the administrators environment variables_ (in addition to the machine wide ones). **How do I edit the environment variables of a standard user?**


The [solution is to run](https://superuser.com/a/25038) the following command from a non-elevated (standard user) terminal:
```shell
rundll32 sysdm.cpl,EditEnvironmentVariables
```

### Question details

From [https://superuser.com/q/25037](https://superuser.com/q/25037)

> When clicking on "Advanced system settings", I need to login as the administrator and hence only edit _the administrators environment variables_ (in addition to the machine wide ones). **How do I edit the environment variables of a standard user?**

> **Details**
>
> With the migration to Windows 7, I decided to work as a **standard user** instead of an unprivileged administrator. Works well so far but I encountered a tiny problem:
>
> When I try to change per user environment variables via the control panel I have to login as an administrator. But since I run that part of the control panel as _the administrator_ I can only edit _the administrators variables_.
>
> **How am I supposed to edit my own environment variables?** Without resorting to extreme measures, such as editing the registry (as suggested in ["Is there any command line tool that can be used to edit environment variables in Windows?"](https://superuser.com/questions/13783/is-there-any-command-line-tool-that-can-be-used-to-edit-environment-variables-in) )


### Answer details

From [https://superuser.com/a/25038](https://superuser.com/a/25038)

> Just type “environment” into the start menu (or press `Win` + `S` in Windows 10 and search for _“Edit environment variables for your account”_).
>
> Similarly, searching for “environment” in the control panel yields that option, too.
>
> Generally, I have noticed that simply searching for something in the start menu or control panel is much faster than trying to remember a series of icons, dialogs, etc. one has to access to find something. At least for the vast majority of tasks[^1]^.
>
> A little digging yields that
> ```shell
> rundll32 sysdm.cpl,EditEnvironmentVariables
> ```
> is the command used to present that dialog. You can put a shortcut to that somewhere if you like.

[^1]: There are exceptions, such as installing a loopback network adapter. I looked for a few minutes before finally finding how to do that. But those things are hardly common scenarios :-)

