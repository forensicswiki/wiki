---
tags:
  - Encryption
---
**unprotect.info** is a software utility that can recover passwords to
the file-based [TrueCrypt](truecrypt.md) volumes by using the
brute-force attack. **unprotect.info** runs on
[Windows 7/Vista/XP/2000](windows.md). It is free for both
personal and commercial use.

## Supported encrypted volumes

**unprotect.info** can currently recover passwords to the volumes
encrypted with the following algorithms:

- Hash functions: RIPEMD-160, [SHA-512](sha-2.md), Whirlpool
- Ciphers: [AES](aes.md), [Serpent](serpent.md),
  [Twofish](twofish.md)
- Encryption modes: XTS

## Unsupported encrypted volumes

If an encrypted volume was created with one of the following options,
its password currently cannot be recovered with the **unprotect.info**
software:

- Deprecated hash functions: [SHA1](sha-1.md)
- Deprecated ciphers: [DES](des.md), CAST, [Blowfish](blowfish.md)
- Deprecated encryption modes: LWR, CBC
- Combination encryption algorithms, such as: AES-Twofish, etc.
- Volumes encrypted with the key files
- Hidden volumes, encrypted partitions, or encrypted drives.

## External Links

- [unprotect.info](https://www.squadhelp.com/name/unprotect.info?lp=d) - Official website
- [truecrypt.org](https://truecrypt.sourceforge.net/) - Official website
