---
tags:
  - Tools
---
This [MD5](md5.md) [hashing](hashing.md) tool, part of
the GNU Coreutils suite, has been a standard in the computer forensics
community for some time. It is intended for \*nix systems, but has been
ported to the [Windows](windows.md) platform. It should be noted
that the program has options to read files in "binary" or "text" mode,
which can produce different hashes. The text mode is the default on most
platforms, which is different from other hashing utilities such as
[md5deep](md5deep.md).

To use this tool in binary mode on Linux systems you would use the
command:

`md5sum -b [filename|volume]`

e.g.

`md5sum -b /dev/sda`

or

`md5sum -b file.dd`

## External Links

- [Official web site](http://www.gnu.org/software/coreutils/) for GNU
  Coreutils
- [Wikipedia entry on md5sum](http://en.wikipedia.org/wiki/Md5sum)
- [md5sum for Windows](http://www.etree.org/md5com.html)
- [A slew of ported tools for Windows include
  md5sum](http://unxutils.sourceforge.net/)
