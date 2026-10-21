---
tags:
  - Data Carving
  - Discontinued
  - Linux
  - Tools
---
Selective File Dumper (SFDumper) is a bash script written by Nanni Bassetti
and Denis Frati that can, in a single run, retrieve all referenced, deleted
and unallocated files of the file types you choose. SFDumper is no longer
maintained.

The SFDUMPER.SH script can recover active, deleted and unallocated files
automatically and then it can delete the carved duplicate files of the deleted
and active files retrieved by [The Sleuth Kit](the_sleuth_kit.md), using
[SHA-256](sha-2.md).

It is possible to recognize renamed files through data carving, and
it is possible to expand the [Foremost](foremost.md)
configuration file inside the script, for adding new extensions.

Finally, it is possible to do a keywords search on the set of files extracted
by [The Sleuth Kit](the_sleuth_kit.md) and [Foremost](foremost.md).

The script can work on the partition chosen from an image file or
directly from the device (e.g., /dev/sdb).

## Actions

1. Choosing the partition to analyze from an image file or a device;
2. Choosing the file type by the extension you need to have;
3. Extracting all referenced files by their extension;
4. Extracting all the deleted files by their extension;
5. Carving all the partitions chosen and, automatically, the script will delete
   the duplicate files leaving only the carved files that are not in the
   referenced or deleted set of files;
6. Executing a keyword search on all the retrieved files;
7. Reporting the results along with the investigator name, date and time.

## Requirements

* [Linux](linux.md)
* [The Sleuth Kit](the_sleuth_kit.md)
* [Foremost](foremost.md)
* [md5deep](md5deep.md)
* sed, grep and awk
* [dd](dd.md)

### Additional requirements for the GUI version

* Zenity

## Use

```bash
sudo sh sfdumper.sh
```

or

```bash
chmod +x sfdumper.sh
./sfdumper.sh
```

## See Also

* [The Sleuth Kit](the_sleuth_kit.md)
* [Foremost](foremost.md)

## External Links

* [Official website](https://sfdumper.sourceforge.net/)
