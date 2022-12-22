---
tags:
  -  Linux
---
**Selective File Dumper** (SFDumper) is a tool written in
[Bash](bash.md) Script for [Linux](linux.md) systems.

It's fast and selective, it can retrieve all the files of the file type
you choose with only one tool referenced, deleted and unallocated in
very fast way.

The [Bash](bash.md) script **SFDUMPER.SH** can recover active,
deleted and unallocated files automatically and then it can delete the
carved duplicate files of the deleted and active files retrieved by the
[The Sleuth Kit](the_sleuth_kit.md), thanks to the comparison of the
[SHA256](sha-2.md) [hash](hash.md) codes.

It's possible to recognize the renamed files by the data carving and
it's possible to expand the [Foremost](foremost.md)
configuration file inside the script, for adding new extensions.

Finally, it is possible to do a [keywords](keywords.md) search
on the set of files extracted by the [The Sleuth Kit](the_sleuth_kit.md)
and [Foremost](foremost.md).

The script can work on the partition chosen from an image file or
directly from the device (eg. /dev/sdb).

## Actions

> 1\) Choosing the partition to analyze from an image file or a
> device;
> 2) Choosing the file type by the extension you need to have;
> 3) Extracting all referenced files by their extension;
> 4) Extracting all the deleted files by their extension;
> 5) Carving all the partitions chosen and, automatically, the script
> will
> delete the duplicate files leaving only the carved files whose are
> not
> into the referenced or delete set of files;
> 6) Executing a keyword search on all the retrieved files;
> 7) Reporting all with the investigator name, date and time.

## Requirements

- [Linux](linux.md)
- [The Sleuth Kit](the_sleuth_kit.md)
- [Foremost](foremost.md)
- [md5deep](md5deep.md)
- [grep](grep.md)
- [awk](awk.md)
- [sed](sed.md)
- [dd](dd.md)

## Requirements for the GUI version

- [Zenity](zenity.md)

## Usage

*sudo sh sfdumper.sh*

or

*chmod +x sfdumper.sh*

*./sfdumper.sh*

## Official web site

- <http://sfdumper.sourceforge.net>

## External links

- <http://freshmeat.net/projects/zenity>

