---
tags:
  -  Disk Encryption
  -  Encryption
  -  Linux
  -  Anti-Forensics
---
Linux Unified Key Setup (LUKS) is commonly used by Linux to encrypt
storage media volumes. LUKS is implemented in the Linux kernel in
dm-crypt (dm = Device Mapper) and the user-space component cryptsetup.

LUKS supports various encryption methods, like:

- [Alleged RC4 (arc4)](rc4.md)
- [AES](aes.md)
- [Anubis](anubis.md)
- [BlowFish](blowfish.md)
- [Cast5](cast5.md)
- [Cast6](cast6.md)
- [Serpent](serpent.md)
- Tnepres a reversed variant of [Serpent](serpent.md)
- [TwoFish](twofish.md)

These encryption methods can be used in various chaining modes and with
various initialization vector modes.

## How to detect

A LUKS encrypted volume starts with the "LUKS\xba\xbe" signature.

A hexdump of the start of the volume should look similar to:

    00000000  4c 55 4b 53 ba be 00 01  61 65 73 00 00 00 00 00  |LUKS....aes.....|
    00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000020  00 00 00 00 00 00 00 00  63 62 63 2d 65 73 73 69  |........cbc-essi|
    00000030  76 3a 73 68 61 32 35 36  00 00 00 00 00 00 00 00  |v:sha256........|
    00000040  00 00 00 00 00 00 00 00  72 69 70 65 6d 64 31 36  |........ripemd16|
    00000050  30 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |0...............|

The encryption method in the example is:

    aes

The encryption mode is in the format:

    chaining_mode[-initialization_vector_mode[:initialization_vector_options]]

Which in the example is:

    cbc-essiv:sha256

And the password hashing method in the example is:

    ripemd160

## How to decrypt

`sudo cryptsetup luksOpen `<device>` `<name>

Provide the passphrase when prompted. The <name> will be created as a
device mapper entry (i.e. /dev/mapper/thename) and this device will
expose the filesystem.

## Dump the header information of a LUKS device

`sudo cryptsetup luksDump `<device>

See the cryptsetup(8) man page for other operations.

## External Links

- [New Methods in Hard Disk
  Encryption](http://clemens.endorphin.org/nmihde/nmihde-A4-ds.pdf), by
  Clemens Fruhwirth, July 18, 2005
- [LUKS On-Disk Format Specification - Version
  1.2.1](http://wiki.cryptsetup.googlecode.com/git/LUKS-standard/on-disk-format.pdf),
  by Clemens Fruhwirth, October 16, 2011
- [LUKS Disk
  Encryption](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security_Guide/sect-Security_Guide-LUKS_Disk_Encryption.html),
  by [RedHat](redhat.md)
- [LUKS Disk Encryption format
  specification](https://googledrive.com/host/0B3fBvzttpiiSNUVYSFF1TmRONmc/Linux%20Unified%20Key%20Setup%20(LUKS)%20Disk%20Encryption%20format.pdf),
  by the [libluksde project](libluksde.md), July 2013
- [Practical malleability attack against CBC-Encrypted LUKS
  partitions](http://www.jakoblell.com/blog/2013/12/22/practical-malleability-attack-against-cbc-encrypted-luks-partitions/),
  by Jakob Lell, December 22, 2013