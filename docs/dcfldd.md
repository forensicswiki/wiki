---
tags:
  - No Category
---
**dcfldd** is an enhanced version of [dd](dd.md) developed by
the U.S. Department of [Defense Computer Forensics
Lab](defense_computer_forensics_lab.md). It has some useful
features for forensic [investigators](investigator.md) such as:

- On-the-fly [hashing](hash.md) of the transmitted data.
- Progress bar of how much data has already been sent.
- Wiping of disks with known patterns.
- Verification that the image is identical to the original drive,
  bit-for-bit.
- Simultaneous output to more than one file/disk is possible.
- The output can be split into multiple files.
- Logs and data can be piped into external applications.

The program only produces [raw image files](raw_image_file.md).

## Example

**Unix/Linux**

`dcfldd if=/dev/sourcedrive hash=md5,sha256 hashwindow=10G md5log=md5.txt sha256log=sha256.txt \`
`       hashconv=after bs=512 conv=noerror,sync split=10G splitformat=aa of=driveimage.dd`

This command will read ten Gigabytes from the source drive and write
that to a file called driveimage.dd.aa. It will also calculate the
[MD5](md5.md) hash and the sha256 hash of the ten Gigabyte
chunk. It will then read the next ten gigs and name that
driveimage.dd.ab. The md5 hashes will be stored in a file called md5.txt
and the sha256 hashes will be stored in a file called sha256.txt. The
block size for transferring has been set to 512 bytes, and in the event
of read errors, dcfldd will write zeros.

**Windows**

While there is a Windows executable of DCFLDD out there, it can be
difficult to use. There is currently a PowerShell Script that can be
used to help newcomers out, located
[here](https://github.com/Linuxuser437442/powershell-dcfldd)

## Precautions

This tool is not suitable for imaging faulty drives:

- dcfldd is based on an extremely old version of [dd](dd.md):
  it's known that dcfldd will misalign the data in the image after a
  faulty sector is encountered on the source drive ([see the NIST
  report](https://www.cyberfetch.org/groups/community/test-results-digital-data-acquisition-tool-dcfldd-134-1)),
  and this kind of bug (wrong offset calculation when seeking over a bad
  block) was fixed for [dd](dd.md) in 2003 ([see the fix in the
  mailing
  list](http://lists.gnu.org/archive/html/bug-coreutils/2003-10/msg00071.html));
- similarly, dcfldd can enter an infinite loop when a faulty sector is
  encountered on the source drive, thus writing to the image over and
  over again until there is no free space left.

## See Also

- [dc3dd](dc3dd.md)