Often, forensic labs are overloaded and investigators complains about
the long waiting time. The solution for both professionals is to reduce
the amount of seized material.

But how do you know if a computer is relevant without looking into it?
And how to look into it in a fast and forensic acceptable way?

Many procedures are emerging around the world to allow the investigator
to access seized computer data remotely, in a environment configured and
maintained by the forensic professional. The investigator can perform an
initial analysis, quickly pointing the most important computers among
all computers seized, speeding the subsequent forensic exam, which is
more time consuming, and reducing the amount of computers in which the
exam will be made.

## Hardware

- Storage server(s) - server(s) with large storage capacity to keep the
  sized disk images.
- Samba server - to be accessed by the investigators.

## Software

- GNU/Linux
- Samba
- SquashFS
- NFS(optional)

## Installation

- Storage server:
  - Install the GNU/Linux distribution of your choice.
  - Install the squashfs kernel-patch package and tools.
  - Install NFS or Samba to share the disk images with the 'Samba
    server'.
  - Install dcfldd, GNU ddrescue, or both, or stay with dd.

<!-- -->

- Samba server:
  - Install the GNU/Linux distribution of your choice.
  - Install Samba.

## Usage

### On the Storage server

- Mirror the seized disk to a temporary folder:

`dcfldd if=/dev/sdXX of=/tmpstg/M090834/image.dd hash=md5 hashlog=/tmpstg/M090834/hashlog.md5 hashwindow=1G`

or

`ddrescue /dev/sdXX /tmpstg/M090834/image.dd /tmpstg/M090834/ddrescue.log`

- Compress the folder to a SquashFs image:

`mksquashfs /tmpstg/M090834 /storage/M090834.squash`

- Make sure the file is shared with the Samba server

`#cat /etc/exports`
`/storage samba_server(ro)`

### On the Samba server

- Add a line in /etc/fstab to access the squash files

`storage:/storage /storage nfs _netdev,ro,soft 0 0`

- Add a line in /etc/fstab to access the dd images

`/storage/M090834.squash /mnt/materials/M090834/ squashfs ro,_netdev,loop`

- Add a line to each partition in the dd image

`/mnt/materials/M090834/image.dd /mnt/mountpoints/M090834/C ntfs iocharset=utf8,offset=32256,loop 0 0`

- Share the partition contents, modifying smb.conf

`[M090834]`
`       path = /mnt/mountpoints/M090834`
`       valid users = investigatorusername`

## Tips

- The number of loop devices can be increased at boot with the
  'max_loop=512' kernel option.
- May be necessary to specify the loop number in fstab, like
  'ro,_netdev,loop=/dev/loopXX'.
- mkshashfs can be used to add new files to an existing squash image, so
  it is easy to group related materials together in a single file.

[Category:Howtos](Category:Howtos "wikilink")