---
tags:
  -  Howtos
  -  MacOS
---
Make sure to [disable the disk arbitration
daemon](disabling_macintosh_disk_arbitration_daemon.md) on the
machine where you will do the acquisition. Alternatively use a FireWire
[write blocker](write_blockers.md)

Prepare a clean firewire drive format is as [HFS+](hfs+.md)
using Mac Disk Utility; name the volume “Target”. This process relies on
being able to identify which drive is the suspect's drive by knowing its
size. Many new Macs are shipping with 250GB drives. Having a unique
firewire target drive size will help you identify it later, as you will
see below.

Note the sizes of all drives on your forensic Mac, if you don't already
know. To find out go to:

    Apple menu > About This Mac > More info > ATA

## Connecting the suspect drive

1\. Without turning anything on, connect the forensic Mac to the
suspect’s computer using a firewire cable.

2\. Hold down the “Option” key on the suspect’s computer and turn it on.

3\. If the suspect’s computer **does not** ask for a password, then
**turn it off**. If the computer **does** ask for a password, then
**turn it off**. You cannot do a simple TDM acquisition if a password is
required. You will have to either:

a\. remove the drive and do a direct acquisition

b\. modify the memory by adding or removing chips and zapping the PRAM.

    To zap the PRAM, start up the computer and as soon as you hear the startup 'bong', hold down these four keys:
    Command-Option-P-R.

    It will bong again, and again. Continue to hold down these four keys until it has 'bonged' a total of three times
    (the initial startup bong and two more after you hold down those four keys).

4\. Assuming that no password was needed, hold down the “T” key and turn
the suspect’s computer back on. The computer will eventually display the
firewire logo on the screen and is then ready for TDM.

## Acquiring the suspect drive

1\. Turn on the acquiring Mac (with the disk arbitration daemon
disabled) 2. Start the Terminal. And at the command prompt run:

    cd /dev
    ls disk?

This will list all drives that are seen by the system. A list containing
at least three drives will appear:

- disk0
- disk1
- disk2

One of these drives is the suspect’s. The other two are either the
forensic Mac’s OS or the **Target** drive. You won’t necessarily know
which is which, so you need to query them to see their size, which will
give you a hint.

3\. Tho probe a drive, e.g. **/dev/disk1** you can use **pdisk**:

    sudo pdisk /dev/disk1

The output of **pdisk** will look something like:

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

5\. Partitions on an HFS are called “slices.” You can see in bold that
this drive has a 34.6G slice listed under the number 9 and a 2.6G under
line 10. Add them up and your looking at a “40G” drive. If the result is
the wrong size, then you are looking at the wrong drive. Repeat step 4
using **disk0** and **disk2** to identify all the disks.

6\. Lets assume that your Target volume is **disk2** and is a 120GB. If
it is formatted as HFS, then the query in step 4 should return something
like this.

    /dev/disk2 map block size=512
      #: type name length base ( size )
         1: Apple_partition_map Apple 63 @ 1
         2: Apple_Free 0+@ 64
         3: Apple_HFS Apple_HFS_Untitled_2 239859504 @ 262208 (114.4G)
         4: Apple_Free 0+@ 240121712

Notice that slice **3** is 114.4 GB in size. Slice 3 is the “working
area” on this 120G drive and is the slice that you will make available
for receiving your evidence, using the mount command shown in green in
line 8 below.

7\. Once you confirm which drive is which, you are ready to go. Lets
assume that your forensic drive is **disk0**, the suspect’s drive is
**disk1**, and the Target drive is **disk2**.

8\. Because we turned off disk arbitration, however, the target drive
isn't available to receive the image. We therefore need to mount the
**Target drive**; specifically slice **3** of **disk2**.

<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

<span class="Section1">Type<b> <span
style='color:maroon'>sudo mount –t hfs
/dev/</span><span style='color:blue'>disk2</span><span
style='color:maroon'>s</span><span style='color:lime'>3 </span></b><span
style='color:maroon;font-weight:normal'>/Volumes</span></span><span class="Section1" style='color:maroon'><b>/</b></span><span class="Section1"
style='color:blue'><b>Target</b></span><span class="Section1">.</span>

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="0">
<tr class="Section12">
<td width="17">

 

</td>
<td width="680">
<div align="left">
<table width="500" border="1" align="center" cellpadding="15" cellspacing="1" bordercolor="#000000">
<tr>
<td align="center" valign="middle" class="Section12">

If you are still unsure about which drive is which, you can verify
things because <span class="style24">Target</span> now has a BSD name.
To clear the Terminal screen, hold down the
<span class="style35">command</span> key and type

k

Then, type

ioreg -l

Buried in the resulting display is information about the connected
drives. Go to the Terminal Menu\>Edit\>Find. Search for
<span class="style30">disk1</span>. Scroll through the hits and you
should see the make and model number for
<span class="style34">disk1</span>. If a search for
<span class="style24">disk2</span> comes up empty, then you know it is
the unmounted drive.

</td>
</tr>
</table>
</div>
</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td class="Section1">

At this point, you have the choice of imaging the suspect’s entire drive
(recommended), or of just imaging the slice that you want. If you want
to image the entire drive, type:  

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr class="Section1">
<td width="4">

<span class="style11"></span>

</td>
<td width="633" align="left" valign="top" class="style11">

<span class="style12" style='color:maroon; page:Section1; font-family: Arial, Helvetica, sans-serif;'><b>sudo
dd
if=/dev/</b></span><span class="style12" style='color:red; page:Section1; font-family: Arial, Helvetica, sans-serif;'><b>disk1</b></span><span class="style10"><b>
<span
style='color:maroon'>bs=1024 conv=notrunc,noerror,sync
of=/Volumes/</span><span
style='color:blue'>Target/Evidence.dmg</span></b><span style='font-weight:normal'>.</span></span>

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td>

This will write a raw DD image to the root of
<span style='color:blue'><b>Target</b></span> and will name the image
<span style='color:blue'><b>Evidence.dmg</b>.</span>

If you only want to image particular slices, then add the slice to the
command, i.e.

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

<span class="style13" style='color:maroon'><span class="style22">sudo dd
if=/dev/</span></span><span class="style15">disk1</span><span class="style17">s</span><span class="style19">9</span>
<span class="style21"><b><span style='color:maroon'>bs=1024
conv=notrunc,noerror,sync of=/Volumes/</span><span
style='color:blue'>Target/Evidence.dmg</span></b><span style='font-weight:normal'>.</span></span>

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td>

A separate acquisition can be done for each slice that you want to
examine by changing the slice number and giving each new image a
different file name, i.e.
<span style='color:blue'><b>EvidOS8.dmg</b></span>.

The advantage of imaging the whole disk is that you can later bring it
into Encase as a single evidence file.

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr class="Section1">
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

9.  <span class="Section1">Your done. Unmount the
    <span class="style24">Target</span> drive by typing
    `           `</span>
    `           `

    cd /Volumes

    <span class="Section1" style='color:maroon'><b>sudo umount
    /</b></span><span class="Section1" style='color:blue'><b>Target</b></span>

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td>

Shut down your forensic Mac and then shut down the suspect’s Mac.
Disconnect the firewire connection to the suspect’s Mac.

Examination

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr class="Section1">
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

1.  <span class="Section1">Reboot your forensic Mac and restore the
    <b>diskarbitrationd.plist</b><span
         style='font-weight:normal'> file back to the
    </span><b>/etc/mach-init.d</b><span
         style='font-weight:normal'> directory. Type </span></span>
    cd /

    <span class="Section1"
    style='color:maroon'><b>sudo cp diskarbitrationd.plist
    /etc/mach_init.d</b></span><span class="Section1">. </span>

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td class="Section1">

Turn the forensic Mac off and back on to initiate diskarbitration. Power
up the <span style='color:blue'><b>Target</b></span> drive. The
<span style='color:blue'><b>Target</b></span> drive should mount and
appear on your desktop. Open it.

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

2.  The <span
         style='color:blue'><b>Evidence.dmg</b></span> file should
    appear. Click on it once. Lock the file via the “GET INFO” menu to
    ensure it is write protected.

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td>

You can now double-click to mount the Evidence.dmg file <b>and explore
it within the native Mac OS environment.</b>

If the image won’t mount, go into the Terminal and type the following:

</td>
</tr>
</table>
<table width="700" border="0" cellspacing="1" cellpadding="15">
<tr>
<td width="4">

 

</td>
<td width="633" align="left" valign="top">

<span class="Section1"
style='color:maroon;layout-grid-mode:line'><b>sudo hdiutil
attach</b></span>
<span class="Section1" style='color:maroon'><b>/Volumes/</b></span><span class="Section1"
style='color:blue'><b>Target/Evidence.dmg</b></span><span class="Section1" style='layout-grid-mode:line'>
<span style='color:maroon'><b>-shadow</b></span></span>

</td>
</tr>
</table>

If you want to move the evidence file over into Encase, change the .dmg
extension to .001 and add it as a raw image.

Jon Muller, San Jose PD, (With guidance from Derrick Donnally), July-05

## See Also

- [Mac OS X](mac_os_x.md)

