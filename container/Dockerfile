# pass 'VERSION_SOURCE' as a build argument to dynamically set the MkDocs version
# https://docs.docker.com/build/building/variables/#arg-usage-example
ARG VERSION_SOURCE=latest

# https://hub.docker.com/r/squidfunk/mkdocs-material
# https://github.com/squidfunk/mkdocs-material/pkgs/container/mkdocs-material
#FROM ghcr.io/squidfunk/mkdocs-material:9.6.19
FROM ghcr.io/squidfunk/mkdocs-material:$VERSION_SOURCE
#FROM ghcr.io/squidfunk/mkdocs-material
# https://hub.docker.com/r/squidfunk/mkdocs-material/tags

# https://docs.docker.com/reference/dockerfile/#understand-how-arg-and-from-interact
# An ARG declared before a FROM is outside of a build stage, so it can't be used in any instruction after a FROM.
# To use the default value of an ARG declared before the first FROM use an ARG instruction without a value inside of a build stage.
ARG VERSION_SOURCE
RUN echo $VERSION_SOURCE

RUN pip install mkdocs-awesome-nav
RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-git-revision-date-localized-plugin
RUN pip install mkdocs-git-committers-plugin-2

LABEL name="mkdocs-material"
LABEL source_version="$VERSION_SOURCE"
LABEL repository="https://github.com/rwaight/rwaight.github.io"
LABEL homepage="https://github.com/rwaight/rwaight.github.io"

# Set working directory
WORKDIR /docs

## Start development server by default
ENTRYPOINT ["/sbin/tini", "--", "mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
