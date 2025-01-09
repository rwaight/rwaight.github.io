---
title: Google docs from markdown
date:
  created: 2024-10-08
  updated: 2025-01-08
authors:
  - rwaight
tags:
  - Markdown
  - Google Docs
  # use 'random' for uncategorized pages in the 'random' directory
  - random
---


## Links to review later

- [https://github.com/googleworkspace/md2googleslides](https://github.com/googleworkspace/md2googleslides)
    - Generate Google Slides from markdown
    - Issues identified in https://github.com/googleworkspace/md2googleslides/issues/216
- [https://github.com/wescpy/md2googleslides/](https://github.com/wescpy/md2googleslides/)
    - Fork of the `googleworkspace/md2googleslides` project
    - Note from https://github.com/googleworkspace/md2googleslides/issues/216#issuecomment-2564725975: this fork of the project avoids the OOB issue
- [https://github.com/vilmacio/gslides-maker](https://github.com/vilmacio/gslides-maker)
    - Generate Google Slides from Wikipedia content
- [https://github.com/intelliavant/gas-markdown-converter](https://github.com/intelliavant/gas-markdown-converter)
- [https://www.reddit.com/r/github/comments/18zaid4/push_google_docs_to_github_as_markdown_including/](https://www.reddit.com/r/github/comments/18zaid4/push_google_docs_to_github_as_markdown_including/)
- Maybe other code options in [https://github.com/topics/google-slides](https://github.com/topics/google-slides)

## googleworkspace/md2googleslides notes

### googleworkspace/md2googleslides issue 216

There is [an issue in the `googleworkspace/md2googleslides` repo](https://github.com/googleworkspace/md2googleslides/issues/216#issue-2633794983) titled **2024 - My experience in getting md2googleslides to work** which has some useful information about using the project:

> #### 2024 - My experience in getting md2googleslides to work
> After spending close to a day reading and debugging all the open issues, I've finally been able to get `example.md` to convert to Google Slides 🎉
> 
> Here's details from my device for your reference:
> 
> ```
>        _,met$$$$$gg.          [REDACTED]
>     ,g$$$$$$$$$$$$$$$P.       ------------------------- 
>   ,g$$P"     """Y$$.".        OS: Debian GNU/Linux trixie/sid x86_64 
>  ,$$P'              `$$$.     Host: [REDACTED] ThinkPad T480s 
> ',$$P       ,ggs.     `$$b:   Kernel: 6.5.0-5-amd64 
> `d$$'     ,$P"'   .    $$$    Uptime: [REDACTED]
>  $$P      d$'     ,    $$P    Packages: [REDACTED]
>  $$:      $$.   -    ,d$$'    Shell: bash 5.2.32 
>  $$;      Y$b._   _,d$P'      Resolution: 1920x1080 
>  Y$$.    `.`"Y$$$$P"'         DE: Xfce 4.18 
>  `$$b      "-.__              WM: Xfwm4 
>   `Y$$                        WM Theme: Nordic-darker 
>    `Y$$.                      Theme: Nordic-darker [GTK2/3] 
>      `$$b.                    Icons: Qogir-dark [GTK2/3] 
>        `Y$$b.                 Terminal: xfce4-terminal 
>           `"Y$b._             Terminal Font: Monospace 12 
>               `"""            CPU: Intel i5-8350U (8) @ 3.600GHz 
>                               GPU: Intel UHD Graphics 620 
>                               Memory: 10166MiB / 15736MiB
> ```
> 
> Here's how I got it to work for anyone that's still planning on using this tool today (cause it is - imo - still very cool):
> 
> ##### Setting up GCP
> 1. Head over to [GCP Console](https://console.cloud.google.com/), create a new project (I called mine `gslides-generator`), search for "APIs & Services" on the top search bar and click on "OAuth consent screen" on the left.
> 2. Setup your OAuth consent screen via the wizard by giving it a suitable name (I called mine `<myname>-md2gslides`) and adding your personal email as a test user.
> 3. Head over to the Credentials tab on the left, click "+ Create Credentials" and select "OAuth Client ID".
> 4. After that, select "Desktop app" as your Application Type and give it a suitable name (I called mine `desktop-md2gslides`)
> 5. Finally, save the generated credentials JSON file into your computer. Open the file and copy the `client_id` and `client_secret` which will come in handy later.
> 
> ##### Setting up Node.js and compiling `md2gslides`
> 1. Clone this repository to get the latest version of the md2googleslides' source code on your computer:
>    `git clone https://github.com/googleworkspace/md2googleslides.git`
> 2. Change your Node.js version to 12 (which is the only version I got this to work in) by typing `nvm use 12` (if you don't have this version installed, you can run `nvm install 12`)
> 3. Ensure that you're using Node.js version 12 by running `node --version`.
> 4. Run `npm i` from within the md2googleslides' folder you just cloned to install all dependencies.
> 5. Run `npm run compile` to build the tool. The code should build in the `lib/` folder.
> 
> #### Updating `bin/md2gslides.js`
> 1. Run `npm install google-auth-library` to install the latest version of [Google's Authentication Library for Node.js](https://cloud.google.com/nodejs/docs/reference/google-auth-library/latest#oauth2). This will be required to get support for the OAuth2 flow.
> 2. Add this import at the top of `bin/md2gslides.js`:
> 
> ```js
> const { OAuth2Client } = require('google-auth-library');
> ```
> 
> 3. To the same file, add this function:
> 
> ```js
> function getAuthenticatedClient() {
>   return new Promise((resolve, reject) => {
>     // create an oAuth client to authorize the API call.  Secrets are kept in a `keys.json` file,
>     // which should be downloaded from the Google Developers Console.
>     const oAuth2Client = new OAuth2Client(
>       "<your_client_id>", // This should come from the credentials JSON file you generated earlier
>       "<your_client_secret>",
>       "http://localhost:3000" // This doesn't matter, as long as it is localhost
>     );
> 
>     // Generate the url that will be used for the consent dialog.
>     const authorizeUrl = oAuth2Client.generateAuthUrl({
>       access_type: 'offline',
>       scope: SCOPES,
>     });
>     console.log('Authorize this app by visiting this url:', authorizeUrl);
>   });
> }
> ```
> 
> This snippet of code will help us run the latest supported version of OAuth to allow the tool to access the Google Slides and Google Drive APIs (without this, I always get the following error on the OAuth Consent Screen: `Error 401: unauthorized_client Request details: lowName=GeneralOAuthFlow`).
> 
> 4. Scroll down this file to find the `authorizeUser()` function. Make this function `async` and at the top of this function, call the `getAuthenticatedClient()` function you just created by adding the following code:
> 
> ```js
> await getAuthenticatedClient()
> ```
> 
> After that, comment out all the lines from below this line to the end of the `authorizeUser()` function to prevent any additional authentication code from running. Finally, this function should look like this:
> 
> ```js
> async function authorizeUser() {
>   // Google OAuth2 clients always have a secret, even if the client is an installed
>   // application/utility such as this.  Of course, in such cases the "secret" is
>   // actually publicly known; security depends entirely on the secrecy of refresh
>   // tokens, which effectively become bearer tokens.
> 
>   // Load and parse client ID and secret from client_id.json file. (Create
>   // OAuth client ID from Credentials tab at console.developers.google.com
>   // and download the credentials as client_id.json to ~/.md2googleslides
>   await getAuthenticatedClient()
> 
>   // let data; // needs to be scoped outside of try-catch
>   // try {
>   //   data = fs.readFileSync(STORED_CLIENT_ID_PATH);
>   // } catch (err) {
>   //   console.log('Error loading client secret file:', err);
>   //   throw err;
>   // }
>   // if (data === undefined) {
>   //   console.log('Error loading client secret data');
>   //   throw 'No client secret found.';
>   // }
>   // const creds = JSON.parse(data).installed;
> 
>   // // Authorize user and get (& store) a valid access token.
>   // const options = {
>   //   clientId: creds.client_id,
>   //   clientSecret: creds.client_secret,
>   //   filePath: STORED_CREDENTIALS_PATH,
>   //   prompt: prompt,
>   // };
>   // const auth = new UserAuthorizer(options);
>   // return auth.getUserCredentials(args.user, SCOPES);
> }
> ```
> 
> 5. Scroll all the way to the end of this file, and comment out the `.then` methods after the first `authorizeUser()` call. Your last code snippet should look like this:
> 
> ```js
> authorizeUser()
> // .then(buildSlideGenerator)
> // .then(eraseIfNeeded)
> // .then(generateSlides)
> // .then(displayResults)
> // .catch(handleError);
> ```
> 
> 6. After that, you can run this file by typing `node bin/md2gslides.js` from your terminal. You will get the following `DepreciationWarning`(s) on your terminal:
> 
> ```
> (node:60689) DeprecationWarning: ArgumentParser(): following options are renamed: 'addHelp' -> 'add_help'
> (node:60689) DeprecationWarning: The "version" argument to ArgumentParser is deprecated. Please use add_argument(..., { action: 'version', version: 'N', ... }) instead.
> (node:60689) DeprecationWarning: _ActionsContainer.addArgument() is renamed to _ActionsContainer.add_argument()
> (node:60689) DeprecationWarning: add_argument(): following options are renamed: 'defaultValue' -> 'default'
> (node:60689) DeprecationWarning: use add_argument('-u', '--user', {...}) instead of add_argument([ '-u', '--user' ], { ... })
> (node:60689) DeprecationWarning: {action: "storeTrue"} is renamed to {action: "store_true"}
> (node:60689) DeprecationWarning: ArgumentParser.parseArgs() is renamed to ArgumentParser.parse_args()
> ```
> 
> ...but not to worry, you should now see a URL output on the screen to open up your OAuth Consent Screen!
> 
> 7. Copy this link over to a web browser, ignore any security messages and complete the OAuth flow. You should end up with a "This site can’t be reached" page at the end - since nothing is running on localhost. This is fine, since what matters to us is that the URL now contains a query parameter called `code`. Copy this!
> 8. Finally, uncomment the lines of code that we commented in `bin/md2gslides.js` and comment out the `await getAuthenticatedClient()`. You may revert the `authorizeUser()` function back to a sync function too.
> 9. Now, re-run `node bin/md2gslides.js examples/example.md --use-fileio`. You should see the following prompt:
> 
> ```
> Authorize this app in your browser.
> Enter the code here:
> ```
> 
> 10. Add the code you copied from Step 7 into this prompt:
> 
> * The `examples/example.md` is the sample Markdown file provided in the source code to test conversion
> * `--use-fileio` enables the use of local files. (Even though I used the `--use-fileio` flag, I was never able to get local images to work. So I deleted the `![](image_slide.png)` on the `example.md` file before re-running the command, because this results in a runtime error)
> 
> 12. If everything worked, you should see the fully converted Google Slides open on your web browser!
> 
> Thanks for following through! I'll try my best to create a fork with these code changes - but until then, best of luck with your slides!


- - -

### googleworkspace/md2googleslides issue 216 comment 2564725975

There is [a response to issue 216](https://github.com/googleworkspace/md2googleslides/issues/216#issuecomment-2564725975) which has some useful information about the updated guide:

> Thanks for the incredibly useful guide!
> 
> When I got to **Updating bin/md2gslides.js step 9**, I got the error that md2googleslides was trying to read my Google OAuth credentials from the file `/Users/<name>/.md2googleslides/client_id.json` rather than getting the prompt you describe.
> 
> If I renamed and moved the json from **setting up GCP step 5** to `/Users/<name>/.md2googleslides/client_id.json` then re-running `node bin/md2gslides.js examples/example.md --use-fileio` results in my browser opening to a google sign in page with a `Error 400: invalid_request`, with the further details:
> 
> > The out-of-band (OOB) flow has been blocked in order to keep users secure. Follow the Out-of-Band (OOB) flow migration guide linked in the developer docs below to migrate your app to an alternative method.
> > Request details: redirect_uri=urn:ietf:wg:oauth:2.0:oob flowName=GeneralOAuthFlow
> 
> **Update:** this fork of the project avoids the OOB issue: [wescpy/md2googleslides](https://github.com/wescpy/md2googleslides/)

