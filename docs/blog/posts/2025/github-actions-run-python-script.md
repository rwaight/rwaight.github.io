---
title: Run Python in a composite GitHub Action
description: >
  Running a Python script in a GitHub Action and capture the output
# icon: octicons/repo-template-24
# https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
status: new
# page metadata
draft: false
date:
  created: 2025-10-22
  updated: 2025-10-22
authors:
  - rwaight
categories:
  - GitHub
slug: github-actions-run-python-script
tags:
  - GitHub
  - Workflows
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Run Python in a composite GitHub Action  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

To pass output from a Python script within a step of a GitHub Actions workflow, you will be able to write the variable using GitHub's specified `GITHUB_OUTPUT` environment variable using Python's `open` function with the `a` (append) mode.

<!-- more -->

<!--- https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/#adding-an-excerpt --->

### A single line variable

An example is available in [this comment](https://github.com/orgs/community/discussions/28146#discussioncomment-4110404) in GitHub discussions, which states:

> Do the same thing as with the shell, _append_ to the file specified in the `GITHUB_OUTPUT` environment variable:
> 
> ```python
> import os
> name = 'my_name'
> value = 'my_value'
> with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
>     print(f'{name}={value}', file=fh)
> ```
> 
> Mind that for values with multiple lines you now have to use the same format as for [multiline environment variables](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#multiline-strings), instead of URL encoding them.


### A multiline variable

An example is available in [this comment](https://github.com/orgs/community/discussions/28146#discussioncomment-5638014) in GitHub discussions, which states:

> For those struggling to do the multiline output work, I made a small method that set its up for you:
> 
> ```python
> import uuid
> 
> def set_multiline_output(name, value):
>     with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
>         delimiter = uuid.uuid1()
>         print(f'{name}<<{delimiter}', file=fh)
>         print(value, file=fh)
>         print(delimiter, file=fh)
> ```
> 
> Just call it with:
> 
> ```python
> set_multiline_output("value", my_multiline_string)
> ```



### Configuring a composite GitHub Action

In a composite GitHub Action, you will need to configure the [`action.yml` metadata file properly](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax). 

When running the Python script within the GitHub Action, be sure to define the **step `id`** as well as declare the [proper `outputs`](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax#outputs-for-composite-actions), here is an example:

```yaml
# [ ... trimmed action.yml config ... ]

outputs:
  json-output:
    description: "a JSON object created by the python script"
    value: ${{ steps.inline-python-script.outputs.MY_OUTPUT_CUSTOM_JSON }}
  var-output:
    description: "a variable created by the python script"
    value: ${{ steps.inline-python-script.outputs.MY_OUTPUT_CUSTOM_VAR }}

runs:
  using: composite
  steps:

    - name: Run inline Python script
      id: inline-python-script
      env:
        MY_CUSTOM_VAR_1: ${{ inputs.custom-input-1 }}
        MY_CUSTOM_VAR_2: ${{ inputs.custom-input-2 }}
      run: |
        """
        This is a custom python script that is part of a composite GitHub Action
        """
        #
        import os
        import requests
        import json
        import uuid
        #
        # [ ... trimmed script ... ]
        #
        # function to send single-line variable to github output
        def set_output(name, value):
            with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
                print(f'{name}={value}', file=fh)
        #
        # function to send multi-line variable to github output
        def set_multiline_output(name, value):
            with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
                delimiter = uuid.uuid1()
                print(f'{name}<<{delimiter}', file=fh)
                print(value, file=fh)
                print(delimiter, file=fh)
        # functions to send to github output are from
        # https://github.com/orgs/community/discussions/28146#discussioncomment-5638023
        # https://github.com/orgs/community/discussions/28146#discussioncomment-5638014
        # Example usage above
        # [ ... trimmed script ... ]
        #
        if __name__ == "__main__":
            # Get parameters from environment variables set by the action
            my_custom_var1 = os.getenv('MY_CUSTOM_VAR_1')
            my_custom_var2 = os.getenv('MY_CUSTOM_VAR_2')
            combined_vars = my_custom_var1 + " " + my_custom_var2
            #
            # [ ... trimmed script ... ]
            #
            # Export to GitHub output
            ## Single line Example
            set_output("MY_OUTPUT_CUSTOM_VAR", combined_vars)
            #
            ## Multiline Example
            set_multiline_output("MY_OUTPUT_CUSTOM_JSON", json.dumps(all_json_details))
            # [ ... trimmed script ... ]
        # [ ... trimmed script ... ]
      shell: python

    - name: Print the output from the Python script
      id: print-python-output
      run: |
        echo "going to print the variable output..."
        echo "$PYTHON_VAR_OUTPUT"
        echo ""
        echo "going to print the JSON output and pipe it to jq..."
        echo "$PYTHON_JSON_OUTPUT" | jq '.'
      env:
        PYTHON_VAR_OUTPUT: ${{ steps.inline-python-script.outputs.MY_OUTPUT_CUSTOM_VAR }}
        PYTHON_JSON_OUTPUT: ${{ steps.inline-python-script.outputs.MY_OUTPUT_CUSTOM_JSON }}
      shell: bash

# [ ... trimmed action.yml config ... ]
branding:
  # Ref: https://haya14busa.github.io/github-action-brandings/
  # fork: https://github.com/rwaight/github-action-brandings
  icon: download
  color: blue
```


### References

- GitHub Docs
    - [Creating a composite action](https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action)
    - [Metadata syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax)
- GitHub `actions/runner`
    - [`#919` Add automatic stdout, stderr and exitcode outputs per step](https://github.com/actions/runner/issues/919)
- GitHub Community Discussions
    - [`#133693` How to pass output from a GitHub Action step that is in python?](https://github.com/orgs/community/discussions/133693)
    - [`#28146` How to set-output from a python script in Github workflow step.](https://github.com/orgs/community/discussions/28146)
    - [`#40515` Setting output using python file working on ubuntu-latest runner, but not working on windows-latest runner](https://github.com/orgs/community/discussions/40515)
    - [`#58980` How to access `output` from a custom action?](https://github.com/orgs/community/discussions/58980)
- Stackoverflow
    - [Github Action use existing Python script and get String output](https://stackoverflow.com/questions/61656704/github-action-use-existing-python-script-and-get-string-output)
    - [How to use the output of github-script action in the next step](https://stackoverflow.com/questions/78379151/how-to-use-the-output-of-github-script-action-in-the-next-step)
    - [broken link](https://stackoverflow.com/questions/79677425/how-to-pass-output-from-a-github-action-step-that-is-in-python)
- Others
    - [Medium - GitHub Actions Workflow — Python and Environment Variables](https://medium.com/@vinod.chelladuraiv/github-actions-workflow-python-and-environment-variables-74f5446f63de)

