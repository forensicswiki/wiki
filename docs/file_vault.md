---
tags:
  - Encryption
---
FileVault (or File Vault) is the cryptographic file system developed by
[Apple](apple_inc.md) and introduced with MacOS 10.3.

FileVault works by storing each user's home directory in an encrypted
".sparseimage" file. The file is
automatically mounted when the user logs in and unmounted when the user
logs out. All of the user's files and preferences are stored in this
file. The file's encryption key is stored in the .sparseimage file, but
that encryption key is itself encrypted with the user's login password.

There are no known attacks against File Vault other than a brute force
attack on the user's password.

As part of the [security enhancements](http://www.apple.com/macosx/features/300.html#security)
in OS X 10.5 (Leopard) Apple have moved from AES-128 to AES-256 for the
encryption used in the disk image.

In Mac OS X 10.7 (Lion) a full volume encryption variant was introduced.

## See Also

* [FileVault Disk Encryption](filevault_disk_encryption.md)

## External Links

* [Design Principles and Patterns for Computer Systems That Are Simultaneously Secure and Usable](http://www.simson.net/thesis),
  by [Simson Garfinkel](simson_garfinkel.md), May 2005. PhD thesis
  that discusses of File Vault's usability shortcomings.
* [Unlocking FileVault](http://events.ccc.de/congress/2006/Fahrplan/track/Hacking/1642.en.html)
  talk at 23rd Chaos Communication Congress (23c3), by Jacob Appelbaum and
  Ralf-Philipp Weinmann, December 2006
  * [slides](http://events.ccc.de/congress/2006/Fahrplan/attachments/1244-23C3VileFault.pdf)

## Tools

* [VileFault](https://code.google.com/p/vilefault)
