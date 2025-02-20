---
title: Random Synology Notes
description: >
  This page has random Synology notes that need to be organized.
#icon: octicons/repo-template-24
#status: new
# page metadata
draft: false
date:
  created: 2017-12-04
  updated: 2025-02-20
authors:
  - rwaight
categories:
  - Synology
#slug: random-synology-notes
tags:
  - Synology
  - Random
  - Need to organize
---

<!---  # Random Synology Notes  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->

## Networking

Network ports

- [What network ports are used by Synology services?](https://www.synology.com/en-us/knowledgebase/DSM/tutorial/General/What_network_ports_are_used_by_Synology_services)


### Networking Issues

- Error: `Please make sure the ip address of the synology NAS is correct`
    - [troubleshoot NAS connection problems](https://kb.synology.com/en-global/DSM/tutorial/What_can_I_do_to_troubleshoot_NAS_connection_problems)
- Error `connection failed`
    - [why connection failed?](https://kb.synology.com/en-us/DSM/tutorial/DSM_update_why_connection_failed)


## DS Audio

### DS Audio and Google Home

#### Untrusted certificate on Chromecast

**error message**: `Your certificate is untrusted by Chromecast. Please log in to DS audio again with HTTPS disabled, or install a valid certificate on Synology NAS.`

Synolog Community links:

- [DS Audio and Google Home (casting)](https://community.synology.com/enu/forum/1/post/127125)
    - Suggestion on Apr 19, 2020
    > Can you check to see if Audio Station is tied to the certificate. Control Panel > Security > Certificate.  If Audiostation isn't there you can select Configure and change Audio Station to use the Let's Encrypt cert.
    - Suggestion on May 04, 2020
    > Can you go to the application portal and assign the port for HTTPS, then see if the application shows up under the drop down for the certificate. If that works and chromecasting doesn't you may need to restart the diskstation. I'd be curious to know if that works or not.
- [Chromecast Certificate Untrusted](https://community.synology.com/enu/forum/17/post/68075)
- [DS Audio to Chromecast Audio HTTPS certificate message](https://community.synology.com/enu/forum/1/post/137039?page=2&sort=oldest)
- [DS Audio and SSL issues](https://community.synology.com/enu/forum/1/post/150667)

Synolog Forum links:

- [SSL Certificate untrusted - workaround issues](https://www.synoforum.com/threads/ssl-certificate-untrusted-workaround-issues.9911/)

Other links:

- Reddit
    - [DS Audio HTTPS problems](https://www.reddit.com/r/synology/comments/qu0qiv/ds_audio_https_problems/)
    - [Certificate Mismatch](https://www.reddit.com/r/synology/comments/ejuzt1/certificate_mismatch/)
    - [DS Audio and Google Home casting/streaming problems](https://www.reddit.com/r/synology/comments/k6jn81/ds_audio_and_google_home_castingstreaming_problems/)
    - [DS Audio Google Home Casting](https://www.reddit.com/r/synology/comments/ewsq32/ds_audio_google_home_casting/)
- [Fixing Synology ‘Untrusted Certificate’](https://www.minmaxgeek.com/blog/fix-synology-ssl)


#### Installing a CA cert on Chromecast

This section is a follow up of the [Untrusted certificate on Chromecast](#untrusted-certificate-on-chromecast) section.  Here are some links related to installing a CA cert on Chromecast

- Google searches
    - ["google install certificate authority on chromecast"](https://www.google.com/search?q=google%20install%20certificate%20authority%20on%20chromecast)
    - ["google home speaker install certificate"](https://www.google.com/search?q=google+home+speaker+install+certificate)
    - ["synology certificate for ds audio"](https://www.google.com/search?q=synology+certificate+for+ds+audio)
- [XDA forums: Install CA cert on Chromecast](https://xdaforums.com/t/install-ca-cert-on-chromecast.4273539/)
- Google Support:
    - [Can I install or import a CA certificate into the Google TV system?](https://support.google.com/googletv/thread/218880777/can-i-install-or-import-a-ca-certificate-into-the-google-tv-system?hl=en)
- Stack Overflow
    - [Chromecast self-signed SSL certificate](https://stackoverflow.com/questions/21959435/chromecast-self-signed-ssl-certificate)
    - [Client Certificate on a Google Chromecast](https://stackoverflow.com/questions/32556497/client-certificate-on-a-google-chromecast)
- Reddit
    - [Integrating google home with HA - SSL certificates and remote access help](https://www.reddit.com/r/homeassistant/comments/1daq1gw/integrating_google_home_with_ha_ssl_certificates/)

