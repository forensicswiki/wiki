# Creating a VM control file from a forensic image

In general, VM software needs both an image and associated control
files.

There are a number of ways to create the VM control files needed to run
an image as a VM instance. At present, this article primarily provides a
series of tools that can create to VMDK VM control files.

## Creating a VMDK file from a forensic image

### By hand

VMDK files are simple text files. They can be created by hand and then
the VM run to allow registry values and passwords to be set as needed
prior to boot.

Jimmy Weg has written a series of blog posts that detail the process.
See the list of blog posts under external links below.

### Linux tools as included in SIFT

Via the SIFT workstation (free), use the following steps:

`1.open a terminal window`
`2.sudo su`
`3.mkdir /mnt/ewf1`
`4.mount_ewf.py (Encase Image file path) /mnt/ewf1`
`5.qemu-img convert /mnt/ewf1/(encase image file name) -O vmdk (give_a_name).vmdk`

### EnCase

use EnCase (Commercial) to mount the E01 image as an emulated disk (you
need to have the Physical Disk Emulator (“PDE”) module installed), then
VMware to create virtual machine from the emulated physical disk.
Guidance software has a good guide on how to do this in their support
portal.

Note – EnCase v7 hasn't been proven to support this, just EnCase 6

### Forensic Explorer

Forensic Explorer is a commercial forensics tool which contains a
feature called "Live Boot" for booting of forensic image files (E01,
EX01, DD). Live Boot works with VMWare Workstation, VMWare Player and
Oracle Virtual Box. Refer to
<http://www.forensicexplorer.com/live-boot.php> for more detail.

### Paladin 4

Paladin 4 (free) can create VMDK files for DD and E01 images.

### Live View

[Live View](http://liveview.sourceforge.net/) (opensource) is reported
as not reliable, but it does work with some images.

### VMware Standalone Converter

This may be an option. Reports of success here and what the steps are
would be great.

### VFC - Virtual Forensic Computing

[VFC.uk.com](http://www.vfc.uk.com)

VFC was written and created by [MD5 Ltd](http://www.md5.uk.com) who
specialise in digital forensics, eDisclosure and software development.

VFC (Commercial) is reportedly very good, but troubles with booting
Windows 2003 servers have been reported. It's a little pricey (\$1350
for a Corp license), cheaper for law enforcement and Government. It
WORKS the vast majority of the time and the developer provides excellent
support and continuous updates. It works on all versions of windows up
to windows 8 enabling an investigating officer to virtualise a suspects
machine in seconds directly from a hard drive, from a forensic image
(e01) or a raw DD image.

## Creating a KVM image

### From the linux command prompt

`kvm -hda myimage.dd`

memory can be set as an option, cd drives can be presented, etc., and
there is an option equivalent to the VMware non persistent mode.

Warning: It has been determined that using kvm's non-persistent mode can
still result in an altered image. Always, always, always work from a
copy.

# Using the VMDK file

Once you have the VMDK file, you can create a virtual machine in
Virtualbox or VMware Workstation and use the VMDK as an existing hard
disk for the virtual machine. I prefer to use VMware Workstation because
it has a non persistent mode which allows you to write changes to a
cache file rather than the forensic image itself thus maintaining
integrity.

# External Links

- [How to Create a Virtual Machine from a Raw Hard Drive
  Image](http://www.myfixlog.com/fix.php?fid=35)
- [Get from e01 to live virtual machine with no image
  conversion](http://cyb3rdaw6.harpermountain.net/2011/06/12/get-from-e01-to-live-virtual-machine-with-no-image-conversion/)

## Jimmy Weg's blog

Jimmy Weg has talked extensively about using VM with forensic images on
his blog. These are detailed tutorials that manually create the VMDK
file!

- [Creating a VMware Virtual Machine from a Raw Image
  File](http://justaskweg.com/?p=7)
- [Creating a VM from E01 Images](http://justaskweg.com/?p=653)
- [What About an XP VM?](http://justaskweg.com/?p=851)
- [How Do I Handle Really\* Big Disks?](http://justaskweg.com/?p=999)
- [Mounted Images – Breaking the 2TB
  Barrier](http://justaskweg.com/?p=1024)