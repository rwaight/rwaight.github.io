---
title: Building Windows 10 with GitHub Actions
date:
  created: 2024-02-13
  updated: 2025-01-28
authors:
  - rwaight
slug: building-windows-10-with-github-actions
tags:
  - GitHub
  - GitHub/Actions
  - Virtualization
  - Windows
---

# Building Windows 10 with GitHub Actions

My goal was to use GitHub Actions to build Windows 10 images... but have been running into some issues...

### Using QEMU Builder

**QEMU Builder Docs**:

- https://developer.hashicorp.com/packer/integrations/hashicorp/qemu/latest/components/builder/qemu
- https://www.qemu.org/docs/master/system/index.html
- https://wiki.qemu.org/Documentation
- https://qemu.weilnetz.de/doc/9.0/index.html
- https://wiki.gentoo.org/wiki/QEMU/Options

##### Use virt-install instead of qemu?

See https://askubuntu.com/questions/1181765/qemu-system-x86-64-property-md-clear-not-found


#### QEMU Builder Logging

Add `-serial file:./qemu-output.log` to the `qemu_args` or to the command.
Otherwise, add `-D qemu-debug.log` to the `qemu_args` or to the command.

References:

- https://en.wikibooks.org/wiki/QEMU/Monitor#log
- https://stackoverflow.com/questions/72375049/logging-as-many-info-as-possible-using-qemu-system
- https://askubuntu.com/questions/1393012/ubuntu-qemu-display-output-to-logfile
- https://superuser.com/questions/269228/write-qemu-booting-virtual-machine-output-to-a-file
- https://cpolizzi.github.io/podman/enabling-qemu-cli-monitoring-and-logging.html
- https://stackoverflow.com/questions/57282462/how-to-enable-kvm-qemu-logs


#### Articles/blogs about building VMs with QEMU and KVM

- https://raphtlw.medium.com/how-to-set-up-a-kvm-qemu-windows-10-vm-ca1789411760
    - Setup a Windows 10 VM with QEMU and KVM
- https://www.tecmint.com/install-qemu-kvm-ubuntu-create-virtual-machines/
    - How to Install QEMU/KVM on Ubuntu to Create Virtual Machines
- Install and Use Qemu on Ubuntu
    - https://itsfoss.com/qemu-ubuntu/
- How to create Windows installation ISO with built-in VirtIO drivers
    - https://portal.nutanix.com/page/documents/kbs/details?targetId=kA00e000000bt28CAA


##### Questions about building VMs with QEMU and KVM

- https://superuser.com/questions/1057959/windows-10-in-kvm-change-boot-disk-to-virtio
    - Windows 10 in KVM: change boot disk to Virtio


# Win10 Build Issue Tracking

This is a list of the known issues related to building Windows 10 images...


## QEMU Builder Known issues

QEMU Builder Known issues:

- https://github.com/hashicorp/packer/issues/10223
    - When using qemu "disk_image: true", packer tries to open output file twice and fails
- https://github.com/hashicorp/packer-plugin-qemu/issues/168
    - QEMU packer build is unable to start the windows OS ISO
    - _Opened on March 19, 2024_ and is **still open**
    - **Overview**: When trying to run the qemu packer build to build windows 2022 image, it is not recognizing the iso and it is struck at the BIOS only.
- https://github.com/hashicorp/packer-plugin-qemu/issues/144
    - Qemu not launching VNC Viewer to connect to VM even with explicit setting 'headless = false'
    - _Opened on June 10, 2023_ and is **still open**
    - **Overview**: Qemu is not launching the user VNC Viewer automatically on my Macs. The docs on this page for the `headless` setting implies that it should be launching the vncviewer unless `headless = true`: https://developer.hashicorp.com/packer/plugins/builders/qemu  I've set `headless = false` explicitly in the packer config and it still doesn't start the user VNC Viewer.
- https://github.com/hashicorp/packer-plugin-qemu/issues/131
    - net_bridge and WinRM communicator
    - _Opened on March 16, 2023_ and is **still open**
    - **Overview**: When defining a net_bridge and using the WinRM communicator, some unexpected things happen.
- https://github.com/hashicorp/packer-plugin-qemu/issues/85
    - QEMU builder unable to bring up builder VM for windows server ISO
    - This _was closed as completed on September 28, 2022_
    - **Overview**: I am currently attempting to use the QEMU builder to build a basic windows 10 image but it seems that whenever it attempts to build it just ends immediately...


### Using the cdrom and disk

There might be an issue accessing the ISO and virtio drivers...

- https://github.com/hashicorp/packer-plugin-qemu/issues/136
- https://github.com/hashicorp/packer-plugin-qemu/issues/35
- https://github.com/hashicorp/packer/issues/10211
- https://github.com/hashicorp/packer/issues/10280


### Testing the ISO

According to https://docs.fedoraproject.org/en-US/quick-docs/qemu/#testing-iso-images, we should be able to test an ISO by running:
```bash
qemu-system-x86_64 -m 512M -cdrom ./virtio-win-0.1.248.iso
```

When attempting to run `qemu-system-x86_64 -m 512M -cdrom ./virtio-win-0.1.248.iso` in the runner, we get the following:
```bash
  gtk initialization failed
  Error: Process completed with exit code 1.
```

**Links about testing an ISO**
- https://www.kubuntuforums.net/forum/general/documentation/knowledge-base/663368-test-a-bootable-iso-cdrom-or-usb-stick-using-qemu


#### error: `gtk initialization failed`

```bash
  gtk initialization failed
  Error: Process completed with exit code 1.
```

Issues related to the `gtk initialization failed` error:

- https://discuss.hashicorp.com/t/qemu-gtk-initialization-error-ubuntu-22-04/39397
- https://github.com/hashicorp/packer/issues/10211
- https://github.com/sickcodes/Docker-OSX/issues/445
- https://github.com/sickcodes/Docker-OSX/issues/517

Other links about the `gtk initialization failed` error:

- https://forum.osdev.org/viewtopic.php?f=13&t=56325


## Other links

QEMU documentation:

- https://web.archive.org/web/20200304204518/https://qemu.weilnetz.de/doc/qemu-doc.html
- https://www.qemu.org/docs/master/system/bootindex.html
- https://wiki.gentoo.org/wiki/QEMU/Options

Run `qemu` in the command line

- https://ostechnix.com/setup-headless-virtualization-server-using-kvm-ubuntu/
- https://stackoverflow.com/questions/6710555/how-to-use-qemu-to-run-a-non-gui-os-on-the-terminal
- https://stackoverflow.com/questions/68512608/how-to-run-headless-qemu-without-libvirt-on-a-remote-ubuntu-debian-linux-server
- https://stackoverflow.com/questions/49716931/how-to-run-qemu-with-nographic-and-monitor-but-still-be-able-to-send-ctrlc-to
- https://www.baeldung.com/linux/qemu-from-terminal


### Debugging and testing

- https://docs.fedoraproject.org/en-US/quick-docs/virtualization-howto-debug-issues/
- https://www.linux-kvm.org/page/WindowsGuestDrivers/UpdatedGuestDebugging
- https://docs.fedoraproject.org/en-US/quick-docs/qemu/#testing-iso-images


### Building a VM

Other links about building a VM using KVM:

- https://www.reddit.com/r/linuxquestions/comments/tlwc1e/kvmqemu_how_to_create_a_vm_on_a_headless_setup/
- https://serverfault.com/questions/434064/correct-way-to-move-kvm-vm
- https://ostechnix.com/setup-headless-virtualization-server-using-kvm-ubuntu/
- https://www.reddit.com/r/linux/comments/11ruj9u/creating_a_qemu_windows_10_vm_on_linux/
- https://askubuntu.com/questions/1293497/help-setting-up-a-windows-vm-with-qemu-kvm
- https://bbs.archlinux.org/viewtopic.php?id=277584
- https://bbs.archlinux.org/viewtopic.php?id=274354
- https://futurewei-cloud.github.io/ARM-Datacenter/qemu/how-to-launch-aarch64-vm/


### Building a VM with virt-install

- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install#sect-Guest_virtual_machine_installation_from_ISO_image

