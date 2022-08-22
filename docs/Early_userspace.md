According to the [Linux
documentation](https://www.kernel.org/doc/Documentation/early-userspace/README),
"early userspace" is a set of libraries and programs that provide
various pieces of functionality that are important enough to be
available while a Linux kernel is coming up, but that don't need to be
run inside the kernel itself.

Early userspace is commonly used in various Linux Live CDs and Live USBs
for loading necessary device and file system drivers, as well as for
other preparatory actions (e.g. setting up a framebuffer).

Early userspace is also responsible for mounting a root file system,
which contains a live system (desktop environment and various
applications reside in a live system, while early userspace contains
only a limited set of programs required for booting up).

Due to varied conditions in which Live CDs and Live USBs are booting up
(for example, it is possible to make Live USB from Live CD by writing
ISO 9660 image [directly to USB
device](https://help.ubuntu.com/community/Installation/FromUSBStick#dd_image_of_iso_file_to_USB_device_safely)
as well as by exporting files from ISO 9660 image to an existing file
system on USB device and setting up a bootloader on this device), early
userspace should locate a root file system first. A root file system can
be stored in a [SquashFS](http://en.wikipedia.org/wiki/SquashFS) image
file, a [raw image](Raw_Image_Format "wikilink") file, a partition with
a file system, a device without a partition table (but with a file
system), or even in a set of directories in unpacked form (although
specific implementations of early userspace may not support everything
listed above).

After booting, contents of a root file system are visible as the
contents of "/" directory.

[Category:Live CD](Category:Live_CD "wikilink")