---
tags:
  -  Encryption
  -  Disk Encryption
  -  Windows
  -  Anti-Forensics
---
**BitLocker Disk Encryption** (BDE) is [Full Volume
Encryption](full_volume_encryption.md) solution by
[Microsoft](microsoft.md) first included with the Enterprise and
Ultimate editions of [Windows Vista](windows.md). It is also
present in [Windows 7](windows.md) and later version along with
a system for encrypting removable storage media devices, like
[USB](usb.md), which is called BitLocker To Go. Unlike previous
versions of BitLocker, BitLocker To Go allows the user to protect
volumes with a password or smart card.

## BitLocker

BitLocker encrypts data with either 128-bit or 256-bit
[AES](aes.md) and optionally using a diffuser algorithm called
Elephant. The key used to do the encryption, the Full Volume Encryption
Key (FVEK) and/or TWEAK key, is stored in the BitLocker metadata on the
protected volume. The FVEK and/or TWEAK keys are encrypted using another
key, namely the Volume Master Key (VMK). Several copies of the VMK are
also stored in the metadata. Each copy of the VMK is encrypted using
another key, also know as key-protector key. Some of the key-protectors
are:

- TPM (Trusted Platform Module)
- Smart card
- recovery password
- start-up key
- clear key; this key-protector provides no protection
- user password

BitLocker has support for partial encrypted volumes.

### BitLocker To Go

Volumes encrypted with BitLocker To Go will have a hybrid encrypted
volume, meaning that part of the volume is unencrypted and contains
applications to unlock the volume and the other part of the volume is
encrypted. The "discovery drive" volume contains BitLocker To Go Reader
to read from encrypted volumes on versions of Microsoft
[Windows](windows.md) without BitLocker support.

## How to detect

Volumes encrypted with BitLocker will have a different signature than
the standard [NTFS](ntfs.md) header.

A BitLocker encrypted volume starts with the "-FVE-FS-" signature.

A hexdump of the start of the volume should look similar to:

    00000000  eb 58 90 2d 46 56 45 2d  46 53 2d 00 02 08 00 00  |.X.-FVE-FS-.....|
    00000010  00 00 00 00 00 f8 00 00  3f 00 ff 00 00 00 00 00  |........?.......|
    00000020  00 00 00 00 e0 1f 00 00  00 00 00 00 00 00 00 00  |................|
    00000030  01 00 06 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000040  80 00 29 00 00 00 00 4e  4f 20 4e 41 4d 45 20 20  |..)....NO NAME  |
    00000050  20 20 46 41 54 33 32 20  20 20 33 c9 8e d1 bc f4  |  FAT32   3.....|

These volumes can also be identified by a GUID:

- for BitLocker: 4967d63b-2e29-4ad8-8399-f6a339e3d00
- for BitLocker ToGo: 4967d63b-2e29-4ad8-8399-f6a339e3d01

Which in a hexdump of the start of the volume should look similar to:

    000000a0  3b d6 67 49 29 2e d8 4a  83 99 f6 a3 39 e3 d0 01  |;.gI)..J....9...|

## manage-bde

To view the BitLocker Drive Encryption (BDE) status on a running Windows
system:

    manage-bde.exe -status

To obtain the recovery password for volume C:

    manage-bde.exe -protectors -get C: -Type recoverypassword

Or just obtain the all “protectors” for volume C:

    manage-bde.exe -protectors -get C:

### manage-bdg.wsf

You can unlock a drive with the cscript command, leaving the master key
in the clear by using these commands:

    cscript manage-bdg.wsf unlock c:
    cscript manage-bdg.wsf autounlock enable c:

### Changes in Bitlocker for Windows 10

As of the fall of 2015, Microsoft introduced a new mode in Bitlocker on
Windows 10, XTS-AES. Volumes encrypted in this manner are not backwards
compatible with previous versions of Windows/Bitlocker and can only be
opened on Windows 10 systems and later.

## See Also

- [BitLocker: How to image](bitlocker:_how_to_image.md)

## External Links

- [Wikipedia entry on BitLocker](https://en.wikipedia.org/wiki/BitLocker_Drive_Encryption)
- [Accessing Bitlocker volumes from linux](http://www.nvlabs.in/nvbit_bitlocker_white_paper.pdf),
  by Nitin Kumar and Vipin Kumar, 2008
- [Implementing BitLocker for Forensic Analysis](http://jessekornblum.com/publications/di09.html),
  *Digital Investigation*, by Jesse D. Kornblum, 2009
- [BitLocker Drive Encryption (BDE) format specification](https://github.com/libyal/libbde/blob/master/documentation/BitLocker%20Drive%20Encryption%20(BDE)%20format.asciidoc),
  by the [libbde project](libbde.md), March 2011
- [Microsoft's Step by Step Guide](http://technet2.microsoft.com/WindowsVista/en/library/c61f2a12-8ae6-4957-b031-97b4d762cf311033.mspx?mfr=true)
- [Microsoft Technical Overview](https://learn.microsoft.com/en-us/)
- [An Introduction to Security in Windows 7](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/dd630640(v=msdn.10))
- [Microsoft FAQ](http://www.microsoft.com/whdc/system/platform/hwsecurity/BitLockerFAQ.mspx)
- [Microsoft Description of the Encryption Algorithm](https://www.microsoft.com/en-us/download/details.aspx?id=13866)
- [Cold Boot Attacks, Full Disk Encryption, and BitLocker](http://secude.com/htm/801/en/White_Paper%3A_Cold_Boot_Attacks.htm)
- [What's New in BitLocker](https://learn.microsoft.com/en-us/previous-versions/orphan-topics/ws.11/hh831412(v=ws.11))
  in Windows 8
- [Windows 10 Version 1511 gets new XTS-AES BitLocker encryption algorithm](https://www.onmsft.com/news/windows-10-version-1511-gets-new-xts-aes-bitlocker-encryption-algorithm/)
- [What's new in BitLocker](https://learn.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-1507-and-1511)
  Windows 10

## Tools

- [dislocker](https://www.hsc.fr/securite-internet/)
- [libbde](libbde.md)
- [M3 Bitlocker Loader for Mac](https://www.m3datarecovery.com/mac-bitlocker/)
- [M3 Bitlocker Recovery](https://www.m3datarecovery.com/bitlocker-recovery/bitlocker-data-recovery.html)
- [Manage-bde.exe](http://technet.microsoft.com/en-us/library/dd875513(v=ws.10>).aspx)
