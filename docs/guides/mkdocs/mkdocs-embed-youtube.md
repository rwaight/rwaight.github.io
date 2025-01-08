---
title: Embed YouTube video in Mkdocs
draft: false
date:
  created: 2025-01-08
  updated: 2025-01-08
description: >
  Embed a YouTube video into MkDocs
authors: [rwaight]
categories:
  - MkDocs
slug: embed-youtube-in-mkdocs
tags:
  - YouTube
  - MkDocs
  - MkDocs/Examples
  - NeedToStandardizeTags
---

This example is from [https://jameshfisher.com/2017/08/30/how-do-i-make-a-full-width-iframe/](https://jameshfisher.com/2017/08/30/how-do-i-make-a-full-width-iframe/)

## Embed YouTube video in Mkdocs
<!--- From https://jameshfisher.com/2017/08/30/how-do-i-make-a-full-width-iframe/ --->

```html
<div>
  <div style="position:relative;padding-top:56.25%;">
    <iframe src="https://www.youtube.com/embed/nckseQJ1Nlg" frameborder="0" allowfullscreen
      style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe>
  </div>
</div>
```

<div>
  <div style="position:relative;padding-top:56.25%;">
    <iframe src="https://www.youtube.com/embed/nckseQJ1Nlg" frameborder="0" allowfullscreen
      style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe>
  </div>
</div>

Per [this discussion comment in `squidfunk/mkdocs-material`](https://github.com/squidfunk/mkdocs-material/discussions/5291#discussioncomment-5466727): if you do not need to maintain an aspect ratio, then the surrounding `div` elements can be dropped
> If you don't need to maintain an aspect ratio, you can drop the surrounding divs mentioned in the article, but it's often desired.
