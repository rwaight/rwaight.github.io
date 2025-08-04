---
title: Updating JSON objects with JQ
description: >
  How to update a JSON array using JQ and bash.
icon: simple/json
status: new
draft: false
date:
  created: 2025-08-04
  updated: 2025-08-04
authors:
  - rwaight
categories:
  - coding
slug: updating-JSON-objects-with-JQ
tags:
  - coding
  - JSON
links:
  # All relative links are resolved from the docs directory.
  - resources/coding/jq-updating-json-objects.md
---

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

## Updating the JSON object

### Updated JSON array

Now we have a more unique set of data in our JSON array

Given the following array containing directory paths:

```json
[
    "/home/user/projects/my-test-abc/foo.txt",
    "/home/user/projects/my-test-abc/bar.log",
    "/home/user/projects/dev-jkl/foo.txt",
    "/home/user/projects/dev-jkl/bar.log",
    "/home/user/projects/dev-jkl/baz.log",
    "/home/user/projects/primary-test-project-xyz/foo.txt",
    "/home/user/projects/primary-test-project-xyz/bar.log",
    "/home/user/projects/primary-test-project-xyz/baz.txt"
]
```

Now stored as the `paths` variable:

```shell
paths='[
    "/home/user/projects/my-test-abc/foo.txt",
    "/home/user/projects/my-test-abc/bar.log",
    "/home/user/projects/dev-jkl/foo.txt",
    "/home/user/projects/dev-jkl/bar.log",
    "/home/user/projects/dev-jkl/baz.log",
    "/home/user/projects/primary-test-project-xyz/foo.txt",
    "/home/user/projects/primary-test-project-xyz/bar.log",
    "/home/user/projects/primary-test-project-xyz/baz.txt"
]'
```

### The planned output

I want the output to be usable by a GitHub actions matrix, so it should be:

```json
{
    "projects": [
        "test-abc",
        "test-jkl",
        "test-xyz"
    ],
    "include": [
        {
            "project": "test-abc",
            "files": [
                "my-test-abc/foo.txt",
                "my-test-abc/bar.log"
            ]
        },
        {
            "project": "dev-jkl",
            "files": [
                "dev-jkl/foo.txt",
                "dev-jkl/bar.log",
                "dev-jkl/baz.log"
            ]
        },
        {
            "project": "primary-test-project-xyz",
            "files": [
                "primary-test-project-xyz/foo.txt",
                "primary-test-project-xyz/bar.log",
                "primary-test-project-xyz/baz.txt"
            ]
        }
    ]
}
```

### Building the new JSON object

```bash
jq -c '
  # 1) Strip off the the '/home/user/projects' directory prefix
  map(sub("^/home/user/projects/";""))  

  # 2) Turn each element into an object with 'project' and 'file' keys
  | map({ project: (split("/")[0]), file: . })     

  # 3) (Optional) Sort by project so group_by will work predictably
  | sort_by(.project)                               

  # 4) Group into arrays by project name
  | group_by(.project)                              

  # 5) Build the final object:
  | {
      projects:   map(.[0].project),                # a simple list of project names
      include:    map({
                     project: .[0].project,         # the project name
                     files:   map(.file)            # all files in that project
                 })
    }
' <<<"$paths"
```

Which produces:

```json
{"projects":["dev-jkl","my-test-abc","primary-test-project-xyz"],"include":[{"project":"dev-jkl","files":["dev-jkl/foo.txt","dev-jkl/bar.log","dev-jkl/baz.log"]},{"project":"my-test-abc","files":["my-test-abc/foo.txt","my-test-abc/bar.log"]},{"project":"primary-test-project-xyz","files":["primary-test-project-xyz/foo.txt","primary-test-project-xyz/bar.log","primary-test-project-xyz/baz.txt"]}]}
```

#### Storing the output as a variable

```bash
matrix=$(jq -c '
  map(sub("^/home/user/projects/";""))
  | map({ project: (split("/")[0]), file: . })
  | sort_by(.project)
  | group_by(.project)
  | {
      projects: map(.[0].project),
      include:  map({ project: .[0].project, files: map(.file) })
    }
' <<<"$paths")
```

Which produces:

```bash
~ echo $matrix
{"projects":["dev-jkl","my-test-abc","primary-test-project-xyz"],"include":[{"project":"dev-jkl","files":["dev-jkl/foo.txt","dev-jkl/bar.log","dev-jkl/baz.log"]},{"project":"my-test-abc","files":["my-test-abc/foo.txt","my-test-abc/bar.log"]},{"project":"primary-test-project-xyz","files":["primary-test-project-xyz/foo.txt","primary-test-project-xyz/bar.log","primary-test-project-xyz/baz.txt"]}]}
```

<!--- another example comment --->

<!---  ...  --->
