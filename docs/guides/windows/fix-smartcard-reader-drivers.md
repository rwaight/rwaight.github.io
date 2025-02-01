---
title: Fix Smartcard Reader Drivers
date:
  created: 2025-02-01
  updated: 2025-02-01
# https://mkdocs-macros-plugin.readthedocs.io/en/latest/rendering/#opt-in-with-the-markdown-pages-header
render_macros: true
---

Some USB Smartcard Readers that work in Windows 10 may not work in Windows 11.

This guide specifically addresses issues with `Code 31` errors.  This is referenced in the Microsoft Windows docs: [Code 31 in Device Manager when Microsoft Usbccid Smartcard Reader is in a problem state](https://learn.microsoft.com/en-us/troubleshoot/windows-client/certificates-and-public-key-infrastructure-pki/code-31-device-manager-usbccid-smartcard-reader-problem)

## Code 31 in Device Manager when Microsoft Usbccid Smartcard Reader is in a problem state

### Symptoms

After a restart, Microsoft Usbccid Smartcard Reader is in a problem state with a yellow bang and this error is displayed in the device status:
> This device is not working properly because Windows cannot load the drivers required for this device. (Code 31)
> {Operation Failed}
> The requested operation was unsuccessful.

### Cause

During initialization, the smartcard driver attempts to create an instance of smart card class extension. The attempt failed and the driver isn't loaded.

### Resolution

To ensure a successful driver initialization, add the **RetryDeviceInitialize** registry key and restart the computer.

#### Registry Key

!!! note "Important"

    The registry key is available for Windows 10, version 1903 (19H1) and later versions.

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\Calais\Readers`

**Name**: RetryDeviceInitialize
**Type**: DWORD (32-bit)
**Data**: 1

#### Registry Key Example

Here is an example of the **RetryDeviceInitialize** registry key: 
```
{% include 'windows/Win11-Registry-RetryDeviceInitialize.reg' %}
```


<!--- Test including external pages in files from https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages --->
