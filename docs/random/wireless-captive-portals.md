---
title: Wireless Captive Portals
date:
  created: 2025-03-25
  updated: 2025-03-25
authors:
  - rwaight
#slug: image-builder-notes
tags:
  - Wireless
  # use 'random' for uncategorized pages in the 'random' directory
  - random
---

While you should not use a public wifi network, there are known wifi networks that use captive portals.  This page has some notes about trying to make sure you can connect to a legitimate captive portal.

### URLs to test

Here are some URLs you can use to test connection to a captive portal:

- Device agnostic
    - [www.example.com](http://www.example.com)
    - [captive.apple.com/hotspot-detect.html](http://captive.apple.com/hotspot-detect.html)
    - [httpforever.com](http://httpforever.com)
    - [1.1.1.1](http://1.1.1.1)
    - [neverssl.com](http://neverssl.com)
    - [www.apple.com/library/test/success.html](http://www.apple.com/library/test/success.html)
- Apple devices
    - [captive.apple.com](https://captive.apple.com/)
    - [captive.apple.com/hotspot-detect.html](http://captive.apple.com/hotspot-detect.html)
    - [www.apple.com/library/test/success.html](https://www.apple.com/library/test/success.html)
- Windows devices
    - [www.msftconnecttest.com/connecttest.txt](http://www.msftconnecttest.com/connecttest.txt)
    - [ipv6.msftconnecttest.com/connecttest.txt](http://ipv6.msftconnecttest.com/connecttest.txt)
    - [msftconnecttest.com/](http://msftconnecttest.com/)
    - [www.msftncsi.com/ncsi.txt](http://www.msftncsi.com/ncsi.txt)
- Android devices
    - [connectivitycheck.gstatic.com](http://connectivitycheck.gstatic.com)


### Other notes

Here are other notes about captive portals and wireless controllers:

- [Zapier blog - force network login page to open](https://zapier.com/blog/open-wifi-login-page/)
- [Medium blog - How to Force a Wifi Login Page](https://medium.com/future-vision/how-to-force-a-wifi-login-page-507841fda86f)
- Device agnostic
    - [IETF datatracker captive portal API](https://datatracker.ietf.org/doc/html/draft-ietf-capport-api)
- Android devices
    - [developer.android.com **captive portal** feature](https://developer.android.com/about/versions/11/features/captive-portal)
- Cisco devices
    - [Cisco 5500 series wireless controllers](https://www.cisco.com/c/en/us/support/docs/wireless/5500-series-wireless-controllers/108501-webauth-tshoot.html)

