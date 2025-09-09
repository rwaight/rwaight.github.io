# https://hub.docker.com/r/squidfunk/mkdocs-material
# https://github.com/squidfunk/mkdocs-material/pkgs/container/mkdocs-material
FROM ghcr.io/squidfunk/mkdocs-material:9.6.19
#FROM ghcr.io/squidfunk/mkdocs-material
# https://hub.docker.com/r/squidfunk/mkdocs-material/tags

RUN pip install mkdocs-awesome-nav
RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-git-revision-date-localized-plugin
RUN pip install mkdocs-git-committers-plugin-2

LABEL name="mkdocs-material"
LABEL repository="http://github.com/rwaight/rwaight.github.io"
LABEL homepage="http://github.com/rwaight/rwaight.github.io"

# Set working directory
WORKDIR /docs

## Start development server by default
ENTRYPOINT ["/sbin/tini", "--", "mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
