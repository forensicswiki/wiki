---
tags:
  -  Howtos
---
Here is a photo of my disk imaging system:

<figure>
<img src="ImagingStationx4.jpg" title="ImagingStationx4.jpg" width="320"
alt="ImagingStationx4.jpg" />
<figcaption aria-hidden="true">ImagingStationx4.jpg</figcaption>
</figure>

Key elements of the disk imaging system:

- You need to have an internal IDE card which is not used for anything
  but disk imaging;
- You need to have an external hard drive power supply, so that you can
  power the IDE drives without using your computer's power supply (if
  you use your computer's power supply, you can easily crash your
  computer when attaching or detaching the power supply);

# Imaging Checklist

1.  [Set up a disk imaging
    station](how_to_set_up_a_disk_imaging_station.md);
2.  You should have a 50-pin IDE ribbon cable going from your IDE
    controller to the desktop;
3.  Do not connect your imaging drive yet!
4.  Boot the computer into [FreeBSD](freebsd.md);
5.  Attach the IDE hard drive to the ribbon cable FIRST;
6.  Now, attach power to the IDE drive;
7.  You need to determine which ATA port the IDE drive is now connected
    to. In all likelihood it is `ata0, ata1, ata2` or `ata3`. If you
    have an internal hard drive on an IDE interface, then the internal
    interface is probably `ata0` and `ata1` and the external is probably
    on `ata2` or `ata3`;
8.  You also need a place to store the [AFF](aff.md) files you
    are going to be creating. I usually put them in `/usr/affs` which is
    a directory you will need to create;
9.  Log in as *root*;
10. mkdir /usr/affs
11. Now, try to image the drive with this command:

` aimage ata2 /usr/affs/disk1.aff`

1.  If this doesn't work, try:

` aimage ata3 /usr/affs/disk1.aff`

1.  If it works, you'll see the [aimage](aimage.md) program
    running.

# What can go wrong

- *[aimage](aimage.md)* may not be installed. If you get the
  error message "aimage: command not found" then you need to install
  [AFFLIB](aff.md) and then make sure that the *aimage*
  command (usually installed in */usr/local/bin*) is in your *PATH*. You
  can check this out by running */usr/local/bin/aimage* instead of
  *aimage*;
- Your source drive can be broken, *[aimage](aimage.md)* should
  tell you this;
- You can run out of disk space. You need a LOT of disk space to store
  disk images — figure 30GB to image a 60GB drive.

# What to do after you have made your images

Once you have made a few images, you'll need to put them somewhere.
Typically this means uploading them to a server.

# See Also

[How To Set Up a Disk Imaging
Station](how_to_set_up_a_disk_imaging_station.md)

[How To Ship Drives](how_to_ship_drives.md)

