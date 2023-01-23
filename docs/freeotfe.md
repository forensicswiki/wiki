---
tags:
  - Encryption
  - Open Source Software
---
**FreeOTFE** is an open source program to create and mount virtual
encrypted disks in [Windows Vista/XP/2000](windows.md) and
[Linux](linux.md). It provides two levels of plausible
deniability (hidden containers and no signatures to make differentiate
containers from random data), on the fly encryption and supports
numerous encryption algorithms (including [AES](aes.md),
[Blowfish](blowfish.md), [Serpent](serpent.md) and [Twofish](twofish.md).

## Hidden volumes

A hidden volume is a volume concealed within the free space of another
FreeOTFE volume. Even when the outer volume is mounted, it is hard to
prove whether there is a hidden volume or not.

When a hidden volume is mounted, the operating system and third-party
applications may write to non-hidden volumes information about the data
stored in the hidden volume (e.g. most recently used [mru](mru.md)).

## External Links

* [Project mirror](https://sourceforge.net/projects/freeotfe.mirror/)
