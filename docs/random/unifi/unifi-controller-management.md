---
title: UniFi Controller Management
description: >
  Notes about managing the UniFi controller.
#icon: octicons/repo-template-24
#status: new
date:
  created: 2024-08-25
  updated: 2025-05-13
---


## Local Management

UniFi Local Management: [https://help.ui.com/hc/en-us/articles/28457353760919-UniFi-Local-Management](https://help.ui.com/hc/en-us/articles/28457353760919-UniFi-Local-Management)

Documentation about local management:

- https://ubntwiki.com/products/software/unifi-controller/api
- PHP API library: https://github.com/Art-of-WiFi/UniFi-API-client
- Python API library: https://unificontrol.readthedocs.io/en/latest/introduction.html


### Local APIs

Local UniFi APIs:

- UniFi Controller API: https://ubntwiki.com/products/software/unifi-controller/api
- UniFi Controller Python Interface: https://unificontrol.readthedocs.io/en/latest/introduction.html
    - GitHub: https://github.com/nickovs/unificontrol

#### UniFi API resources

Resources to access the UniFi API:

- API Client: https://github.com/Art-of-WiFi/UniFi-API-client
    - https://artofwifi.net/blog/how-to-access-the-unifi-controller-by-wan-ip-or-hostname-on-a-udm-pro
- API Browser: https://github.com/Art-of-WiFi/UniFi-API-browser
    - Docker for API browser: https://github.com/scyto/docker-UnifiBrowser
- Resources [from this community post](https://community.ui.com/questions/Accessing-UniFi-Controller-API-locally-hosted-via-Python/f9728aba-caac-4897-955c-08b1c839c235#answer/3c8ec42f-2adb-492e-a1ce-07be53d029c1)
    - Using Python
        - PyUnifi: https://github.com/finish06/pyunifi
        - UniFi Python API: https://github.com/frehov/Unifi-Python-API
            - Archived August 2022
            - from https://community.ui.com/questions/Unifi-Python-API/4c58d69c-3278-4b61-86fd-7b497c70c102
        - UniFi API: https://github.com/brontide/unifiapi
        - unificontrol: https://github.com/nickovs/unificontrol
        - aiounifi: https://github.com/Kane610/aiounifi
    - Websocket
        - UniFi Websocket Interface: https://github.com/NickWaterton/Unifi-websocket-interface/


#### Community posts

Community posts related to managing the UniFi controller with the API:

- [Remote access to controller API](https://community.ui.com/questions/Remote-access-to-controller-API/33846504-9ede-49e2-a959-4d28f19154c5)
- [Accessing UniFi Controller API, locally hosted via Python](https://community.ui.com/questions/Accessing-UniFi-Controller-API-locally-hosted-via-Python/f9728aba-caac-4897-955c-08b1c839c235)
- [It's possible to automate Unifi Controller configs](https://community.ui.com/questions/Its-possible-to-automate-Unifi-Controller-configs/60c753ee-ec19-43f3-b758-cfce6eae6162)


#### Automation resources

Automation resources:

- Ansible role for Unifi Admin service: https://github.com/ajanis/ansible-unifi

## Remote Management

UniFi Remote Management via Site Manager: [https://help.ui.com/hc/en-us/articles/11444786290071-UniFi-Remote-Management-via-Site-Manager](https://help.ui.com/hc/en-us/articles/11444786290071-UniFi-Remote-Management-via-Site-Manager)

#### Non-local APIs

UniFi Site Manager API:  [https://developer.ui.com/site-manager-api/](https://developer.ui.com/site-manager-api/)
