---
tags:
  - Disk Encryption
  - Howtos
  - Windows
---
# Imaging Options

There are multiple ways to image a computer with BitLocker security in
place, namely:

- Offline imaging
- Live imaging

## Offline imaging

One can make an offline image with the image containing encrypted
information.

Multiple options to offline decrypt the information, provided the
password or recovery password is available, are available. Some of which
are:

- [dislocker](https://www.hsc.fr/securite-internet/)
- [EnCase](encase.md)
  encryption module
- [libbde](libbde.md)

The recovery password is a long series of digits broken up into 8
segments.

    123456-123456-123456-123456-123456-123456-13456-123456

Note that there is no white space in the recovery password including not
at the end, e.g. EnCase does not accept the recovery password if there
is trailing white space.

The recovery password can be recovered from a BitLocker enabled computer
provided it can be logged into e.g. by running:

    manage-bde.exe -protectors -get C: -Type recoverypassword

The basic steps are:

1.  Make an offline full disk image.
2.  Recover the password, this can be done by booting the original
    computer, or by creating a clone and booting the clone. (booting
    from a clone has not been tested at this time.)
    1.  Once booted log into the computer
    2.  Use the BitLocker control panel applet to display the password.
        This can also be done from the command-line.
    3.  record the password


3.  For EnCase v6 or higher with the encryption module installed
    1.  Load the image into EnCase
    2.  You will be prompted for the password. Simply enter it and
        continue.
    3.  If you prefer to have an un-encrypted image to work with other
        tools or share with co-workers, you can "re-acquire" the image
        from within EnCase. The new image will have unencrypted data.
    4.  After adding the encrypted image into your case, simply right
        click on the drive in the left panel and select acquire. Select
        "do not add to case". You will be presented a dialog window to
        enter new information about the image. Make sure the destination
        you select for your new image does not exist.

## Live imaging

### FTK Lite

#### Imaging of a physical drive

Using FTK Imager lite, it was determined a live image of the physical
system disk resulted in an image with an encrypted bitlocker container
on it.

Note that the phrase "physical" here corresponds directly with FTK
Imagers use of the term in their image acquire menu.

#### Imaging of a logical partition

I was able to add a partition and create an image in which the data was
unencrypted.

Note that the phrase "logical" here corresponds directly with FTK
Imagers use of the term in their image acquire menu.

#### Files and Folders collections

This was not attempted, but it seems reasonable to assume this will
collect unencrypted files.

### X-Ways

#### Imaging of a physical drive

X-Ways support states this is not supported.

#### Imaging of a logical partition

X-Ways support states that this should work.

In at least one instance, I was able to add C: drive (not the physical
disk, just the partition) and create an image that could in turn be
processed by X-Ways. Both existing and deleted files were available
within X-Ways after processing.

There has been atleast one report on the X-Ways forum that this feature
does not work, so it may not work for all configurations of bitlocker.

## See Also

* [BitLocker Disk Encryption](bitlocker_disk_encryption.md)
