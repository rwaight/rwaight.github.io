---
title: Updating JSON objects used in a GitHub matrix
description: >
  How to update JSON objects that are used within a GitHub workflow using the GitHub matrix strategy
icon: simple/json
status: new
draft: false
date:
  created: 2025-10-30
  updated: 2025-10-30
authors:
  - rwaight
categories:
  - coding
  - GitHub
slug: using-json-with-github-matrix-strategy
tags:
  - coding
  - GitHub
  - JSON
  - Workflows
links:
  # All relative links are resolved from the docs directory.
  - resources/coding/jq-updating-json-objects.md
  - blog/posts/2025/jq-updating-json-objects.md
---

<!---  # Updating JSON objects used in a GitHub matrix  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

I have been using GitHub workflows and found that I can dynamically build JSON objects 
and use them to run GitHub workflow job variations using the [GitHub matrix strategy](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations#about-matrix-strategies). 
Each new workflow and each dynamically built JSON object can require some troubleshooting, 
especially if customizations are made compared to other workflows.


!!! note

    This is a follow up to the [_Updating JSON objects with JQ_ blog](./jq-updating-json-objects.md) when
    using JSON objects within a GitHub workflow.


### GitHub Actions Project Matrix

Some of my project **Build Workflows** use the [GitHub matrix strategy](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations#about-matrix-strategies) to process individual builds. 
Sometimes I will need to troubleshoot the `PROJECT_GH_MATRIX` variable locally; this post provides 
information about using the `PROJECT_GH_MATRIX` variable locally when working with the JSON objects.

<!-- more -->

<!--- keep the 'more' entry above in place, the text above will become an 'excerpt' on the blog site
https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/#adding-an-excerpt --->


**Capturing the Project Matrix from GitHub Actions**

When you are reviewing the output within GitHub Actions, you may see the `PROJECT_GH_MATRIX` variable. 
Copy the output from the variable to your clipboard.


#### Example converting the GitHub matrix output for local use

Given this output from a GitHub workflow:

```yaml
PROJECT_GH_MATRIX: {"project":["my-test-abc","dev-jkl","primary-test-project-xyz"],"include":[{"project":"my-test-abc","files":["my-test-abc/foo.txt"]},{"project":"dev-jkl","files":["dev-jkl/foo.txt"]},{"project":"primary-test-project-xyz","files":["primary-test-project-xyz/foo.txt"]}]}
```


In order to convert it to use locally, echo the JSON object within a command and wrap the JSON object in single quotes `'` and pipe the output to `jq . -c`; see the example below:  

!!! example "Storing the Project Matrix output for local use"

    Storing the output for local use:

    ```shell
    PROJECT_GH_MATRIX=$(echo '{"project":["my-test-abc","dev-jkl","primary-test-project-xyz"],"include":[{"project":"my-test-abc","files":["my-test-abc/foo.txt","my-test-abc/bar.log"]},{"project":"dev-jkl","files":["dev-jkl/foo.txt","dev-jkl/bar.log","dev-jkl/baz.log"]},{"project":"primary-test-project-xyz","files":["primary-test-project-xyz/foo.txt","primary-test-project-xyz/bar.log","primary-test-project-xyz/baz.txt"]}]}' | jq . -c)
    ```


Then you can use the JSON object within `jq`

```shell
echo $PROJECT_GH_MATRIX | jq .
echo $PROJECT_GH_MATRIX | jq
echo $PROJECT_GH_MATRIX | jq -r '.project'
echo $PROJECT_GH_MATRIX | jq -c
```

##### Extract project names with a space delimiter

!!! example "Extract project names with a space delimiter"

    ```shell
    # Extract project names with a space delimiter
    echo "$PROJECT_GH_MATRIX" | jq -r '.project | join(" ")'
    PROJECTS_SPACE_DELIMITED=$(echo "$PROJECT_GH_MATRIX" | jq -r '.project | join(" ")')
    ```


##### Extract project names as individual lines

!!! example "Extract project names as individual lines"

    ```shell
    # Extract project names as individual lines
    echo "$PROJECT_GH_MATRIX" | jq -r '.project[]'
    PROJECTS_LINE_DELIMITED=$(echo "$PROJECT_GH_MATRIX" | jq -r '.project[]')

    # Use in a for loop with while read
    while read -r project; do
        echo "Processing project: $project"
        # Your processing logic here
    done <<< "$PROJECTS_LINE_DELIMITED"
    ```

    Running the first command produces:

    ```shell
    $ echo "$PROJECT_GH_MATRIX" | jq -r '.project[]'
    my-test-abc
    dev-jkl
    primary-test-project-xyz
    ```



<!--- another example comment --->

<!---  ...  --->
