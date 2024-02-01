---
tags:
  - Articles that need to be expanded
---
**Hashing** is a method for reducing large inputs to a smaller fixed size
output. When doing forensics, typically cryptographic hashing algorithms like
[MD5](md5.md) and [SHA-1](sha-1.md) are used. These functions have a few
properties useful to forensics. Other types of hashing, such as
[Context Triggered Piecewise Hashing](context_triggered_piecewise_hashing.md)
can also be used.

## Tools

There are literally hundreds of hashing programs out there, but a few
related to forensics are:

* [md5sum](md5sum.md) - Part of the GNU coreutils suite, this program is
  standard on many computers.
* [md5deep](md5deep.md) - Computes hashes, recursively if
  desired, and can compare the results to known values.
* [ssdeep](ssdeep.md) - Computes and matches Context Triggered
  Piecewise Hashes.

## Hash Databases

[National Software Reference Library](national_software_reference_library.md)
The largest hash database.

[Hashkeeper](hashkeeper.md)
National Drug Intelligence Center

## MD5 Reverse Hash Services

There are several online services that allow you to enter a hash code
and find out what the preimage might have been. One way to find these
services is to google for 'd41d8cd98f00b204e9800998ecf8427e' (the MD5 of
the null string).

Here are some services that we have been able to find:

[XMD5](http://www.xmd5.org/index_en.htm)
This site is another simple MD5 reverse lookup. It claims a database
with "billions" of entries. Mostly for password cracking.

## Online Malware Hash Lookups

[VirusTotal](https://www.virustotal.com/gui/home/search)

## Segmented Hashing

Segmented hashing produces not a single hash value for the entire image,
but a list of hashes of corresponding LBA ranges of the image. By
validating all hashes in a set it is still verify image integrity.
Segmented Hashes are saved in a CSV file with the following format:
hash, start LBA, end LBA

When Segmented hashing is useful

* Segmented hashes support multi-pass imaging and handling of bad
  sectors: Hashes are calculated only for the imaged regions, while all
  bad sectors are excluded from calculation. This allows to validate a
  hash even when the source drive is damaged.
* Better resiliency against data corruption: If an acquired image gets
  damaged later, regular hash is invalid upon verification making the
  entire image useless. With segmented hashing, only a single hash value
  becomes invalid, while the rest of the image can still be validated.

[Seghash on GitHub](https://github.com/atola-technology/seghash) is a
free open-source tool for both calculating and validating segmented
hashes.

## Tooling

* [hashR](https://github.com/google/hashr) build your own hash sets based on your data sources
