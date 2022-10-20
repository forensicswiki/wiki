---
tags:
  -  Libyal
  -  Disk Imaging
  -  Tools
  -  Linux
  -  Windows
  -  MacOS
  -  Open Source Software
---
**Libewf** is a library to access the [Expert Witness Compression Format (ewf)](encase_image_file_format.md).

## Features

Read or write supported EWF formats:

- [SMART](smart.md)
- [EnCase](encase.md)

Read-only supported EWF formats:

- Logical Evidence File (LEF) .L01 (EWF-L01) and .Lx01 (EWF2-Lx01)

Other features:

- empty-block compression
- read/write access using delta (or shadow) files
- write resume

## Tools

The **libewf** package contains the following tools:

- **ewfacquire**, which writes storage media data from devices and files
  to EWF files.
- **ewfacquirestream**, which writes data from stdin to EWF files.
- **ewfdebug**; experimental tool does nothing at the moment.
- **ewfexport**, which exports storage media data in EWF files to
  (split) RAW format or a specific version of EWF files.
- **ewfinfo**, which shows the metadata in EWF files.
- **ewfmount**, which FUSE mounts EWF files.
- **ewfrecover**; special variant of ewfexport to create a new set of
  EWF files from a corrupt set.
- **ewfverify**, which verifies the storage media data in EWF files.
- **ewfaquirestream-mt**, C++ 11 multi-threaded version of
  ewfacquirestream contributed by Bernhard Zach in 2013.

The **libewf** package also contains the following bindings:

- **ewf.net**, bindings for .Net
- **pyewf**, bindings for Python contributed by [David
  Collett](david_collett.md) in 2008

### Contributions

Tools that have been contributed to the project are provided as separate
tools on the sourceforge libewf project site. These are:

- **mount_ewf.py**, which allows the storage media data in a EWF files
  to be mounted, contributed by [David
  Loveall](david_loveall.md) in 2007.
- **libewf-java**, Java (JNA) bindings were contributed by [Bradley
  Schatz](bradley_schatz.md) in 2009.
- **delphi imdisk proxy**, Borland Delphi imdisk proxy, as an
  alternative to mount_ewf.py for Windows, contributed by [Brendan
  Berney](brendan_berney.md) in 2010. In 2014 this was updated
  by Erwan L and is currently maintained as a separate project
  [here](http://labalec.fr/erwan/?p=1235).
- **jlibewf**, native Java EWF reader contributed by [Bruce
  Allen](bruce_allen.md) in 2010.
- **libewfcs**, native C# EWF reader contributed by [Bruce
  Allen](bruce_allen.md) in 2011.

A menu based interface for ewfacquirestream called pyEWF, contributed by
[Dennis Schreiber](dennis_schreiber.md), was originally also
available on the uitwisselplatform project site. However this is
currently no longer maintained and was not moved to the sourceforge
project size. The uitwisselplatform no longer exists. The name pyewf was
reused for the libewf Python bindings created by [David
Collett](david_collett.md) which is now included in the libewf
package.

### Examples

Imaging a device on a Unix-based system:

    ewfacquire /dev/sda

Imaging a device on a Windows system:

    ewfacquire \\.\PhysicalDrive0

Converting a RAW into an EWF image

    ewfacquire myfile.raw

or:

    ewfacquire -c best -m fixed -t myfile -S 1T -u [-q] myfile.raw

or

    cat split.raw.??? | ewfacquirestream
    cat myfile.??? | ewfacquirestream  -c best -m fixed -t myfile -S 1T

Converting an optical disc (split) RAW into an EWF image (libewf
20110109 or later)

    ewfacquire -T optical.cue optical.iso

Converting an EWF into another EWF format or a (split) RAW image

    ewfexport image.E01

Exporting files from a logical image (L01)

    ewfexport image.L01

FUSE mounting an EWF image (libewf 20110828 or later)

    ewfmount image.E01 mount_point

FUSE mounting a logical image (L01) (libewf 20111016 or later)

    ewfmount -f files image.L01 mount_point

Verify an single image with results to the screen

    ewfverify image.E01

From a linux shell, verify a group of images in subdirectories of the
current directory creating a simple log file per image.

    find . -name \*.E01 -printf '%f %p\n' | xargs printf "ewfverify -l \$(basename -s .E01 %s).ewfverify.out  %s\n" | sh

or

    find . -name '*.E01' | while read F
    do
      echo ewfverify -l "$(basename -s .E01 $F).ewfverify.out" "$F"
    done

On Mac OS X you can run hdiutil on a mounted EWF file set:

    hdiutil attach -imagekey diskimage-class=CRawDiskImage fuse/ewf1

## History

Libewf was created by [Joachim Metz](joachim_metz.md) in 2006,
while working for [Hoffmann Investigations](http://en.hoffmannbv.nl/).

Libewf is a rewrite of earlier work on the EnCase 4 file format by
[Michael Cohen](michael_cohen.md) part of
[PyFlag](pyflag.md) and the [Expert Witness Compression
Format](:file:asr_data's_expert_witness_compression_format.pdf.md)
Specification by [Andrew Rosen](andrew_rosen.md). It has been
updated to read and write EnCase version 1 to 7 .E01 files, EnCase 5 to
7 .L01 files, EnCase 7 .Ex01 and .Lx01 files and SMART .s01 files.
Libewf has initiated an Extended EWF (EWF-X) specifications to bypass
limitations on the format imposed by the EnCase .E01 format.

In 2007 [David Loveall](david_loveall.md) contributed
mount_ewf.py to the libewf project. This application allows a
[fuse](fuse.md) based mount of the storage media data in the EWF
files to be mounted. Due to repeated issues with Python and the fuse
Python-bindings on [Mac OS X](mac_os_x.md) part of the
functionality of these scripts has been rewritten into **ewfmount**.

As of version 20120715 support for EWF version 2 (.Ex01 and .Lx01) was
added.

## External Links

- [Project site](https://github.com/libyal/libewf/)
- [Building libewf and tools from
  source](https://github.com/libyal/libewf/wiki/Building)
- [Mounting a set of EWF
  file(s)](https://github.com/libyal/libewf/wiki/Mounting)
- [Old project site](http://libewf.sourceforge.net)
- [Build a dynamic Libewf dll, using MinGW or Borland C++
  5.5](https://www.isobuster.com/tips/build_libewf_dll_for_isobuster)

