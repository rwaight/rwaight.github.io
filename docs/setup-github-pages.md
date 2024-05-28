# GitHub Pages Setup

Resources:
* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)


## MkDocs

Resources:
* [Getting Started with MkDocs](https://www.mkdocs.org/getting-started/)
* [Deploying your docs to GitHub Pages](https://www.mkdocs.org/user-guide/deploying-your-docs/#github-pages)
* [`squidfunk/mkdocs-material` on GitHub](https://github.com/squidfunk/mkdocs-material)
    * the [`squidfunk/mkdocs-material` docker image](https://hub.docker.com/r/squidfunk/mkdocs-material)
* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)


### Install MkDocs Material with Docker

Here are the steps from the [installing with Docker](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker) guide:

```bash
# pull the image
docker pull squidfunk/mkdocs-material

# navigate to the root directory of the repo
cd /path/to/root/of/repo

# run the container and attach the current directory to /docs
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```


#### Adding plugins to the Docker image
From https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker

> Material for MkDocs only bundles selected plugins in order to keep the size of the official image small. If the plugin you want to use is not included, create a new `Dockerfile` and extend the official Docker image:
```bash
FROM squidfunk/mkdocs-material
RUN pip install ...
```
> Next, you can build the image with the following command:
```bash
docker build -t squidfunk/mkdocs-material .
```
> The new image can be used exactly like the official image.


### Creating a new site with Docker

After issuing the `docker run` command above, issue the following:
```bash
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
```


### Publish the site with GitHub Actions
From From https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker

> Using [GitHub Actions](https://github.com/features/actions) you can automate the deployment of your project documentation. At the root of your repository, create a new GitHub Actions workflow, e.g. .github/workflows/ci.yml, and copy and paste the following contents:
```yml
name: ci 
on:
  push:
    branches:
      - master 
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```
> Now, when a new commit is pushed to either the `master` or `main` branches, the static site is automatically built and deployed. Push your changes to see the workflow in action.

