---
tags:
  - Hashing
---
The **Message-Digest algorithm 5** (**MD5**) is a cryptographic [hash
function](hash.md) that produces a 128-bit hash value.
Originally developed in 1991, much as has been written about this
algorithm. As such, this article concentrates only on its application to
computer forensics.

## Tools

On most [Unix](unix.md) systems the tools [digest](digest.md), md5 (BSD) or
[md5sum](md5sum.md) can be used to compute the MD5 hash of a file or device.
[md5deep](md5deep.md) can compute MD5 hashes of whole directory trees.

## Weaknesses

Recently some cryptographic weaknesses have been found in MD5. Tool developers
should avoid using MD5 in new products in favor of other hash functions like
[RIPEMD-160](ripemd-160.md), [Tiger](tiger.md), WHIRLPOOL,
[SHA-256](sha-256.md) or [SHA-512](sha-512.md). Host Intrusion Detection
systems and hash databases should also use multiple hash algorithms.

## External Links

* [Wikipedia: MD5](https://en.wikipedia.org/wiki/MD5)
* [Is the MD5 hash unreliable?](http://deepbyte.com/blog/2006/02/is_the_md5_hash_unreliable.html)
* [Collection of exploits and weaknesses in MD5](http://unixsadm.blogspot.com/2007/11/exploiting-md5-and-other-hashing.html)
