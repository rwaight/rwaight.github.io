---
# page configuration
title: Using GitHub Matrix Strategy in Workflows
description: >
  Using GitHub Matrix Strategy in Workflows
icon: octicons/repo-template-24
status: new
# page metadata
draft: true
date:
  created: 2025-07-31
  updated: 2025-09-18
authors:
  - rwaight
categories:
  - GitHub
slug: github-workflows-matrix-strategy
tags:
  - GitHub
links:
  # All relative links are resolved from the docs directory.
  - references/index.md
  - resources/index.md
---

<!---  # Using GitHub Matrix Strategy in Workflows  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

This is a template file for blog posts in MkDocs.  In order to keep it simple to create new posts, the template file should have the following:

### References

- https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs#using-job-outputs-in-a-matrix-job
- https://github.com/actions/download-artifact#download-multiple-filtered-artifacts-to-the-same-directory
- https://github.com/actions/upload-artifact#not-uploading-to-the-same-artifact
- GitHub Discussions:
    - https://github.com/orgs/community/discussions/17245
        - https://github.com/actions/runner/pull/2477
        - https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions#status-check-functions
    - https://github.com/orgs/community/discussions/26639
    - https://github.com/orgs/community/discussions/25364
    - [`26822` - Status check for a matrix jobs](https://github.com/orgs/community/discussions/26822)

### Download multiple (filtered) Artifacts to the same directory
<!--- from https://github.com/actions/download-artifact#download-multiple-filtered-artifacts-to-the-same-directory --->

In multiple arch/os scenarios, you may have Artifacts built in different jobs. To download all Artifacts to the same directory (or matching a glob pattern), you can use the `pattern` and `merge-multiple` inputs.

```yml
jobs:
  upload:
    strategy:
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.runs-on }}
    steps:
    - name: Create a File
      run: echo "hello from ${{ matrix.runs-on }}" > file-${{ matrix.runs-on }}.txt
    - name: Upload Artifact
      uses: actions/upload-artifact@v4
      with:
        name: my-artifact-${{ matrix.runs-on }}
        path: file-${{ matrix.runs-on }}.txt
  download:
    needs: upload
    runs-on: ubuntu-latest
    steps:
    - name: Download All Artifacts
      uses: actions/download-artifact@v4
      with:
        path: my-artifact
        pattern: my-artifact-*
        merge-multiple: true
    - run: ls -R my-artifact
```


### Status Checks for Matrix Jobs

Example from [`26822` - Status check for a matrix jobs](https://github.com/orgs/community/discussions/26822), provided in [this comment](https://github.com/orgs/community/discussions/26822#discussioncomment-3305794)":

> late to the party but looks like `result` of matrix now works as expected when using: `needs.<job_id>.result`
> 
> so I can have just one single additional job which I can set as required

```yaml
results:
    if: ${{ always() }}
    runs-on: ubuntu-latest
    name: Final Results
    needs: [build]
    steps:
      - run: |
          result="${{ needs.build.result }}"
          if [[ $result == "success" || $result == "skipped" ]]; then
            exit 0
          else
            exit 1
          fi
```


#### Testing in a build workflow

```yaml
  final-checks:
    needs: [changes, run-build]
    if: always()
    runs-on: ubuntu-latest
    steps:

      - name: Check if 'run-build' job succeeded or was skipped
        id: check-build
        if: needs.run-build.result != 'skipped'
        run: |
          echo "Checking the result of the 'run-build' job... "
          ##
          result="${{ needs.run-build.result }}"
          ##
          ##if [[ $result == "success" || $result == "skipped" ]]; then
          if [[ $result == "success" ]]; then
              echo "Setting my_var to 'true' since the 'run-build' job succeeded... "
              my_var=true
          else
              echo "Setting my_var to 'false' since the 'run-build' job did not succeed... "
              my_var=false
          fi
          echo "My var: ${my_var} "
          echo "my-var=${my_var}" >> $GITHUB_OUTPUT
          ##
          echo "end of the 'check-build' step... "
        shell: bash
```


## Example section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
massa, nec semper lorem quam in massa.

<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
