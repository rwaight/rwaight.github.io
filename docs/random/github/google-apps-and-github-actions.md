---
title: Using Google Apps Script with GitHub Actions
date:
  created: 2023-10-24
  updated: 2024-06-25
authors:
  - rwaight
#slug: github-ops-notes
tags:
  - GitHub
  - GitHub/Actions
  - Google/Apps Script
---


# Using Google Apps Script with GitHub Actions

https://developers.google.com/apps-script - Google Apps Script
https://github.com/google/clasp - Command Line Apps Script Projects


#### Use python to interact with Google App Script

Links:
- https://developers.google.com/apps-script/api/quickstart/python

Other links:
- https://www.google.com/search?q=python+connect+to+google+app+script
- https://www.xlwings.org/blog/python-for-google-sheets


##### Example execute_apps_script.py

Execute Google Sheets Macro or Apps Script Programatically using python and Google Apps Script API
- from: https://gist.github.com/vperezb/6bdcdd23ea2754f152ffd7c9c82b127e

```python
'''
Gist from the post https://medium.com/@victor.perez.berruezo/execute-google-apps-script-functions-or-sheets-macros-programmatically-using-python-apps-script-ec8343e29fcd
Code partially from Google Apps Script Quickstart https://developers.google.com/apps-script/api/quickstart/python
'''

import pickle
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.currentonly']
    
def get_scripts_service():
    """Calls the Apps Script API.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Credentials path from the credentials .json file 
            # from step 3 from Google Cloud Platform section
            flow = InstalledAppFlow.from_client_secrets_file(
                '.credentials/client_id.json', SCOPES) 
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('script', 'v1', credentials=creds)


service = get_scripts_service()
# API ID from step 3 in Google Sheets/Script section
API_ID = "YOUR_API_ID___NO_SCRIPT_ID" 

# Instead macro_test select your macro function name 
# from step 5 in Sheets/Script section
request = {"function": "macro_test"} 

try:
    response = service.scripts().run(body=request, scriptId=API_ID).execute()
except errors.HttpError as error:
    # The API encountered a problem.
    print(error.content)
```


### Links for integrations
- https://developers.google.com/apps-script
- https://github.com/google/clasp
- https://github.com/ericanastas/deploy-google-app-script-action

Other links:
- https://gist.github.com/NikitaAvvakumov/10cad2fef7d5ae303b2ba92c0fffec2d
- https://codenotary.com/blog/use-google-sheets-apps-script-to-track-open-source-github-and-docker-statistics
- https://ramblings.mcpher.com/drive-sdk-and-github/getting-your-apps-scripts-to-github/
- https://github.com/brucemcpherson/gasGit
- https://www.google.com/search?q=github+action+run+google+app+script
- https://hawksey.info/blog/2022/06/repost-how-to-automate-google-apps-script-deployments-and-workflows-with-github-actions/


#### Example code.js

Google Apps Script - send spreadsheet changes to an external API
- from: https://gist.github.com/NikitaAvvakumov/10cad2fef7d5ae303b2ba92c0fffec2d

```js
// provided `onEdit` trigger cannot use `UrlFetchApp.fetch`.
// create a custom-named function, then add it as a new trigger in "Edit" > "Current Project Triggers"
// with events "From spreadsheet" > "On edit"
function customOnEdit(e) {
  const range = e.range;
  const row = range.getRow();
  const sheet = e.source.getActiveSheet();
  
  const data = {
    vendor: sheet.getRange(row, 1).getValue(),
    sku: sheet.getRange(row, 2).getValue(),
    title: sheet.getRange(row, 3).getValue(),
    cost: sheet.getRange(row, 4).getValue()
  };
  Logger.log('data: ' + JSON.stringify(data));
  
  const keys = Object.keys(data);
  for (var i = 0; i < keys.length; i++) {
    var key = keys[i];
    if (data[key].length === 0) {
      Logger.log(key + ' contains no data, aborting.');
      return;
    }
  }
  
  Logger.log('All values in place, sending.');
  send(data);
}

function send(data) {
  // Key-value properties can be added under "File" > "Project properties" > "Script properties"
  const scriptProperties = PropertiesService.getScriptProperties();
  const baseURL = scriptProperties.getProperty('baseURL');
  // const baseURL = 'https://xxxxxxx.ngrok.io';  // for local testing
  
  const authData = {
    'email': scriptProperties.getProperty('email'),
    'password': scriptProperties.getProperty('password')
  };
  
  const authOpts = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(authData)
  };

  const authResp = UrlFetchApp.fetch(baseURL + '/api/login', authOpts);  
  
  const authorization = authResp.getHeaders()["Authorization"];

  const options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(data),
    'headers': {
      'Authorization': authorization
    }
  };
  
  const response = UrlFetchApp.fetch(baseURL + '/admin_api/vendor_products', options);
  Logger.log(JSON.stringify(response));
}
```


#### Example copy_files.gs

Google Apps Script to Copy Folder Recursively
- from: https://gist.github.com/KenjiOhtsuka/d4432b6d80ad2b81ab7c965de2a8a00d

```js
/**
This is a code of Google Apps Script for copying google drive folder content to other folder.

## Which situation the code resolve.

Google doesn't allow to move folder content to other folder which is managed by
other organization according to the policy of the GSUITE organization.
And, Google doesn't allow to change the content owner to the user in other
organizations.

For example, XXXXX@gmail.com can not move the folder to
shared folder managed by a GSUITE organization.
And, XXXXX@gmail.com can not change owner to the user in
a GSUITE user.

Even in such situation, a user can read the folder content so the user can
copy the content.

This script copies the folder to other folder recursively,
even if the destination folder is accessible and managed by other GSUITE
organization.

## Why it is created.

There is a webpage to copy a folder recursively but
the user in a GSUITE organization is sometimes prohibited
to use the script managed by others.
*/

function myFunction() {
  // put source folder ID.
  const fromFolder = DriveApp.getFolderById('1234567ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  // put destination folder ID.
  const toFolder = DriveApp.getFolderById('1234567abcdefghijklmnopqrstuvwxyz')
  // copy the folder content recursively.
  copy(fromFolder, toFolder)
}

function copy(fromFolder, toFolder) {
  // copy files
  var files = fromFolder.getFiles()
  while (files.hasNext()) {
    var file = files.next();
    var newFile = file.makeCopy(toFolder)
    newFile.setName(file.getName())
  }

  // copy folders
  var folders = fromFolder.getFolders()
  while (folders.hasNext()) {
    var folder = folders.next()
    var newFolder = toFolder.createFolder(folder.getName())
    copy(folder, newFolder)
  }
}
```


## End
