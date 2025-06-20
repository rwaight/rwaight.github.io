---
title: GitHub Repo Management Resources
description: >
  Resources to assist managing GitHub Repos
date:
  created: 2025-05-13
  updated: 2025-06-06
---

<!--- Do not use a H1 element when the title is set in the frontmatter --->
<!--- # Coding Resources --->

This page might be better off as a blog...


## Setting Up

The following items can be helpful when managing multiple GitHub repos:

- A `.json` repo inventory file
- Variables or an `.env` file
- An inventory array, sourced from the `.json` repo inventory file


### Repo Inventory File

In this case, we are using a `.json` file to keep track of the GitHub repos that will be managed.
Here are the contents of the `repo-list.json` file:

```json
{
    "repo": [
        "actions",
        "test-actions",
        "rwaight.github.io"
    ]
}
```

### Variables

Set variables and "reset" the secrets inventory list:

1. Set the `repoOwner` variable to `yourusername`
```bash
repoOwner=yourusername
```


### Inventory array

We will first create an array of repos from the `./repo-list.json` file

#### 1. Verify inventory output from `jq`

1. Run the following `jq` command to test the format of the JSON file:
```bash
jq --raw-output '.repo | to_entries | map("[\(.key)]=\(.value)")' ./repo-list.json
```

2. Review the output from the command to make sure the repos output the proper format:
```json
[
    "[0]=actions",
    "[1]=test-actions",
    "[2]=rwaight.github.io"
]
```

<!--- other commands

# use 'jq' to print the entries with the '.key' and '.value'
jq -r '.repo | to_entries[]' ./repo-list.json

# use 'jq' to print the entries with only the '.value'
jq -r '.repo | to_entries[] | .value' ./repo-list.json

# use 'for' and 'jq' to iterate through the '.value' entries and print them one by one
for k in $(jq -r '.repo | to_entries[] | .value' ./repo-list.json); do
    echo $k
done

# extra commands to create an array object that is not sorted
array=()
while read -r value; do
    array+=("$value")
while> done < <(jq -r '.repo | to_entries[] | .value' ./repo-list.json)
for str in "${array[@]}"; do echo "the repo is ${str} "; done

# messy ways to sort by values within an array object
jq --sort-keys .repo ./repo-list.json | jq 'sort'
jq --sort-keys '.repo | sort' ./repo-list.json

# this is how to sort by values within an array object
jq -r '.repo | to_entries | sort_by(.value)' ./repo-list.json

--->

#### 2. Create the inventory array

Create the array using either `bash` or `zsh`

<!--- Resources about creating an array from JQ in either bash or zsh

- https://unix.stackexchange.com/questions/681354/using-jq-to-parse-json-string-with-multi-word-values-into-an-associative-array
- https://unix.stackexchange.com/questions/771700/how-to-persistently-store-associative-arrays-dictionaries-in-bash
- https://unix.stackexchange.com/questions/708130/how-can-i-create-a-json-object-from-an-associative-array-in-shell-using-jo

--->

##### Create the inventory array using `bash`

```bash
# Create the variable that contains the array:
arrayAsString=$(jq --raw-output '.repo | to_entries | map("[\(.key)]=\(.value)") | reduce .[] as $item ("myRepos=("; . + $item + " ") + ")"' ./repo-list.json)
# Declare the array:
declare -A "$arrayAsString"
```

<!--- Resources specific to bash

- https://phoenixnap.com/kb/bash-associative-array
- https://stackoverflow.com/questions/19742062/why-are-declare-f-and-declare-a-needed-in-bash-scripts/19742842#19742842

--->

##### Create the inventory array using `zsh`

```zsh
# Declare the array:
typeset -A myRepos
# Create the variable that contains the array:
arrayAssignments=$(jq -r '.repo | to_entries[] | "myRepos[\(.key)]=\(.value)"' ./repo-list.json)
```

<!--- Resources specific to zsh

- ZSH CheatSheet: https://gist.github.com/ClementNerma/1dd94cb0f1884b9c20d1ba0037bdcde2
- Associative arrays in zsh: https://scriptingosx.com/2019/11/associative-arrays-in-zsh/
- https://unix.stackexchange.com/questions/606070/how-to-iterate-over-array-indices-in-zsh
- https://unix.stackexchange.com/questions/702295/zsh-how-to-set-an-associative-array-name-and-content-dynamically
- https://www.reddit.com/r/zsh/comments/ijk0j5/join_key_and_values_of_associative_arrays_with/
- https://stackoverflow.com/questions/55615410/using-declare-in-zsh


--->


#### 3. Test the inventory array

Test the array using either `bash` or `zsh`:

##### Test the inventory array using `bash`

```bash
for str in "${myRepos[@]}"; do echo "the repo is ${str} "; done
```

##### Test the inventory array using `zsh`

```zsh
for str in "${myRepos[@]}"; do echo "the repo is '${repoOwner}/$myRepos[$str]' "; done
```
