# Material for MkDocs Container

Public image: `ghcr.io/rwaight/rwaight.github.io/mkdocs-material`

This image is built in this repository from a public Python Alpine base and pinned PyPI packages. It does not wrap the upstream `squidfunk/mkdocs-material` image. It is intended for **local preview** of this site. The MkDocs development server is not suitable for production deployment.

Plugin versions for the image are pinned in [`requirements.txt`](requirements.txt). The root `mkdocs-requirements.txt` file is a separate local lockfile and is not used by this image or by the GitHub Pages deploy workflow.

The image is **linux/amd64** only. On Apple Silicon, Docker Desktop will emulate it.

## Pull

After a production `vX.Y.Z` git tag, GHCR publishes `latest`. A new package can start **private** even from a public repository; set `ghcr.io/rwaight/rwaight.github.io/mkdocs-material` to Public in GitHub Packages once, then pull without logging in:

```shell
docker pull ghcr.io/rwaight/rwaight.github.io/mkdocs-material:latest
```

## Tags

Git tags in this repository look like `v0.1.13`. The literal `v`-prefixed patch tag (for example `v0.1.13`) is not also a GHCR tag.

| Event | GHCR tags |
| --- | --- |
| Production git tag `v0.x.y` (push or manual dispatch) | `0.x.y`, `v0.x`, `latest`, `sha-<short>` |
| Production git tag `v1.x.y` or later | `X.Y.Z`, `vX.Y`, `vX`, `latest`, `sha-<short>` |
| Feature branch (path-filtered) | `branch-<sanitized-name>`, `sha-<short>` |
| Manual dispatch from `main` | `sha-<short>` only |

While the image is in the `0.x` series, a moving `v0` tag is **not** published.

Feature-branch and other test images never receive `latest` or production semver aliases.

## Run (local preview)

From the repository root:

```shell
docker run --rm -it -p 8000:8000 -e ENABLE_GIT_COMMITTERS=false -v ${PWD}:/docs ghcr.io/rwaight/rwaight.github.io/mkdocs-material:latest
```

Then open [http://localhost:8000](http://localhost:8000). `ENABLE_GIT_COMMITTERS=false` skips unauthenticated GitHub API calls from the git-committers plugin during local preview.

## Included packages

Pinned in `requirements.txt`:

- mkdocs-material 9.7.7
- mkdocs-awesome-nav
- mkdocs-macros-plugin
- mkdocs-git-revision-date-localized-plugin
- mkdocs-git-committers-plugin-2
