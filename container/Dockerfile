FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

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

WORKDIR /docs

EXPOSE 8000

ENTRYPOINT ["/sbin/tini", "--", "mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
