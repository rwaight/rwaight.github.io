---
title: Check epoch date
date:
  created: 2024-01-08
  updated: 2024-06-25
authors:
  - rwaight
#slug: image-builder-notes
tags:
  - bash
  # use 'random' for uncategorized pages in the 'random' directory
  - random
---

<!--- move the 'ubuntu container' section to the random 'index.md' page

### Running an Ubuntu container to test bash commands

Optionally, you can create an ubuntu container using:
```bash
docker run -dt --name ubuntu-temp ubuntu:22.04
```

Then you can access `bash` in the ubuntu container using:
```bash
docker exec -it ubuntu-temp /bin/bash
```

--->

## Checking epoch dates with bash

Assuming you are given a date in millis of `1677628800000`, you can use bash for some time calculations...

> Note: This can be useful if you are checking the start date or expiration date of an Elasticsearch license, as it is provided in millis.

#### using bash for integer division

To perform integer division, you can use the shell:
```bash
$ echo $(( var1 / var2 ))
0
```

The `$(( ... ))` syntax is known as an _arithmetic expansion_.

#### convert millis to epoch

First, convert the millis to epoch time by dividing it by 1000:
```bash
$ echo $((1677628800000/1000))
1677628800
```

This returns `1677628800`, which is what we will use for our calculations.  You can also use `@$((1677628800000/1000))` instead, if you would prefer.

#### formatting the date

Printing a date without any formatting:
```bash
$ date -d @1677628800
Wed Mar  1 00:00:00 UTC 2023
```

Format the date as mm-dd-yy:
```bash
$ date -d @1677628800 +"%m-%d-%y"
03-01-23
```

Format the date as mm/dd/yy:
```bash
$ date -d @1677628800 +"%D"
03/01/23
```

Format the date as mm-dd-yyyy:
```bash
$ date -d @1677628800 +"%m-%d-%Y"
03-01-2023
```

Format the date as Month dd yyyy:
```bash
$ date -d @1677628800 +"%B %d %Y"
March 01 2023
```

Format the date as Month dd, yyyy:
```bash
$ date -d @1677628800 +"%B %d, %Y"
March 01, 2023
```

Format the date as yyyymmdd:
```bash
$ date -d @1677628800 +"%Y%m%d"
20230301
```

### days since a past date

The following command will print how long it has been since `1677628800`, which is **Wednesday March 1, 2023**:
```bash
$ echo $(expr '(' $(date +%s) + 86399 - $(date -d @1677628800 +%s) ')' / 86400) "days since $(date -d @1677628800 +"%B %d, %Y")"
484 days since March 01, 2023
```

Same as above, but using `@$((1677628800000/1000))` instead:
```bash
$ echo $(expr '(' $(date +%s) + 86399 - $(date -d @$((1677628800000/1000)) +%s) ')' / 86400) "days since $(date -d @$((1677628800000/1000)) +"%B %d, %Y")"
484 days since March 01, 2023
```

### days until a date

The following command will print **days until deadline** against `1677628800`; it will return a negative number since this is in the past:
```bash
$ echo $(expr '(' $(date -d @1677628800 +%s) - $(date +%s) + 86399 ')' / 86400) "days until deadline"
-482 days until deadline
```

Same as above, but using `@$((1677628800000/1000))` instead:
```bash
$ echo $(expr '(' $(date -d @$((1677628800000/1000)) +%s) - $(date +%s) + 86399 ')' / 86400) "days until deadline"
-482 days until deadline
```

#### more fancy

The following command will print both the **days until deadline** and the **deadline date** against `1677628800`; it will return a negative number since this is in the past:
```bash
$ echo $(expr '(' $(date -d @1677628800 +%s) - $(date +%s) + 86399 ')' / 86400) "days until the $(date -d @1677628800 +"%B %d, %Y") deadline"
-482 days until the March 01, 2023 deadline
```

Same as above, but using `@$((1677628800000/1000))` instead:
```bash
$ echo $(expr '(' $(date -d @$((1677628800000/1000)) +%s) - $(date +%s) + 86399 ')' / 86400) "days until the $(date -d @$((1677628800000/1000)) +"%B %d, %Y") deadline"
-482 days until the March 01, 2023 deadline
```

### Links found while looking up this topic


#### Links about checking epoch date with bash

- https://unix.stackexchange.com/questions/453703/determine-if-date-is-beyond-90-days-in-bash
- https://dev.to/dm8ry/bash-script-to-find-the-difference-between-an-epoch-timestamp-and-the-current-date-1hik
- https://stackoverflow.com/questions/16311688/bash-convert-epoch-to-date-showing-wrong-time
- https://stackoverflow.com/questions/6282059/how-do-you-print-the-days-until-a-deadline-from-the-command-line
- https://www.networkworld.com/article/968163/counting-down-the-days-using-bash.html
- https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/


#### Maybe less useful links about checking epoch date with bash

- https://stackoverflow.com/questions/4946785/how-to-find-the-difference-in-days-between-two-dates
- https://stackoverflow.com/questions/1706882/get-the-date-a-day-before-current-time-in-bash
- https://stackoverflow.com/questions/67613190/how-to-find-30-days-older-epoch-time-in-ms-from-current-time-in-shell-script
- https://stackoverflow.com/questions/66920940/parsing-the-date-to-calculate-days-until-cert-expiry-from-a-shell-script
- https://www.epochconverter.com/
- https://serverfault.com/questions/1044369/how-do-i-get-the-current-time-in-milliseconds-in-a-shell-script-in-buildroot-env
- https://stackoverflow.com/questions/16548528/linux-command-to-get-time-in-milliseconds
- https://serverfault.com/questions/151109/how-do-i-get-the-current-unix-time-in-milliseconds-in-bash
- https://stackoverflow.com/questions/62025091/how-to-convert-column-with-millisecond-timestamp-to-date-in-a-file-using-bash
- https://stackoverflow.com/questions/16311688/bash-convert-epoch-to-date-showing-wrong-time
- https://stackoverflow.com/questions/50466939/get-end-of-day-epoch-in-shell-script-bash
- https://stackoverflow.com/questions/70781768/remove-millisecond-from-echo-time-bash
- https://unix.stackexchange.com/questions/2987/how-do-i-convert-an-epoch-timestamp-to-a-human-readable-format-on-the-cli

