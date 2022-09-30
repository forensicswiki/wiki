---
tags:
  -  Libyal
---
The **liblnk** package contains a library and applications to read the
[Windows Explorer Shortcut (lnk)](lnk.md) format.

## Tools

The **liblnk** package contains the following tools:

- **lnkinfo**, which shows information about LNK files.

## Examples

Requesting the information in a LNK file:

    lnkinfo Calculator.lnk

    lnkinfo 20150617

    Windows Shortcut information:
        Contains a link target identifier
        Contains a description string
        Contains a working directory string
        Contains an environment variables block

    Link information:
        Creation time           : Aug 10, 2004 16:54:24.000000000 UTC
        Modification time       : Aug 04, 2004 14:00:00.000000000 UTC
        Access time         : Jun 26, 2006 10:36:41.703125000 UTC
        File size           : 114688 bytes
        File attribute flags        : 0x00000020
            Should be archived (FILE_ATTRIBUTE_ARCHIVE)
        Drive type          : Fixed (3)
        Drive serial number     : 0xc868f004
        Volume label            : System
        Local path          : C:\WINDOWS\system32\calc.exe
        Description         : @%SystemRoot%\system32\shell32.dll,-22531
        Working directory       : C:\WINDOWS\system32
        Environment variables location  : %SystemRoot%\system32\calc.exe

    Link target identifier:
        Shell item list
            Number of items     : 5

        Shell item: 1
            Item type       : Root folder
            Class type indicator    : 0x1f (Root folder)
            Shell folder identifier : 20d04fe0-3aea-1069-a2d8-08002b30309d
            Shell folder name   : My Computer

        Shell item: 2
            Item type       : Volume
            Class type indicator    : 0x2f (Volume)
            Volume name     : C:\

        Shell item: 3
            Item type       : File entry
            Class type indicator    : 0x31 (File entry: Directory)
            Name            : WINDOWS
            Modification time   : Dec 17, 2006 20:55:44
            File attribute flags    : 0x00000010
                Is directory (FILE_ATTRIBUTE_DIRECTORY)
        Extension block: 1
            Signature       : 0xbeef0004 (File entry extension)
            Long name       : WINDOWS
            Creation time       : Feb 01, 2006 21:49:46
            Access time     : Dec 17, 2006 20:55:48

        Shell item: 4
            Item type       : File entry
            Class type indicator    : 0x31 (File entry: Directory)
            Name            : system32
            Modification time   : Nov 26, 2006 19:56:54
            File attribute flags    : 0x00000030
                Is directory (FILE_ATTRIBUTE_DIRECTORY)
                Should be archived (FILE_ATTRIBUTE_ARCHIVE)
        Extension block: 1
            Signature       : 0xbeef0004 (File entry extension)
            Long name       : system32
            Creation time       : Feb 01, 2006 21:49:46
            Access time     : Dec 17, 2006 20:49:46

        Shell item: 5
            Item type       : File entry
            Class type indicator    : 0x32 (File entry: File)
            Name            : calc.exe
            Modification time   : Aug 04, 2004 14:00:00
            File attribute flags    : 0x00000020
                Should be archived (FILE_ATTRIBUTE_ARCHIVE)
        Extension block: 1
            Signature       : 0xbeef0004 (File entry extension)
            Long name       : calc.exe
            Creation time       : Aug 10, 2004 16:54:24
            Access time     : Jun 26, 2006 10:36:42

    Distributed link tracking data:
            Machine identifier              : hostname
            Droid volume identifier         : aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
            Droid file identifier           : 00000000-1111-2222-3333-444444444444
            Birth droid volume identifier   : aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
            Birth droid file identifier     : 00000000-1111-2222-3333-444444444444

## History

Liblnk was created by [Joachim Metz](joachim_metz.md) in 2009,
while working for [Hoffmann Investigations](http://en.hoffmannbv.nl/).

## See Also

- [Windows Shortcut File (LNK) format](lnk.md)

## External Links

- [Project site](https://github.com/libyal/liblnk/)

