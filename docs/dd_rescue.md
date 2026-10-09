---
tags:
  - Tools
---
dd_rescue, is an an advanced evolution of [dd](dd.md), a
command line program that has been ported only for UNIX/Linux. The
program uses a complex series of flags to allow the user to image or
write data from and to [raw image files](raw_image_format.md).
Like [dcfldd](dcfldd.md), the program makes an effort to keep
the user apprised of the status of the current operation.

[ddrescue](ddrescue.md) and dd_rescue are completely
different programs which share no development between them. The two
projects are not related in any way except that they both attempt to
enhance the standard [dd](dd.md) tool and coincidentally chose
similar names for their new programs.

A large difference between [ddrescue](ddrescue.md) and
dd_rescue is that dd_rescue can pipe output to stdout whereas
[ddrescue](ddrescue.md) can only transfer block/file to
block/file.

## Use

Creating a disk image from a device.

```bash
dd_rescue /dev/hda myfile.img
```

Transferring a disk image over the network using ssh.

```bash
dd_rescue /dev/sda1 - | ssh user@remote.host "cat - > /remote/destination/file.img"
```

Adding compression to an image file on the fly.

```bash
dd_rescue /dev/sda1 - | bzip2 > /dir/file.img.bz2
```

## Caution

Unlike regular [dd](dd.md), dd_rescue does not use the command
line arguments `if` or `of`.

## See also

* [aimage](aimage.md)
* [Blackbag](blackbag.md)
* [dcfldd](dcfldd.md)
* [dd](dd.md)
* [ddrescue](ddrescue.md)
