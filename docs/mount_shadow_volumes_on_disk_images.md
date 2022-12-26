---
tags:
  - Howtos
---
Windows Shadow Volumes when created are automatically mounted at the
file system root by Windows. Unfortunately this is invisible to the user
and can not be directly accessed. Mklink, an included command line
utility that ships with Windows, is able to create a symbolic link that
allows access to these shadow volumes.

Shadow Volumes that exist on a drive image are no different. They too
can be accessed by creating a symbolic link to the location of the
volume. There is a caveat here though – the Shadow Volume is mounted at
the local file system's root rather than the drive image's file system
root.

This example will be showing how to mount a virtual disk image in the
VHD format using Windows 7's built in tools. It will then proceed to
detail the steps of mounting a Shadow Volume that exists on the disk
image. Note: Windows 7 Professional or Ultimate edition are required as
the necessary tools are not bundled with other versions.

## Mounting the Disk Image

The first step is to mount the VHD. If you have a RAW image or another similar
format these can be converted to VHD using a tool such as qemu-img
(https://wiki.qemu.org/Main_Page) or vmToolkit's Vmdk2Vhd utility.

- To mount the VHD bring up the Start menu in Windows.

<!-- -->

- Right click on "Computer" and click "Manage". This will bring up a

window titled "Computer Management".

- Now double click on "Storage" in the center pane.

<!-- -->

- Next double click the "Manage Storage" in the center pane.

<!-- -->

- Now click the "More Actions" menu in the right most pane and select
  "Attach VHD".

<!-- -->

- Browse to the location of the drive image that you would like to mount
  and hit "OK".

Now that the image is mounted we can begin the examine the Shadow
Volumes on it.

### Command Prompt Method

These steps can also be accomplished using an administrator enabled
Command Prompt. To perform these steps using the command prompt the
diskpart command must be used.

- To start type "diskpart" at the command prompt.

`C:\> diskpart`

When diskpart starts the prompt will change to say DISKPART\>.

- Next select the drive image by typing "select vdisk
  file=<path to image>" where <path to image> is the path to the vhd
  file.

`DISKPART> select vdisk file=C:\myimage.vhd`

- Last type "attach vdisk" or optionally if you'd like to mount it read
  only "attach vdisk readonly".

`DISKPART> attach vdisk readonly`

## Mounting the Shadow Volume

To work with the Shadow Volumes we will use the VSSAdmin tool bundled
with Windows 7 Ultimate and Professional editions.

- Start by opening an Administrator enabled command shell. This can be
  done by right clicking on the Command Prompt application in Start \>
  Accessories \> Command Prompt and selecting "Run As Administrator".

<!-- -->

- Once the command prompt is open you can view the available Shadow
  Volumes by typing: "vssadmin list shadows".

`C:\> vssadmin list shadows`

- At this point you may see a long list of Shadow Volumes that were

created both by the machine the disk image is from as well as local
shadow volumes. To list just the Shadow Volumes associated with the
drive image you can add an optional /FOR=\<DriveLetter:\\\> where
DriveLetter is the drive letter that the drive image is mounted on.

`C:\> vssadmin list shadows /for=E:\`

- Now that we have a list of the Shadow Volumes we can mount them using
  the mklink tool. To do this, on the command line type:

`"mklink /D C:\`<some directory>`\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy#\"`

Where <some directory> is the path that you'd like the mount the Shadow
Volume at, and the \# in HarddiskVolumeShadowCopy is the number o the
Shadow Volume to mount. Please note that the trailing slash is absoutely
necessary. Without the slash you will receive a permissions error when
trying to access the directory.

`mklink /D C:\shadow_volume_1 \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\`

- If all was successful you should receive a message that looks like
  this:

`symbolic link created for `<some directory>` <<===>> \\?GLOBALROOT\Device\HarddiskVolumeShadowCopy1\`

You can now browse the files contained in the Shadow Volume just like
any other files in your file system!

## Also See

* [Windows Shadow Volumes](windows_shadow_volumes.md)
