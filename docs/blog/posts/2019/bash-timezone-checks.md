---
title: Bash timezone checks
draft: false
date:
  created: 2019-10-14
  updated: 2025-02-04
authors:
  - rwaight
categories:
  - bash
tags:
  - bash
  - random
---


If you try to build an over-complicated scheduler using `bash`, you may run into issues when it comes to Daylight Saving Time.  While it is a good idea to use Coordinated Universal Time (UTC), you might want to make sure you do not run into issues.  The examples will use the `date` with the `+"%H:%M"` format.

Using `date` with the `-u` option:
```bash
$ date -u +"%H:%M"
03:59
```

Using `date` after specifying the timezone with `TZ=`
```bash
$ TZ="UTC" date +"%H:%M"
03:59
```

Here is a way to ensure you include the appropriate Daylight Saving Time and its dates of applicability. The example is from the [21.5.6 Specifying the Time Zone with `TZ`](https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html#TZ-Variable) page.

In North American Eastern Standard Time (EST) and Eastern Daylight Time (EDT), the normal offset from UTC is 5 hours; since this is west of the prime meridian, the sign is positive. Summer time begins on March’s second Sunday at 2:00am, and ends on November’s first Sunday at 2:00am.
> `EST+5EDT`

Here are some examples using `date +"%H:%M"` for timezones in the continental United States:
```bash
$ TZ=":EST+5EDT" date +"%H:%M"
22:59
$ TZ=":CST+6CDT" date +"%H:%M"
21:59
$ TZ=":MST+7MDT" date +"%H:%M"
20:59
$ TZ=":PST+8PDT" date +"%H:%M"
19:59
```
