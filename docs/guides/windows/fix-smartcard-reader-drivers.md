---
title: Fix Smartcard Reader Drivers
date:
  created: 2025-02-01
  updated: 2025-02-01
categories:
  - Windows
tags:
  - Windows
  - Smartcard
  - NeedToStandardizeTags
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
```PowerShell
{% include 'windows/win-registry-RetryDeviceInitialize' %}
```


<!--- Test including external pages in files from https://mkdocs-macros-plugin.readthedocs.io/en/stable/advanced/#including-external-files-in-pages --->

- - -

## IOGEAR Smartcard Readers

Local notes from the [IOGEAR Product Knowledge Site](https://iogear.custhelp.com/) about their smartcard reader devices.

### Why does my GSR202/GSR205/GSR212 not work with my smart card and my Windows Computer?

!!! note "Important"

    In order to get the GSR202/GSR205/GSR212 device to work, the **code 31** error had to be resolved first.

- - -

> This section is from [https://iogear.custhelp.com/app/answers/detail/a_id/2931/](https://iogear.custhelp.com/app/answers/detail/a_id/2931/)

<!--- from https://iogear.custhelp.com/app/answers/detail/a_id/2931/ --->

The Driver on the GSR202 / GSR205 / GSR212 should be plug and play on Windows 10 and 11. 

However, sometimes it can help to reinstall the driver. 

*Do this without the card inserted*

You can double check and ensure that Windows installed the correct driver by going into Device Manager > locate the smart card readers category and expand > double click the entry in that category > Driver > Update driver > Browse my computer Let me pick from a list of available drivers. Microsoft usbccid smart card reader (WUDF).

Once the driver is installed, try rebooting and attempt to use the reader again. This would be the only thing to check on regarding drivers for this unit.
You can then go back into Device Manager and try inserting your card. Upon inserting, there should now see a new category named, "Smart Cards" which means that the PC is ackowledging a card being inserted to the reader.

- - -
