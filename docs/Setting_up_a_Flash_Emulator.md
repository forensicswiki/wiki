Experiments with flash file system forensics can be done usefully using
a flash emulator, such as the MTD device. This stores the "contents" of
a simulated flash memory in a disk file. You can then use that disk file
with JFFS2 or YAFFS. Follow these instructions.

First, you need to have MTD working. Use this:

`   modprobe mtd jffs2 mtdram mtdchar mtdblock`
`   cat /proc/mtd`

We will use the RAM MTD device, and then dump it into a file to get the
results.

### JFFS2

(from <http://wiki.openmoko.org/wiki/Userspace_root_image>)

    mkfs.jffs2 --pad=0x700000 -o rootfs.jffs2 -e 0x4000 -n -d/tmp/jffsroot/ # for GTA01?
    mkfs.jffs2 --pad=0x700000 -o rootfs.jffs2 -e 0x20000 -n -d/tmp/jffsroot/ # for GTA02

    export loop=$(losetup -f)
    losetup $loop <rootfs.jffs2>
    modprobe block2mtd block2mtd=$loop,131072
    modprobe jffs2
    modprobe mtdblock
    mkdir /mnt/jffs2
    mount -t jffs2 -o ro /dev/mtdblock0 /mnt/jffs2

### YAFFS

    flash_eraseall
    mtd_debug write /dev/mtd1 0 16777216 /dev/zero
    mount /dev/mtdblock1 /mnt/yaffs
    do smoething
    umount /mnt/yaffs
    mtd_debug read /dev/mtd1 0 16777216 mtd-output # writes to the file mtd-output