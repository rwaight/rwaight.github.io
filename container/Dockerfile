# Independently built from a public Python Alpine base and pinned PyPI packages.
# Plugin versions are pinned in requirements.txt (not the repo-root mkdocs-requirements.txt).
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

# git + openssh: git-revision-date and git-committers plugins
# tini: used as the image entrypoint
RUN apk add --no-cache \
      git \
      git-fast-import \
      openssh \
      tini \
 && pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r /tmp/requirements.txt \
 && rm -rf /tmp/* /root/.cache \
 && git config --system --add safe.directory /docs \
 && git config --system --add safe.directory /site

# Set working directory
WORKDIR /docs

EXPOSE 8000

## Start development server by default
ENTRYPOINT ["/sbin/tini", "--", "mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
