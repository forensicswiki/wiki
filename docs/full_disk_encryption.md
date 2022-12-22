---
tags:
  -  Encryption
  -  Disk Encryption
  -  Anti-Forensics
---
**Full Disk Encryption** or **Whole Disk Encryption** is a phrase that
was coined by [Seagate](seagate.md) to describe their encrypting
[hard drive](hard_drive.md). Under such a system, the entire
contents of a hard drive are encrypted. This is different from [Full
Volume Encryption](full_volume_encryption.md) where only certain
portions, such as a partition or volume is encrypted.

Some examples of full disk encryption:

## Hardware Solutions

### Embedded into internal HDD

Hitachi *Bulk Data Encryption* ("BDE")
<http://www.hitachigst.com/tech/techlib.nsf/techdocs/74D8260832F2F75E862572D7004AE077/$file/bulk_encryption_white_paper.pdf>

- FIPS 197 (Federal Information Processing Standard 197 certification
  issued by NIST)
- [AES-128](http://csrc.nist.gov/groups/STM/cavp/documents/aes/aesval.html)

Seagate *Full Disk Encryption* ("FDE")
<http://www.seagate.com/docs/pdf/marketing/PO-Momentus-FDE.pdf>

Seagate's encrypted drives are only available as OEM products. Seagate
provides no software to utilize encrypted drive features (such as key
management). There is a proprietary Windows-only API, but it is not
available to the public.

- [FIPS
  140-2](http://www.seagate.com/ww/v/index.jsp?name=st9500422as-momentus-7200-fde-fips-140-2-sata-500gb-hd&vgnextoid=0be9f080d2c55210VgnVCM1000001a48090aRCRD&locale=en-US&pf=1)
  (Federal Information Processing Standard 140-2 certification issued by
  NIST)

Toshiba *Self-Encrypting Drives* ("SED")

- [AES-256](http://sdd.toshiba.com/main.aspx?Path=ServicesSupport/Self-EncryptingDrives)
  (certification issued by NIST)

### Supplemental Hardware / External Chassis

Addonics product lines
<http://www.addonics.com/products/cipher/CPD256U.asp>

<!-- -->

Apricorn product lines
<http://www.apricorn.com/products.php?cat_id=72>

<!-- -->

DigiSafe
<http://www.digisafe.com/products/products_DiskCryptMobile.htm>

<!-- -->

Eracom Technology DiskProtect
<http://www.eracom-tech.com/drive_encryption.0.html>

<!-- -->

iStorage DiskCrypt Mobile
<http://www.istorage-uk.com/diskcryptmobile.php>

<!-- -->

Network Appliance (Decru)
<http://www.netapp.com/ftp/decru-fileshredding.pdf>

<http://www.netapp.com/us/products/storage-security-systems/>

<http://www.forensicswiki.org/images/6/6f/Securing_Storage_White_Paper.pdf>
(Decru white paper)

## Software Solutions

beCrypt
<http://www.becrypt.com/our_products/disk_protect.php>

<!-- -->

[BitArmor](bitarmor.md) [DataControl](datacontrol.md) FDE tool that protects
fixed and removable media.

<!-- -->

[BitLocker](bitlocker.md)
Part of Windows Vista that uses [AES](aes.md) 128 or 256 bit
encryption

<!-- -->

[CGD](cgd.md)
Cryptographic Device Driver. Provides transparent full disk encryption
for [NetBSD](netbsd.md).

Supports various [ciphers](ciphers.md): [AES](aes.md)
(128 bit blocksize and accepts 128, 192 or 256 bit keys),
[Blowfish](blowfish.md) (64 bit blocksize and accepts 128 bit
keys) and [3DES](3des.md) (uses a 64 bit blocksize and accepts
192 bit keys (only 168 bits are actually used for encryption).

<http://www.netbsd.org/docs/guide/en/chap-cgd.html>

<!-- -->

[Checkpoint Full Disk Encryption](checkpoint_full_disk_encryption.md)
<http://www.checkpoint.com/products/datasecurity/pc/>

<!-- -->

[DiskCryptor](diskcryptor.md)
Free solution provided under GNU General Public License.

<http://diskcryptor.net/index.php/DiskCryptor_en>

<!-- -->

[FreeOTFE](freeotfe.md)
Transparent on the fly encryption for [MS Windows](windows.md)
and [Windows Mobile](microsoft_windows_mobile.md) PDAs. Also
supports mounting [Linux](linux.md)
[dm-crypt](dm-crypt.md) and
[LUKS](linux_unified_key_setup_(luks).md) volumes

<http://www.FreeOTFE.org/>

<!-- -->

[GBDE](gbde.md)
[GEOM](geom.md) Based Disk Encryption. Provides transparent full
disk and swap encryption for [FreeBSD](freebsd.md). Supported
[ciphers](ciphers.md): [AES](aes.md) (128 bit).

Supports hidden volumes and Pre-Boot Authentification.

Since data loss can occur on unexpected shutdowns, GELI is recommended
instead of GBDE.

<http://www.freebsd.org/cgi/man.cgi?query=gbde&apropos=0&sektion=8&manpath=FreeBSD+6.2-RELEASE&format=html>

<http://phk.freebsd.dk/pubs/bsdcon-03.gbde.paper.pdf>

<!-- -->

[GELI](geli.md)
Cryptographic [GEOM](geom.md) class. Provides transparent full
disk encryption for [FreeBSD](freebsd.md). Supports various
[ciphers](ciphers.md): [AES](aes.md),
[Blowfish](blowfish.md) and [3DES](3des.md).

Supports hidden volumes and Pre-Boot Authentification.

<http://www.freebsd.org/cgi/man.cgi?query=geli&sektion=8>

<!-- -->

[FileVault Disk Encryption](filevault_disk_encryption.md)

<!-- -->

Jetico BestCrypt
<http://www.jetico.com/>

<!-- -->

[loop-AES](loop-aes.md)
Transparent [file system](file_system.md) and
[swap](swap.md) encryption for [Linux](linux.md) using
the loopback device and [AES](aes.md).

<http://sourceforge.net/projects/loop-aes/>

<!-- -->

[Linux Unified Key Setup (LUKS)](linux_unified_key_setup_(luks).md) or [dm-crypt](dm-crypt.md)
Transparent [file system](file_system.md) and
[swap](swap.md) encryption for [Linux](linux.md) using
the Linux 2.6 device mapper. Supports various
[ciphers](ciphers.md) and [Linux Unified Key Setup
(LUKS)](linux_unified_key_setup_(luks).md).

<http://www.saout.de/misc/dm-crypt/>

<!-- -->

[PGPDisk](pgpdisk.md)
Pretty Good Privacy Whole Disk Encryption provides transparent whole
disk encryption with Pre-Boot authentification for
[Windows](windows.md). Also supports [MacOS](macos.md) X
10.4 (non-boot disks only).

Can use OpenPGP RFC 2440 keys and X.509 keys for authentification.

Supports USB Tokens for authentification.

Supported [ciphers](ciphers.md): [AES](aes.md) (256 bit
keys).

<http://www.pgp.com/products/wholediskencryption/>

<!-- -->

[SafeGuard Easy](safeguard_easy.md)
Certified according to [Common Criteria](common_criteria.md)
EAL3 and FIPS 140-2

Encryption algorithms supported: [AES](aes.md) (128 and 256 bit)
and [IDEA](idea.md)

Provides complete [hard drive](hard_drive.md) encryption
including the boot disk.

<http://www.utimaco.us/products>

<!-- -->

[SECUDE](secude.md)
[SECUDE](secude.md) provides a software and hardware solution
for full disk encryption.

<http://www.secude.com>

<!-- -->

Securstar DriveCrypt
<http://www.securstar.com/products_drivecryptpp.php>

<!-- -->

[TrueCrypt](truecrypt.md)
Transparent full disk encryption for [Linux](linux.md) and
[Windows](windows.md). Supports [AES](aes.md) (256 bit), [Serpent](serpent.md)
and [Twofish](twofish.md).

Supports hidden volumes within TrueCrypt volumes (plausible deniability).

<http://www.truecrypt.org/>

<!-- -->

[VeraCrypt](veracrypt.md)
Fork of [TrueCrypt](truecrypt.md) project. Support for for
[Linux](linux.md), [Windows](windows.md), and
[MacOS](macos.md).

<http://veracrypt.codeplex.com/>

<!-- -->

[vnconfig](vnconfig.md)
The -K option of [OpenBSD](openbsd.md) associates
and encryption key with the svnd device. Supports saltfiles. Supported
[ciphers](ciphers.md): [Blowfish](blowfish.md).

<http://www.openbsd.org/cgi-bin/man.cgi?query=vnconfig&sektion=8>

## Full Disk Encryption Analysis Tools

Due to continual updates and variances to full disk encryption software,
there is varied coverage of each software by digital forensics tools.
Additionally, each forensic tool may only support limited versions of
the encryption software, as noted in the table below:

|                                                  |
|--------------------------------------------------|
| Solution                                         |
| [EnCase Forensics v6](encase.md)         |
| [EnCase Forensics v7](encase.md)         |
| [EnCase Forensics v8](encase.md)         |
| [AccessData FTK v6](forensic_toolkit.md) |
| [X-Ways](x-ways.md)                      |
| Other Applications                               |

## See Also

[Full Volume Encryption](full_volume_encryption.md)

[BitLocker Disk Encryption](bitlocker_disk_encryption.md)

## External Links

- [Wiki page for FDE on
  Thinkpads](http://www.thinkwiki.org/wiki/Full_Disk_Encryption_(FDE))
- [Bypassing SelfEncrypting Drives (SED) in Enterprise
  Environments](https://www.blackhat.com/docs/eu-15/materials/eu-15-Boteanu-Bypassing-Self-Encrypting-Drives-SED-In-Enterprise-Environments.pdf),
  by Daniel Boteanu and Kevvie Fowler, November 12, 2015

