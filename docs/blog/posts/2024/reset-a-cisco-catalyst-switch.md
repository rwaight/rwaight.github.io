---
title: Reset a Cisco Catalyst Switch
description: >
  Commands needed to reset Cisco Catalyst Switches to factory defaults
icon: material/factory
#status: new
# page metadata
draft: false
date:
  created: 2024-09-05
  updated: 2025-02-18
authors:
  - rwaight
categories:
  - Hardware
#slug: reset-a-cisco-catalyst-switch
tags:
  - Cisco
  - Hardware
  - Reset
---

<!---  ### Reset a Cisco Switch  --->
<!---  do not put an actual 'heading 1' if it is the same as the title  --->
<!--- this section was created on 2024-09-05 --->

Here is a summary of the commands needed to [reset Cisco Catalyst Switches to factory defaults](https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/217969-reset-catalyst-switches-to-factory-defau.html):
```shell
# enter configuration mode
enable
# remove the startup configuration file
write erase
# remove the VLAN configuration
delete flash:vlan.dat
# then reboot the switch
reload
```

If there are other files that need to be deleted, run the following **before** issuing the `reload` command:
```shell
show file information flash:?
delete flash:config.text.backup
delete flash:config.text.old
delete flash:*.old
```


<!---  below are notes from the Cisco support docs:  https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/217969-reset-catalyst-switches-to-factory-defau.html  --->
<!--- 
## Reset Catalyst Switches with Cisco IOS Software

### Reset Switch Configuration
 --->
<!--- from https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/217969-reset-catalyst-switches-to-factory-defau.html#toc-hId-1031752778 --->
<!---
To reset the switch to factory default, issue the `erase startup-config` or `write erase` command. This command does not clear the boot variables, such as config-register and boot system settings.

You can alter the boot system parameters with the `boot` command. In Catalyst 4500/4000 and 6500/6000 series switches which run Cisco IOS Software, you can change the configuration register value with the `config-register`  command.

This example shows how to reset a switch which runs Cisco IOS Software to factory defaults with the `write erase` command:
```shell
Cat2950# write erase
Erasing the nvram filesystem will remove all files! Continue? [confirm]y[OK]
Erase of nvram: complete
Cat2950#
Cat2950# reload

System configuration has been modified. Save? [yes/no]: n    

!--- Do not save the configuration at this prompt. Otherwise, the switch !--- reloads with the current running configuration and does not reset to default. 

Proceed with reload? [confirm]y                              

2w0d: %SYS-5-RELOAD: Reload requested

C2950 Boot Loader (C2950-HBOOT-M) Version 12.1(11r)EA1, RELEASE SOFTWARE (fc1)
Compiled Mon 22-Jul-02 18:57 by antonino
WS-C2950G-12-EI starting...


!--- Output suppressed. 


32K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address: 00:05:DC:C9:79:00
Motherboard assembly number: 73-5781-08
Motherboard serial number: FAB0515A069
Model revision number: 02
Model number: WS-C2950-24
System serial number: FAB0517Q00B

--- System Configuration Dialog ---

Would you like to enter the initial configuration dialog? [yes/no]:n 
00:00:16: %SPANTREE-5-EXTENDED_SYSID: Extended SysId enabled for type vlan
00:00:21: %SYS-5-RESTART: System restarted --
Cisco Internetwork Operating System Software 
Cisco IOS (tm) C2950 Software(C2950-I6Q4L2-M)Version 12.1(19)EA1, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2003 by cisco Systems, Inc.
Compiled Tue 09-Dec-03 00:12 by yenanh

Press RETURN to get started!

00:00:37: %LINK-5-CHANGED: Interface Vlan1, changed state to administratively down
00:00:38: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to down
Switch>
Switch>
```

At this stage, the switch configuration has reset to the factory defaults, with the exclusion of the VLAN information.

 --->
<!--- 
### Reset VLAN Information
 --->
<!--- from https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/217969-reset-catalyst-switches-to-factory-defau.html#toc-hId--775701685 --->
