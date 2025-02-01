---
title: Setup auth with GitHub Pages
draft: true
date:
  created: 2025-01-09
  updated: 2025-01-09
authors:
  - rwaight
#slug: setup-auth-with-github-pages
tags:
  - GitHub
  - GitHub Pages
  - MkDocs
  - Jekyll
---


### Basic Auth with GitHub Pages

- GitHub repo's on the topic:
    - [`oauth2-proxy/oauth2-proxy`](https://github.com/oauth2-proxy/oauth2-proxy)
        - A reverse proxy and static file server that provides authentication using Providers (Google, GitHub, and others) to validate accounts by email, domain or group.
        - [https://oauth2-proxy.github.io/oauth2-proxy/](https://oauth2-proxy.github.io/oauth2-proxy/)
    - [oauth2-proxy/oauth2-proxy-template](https://github.com/oauth2-proxy/oauth2-proxy-template)
        - A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.
    - [therootcompany/sso-dev](https://github.com/therootcompany/sso-dev)
        - GitHub page for OpenID Configuration and JWKs
        - [https://therootcompany.github.io/sso-dev/](https://therootcompany.github.io/sso-dev/)
        - [https://sso-dev.therootcompany.com/](https://sso-dev.therootcompany.com/)
    - [hamelsmu/oauth-tutorial](https://github.com/hamelsmu/oauth-tutorial)
        - Like GitHub Pages, but you choose who can see it without usernames & passwords.
        - Make Static Sites Private With OAuth For Free
        - [Minimal OAuth Locally](https://github.com/hamelsmu/oauth-tutorial/blob/main/local/README.md)
        - [Serving Your Site](https://github.com/hamelsmu/oauth-tutorial/blob/main/simple/README.md)
    - [austenstone/github-actions-oauth](https://github.com/austenstone/github-actions-oauth)
        - GitHub OAuth using GitHub Pages & Actions
        - [https://austenstone.github.io/github-actions-oauth/](https://austenstone.github.io/github-actions-oauth/)
    - [BorczeAngelov/PoC-NgApp-OAuth2-GoogleSheetsAPI](https://github.com/BorczeAngelov/PoC-NgApp-OAuth2-GoogleSheetsAPI)
        - Angular app integrating OAuth 2.0 with Google Sheets API, deployed on GitHub Pages
    - [peppelinux/oidc-federation-over-gh-pages](https://github.com/peppelinux/oidc-federation-over-gh-pages)
        - PoC of a OpenID Federation Trust Anchor that works entirely on github pages
    - [progrium/gh-pages-auth](https://github.com/progrium/gh-pages-auth)
        - Set up GitHub Pages and Auth0 authentication with minimal effort
    - [oxyno-zeta/s3-proxy](https://github.com/oxyno-zeta/s3-proxy)
        - S3 Reverse Proxy with GET, PUT and DELETE methods and authentication (OpenID Connect and Basic Auth)
    - [rwth-acis/openidconnect-signin](https://github.com/rwth-acis/openidconnect-signin)
        - HTML5 elements to authenticate with OpenID Connect providers
    - [felleslosninger/docs - English OIDC guide](https://github.com/felleslosninger/docs/blob/gh-pages/_docs/idporten/oidc/oidc_guide_english.md)
    - asdf
- reddit posts:
    - [Add a password to mkdocs page?](https://www.reddit.com/r/sysadmin/comments/yjlma3/add_a_password_to_mkdocs_page/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
        - [mkdocs-encryptcontent-plugin](https://pypi.org/project/mkdocs-encryptcontent-plugin/)
- [static site hosting basic auth](https://www.google.com/search?q=static+site+hosting+basic+auth)
    - [squidfunk/mkdocs-material discussions#5050](https://github.com/squidfunk/mkdocs-material/discussions/5050#discussioncomment-4972798)
- [basic auth on github pages](https://www.google.com/search?q=basic+auth+on+github+pages)
- [`oauth2-proxy/oauth2-proxy`](https://github.com/oauth2-proxy/oauth2-proxy)
    - A reverse proxy and static file server that provides authentication using Providers (Google, GitHub, and others) to validate accounts by email, domain or group.
    - [https://oauth2-proxy.github.io/oauth2-proxy/](https://oauth2-proxy.github.io/oauth2-proxy/)
    - template: [oauth2-proxy/oauth2-proxy-template](https://github.com/oauth2-proxy/oauth2-proxy-template)
        - A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.
- [GitHub login for static websites hosted on GitHub pages](https://github.com/hoodiehq/camp/issues/106)



#### The need for a proxy

As mentioned in [mkdocs/mkdocs#2832](https://github.com/mkdocs/mkdocs/issues/2832#issuecomment-1667204853), a tool like [`oauth2-proxy/oauth2-proxy`](https://github.com/oauth2-proxy/oauth2-proxy) would need to be put in front of GitHub Pages in order to enable OAuth or OIDC.
- [`oauth2-proxy/oauth2-proxy`](https://github.com/oauth2-proxy/oauth2-proxy)
    - [https://oauth2-proxy.github.io/oauth2-proxy/configuration/providers/google](https://oauth2-proxy.github.io/oauth2-proxy/configuration/providers/google)
- [Using Nginx as an SSL proxy to GitHub Pages](https://josh.fail/2017/using-nginx-as-an-ssl-proxy-to-github-pages/)
- [Blog on GitHub pages that is served from a Sub-URL](https://www.elitmus.com/blog/technology/how-we-host-our-blog-on-github-pages-and-yet-serve-it-from-our-own-sub-url/)
- [nginx reverse proxy github pages](https://gist.github.com/rrmerugu/ec0f31a4ec87b09e2f35d920daa7ce1c)
- [NGINX Reverse proxy settings to Github pages](https://gist.github.com/taddev/8872330)


### Other resources about single sign-on (SSO) setup

- [readthedocs.io](https://docs.readthedocs.io/)
    - [Setup Single Sign-On (SSO) with Google Workspace](https://docs.readthedocs.io/en/stable/guides/setup-single-sign-on-google-email.html)
    - [Setup Single Sign-On (SSO) with GitHub, GitLab, or Bitbucket](https://docs.readthedocs.io/en/stable/guides/setup-single-sign-on-github-gitlab-bitbucket.html)

