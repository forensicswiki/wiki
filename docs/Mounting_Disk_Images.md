# FreeBSD

To mount a disk image on [FreeBSD](FreeBSD "wikilink"):

First attach the image to unit \#1:

` # mdconfig -a -t vnode -f /big3/project/images/img/67.img -u 1`

Then mount:

` # mount -t msdos /dev/md1s1 /mnt`

` # ls /mnt`
` BOOTLOG.PRV     BOOTLOG.TXT     COMMAND.COM     IO.SYS          MSDOS.SYS`

To unmount:

` # umount /mnt`
` # mdconfig -d -u 1`

To mount the image read-only, use:

` # mdconfig -o readonly -a -t vnode -f /big3/project/images/img/67.img -u 1`
` # mount -o ro -t msdos /dev/md1s1 /mnt`

# Linux

## To mount a disk image on [Linux](Linux "wikilink")

`# mount -t vfat -o loop,ro,noexec img.dd /mnt`

The ***ro*** is for read-only.

This will mount NSRL ISOs:

` # mount /home/simsong/RDS_218_A.iso /mnt/nsrl -t iso9660 -o loop,ro,noexec `

Some raw images contains multiple partitions (e.g. full HD image). In
this case, it's necessary to specify a starting offset for each
partition.

`# mount -t vfat -o loop,offset=32256,ro,noexec img.dd /mnt/tmp_1`
`# mount -t vfat -o loop,offset=20974464000,ro,noexec img.dd /mnt/tmp_2`

### kpartx

Mounting raw images with multiple partitions is easy with *kpartx*. Type
*aptitude install kpartx* as root to install *kpartx* under Debian.
*kpartx* is creating device-mappings for each partition. If the raw
image looks like this:

`       Device        Boot      Start       End      Blocks Id  System`
`    rawimage.dd1               1           1        8001   83  Linux`
`    rawimage.dd2               2           2        8032+   5  Extended`
`    rawimage.dd5               2           2        8001   83  Linux`

The command

`#   kpartx -v -a rawimage.dd`

creates these mappings

`   /dev/mapper/loop0p1`
`   /dev/mapper/loop0p2`
`   /dev/mapper/loop0p5`

The partitions can be mounted with these commands:

`# mount /dev/mapper/loop0p1 /media/suspectHD_01/ -o ro`
`# mount /dev/mapper/loop0p5 /media/suspectHD_02/ -o ro`

Don't forget the switch ***-o ro*** !

## To unmount

`# umount /mnt`

## Mounting Images Using Alternate Superblocks

- [Mounting Images Using Alternate
  Superblocks](http://sansforensics.wordpress.com/2008/12/18/mounting-images-using-alternate-superblocks/)

# Windows

MS Windows does not include a native means for mounting acquired images.
However, there are tools available for mounting acquired images on
Windows systems.

## Free Tools

- [Arsenal Image
  Mounter](Arsenal_Recon#Arsenal_Image_Mounter "wikilink") - Arsenal
  Image Mounter takes the contents of disk images and presents them to
  Windows as SCSI disks
- [FTK Imager](http://accessdata.com/product-download)
- [ImDisk](http://www.ltr-data.se/opencode.html#ImDisk) - also on
  [WikiPedia](http://en.wikipedia.org/wiki/ImDisk)
- [Paraben](Paraben "wikilink") P2X
- [VDKWin](http://www.vmxbuilder.com/vdk-gui/), requires
  [VDK](http://chitchat.at.infoseek.co.jp/vmware/vdk.html)
- [vhdtool](http://archive.msdn.microsoft.com/vhdtool) - an unsupported
  MS tool that you can use to convert a raw/dd image to a VHD file and
  mount as a read-only volume via Disk Manager

## Commercial Tools

- [SmartMount](http://www.asrdata.com/SmartMount/)
- [Mount Image Pro](http://www.mountimage.com/) - has a 14-day trial
  version

[Category:Howtos](Category:Howtos "wikilink")