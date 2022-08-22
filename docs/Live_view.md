Live View is a Java-based graphical forensics tool that creates a VMware
virtual machine out of a [raw image file](raw_image_file "wikilink") or
physical disk. This allows a forensic examiner to "boot up" the image or
disk and gain an interactive, user-level perspective of the environment,
all without modifying the underlying image or disk. Because all changes
made to the disk are written to a separate file, the examiner can
instantly revert all of his or her changes back to the original pristine
state of the disk. The end result is that one need not create extra
"throw away" copies of the disk or image to create the virtual machine.

Live View is capable of booting

- Full disk raw images
- Bootable partition raw images
- Physical Disks (attached via a USB or Firewire bridge)

Containing the following operating systems

- Windows 2008, Vista, 2003, XP, 2000, NT, Me, 98
- Linux (limited support)

Behind the scenes, Live View automates a wide array of technical tasks.
Some of these include: resolving hardware conflicts resulting from
booting on hardware other than that on which the OS was originally
installed; creating a customized [master boot
record](master_boot_record "wikilink") for partition-only images; and
correctly specifying a virtual disk to match the original image or
physical disk.

Live View is developed by CERT, Software Engineering Institute

## External Links

- [Official website](http://liveview.sourceforge.net/)
- [CERT, Software Engineering Institute
  homepage](http://www.sei.cmu.edu/)