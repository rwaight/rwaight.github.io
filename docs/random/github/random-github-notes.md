---
title: Random GitHub notes
date:
  created: 2023-05-28
  updated: 2024-06-25
authors:
  - rwaight
#slug: random-github-notes
tags:
  - GitHub
---

# Random GitHub notes


### Marking all PR files as viewed in the GitHub Web UI

The "marking all files as viewed" might be fixed in https://github.com/refined-github/refined-github/issues/3043

From https://github.com/refined-github/refined-github/issues/2444#issuecomment-613557336

> FYI: I've been using a [custom search engine in Google Chrome](chrome://settings/searchEngines) to mark all files as read/unread, switch to the rich diffs, etc.; this could be modified to use `%s` in the search URL to take "arguments" to a "Mark all as viewed" function to match file names or contents of files (you'd have to modify the script to detect such, etc.)

| Search engine                    | Keyword | Query URL                                                                                                           |
| -------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| GitHub: Display all rich diffs   | ghrd    | javascript: document.querySelectorAll('.js-rendered').forEach(button => button.click());                            |
| GitHub: Display all source diffs | ghsd    | javascript: document.querySelectorAll('.js-source').forEach(button => button.click());                              |
| GitHub: Mark all as not viewed   | gh-v    | javascript: document.querySelectorAll('.js-reviewed-checkbox').forEach(input => !input.checked \|\| input.click()); |
| GitHub: Mark all as viewed       | gh+v    | javascript: document.querySelectorAll('.js-reviewed-checkbox').forEach(input => input.checked \|\| input.click());  |

_Originally posted by @mfulton26 in https://github.com/refined-github/refined-github/issues/2444#issuecomment-613557336_

#### screenshot

![alt text](mark-pr-files-viewed-image.png)


