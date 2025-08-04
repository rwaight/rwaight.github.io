---
title: Updating JSON objects with JQ
description: >
  How to update a JSON array using JQ and bash.
date:
  created: 2025-08-04
  updated: 2025-08-04
authors:
  - rwaight
tags:
  - JSON
  - coding
  - Resource
---

!!! note

    This page was originally posted in the [_Updating JSON objects with JQ_ blog](blog/posts/2025/jq-updating-json-objects.md).

<!---  # Updating JSON objects with JQ  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

## Parsing entires in a JSON array

Given the following array containing directory paths:

```json
[
    "/home/user/project/file1.txt",
    "/home/user/project/subdir/file2.log"
]
```

Now stored as the `paths` variable:

```shell
paths='[
    "/home/user/project/file1.txt",
    "/home/user/project/subdir/file2.log"
]'
```

### Removing the prefix

#### Removing the prefix with `gsub`

We can use `gsub` to remove the `/home/user/` directory prefix:

```bash
gsub_no_prefix=$(jq -c '.[] |= gsub("^/home/user/";"")' <<< "$paths")
```

Which produces:

```bash
~ echo $gsub_no_prefix
["project/file1.txt","project/subdir/file2.log"]
```

#### Removing the prefix with JQ `map`

We can also use JQ `map` to remove the `/home/user/` directory prefix:

```bash
map_no_prefix=$(echo "$paths" |
  jq -c 'map(gsub("^/home/user/";""))'
)
```

Which produces:

```bash
~ echo $map_no_prefix
["project/file1.txt","project/subdir/file2.log"]
```


### Selecting entries based on a pattern

#### Selecting entries that match a pattern

Use `select(test(...))` to create a new array containing only paths that end in `.txt`:

```bash
dot_txt=$(jq -c 'map(select(test("\\.txt$")))' <<< "$paths")
```

Which produces:

```bash
~ echo $dot_txt
["/home/user/project/file1.txt"]
```

#### Selecting entries that do not match a pattern

Use `select(test(... | not))` to create a new array _excluding_ paths that end in `.log`:

```bash
no_dot_log=$(jq -c 'map(select(test("\\.log$") | not))' <<< "$paths")
```

Which produces:

```bash
~ echo $no_dot_log
["/home/user/project/file1.txt"]
```

### Putting it all together

We now have an updated array stored as the `paths` variable:

```bash
#!/usr/bin/env bash

# updated array
paths='[
    "/home/user/project/file1.txt",
    "/home/user/project/subdir/file2.log",
    "/home/user/data/foo.txt",
    "/home/user/data/bar.log",
    "/home/user/data/baz.txt"
]'

# 1) remove the '/home/user/' prefix
no_prefix=$(jq -c '.[] |= gsub("^/home/user/";"")' <<< "$paths")

# 2) keep only '.txt' files
only_txt_files=$(jq -c 'map(select(test("\\.txt$")))' <<< "$no_prefix")

# 3) exclude '.txt' files
no_txt_files=$(jq -c 'map(select(test("\\.txt$") | not))' <<< "$no_prefix")

# 4) print the results
echo "Only '.txt' files: "
echo "  ${only_txt_files}"
echo ""
echo "Exclude '.txt' files: "
echo "  ${no_txt_files}"
```

Which produces:

```bash
Only '.txt' files:
  ["project/file1.txt","data/foo.txt","data/baz.txt"]

Exclude '.txt' files:
  ["project/subdir/file2.log","data/bar.log"]
```


<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
