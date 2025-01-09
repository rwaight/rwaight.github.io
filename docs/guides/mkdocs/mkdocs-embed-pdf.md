---
title: Embed PDF in Mkdocs
draft: false
date:
  created: 2025-01-03
  updated: 2025-01-08
description: >
  Embed a PDF into MkDocs
authors: [rwaight]
categories:
  - MkDocs
slug: embed-pdf-in-mkdocs
tags:
  - MkDocs
  - MkDocs/Examples
  - ShouldBeInGuides
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

From https://fabacademy.org/2022/labs/kannai/Instruction/tips/embed_pdf/

## Embed PDF in Mkdocs

```shell
docs
├── guides
│   └── mkdocs
│       ├── mkdocs-embed-google-docs.md
│       └── mkdocs-embed-pdf.md
├── files
│   └── example.pdf
└── index.md
```

```markdown
<embed src="../../../files/example.pdf" type="application/pdf" width="100%" height=800>
```

The PDF is from [https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf](https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf)

<embed src="../../../files/example.pdf" type="application/pdf" width="100%" height=800>
