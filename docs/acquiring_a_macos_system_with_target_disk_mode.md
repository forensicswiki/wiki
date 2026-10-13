---
tags:
  - Howtos
  - MacOS
---
Make sure to [disable the disk arbitration daemon](disabling_macintosh_disk_arbitration_daemon.md)
on the machine where you will do the acquisition. Alternatively use a FireWire
[write blocker](write_blockers.md)

Prepare a clean firewire drive format is as [HFS+](hfs+.md)
using Mac Disk Utility; name the volume "Target". This process relies on
being able to identify which drive is the suspect's drive by knowing its
size. Many new Macs are shipping with 250GB drives. Having a unique
firewire target drive size will help you identify it later, as you will
see below.

Note the sizes of all drives on your forensic Mac, if you don't already
know. To find out go to:

```text
Apple menu > About This Mac > More info > ATA
```

## Connecting the suspect drive

Step 1. Without turning anything on, connect the forensic Mac to the
suspect’s computer using a firewire cable.

Step 2. Hold down the "Option" key on the suspect’s computer and turn it on.

Step 3. If the suspect’s computer **does not** ask for a password, then
**turn it off**. If the computer **does** ask for a password, then
**turn it off**. You cannot do a simple TDM acquisition if a password is
required. You will have to either:
  a. remove the drive and do a direct acquisition
  b. modify the memory by adding or removing chips and zapping the PRAM.

> To zap the PRAM, start up the computer and as soon as you hear the startup
> 'bong', hold down these four keys: Command-Option-P-R.
>
> It will bong again, and again. Continue to hold down these four keys until it
> has 'bonged' a total of three times (the initial startup bong and two more
> after you hold down those four keys).

Step 4. Assuming that no password was needed, hold down the "T" key and turn
the suspect’s computer back on. The computer will eventually display the
firewire logo on the screen and is then ready for TDM.

## Acquiring the suspect drive

Step 1. Turn on the acquiring Mac (with the disk arbitration daemon
disabled) 2. Start the Terminal. And at the command prompt run:

```text
cd /dev
ls disk?
```

This will list all drives that are seen by the system. A list containing
at least three drives will appear:

* disk0
* disk1
* disk2

One of these drives is the suspect’s. The other two are either the
forensic Mac’s OS or the **Target** drive. You won’t necessarily know
which is which, so you need to query them to see their size, which will
give you a hint.

Step 2. Tho probe a drive, e.g. **/dev/disk1** you can use **pdisk**:

```text
sudo pdisk /dev/disk1
```

The output of **pdisk** will look something like:

```text
/dev/disk0 map block size=512
    #: type name length base ( size )
    1: Apple_partition_map Apple 63 @ 1
    2: Apple_Driver43*Macintosh 56 @ 64
    3: Apple_Driver43*Macintosh 56 @ 120
    4: Apple_Driver_ATA*Macintosh 56 @ 176
    5: Apple_Driver_ATA*Macintosh 56 @ 232
    6: Apple_FWDriver Macintosh 512 @ 288
    7: Apple_Driver_IOKit Macintosh 512 @ 800
    8: Apple_Patches Patch Partition 512 @ 1312
    9: Apple_HFS OS X 72600384 @ 1824 ( 34.6G)
    10: Apple_HFS OS 8.6 5537944 @ 72602208 ( 2.6G)
    11: Apple_Free 0+@ 78140152
```

Step 3. Partitions on an HFS are called "slices." You can see in bold that
this drive has a 34.6G slice listed under the number 9 and a 2.6G under
line 10. Add them up and your looking at a "40G" drive. If the result is
the wrong size, then you are looking at the wrong drive. Repeat step 4
using **disk0** and **disk2** to identify all the disks.

Step 4. Lets assume that your Target volume is **disk2** and is a 120GB. If
it is formatted as HFS, then the query in step 4 should return something
like this.

```text
/dev/disk2 map block size=512
    #: type name length base ( size )
    1: Apple_partition_map Apple 63 @ 1
    2: Apple_Free 0+@ 64
    3: Apple_HFS Apple_HFS_Untitled_2 239859504 @ 262208 (114.4G)
    4: Apple_Free 0+@ 240121712
```

Notice that slice **3** is 114.4 GB in size. Slice 3 is the "working
area" on this 120G drive and is the slice that you will make available
for receiving your evidence, using the mount command shown in green in
line 8 below.

Step 5. Once you confirm which drive is which, you are ready to go. Lets
assume that your forensic drive is **disk0**, the suspect’s drive is
**disk1**, and the Target drive is **disk2**.

Step 6. Because we turned off disk arbitration, however, the target drive
isn't available to receive the image. We therefore need to mount the
**Target drive**; specifically slice **3** of **disk2**.

Type `sudo mount -t hfs /dev/disk2s3 /Volumes/Target`:

```text
sudo mount -t hfs /dev/disk2s3 /Volumes/Target
```

If you are still unsure about which drive is which, you can verify
things because **Target** now has a BSD name. To clear the Terminal
screen, hold down the **command** key and type **k**. Then, type
`ioreg -l`. Buried in the resulting display is information about the
connected drives. Go to the Terminal menu > Edit > Find. Search for
**disk1**. Scroll through the hits and you should see the make and
model number for **disk1**. If a search for **disk2** comes up empty,
then you know it is the unmounted drive.

At this point, you have the choice of imaging the suspect’s entire drive
(recommended), or of just imaging the slice that you want. If you want
to image the entire drive, type:

```text
sudo dd if=/dev/disk1 bs=1024 conv=notrunc,noerror,sync of=/Volumes/Target/Evidence.dmg
```

This will write a raw DD image to the root of **Target** and will name
the image **Evidence.dmg**. If you only want to image particular slices,
then add the slice to the command, i.e.

```text
sudo dd if=/dev/disk1s9 bs=1024 conv=notrunc,noerror,sync of=/Volumes/Target/Evidence.dmg
```

A separate acquisition can be done for each slice that you want to
examine by changing the slice number and giving each new image a
different file name, i.e. **EvidOS8.dmg**.

The advantage of imaging the whole disk is that you can later bring it
into Encase as a single evidence file.

Step 9. Your done. Unmount the **Target** drive by typing:

```text
cd /Volumes
sudo umount /Target
```

Shut down your forensic Mac and then shut down the suspect’s Mac.
Disconnect the firewire connection to the suspect’s Mac.

## Examination

Step 1. Reboot your forensic Mac and restore the
**diskarbitrationd.plist** file back to the **/etc/mach-init.d**
directory. Type:

```text
cd /
sudo cp diskarbitrationd.plist /etc/mach_init.d
```

Turn the forensic Mac off and back on to initiate diskarbitration.
Power up the **Target** drive. The **Target** drive should mount and
appear on your desktop. Open it.

Step 2. The **Evidence.dmg** file should appear. Click on it once.
Lock the file via the "GET INFO" menu to ensure it is write protected.

You can now double-click to mount the Evidence.dmg file **and explore
it within the native Mac OS environment.** If the image won’t mount,
go into the Terminal and type the following:

```text
sudo hdiutil attach /Volumes/Target/Evidence.dmg -shadow
```

If you want to move the evidence file over into Encase, change the .dmg
extension to .001 and add it as a raw image.

Jon Muller, San Jose PD, (With guidance from Derrick Donnally), July-05

## See Also

* [Mac OS X](mac_os_x.md)
