---
tags:
  - Articles that need to be expanded
  - Volume Systems
---
The [Linux](linux.md) Logical Volume Manager, is commonly
abbreviated to LVM. Although LVM can used for other [Logical Volume
Management](https://en.wikipedia.org/wiki/Logical_Volume_Management)
variants as well.

Not all forensic tools have support for Linux Logical Volume Manager
(LVM) volumes, but most modern Linux distributions do.

## Forensic analysis

The metadata area of a LVM Physical Volume can contain multiple versions
of metadata section that contains the LVM Volume Group definitions,
including a creation date and time value.

## Mounting an LVM

### Mounting an LVM from an image

If you have an image mount the LVM read-only on a loopback device (e.g.
/dev/loop1) by:

    sudo losetup -r -o $OFFSET /dev/loop1 image.raw

Note that the offset is in bytes.

If you need to write to the image, e.g. for recovery, use
[xmount](xmount.md) to write the changes to a shadow file.

    sudo xmount --in dd --cache sda.shadow sda.raw image/

You can then safely mount the LVM in read-write mode (just omit the -r
in the previous losetup command).

To remove this mapping afterwards run:

    sudo losetup -d /dev/loop1

To scan for new physical volumes:

    lvm pvscan

You cannot unmount an active volume group. To detach (or deactivate) the
volume group:

    vgchange -a n $VOLUMEGROUP

Where \$VOLUMEGROUP is the corresponding name of the volume group

The individual volume devices are now available in:

    /dev/mapper/$VOLUMEGROUP-$VOLUMENAME

### Mounting an LVM from a device

To list the Volume Groups (VG) run:

    pvs

To list information about a Volume Group (VG) run:

    lvdisplay $VOLUMEGROUP

The field "LV Name" provides the volume name

To make the volume group known to the system (only if it was previously
exported using *vgexport* command, note that *vgimport* will alter the
data in the LVM2 header):

    vgimport $VOLUMEGROUP

And activate the volumes in the volume group (sometimes you need to run
*vgscan* first):

    vgchange -a y $VOLUMEGROUP

**Warning: LVM driver will synchronize all physical volumes if they are
out of sync after the command above is issued**

The individual volume devices are now available in:

    /dev/mapper/$VOLUMEGROUP-$VOLUMENAME

These now can be analyzed with e.g. a tool like the
[The Sleuth Kit](the_sleuth_kit.md) or loop-back mounted.

To read-only loop-back mount an individual volume:

    mount -o ro,loop /dev/mapper/$VOLUMEGROUP-$VOLUMENAME filesystem/

## Also see

* [File Systems](file_systems.md)

## External Links

* [Wikipedia article on Logical Volume Manager](https://en.wikipedia.org/wiki/Logical_Volume_Manager_%28Linux%29)
* [LVM Howto](https://tldp.org/HOWTO/LVM-HOWTO/),
  by [The Linux Documentation Project](https://tldp.org/)
* [LVM2 Resource Page](http://www.sourceware.org/lvm2/)
* [The Linux Logical Volume Manager](https://opensource.com),
  by Heinz Mauelshagen and Matthew O'Keefe
* [LVM cheatsheet](http://www.datadisk.co.uk/html_docs/redhat/rh_lvm.htm),
  by RedHat
* [Unix/Linux Administration Logical Volume Management Guide](https://wpollock.com/AUnix1/LVM.htm),
  by Wayne Pollock, 2005
* [LVM2 – data recovery](http://lvb.sti.fce.vutbr.cz/public/LinuxAlt_2009/2009_11_08_LA_04_LVM/2009_11_08_LA_04_LVM.pdf),
  by Milan Brož, LinuxAlt 2009
* [Logical Volume Manager ‐ Software RAID](http://forensic-proof.com/wp-content/uploads/2010/03/FP_Logical_Volume_Manager.pdf),
  by Proneer, March 30, 2010

## Tools

* [libvslvm](libvslvm.md)
