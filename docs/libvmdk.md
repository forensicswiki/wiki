---
tags:
  -  Libyal
  -  Disk Imaging
  -  LGPL
  -  Tools
---
The **libvmdk** package contains a library and applications to read the
[VMWare Virtual Disk Format
(vmdk)](vmware_virtual_disk_format_(vmdk).md) format.

## Tools

The **libvmdk** package contains the following tools:

- **vmdkinfo**, which shows the information about VMDK files.
- **vmdkmount**, which FUSE mounts VMDK image files.

## Examples

FUSE mounting a VMDK image

    vmdkmount image.vmdk mount_point

## History

Libvmdk was created by [Joachim Metz](joachim_metz.md) in 2009.

## Also See

- [VMWare Virtual Disk Format
  (vmdk)](vmware_virtual_disk_format_(vmdk).md)

## External Links

- [Project site](https://github.com/libyal/libvmdk/)
- [Building libvmdk and tools from
  source](https://github.com/libyal/libvmdk/wiki/Building)
- [Mounting a VMDK
  image](https://github.com/libyal/libvmdk/wiki/Mounting)

