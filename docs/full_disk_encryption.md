---
tags:
  - Disk Encryption
---
**Full Disk Encryption** or **Whole Disk Encryption** is a phrase that
was coined by Seagate to describe their encrypting
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
- [AES-128](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/validation-search)

Seagate *Full Disk Encryption* ("FDE")
<http://www.seagate.com/docs/pdf/marketing/PO-Momentus-FDE.pdf>

Seagate's encrypted drives are only available as OEM products. Seagate
provides no software to utilize encrypted drive features (such as key
management). There is a proprietary Windows-only API, but it is not
available to the public.

- [FIPS 140-2](https://www.seagate.com/de/de/)
  (Federal Information Processing Standard 140-2 certification issued by
  NIST)

Toshiba *Self-Encrypting Drives* ("SED")

## Software Solutions

[beCrypt](https://www.becrypt.com/)

[BitLocker](bitlocker_disk_encryption.md)
Part of Windows Vista that uses [AES](aes.md) 128 or 256 bit
encryption

[CGD](cgd.md)
Cryptographic Device Driver. Provides transparent full disk encryption
for [NetBSD](netbsd.md).

Supports various ciphers: [AES](aes.md)
(128 bit blocksize and accepts 128, 192 or 256 bit keys),
[Blowfish](blowfish.md) (64 bit blocksize and accepts 128 bit
keys) and [3DES](3des.md) (uses a 64 bit blocksize and accepts
192 bit keys (only 168 bits are actually used for encryption).

<http://www.netbsd.org/docs/guide/en/chap-cgd.html>

[Checkpoint Full Disk Encryption](checkpoint_full_disk_encryption.md)
<https://www.checkpoint.com/quantum/data-loss-prevention/>

[DiskCryptor](diskcryptor.md)
Free solution provided under GNU General Public License.

<https://diskcryptor.org/>

[FreeOTFE](freeotfe.md)
Transparent on the fly encryption for [MS Windows](windows.md)
and [Windows Mobile](microsoft_windows_mobile.md) PDAs. Also
supports mounting [Linux](linux.md)
dm-crypt and
[LUKS](linux_unified_key_setup_(luks).md) volumes

[GBDE](gbde.md)
GEOM Based Disk Encryption. Provides transparent full
disk and swap encryption for [FreeBSD](freebsd.md). Supported
ciphers: [AES](aes.md) (128 bit).

Supports hidden volumes and Pre-Boot Authentification.

Since data loss can occur on unexpected shutdowns, GELI is recommended
instead of GBDE.

[GELI](geli.md)
Cryptographic GEOM class. Provides transparent full
disk encryption for [FreeBSD](freebsd.md). Supports various
ciphers: [AES](aes.md),
[Blowfish](blowfish.md) and [3DES](3des.md).

Supports hidden volumes and Pre-Boot Authentification.

[FileVault Disk Encryption](filevault_disk_encryption.md)

[Jetico BestCrypt](https://www.jetico.com/)

[loop-AES](https://sourceforge.net/projects/loop-aes/)
Transparent file system and swap encryption for [Linux](linux.md)
using the loopback device and [AES](aes.md).

[Linux Unified Key Setup (LUKS)](linux_unified_key_setup_(luks).md) or dm-crypt
Transparent file system and swap encryption for [Linux](linux.md)
using the Linux 2.6 device mapper. Supports various ciphers and
[Linux Unified Key Setup (LUKS)](linux_unified_key_setup_(luks).md).

<https://www.saout.de/misc/dm-crypt/>

SafeGuard Easy
Certified according to Common Criteria
EAL3 and FIPS 140-2

Encryption algorithms supported: [AES](aes.md) (128 and 256 bit)
and IDEA

Provides complete [hard drive](hard_drive.md) encryption
including the boot disk.

<https://utimaco.com/products>

[Securstar DriveCrypt](http://www.securstar.com/products_drivecryptpp.php)

[TrueCrypt](truecrypt.md)
Transparent full disk encryption for [Linux](linux.md) and
[Windows](windows.md). Supports [AES](aes.md) (256 bit), [Serpent](serpent.md)
and [Twofish](twofish.md).

Supports hidden volumes within TrueCrypt volumes (plausible deniability).

<https://truecrypt.sourceforge.net/>

[VeraCrypt](https://www.veracrypt.fr/)
Fork of [TrueCrypt](truecrypt.md) project. Support for for
[Linux](linux.md), [Windows](windows.md), and
[MacOS](mac_os_x.md).

[vnconfig](vnconfig.md)
The -K option of [OpenBSD](openbsd.md) associates
and encryption key with the svnd device. Supports saltfiles. Supported
ciphers: [Blowfish](blowfish.md).

<http://www.openbsd.org/cgi-bin/man.cgi?query=vnconfig&sektion=8>

## Full Disk Encryption Analysis Tools

Due to continual updates and variances to full disk encryption software,
there is varied coverage of each software by digital forensics tools.
Additionally, each forensic tool may only support limited versions of
the encryption software, as noted in the table below:

|                                                  |
|--------------------------------------------------|
| Solution                                         |
| [EnCase Forensics](encase.md)                    |
| [AccessData FTK v6](forensic_toolkit.md)         |
| [X-Ways](x-ways_ag.md)                           |
| Other Applications                               |

## See Also

* [BitLocker Disk Encryption](bitlocker_disk_encryption.md)
* [Full Volume Encryption](full_volume_encryption.md)

## External Links

* [Wiki page for FDE on Thinkpads](https://www.thinkwiki.org/wiki/Full_Disk_Encryption_(FDE))
* [Bypassing SelfEncrypting Drives (SED) in Enterprise Environments](https://www.blackhat.com/docs/eu-15/materials/eu-15-Boteanu-Bypassing-Self-Encrypting-Drives-SED-In-Enterprise-Environments.pdf),
  by Daniel Boteanu and Kevvie Fowler, November 12, 2015
