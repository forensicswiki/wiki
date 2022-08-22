**affuse** is a Filesystem in Userspace (FUSE) implementation that
allows [AFF](AFF "wikilink") files to appear as raw files on Linux
systems. This allows the files to be processed with forensic tools that
do not understand AFF. It also allows the disk images to be actually
mounted, should you want to do that.

For example, say that /project/0089.aff is a disk image that you wish to
process with raw tools. With affuse you can mount it like this:

`  # affuse /project/00709.aff /mnt/p`
`  # ls /mnt/p`
`  0070.aff.raw`

This raw file could then be mounted:

`  # mount -t vfat -o loop=/dev/loop0,ro,noexec,offset=32256 /mnt/p/0070.aff.raw  /mnt/r`
`  # ls /mnt/r`
`  total 316`
`  -rwxr-xr-x 1 root root  93880 May 11  1998 command.com`
`  -r-xr-xr-x 1 root root 222390 May 11  1998 io.sys`
`  -r-xr-xr-x 1 root root      9 May 11  1998 msdos.sys`

## External Links

- [FUSE](http://fuse.sourceforge.net/) - Filesystem in User Space