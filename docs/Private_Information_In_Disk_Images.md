Disk images potentially contain a lot of information. Below is a list of
information on disk images that we consider private and information that
we do not consider private. Please feel free to edit this list as
appropriate. Where possible, please provide references for your claims.

## Private Information

- File names in general should be considered private.
- File contents.
- User account Names.
- Geolocation information
- MAC addresses and IP addresses extracted from the disk.
  - Note: Multi-case MAC addresses and private address space IP
    addresses are **not** privacy-sensitive.
- Serial number of the drive (currently there are no publicly available
  databases of serial numbers, but such a database could later be
  released, making serial numbers private).
- Hash of the hard drive.
- Wireless networks to which you have associated.
- File names and executables that are from applications that are
  contraband, sensitive, or not widely available.

Files that are *encrypted* need to be treated as private until they are
decrypted, because you don't know what's inside them.

## Non-Private Information

- City, Country of origin (where it obtained)
- Size of Disk
- Manufacturer of hard drive and model number.
- Time stamps (therefore, timeline information is not private, but the
  names of the files modified are private).
- Operating System Version
- Number of accounts on the disk.
- Hashes of individual files.
- Histogram of file types.
- Number of partitions.
- Overall storage allocation.
- File names of executables and DLLs that are part of widely available
  software packages (e.g., applications in NSRL).