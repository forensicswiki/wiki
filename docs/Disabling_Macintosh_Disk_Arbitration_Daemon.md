- Start Terminal (in the Utilities folder).
- Type:

`  cd /etc/mach_init.d`
`  ls`

- Look for the file called diskarbitrationd.plist. If this file is in
  this directory, then disk arbitration is turned on. The disk
  arbitration file will attempt to mount any device it sees connected to
  the Mac, so one way you can stop disk arbitration from mounting the
  suspect's drive is by hiding this file. Simply renaming the file may
  not work. To do this, store a backup copy of diskarbitrationd.plist
  under the root directory and then delete the original.
- Type

`  sudo cp diskarbitrationd.plist /`

- Confirm that the copy is there.

`  ls /`

- Remove the original file from the **mach-int.d** directory by typing:

` sudo rm diskarbitrationd.plist.`

- You can restore disk arbitration when your done by typing:

`   sudo cp /diskarbitrationd.plist /etc/mach_init.d.`

You can leave the copy in root for the next time, as it will have no
effect on your system if it is left in that directory. When you are
done, **reboot your computer** to make sure that the disk arbitration
daemon is not running.