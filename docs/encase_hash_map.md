---
tags:
  - Forensics File Formats
  - Articles that need to be expanded 
---
The [EnCase](encase.md) suite of tools can generate 'hash maps',
or 'EnMap' files, which allow users to identify chunks of files when the
whole file is not available. This data is stored in a file with a .EnMap
extension and contains piecewise [MD5](md5.md) hashes of the
file. Each EnMap file has the following format:

The file has an ASCII header, ENMAP V4, or in hex 45 4e 4d 41 50 20 56
34 0b 00 00 00.

This is followed by a Unicode representation of the original filename.

There is then an [MD5](md5.md) hash of the entire file. This
hash is followed by three bytes of zeros, and then a hexadecimal
representation of each piecewise hash.