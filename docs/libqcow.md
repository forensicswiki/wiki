---
tags:
  -  Libyal
  -  Disk Imaging
  -  LGPL
  -  Tools
---
The **libqcow** package contains a library and applications to read the
[QEMU Copy-On-Write (QCOW) image](qcow_image_format.md) format.

## Tools

The **libqcow** package contains the following tools:

- **qcowinfo**, which shows the information about QCOW files.
- **qcowmount**, which FUSE mounts QCOW image files.

## Examples

FUSE mounting a QCOW image (libqcow 20111009 or later)

    qcowmount image.qcow mount_point

## History

Libqcow was created by [Joachim Metz](joachim_metz.md) in 2010.

## Also See

[QEMU Copy-On-Write (QCOW) image format](qcow_image_format.md)

## External Links

- [Project site](https://github.com/libyal/libqcow/)
- [Building libqcow and tools from
  source](https://github.com/libyal/libqcow/wiki/Building)
- [Mounting a QCOW
  image](https://github.com/libyal/libqcow/wiki/Mounting)

