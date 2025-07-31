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
  updated: 2025-07-31
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

<!---  # Blog post template  --->
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

## This is a draft page

<!--- 
- The page **front-matter** section, which includes:
    - Page configuration
    - Page metadata
- Standard category (or categories)
- Standard tag(s)
 --->

### Page configuration

When creating a new blog post, determine the following [page configuration](https://squidfunk.github.io/mkdocs-material/reference/) options:

- the page [`title`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-title)
- the page [`description`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-description) (**optional**)
- the page [`icon`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-icon) (**optional**)
- the page [`status`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-status) (**optional**)
- the page [`subtitle`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-subtitle) (**optional**)
- the page [`template`](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-template) (**optional**)


### Page metadata

When creating a new blog post, determine the following [page metadata](https://squidfunk.github.io/mkdocs-material/plugins/blog/#metadata):

- the post [`draft` option](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.draft)
- the post [`date`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.date)
    - can be just `date: 2025-02-18`
    - can also include [**date created** and **date updated**](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.date-update-date)
- the post [`authors`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.authors)
- the post [`categories`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.categories)
- the post [`slug`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#meta.slug)
- the post [`tags`](https://squidfunk.github.io/mkdocs-material/plugins/tags/#meta.tags)


## Putting it all together

### Front-matter

The front-matter consists of [YAML Style Meta-Data](https://www.mkdocs.org/user-guide/writing-your-docs/#yaml-style-meta-data) to define the [page configuration settings](https://squidfunk.github.io/mkdocs-material/reference/):
````yaml
---
# page configuration
title: Blog post template
description: >
  This is a template file for blog posts in MkDocs.
icon: octicons/repo-template-24
status: new
# page metadata
draft: false
date:
  created: 2025-02-18
  updated: 2025-02-18
authors:
  - rwaight
categories:
  - MkDocs
slug: blog-post-template
tags:
  - MkDocs
  - Template
---
````

## Example section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
massa, nec semper lorem quam in massa.

<!--  example comment here  -->
<!--- another example comment --->

<!---  ...  --->
