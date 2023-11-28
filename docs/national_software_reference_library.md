---
tags:
  - Hashing
---
The **National Software Reference Library** (NSRL) is the National
Institute of Standards and Technology's National Software Reference
Library. The NSRL is a physical resource located in Gaithersburg
Maryland. The NSRL consists of more than 21,000 individual software
packages. NIST has the original packaging and distribution media for
15,000 packages, and archived digital distributions for the remainder.

RDS is the Reference Data Set. The RDS consists of the metadata
describing software package titles, manufacturers, operating systems,
file metadata and hash codes of the files in the NSRL. Originally (ca.
2000-2002) it was created by installing the software on systems and then
generating a list of the hash codes. During 2003-2012 it was created by
processing only the distributed media and extracting the installation
files from the Microsoft .CAB, .MSI and .ZIP files, Unix/Linux .RPM and
.DEB files, Apple .DMG files, and generic archive files. As of 2013,
operating systems and packages are installed in virtual machines to
facilitate collection of metadata and hashes from those installations.

The RDS is typically used for [data reduction](data_reduction.md). That is, the
set of hash codes is used as a filter to eliminate or highlight files from
examination. Most frequently the RDS used as a list of *known goods* that can
be safely suppressed. *This is an incorrect usage of the RDS and should be
discouraged,* because the RDS does not indicate if a file is known good or bad,
only that it is known. Indeed, the RDS has many files that were once throught
to be good, but are now thought to be bad---for example, versions of Adobe
Flash with known security vulnerabilities. Categories such as "Steganography"
or "Keylogger" are assigned to allow filtering by need.

The NSRL is distributed online can be downloaded from the
[NSRL website](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download).

## RDS File Format

Each RDS consists of several files, but the hashes are stored in
`NSRLFile.txt`. These files have a header followed by many hash records.
The header denotes the columns in each file. (See the External Links for
the complete specification). RDS files can be used directly with
programs like [md5deep](md5deep.md), [FTK](forensic_toolkit.md), and
[EnCase](encase.md).

The file format has changed slightly over time. Releases occur four
times per year. The latest version was dated 1 Mar 2013:

### Version 2.0

Starting in version 2.0, the NSRL moved the hashes to the start of each
line and dropped the MD4 hash. The file header:

```
"SHA-1","MD5","CRC32","FileName","FileSize","ProductCode","OpSystemCode","SpecialCode"
```

### Version 1.5

Information on the older header version is kept here so that programs
can read older files. The file header:

```
"SHA-1","FileName","FileSize","ProductCode","OpSystemCode","MD4","MD5","CRC32","SpecialCode"
```

`OpSystemCode` refers to the operating system code. The `SpecialCode` is
a single character that can be used to mark records. A normal file has a
blank value here. An `M` in this field denotes a malicious file.

## External Links

* [NSRL website](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl)
* [Data Formats of the NSRL Reference Data Set (RDS) Distribution](https://www.nist.gov/system/files/data-formats-of-the-nsrl-reference-data-set-16.pdf)
