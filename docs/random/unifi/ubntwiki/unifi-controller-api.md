---
title: Ubiquiti Community Wiki UniFi Controller API docs
date:
  created: 2024-12-18
  updated: 2024-12-19
---


# UniFi Controller API docs

from https://ubntwiki.com/products/software/unifi-controller/api

Documentation of API endpoints on the UniFi controller software.  This is a reverse engineering project that is based on browser captures, jar dumps, and reviewing other software that has been written to work with the controller.  It's received minimal testing.

There are two main types of calls.  One would be the REST-like which provide get/post/put/delete where post is to the base and put/delete are often tied to the _id of the object that you are working with.  The second major type of web interface provided is an agent/call based system where you pass a command to an agent to perform an action.  Both use application/json formatting for all data transfer.  When updating a specific object you must use PUT or else a new object will be created.

**NOTE: All calls are relative to the base controller URL**

Calls return both a web status as well as JSON formatted output.  200 codes indicate a successful call and other indicate errors. I am using the placeholder `{site}` for the site name which for many installations will be `default`.

```json
# Login required
{ "data" : [ ] , "meta" : { "msg" : "api.err.LoginRequired" , "rc" : "error"}}
# Call was a success but returned no values
{ "data" : [ ] , "meta" : { "rc" : "ok"}}
# NOTE: If meta contains a count it's because the data values have been truncated
'meta': {'count': 4818, 'rc': 'ok'} # from the api/s/{site}/stat/event endpoint
```

## UDM Pro API

**NOTE:** There are two critical differences between Unifi controllers and the UDM Pro's API:

  * The login endpoint is `/api/auth/login``
  * All API endpoints need to be prefixed with `/proxy/network` (e.g. `https://192.168.0.1/proxy/network/api/s/default/self`)

### Examples

<!--- <accordion collapsed="true"> --->
 
```shell
# authenticate and save the cookie contents in local file cookie.txt with switch '-c'
curl -k -X POST --data '{"username": "usr", "password": "$pw"}' --header 'Content-Type: application/json' -c cookie.txt https://udmp:443/api/auth/login
# responds with json data

# pass the local file cookie.txt with switch '-b'
curl -k -X GET -b cookie.txt https://udmp/proxy/network/api/s/default/self
# responds with proper json
```

```python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {"Accept": "application/json","Content-Type": "application/json"}
data = {'username': 'usr', 'password': 'pw'}
s = requests.Session()
r = s.post('https://udmp:443/api/auth/login', headers = headers,  json = data , verify = False, timeout = 1)
print(r.status_code)
print(s.get('https://udmp/proxy/network/api/s/default/self', headers = headers, verify = False, timeout = 1).text)
```

## Controller Endpoints

These are REST calls that can be made without a site context.  I do not believe any updates ( PUT ) can be called on these endpoints.

| Path                 | Method  | Notes |
|:---------------------|:--------|:------|
| status               | GET     | Returns some very basic server information - This appears to be the only endpoint that can be reached without an authentication       |
| <code> { "data" : [ ] , "meta" : { "rc" : "ok" , "server_version" : "5.7.23" , "up" : true , "uuid" : "0e727580-ffff-ffff-ffff-403dcd5a7bd4"}}  </code>         |||
| api/login            | POST    | requires dict of username, password, and optionally remember=true for long-running sessions.  Returns 200 for success and a cookie that is your session. **NOTE:** On UDM Pros this is api/auth/login.  |
| api/logout           | POST    | destroys the sever side session id which will make future attempts with that cookie fail |
| api/self             | GET     | Logged in user **NOTE:** On UDM Pros this is api/users/self.    |
| api/self/sites       | GET     | Get basic information for all sites on this controller          |
| api/stat/sites       | GET     | Same as above with an additional information on health and new alerts for each site      |
| api/stat/admin       | GET     | List administrators and permissions for all sites               |
| api/system/poweroff  | POST    | Turns off the UDM **NOTE:** X-CSRF-Token header required (from e.g. the login response) + Super Admin access rights        |
| api/system/reboot    | POST    | Reboot the UDM **NOTE:** X-CSRF-Token header required (from e.g. the login response) + Super Admin access rights           |

## Site Endpoints

All commands are presumed to be prefixed with `api/s/{site}`

| Path                           | Method        | Notes |
|:-------------------------------|:--------------|:------|
| stat/health                    | GET           | Health status of the site   |
| self                           | GET           | Logged in user              |
| stat/ccode                     | GET           | List of country codes       |
| stat/current-channel           | GET           | List of all RF channels based on the site country code                  |
| stat/sysinfo                   | GET           | Some high-level information about the controller                        |
| stat/event                     | GET           | List site events by most recent first, 3000 result limit                |
| rest/event                     | GET           | List site events by oldest, no limit? (api.err.NotFound per controller version 7.1.66)  |
| stat/alarm                     | GET           | List alarms by most recent, 3000 result limit?                          |
| rest/alarm                     | GET           | List alarms by oldest, no limit? (api.err.NotFound per controller version 7.1.66)       |
| stat/sta                       | GET           | List of all _active_ clients on the site                                |
| rest/user                      | GET/POST/PUT  | List of all configured/known clients on the site                        |
| stat/device-basic              | GET           | List of site devices with only 'adopted', 'disabled', 'mac', 'state', 'type' keys, useful for filtering on type     |
| stat/device                    | GET/POST      | Detailed list of all devices on site.  (**Controller only**) Can be filtered by POSTing `{"macs": ["mac1", ... ]}`  |
| stat/device/{mac}              | GET           | (**UDM only**) Detailed list of device filtered by mac address          |
| rest/device/{_id}              | PUT           | Updates to devices get PUT here, why?                                   |
| rest/setting                   | GET/PUT       | Detailed site settings, updating requires adding key and _id to path for PUT ../setting/{key}/{_id}                 |
| stat/routing                   | GET           | All active routes on the device                                         |
| rest/routing                   | GET/PUT       | User defined routes (HTTP response 500 per controller version 7.1.66)   |
| rest/firewallrule              | GET/PUT       | User defined firewall rules.  This does not show auto-generated rules   |
| rest/firewallgroup             | GET/PUT       | ​User defined firewall groups.                                           |
| rest/wlanconf                  | GET/PUT       | List WLANs, edit current WLANs and create new WLANs                     |
| rest/wlanconf/{_id}            | PUT           | Update configuration of current WLAN designated by '_id'                |
| rest/tag                       | GET/PUT?      | Tagged macs (api.err.Invalid per controller version 7.1.66)             |
| stat/rogueap                   | GET/POST      | Neighboring APs optional json post 'within' = seen in the last x hours  |
| stat/sitedpi                   | GET/POST      | DPI stats requires type="by_app" or "by_cat"                            |
| stat/stadpi                    | GET/POST      | DPI stats requires type="by_app" or "by_cat" optionally filtered macs=[..., ]     |
| stat/dynamicdns                | GET           | DynamicDNS information and status like current ip, last changed, and status       |
| rest/dynamicdns                | GET/PUT       | DynamicDNS configuration    |
| rest/portconf                  | GET           | Switch port profiles        |
| stat/spectrumscan              | GET           | Get RF scan results, can be for a specific mac by appending to endpoint |
| rest/radiusprofile             | GET/POST/PUT  | Radius profiles             |
| rest/account                   | GET/POST/PUT  | Radius accounts             |
| rest/portforward               | GET           | List all port forwards configured on the site                           |
| stat/report/{interval}.{type}  | POST          | Intervals are '5minutes', 'hourly', and 'daily'.  Report types are 'site', 'user', and 'ap'.  Must specify attributes to be returned 'bytes', 'wan-tx_bytes', 'wan-rx_bytes', 'wlan_bytes', 'num_sta', 'lan-num_sta', 'wlan-num_sta', 'time', 'rx_bytes', 'tx_bytes'.  Can be filtered with 'macs': [...]  |
| stat/authorization             | POST          | JSON as "%%{"start": "START TIMESTAMP", "end": "END TIMESTAMP"}%%" and you will get the code that have been used between the Timestams    NOTE: X-CSRF-Token header required (from e.g. the login response) for UDM|
| stat/sdn                       | GET           | Return values as if the site is connected with the Unifi Cloud or the SSO         |

### Callable commands

<!--- the '`{"cmd": "command"}`' in the next line was '`json {"cmd": "command"}`' --->
Posting to the endpoint `api/s/{site}/cmd/<manager>` with the `{"cmd": "command"}` you can invoke commands on the controller.

| Manager  | Call                | Notes |
|:---------|:--------------------|:------|
| evtmgt   | archive-all-alarms  |       |
| sitemgr  | add-site            | desc = Descriptive name ( required ), name = shortname ( in the URL ) |
| sitemgr  | delete-site         | name = short name ( required )               |
| sitemgr  | update-site         | desc = Descriptive name ( required )         |
| sitemgr  | get-admins          | List all administrators and permission for this site   |
| sitemgr  | move-device         | mac = device mac ( required ), site_id = 24 digit id ( required )     |
| sitemgr  | delete-device       | mac = device mac ( required )                |
| stamgr   | block-sta           | mac = client mac ( required )                |
| stamgr   | unblock-sta         | mac = client mac ( required )                |
| stamgr   | kick-sta            | Disconnect: mac = client mac (required )     |
| stamgr   | forget-sta          | Forget a client ( controller 5.9.x only )    |
| stamgr   | unauthorize-guest   | Unauthorize a client device, mac = client mac (required)              |
| devmgr   | adopt               | mac = device mac ( required )                |
| devmgr   | restart             | mac = device mac ( required )                |
| devmgr   | force-provision     | mac = device mac ( required )                |
| devmgr   | power-cycle         | mac = switch mac ( required ), port_idx = PoE port to cycle ( required )                 |
| devmgr   | speedtest           | Start a speed test                           |
| devmgr   | speedtest-status    | get the current state of the speed test      |
| devmgr   | set-locate          | mac = device mac ( required ) blink unit to locate     |
| devmgr   | unset-locate        | mac = device mac ( required ) led to normal state      |
| devmgr   | upgrade             | mac = device mac ( required ) upgrade firmware         |
| devmgr   | upgrade-external    | mac = device mac ( required ), url = firmware URL ( required )        |
| devmgr   | migrate             | mac = device mac ( required ), inform_url = New Inform URL to push to device (required)  |
| devmgr   | cancel-migrate      | mac = device mac ( required )                |
| devmgr   | spectrum-scan       | mac = device mac ( ap only, required ) trigger RF scan |
| backup   | list-backups        | list of autobackup files                     |
| backup   | delete-backup       | filename ( required )                        |
| system   | backup              | create a backup.  This appears to backup to a fixed location in the filesystem           |
| stat     | clear-dpi           | resets the site wide DPI counters            |


#### Data Tables

This data was extracted from the javascript of the site.

| Model    | Type                | SKU   | Name                |
|:---------|:--------------------|:------|:--------------------|
| BZ2 | uap | UAP | Access Point |
| BZ2LR | uap | UAP-LR | Access Point Long-Range |
| S216150 | usw | US-16-150W | Switch 16 PoE (150 W) |
| S224250 | usw | US-24-250W | Switch 24 PoE (250 W) |
| S224500 | usw | US-24-500W | Switch 24 PoE (500 W) |
| S248500 | usw | US-48-500W | Switch 48 PoE (500 W) |
| S248750 | usw | US-48-750W | Switch 48 PoE (750 W) |
| S28150 | usw | US-8-150W | Switch 8 PoE (150 W) |
| U2HSR | uap | UAP-Outdoor+ | Access Point Outdoor+ |
| U2IW | uap | UAP-IW | Access Point In-Wall |
| U2L48 | uap | UAP-LR | Access Point Long-Range |
| U2Lv2 | uap | UAP-LRv2 | Access Point Long-Range |
| U2M | uap | UAP-Mini | Access Point Mini |
| U2O | uap | UAP-Outdoor | Access Point Outdoor |
| U2S48 | uap | UAP | Access Point |
| U2Sv2 | uap | UAPv2 | Access Point |
| U5O | uap | UAP-Outdoor5 | Access Point Outdoor 5 |
| U6ENT | uap | U6-Enterprise | Access Point WiFi 6 Enterprise |
| U6EXT | uap | U6-Extender | Access Point WiFi 6 Extender |
| U6IW | uap | U6-IW | Access Point WiFi 6 In-Wall |
| U6M | uap | U6-Mesh | Access Point WiFi 6 Mesh |
| U7E | uap | UAP-AC | Access Point AC |
| U7EDU | uap | UAP-AC-EDU | Access Point AC EDU |
| U7Ev2 | uap | UAP-AC | Access Point AC |
| U7HD | uap | UAP-AC-HD | Access Point AC HD |
| U7IW | uap | UAP-AC-IW | Access Point AC In-Wall |
| U7IWP | uap | UAP-AC-IW-Pro | Access Point AC In-Wall Pro |
| U7LR | uap | UAP-AC-LR | Access Point AC Long-Range |
| U7LT | uap | UAP-AC-Lite | Access Point AC Lite |
| U7MP | uap | UAP-AC-M-Pro | Access Point AC Mesh Pro |
| U7MSH | uap | UAP-AC-M | Access Point AC Mesh |
| U7NHD | uap | UAP-nanoHD | Access Point nanoHD |
| U7O | uap | UAP-AC-Outdoor | Access Point AC Outdoor |
| U7P | uap | UAP-AC-Pro | Access Point AC Pro |
| U7PG2 | uap | UAP-AC-Pro | Access Point AC Pro |
| U7SHD | uap | UAP-AC-SHD | Access Point AC SHD |
| UAE6 | uap | U6-Extender-EA | Access Point WiFi 6 Extender |
| UAIW6 | uap | U6-IW-EA | Access Point WiFi 6 In-Wall |
| UAL6 | uap | U6-Lite | Access Point WiFi 6 Lite |
| UALR6 | uap | U6-LR-EA | Access Point WiFi 6 Long-Range |
| UALR6v2 | uap | U6-LR | Access Point WiFi 6 Long-Range |
| UALR6v3 | uap | U6-LR | Access Point WiFi 6 Long-Range |
| UAM6 | uap | U6-Mesh-EA | Access Point WiFi 6 Mesh |
| UAP6 | uap | U6-LR | Access Point WiFi 6 Long-Range |
| UAP6MP | uap | U6-Pro | Access Point WiFi 6 Pro |
| UASXG | uas | UAS-XG | Application Server XG |
| UBB | ubb | UBB | Building-to-Building Bridge |
| UBBXG | ubb | UBB-XG | Building-to-Building Bridge XG |
| UCK | uck | UCK | Cloud Key |
| UCK-v2 | uck | UCK | Cloud Key |
| UCK-v3 | uck | UCK | Cloud Key |
| UCKG2 | uck | UCK-G2 | Cloud Key Gen2 |
| UCKP | uck | UCK-G2-Plus | Cloud Key Gen2 Plus |
| UCMSH | uap | UAP-XG-Mesh | Access Point Mesh XG |
| UCXG | uap | UAP-XG | Access Point XG |
| UDC48X6 | usw | USW-Leaf | Switch Leaf |
| UDM | udm | UDM | Dream Machine |
| UDMB | uap | UAP-BeaconHD | Access Point BeaconHD |
| UDMPRO | udm | UDM-Pro | Dream Machine Pro |
| UDMPROSE | udm | UDM-SE | Dream Machine Special Edition |
| UDR | udm | UDR | Dream Router |
| UDW | udm | UDW | Dream Wall |
| UDWPRO | udm | UDWPRO | Dream Wall Pro |
| UFLHD | uap | UAP-FlexHD | Access Point FlexHD |
| UGW3 | ugw | USG-3P | Security Gateway |
| UGW4 | ugw | USG-Pro-4 | Security Gateway Pro |
| UGWHD4 | ugw | USG | Security Gateway |
| UGWXG | ugw | USG-XG-8 | Security Gateway XG |
| UHDIW | uap | UAP-IW-HD | Access Point In-Wall HD |
| ULTE | uap | U-LTE | UniFi LTE |
| ULTEPEU | uap | U-LTE-Pro | UniFi LTE Pro |
| ULTEPUS | uap | U-LTE-Pro | UniFi LTE Pro |
| UP1 | uap | USP-Plug | SmartPower Plug |
| UP4 | uph | UVP-X | Phone |
| UP5 | uph | UVP | Phone |
| UP5c | uph | UVP | Phone |
| UP5t | uph | UVP-Pro | Phone Professional |
| UP5tc | uph | UVP-Pro | Phone Professional |
| UP6 | uap | USP-Strip | SmartPower Strip (6 ports) |
| UP7 | uph | UVP-Executive | Phone Executive |
| UP7c | uph | UVP-Executive | Phone Executive |
| US16P150 | usw | US-16-150W | Switch 16 PoE (150 W) |
| US24 | usw | USW-24-G1 | Switch 24 |
| US24P250 | usw | US-24-250W | Switch 24 PoE (250 W) |
| US24P500 | usw | US-24-500W | Switch 24 PoE (500 W) |
| US24PL2 | usw | US-L2-24-PoE | Switch 24 PoE |
| US24PRO | usw | USW-Pro-24-PoE | Switch Pro 24 PoE |
| US24PRO2 | usw | USW-Pro-24 | Switch Pro 24 |
| US48 | usw | US-48-G1 | Switch 48 |
| US48P500 | usw | US-48-500W | Switch 48 PoE (500 W) |
| US48P750 | usw | US-48-750W | Switch 48 PoE (750 W) |
| US48PL2 | usw | US-L2-48-PoE | Switch 48 PoE |
| US48PRO | usw | USW-Pro-48-PoE | Switch Pro 48 PoE |
| US48PRO2 | usw | USW-Pro-48 | Switch Pro 48 |
| US624P | usw | USW-Enterprise-24-PoE | Switch Enterprise 24 PoE |
| US648P | usw | USW-Enterprise-48-PoE | Switch Enterprise 48 PoE |
| US68P | usw | USW-Enterprise-8-PoE | Switch Enterprise 8 PoE |
| US6XG150 | usw | US-XG-6PoE | Switch 6 XG PoE |
| US8 | usw | US-8 | Switch 8 |
| US8P150 | usw | US-8-150W | Switch 8 PoE (150 W) |
| US8P60 | usw | US-8-60W | Switch 8 (60 W) |
| USAGGPRO | usw | USW-Pro-Aggregation | Switch Aggregation Pro |
| USC8 | usw | US-8 | Switch 8 |
| USC8P150 | usw | US-8-150W | Switch 8 PoE (150 W) |
| USC8P450 | usw | USW-Industrial | Switch Industrial |
| USC8P60 | usw | US-8-60W | Switch 8 (60 W) |
| USF5P | usw | USW-Flex | Switch Flex |
| USFXG | usw | USW-Flex-XG | Switch Flex XG |
| USL16LP | usw | USW-Lite-16-PoE | Switch Lite 16 PoE |
| USL16P | usw | USW-16-PoE | Switch 16 PoE |
| USL24 | usw | USW-24-G2 | Switch 24 |
| USL24P | usw | USW-24-PoE | Switch 24 PoE |
| USL48 | usw | USW-48-G2 | Switch 48 |
| USL48P | usw | USW-48-PoE | Switch 48 PoE |
| USL8A | usw | USW-Aggregation | Switch Aggregation |
| USL8LP | usw | USW-Lite-8-PoE | Switch Lite 8 PoE |
| USL8MP | usw | USW-Mission-Critical | Switch Mission Critical |
| USMINI | usw | USW-Flex-Mini | Switch Flex Mini |
| USPPDUP | usw | USP-PDU-Pro | SmartPower PDU Pro |
| USPRPS | usw | USP-RPS | SmartPower Redundant Power System |
| USXG | usw | US-16-XG | Switch XG 16 |
| USXG24 | usw | USW-EnterpriseXG-24 | Switch Enterprise XG 24 |
| UXBSDM | uap | UWB-XG-BK | WiFi BaseStation XG |
| UXGPRO | uxg | UXG-Pro | Next-Generation Gateway Pro |
| UXSDM | uap | UWB-XG | WiFi BaseStation XG |
| p2N | uap | PICOM2HP | PicoStation M2 HP |

##### DPI Category Codes

| DPI Category Code | Name |
|:------------------|:-----|
| 0 | Instant messaging |
| 1 | P2P |
| 3 | File Transfer |
| 4 | Streaming Media |
| 5 | Mail and Collaboration |
| 6 | Voice over IP |
| 7 | Database |
| 8 | Games |
| 9 | Network Management |
| 10 | Remote Access Terminals |
| 11 | Bypass Proxies and Tunnels |
| 12 | Stock Market |
| 13 | Web |
| 14 | Security Update |
| 15 | Web IM |
| 17 | Business |
| 18 | Network Protocols |
| 19 | Network Protocols |
| 20 | Network Protocols |
| 23 | Private Protocol |
| 24 | Social Network |
| 255 | Unknown |

There are 2,213 named applications in the javascript **dynamic.dpi.js**.  See extracted [[products:software:unifi-controller:api:cat_app_json|cat_app.json]] to include for lookups and example usage.

The application id is a compound id using bitwise shift left on the category id + application id sent from the api using `list_dpi_stats_filtered`
```js
function compoundId($cat, $app){
  return (intval($cat) << 16) + intval($app);
}
```

### Uncategorized

Dump of found endpoints waiting for documentation

```shell
# logged in user
api/s/{site}/self

# Country codes
api/s/{site}/stat/ccode
# Availible WiFi channels
api/s/{site}/stat/current-channel

# Dashboard health
api/s/{site}/stat/health

# Active client devices
api/s/{site}/stat/sta
# Configured clients
api/s/{site}/stat/user

# Devices
api/s/{site}/stat/device-basic - mac, type
api/s/{site}/stat/device - can be filtered with macs: [ ..., ... ]

# Detailed site settings
api/s/{site}/stat/sysinfo

# /rest/ endpoints also have a /cnt/ which returns the count for the data portion
# can be used for any but seems targeted towards alarms

# Site settings
api/s/{site}/rest/setting - this is a big one with a weird mechanism for updating

# Firewall rules
api/s/{site}/rest/firewallrule - only lists user-defined rules

# Firewall groups
api/s/{site}/rest/firewallgroup

# routes
api/s/{site}/rest/routing

# Alarms
# List of alarms
api/s/{site}/rest/alarm
# list of unarchived alarms
api/s/{site}/rest/alarm?archived=false

# User groups - bandwith settings
api/s/{site}/rest/usergroup

# ?
api/s/{site}/rest/wlangroup

# Wireless networks
api/s/{site}/rest/wlanconf

# ?
api/s/{site}/rest/tag

# Site networks
api/s/{site}/rest/networkconf

# example backup path
dl/autobackup/autobackup_5.7.23_20180513_0000_1526169600008.unf

# Insights - sessions
api/s/{site}/stat/session?type=all&start=1526515200&end=1526688000

# Insights - EDU streams
api/s/{site}/stat/stream

# Switch port conf?
api/s/{site}/rest/portconf

# Configured port forwards and uPNP - transfer bytes is listed but doesn't appear populated
api/s/{site}/stat/portforward

# Update User (User are the clients)  
api/s/{site}/upd/user/{UserId}
you can get the users and the userid from "/api/s/{SiteId}/stat/alluser" (All Clients) or "/api/s/{SiteId}/stat/sta" (Active Clients) which contains the client id (_id).
example: change name of user with clientid 5aca464bb79fc60200460394 to 'test-raw':
${curl_cmd} --data "json={'name':'test-raw'}" $baseurl/api/s/$site/upd/user/5aca464bb79fc60200460394

# Get Hotspot Configuration
guest/s/{site}/hotspotconfig
You will get in "auth" the value "none" if it is not activated, if it is activated you will get for exemple "hotspot" and many other values on the design of the page.

# Get Hotspot Packages
guest/s/{site}/hotspotpackages
 ??

# Get trafficrules
v2/api/site/{site}/trafficrules
also possible to add new rule with a POST request.

# Edit trafficrules
v2/api/site/{site}/trafficrules/{id}/
PUT or DELETE request to update or delete traffic rule
GET is not allowed on specific trafficrules.
With PUT the result code is 201 and not 200 for successful change.


# Possible list of all callable managers
system
devmgr
stamgr
evtmgr
cfgmgr
hotspot
sitemgr
streammgr
backup
throughput
stat
firmware
firewall
elite

```

## Update of Port Forward Rules

This may apply to other configurations, but initial testing shows that port forward rules can be enabled/disabled using PUT against the endpoint /api/s/{site}/rest/portforward/{rule-id} with a body such as:
```json
{
    "enabled": true
}
```

The rule ID can be retrieved using the above described port forwarding GET request and is found in the "_id" key.

New rules can be created using POST, but be aware that there seems to be very little validation (it's possible to create entries with no information other than the fact that they're enabled, for example).
