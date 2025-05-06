# https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker
FROM squidfunk/mkdocs-material
# be sure to include the plugins that are installed in the 'publish-pages' workflow
#     check the '.github/workflows/publish-pages.yml' file
RUN pip install mkdocs-awesome-nav
RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-git-revision-date-localized-plugin
RUN pip install mkdocs-git-committers-plugin-2
