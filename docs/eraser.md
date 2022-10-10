---
tags:
  -  Anti-Forensics 
  -  Tools
  -  Windows
  -  Secure Deletion
  -  Opensource Software
---
Eraser is a Windows tool that allows you to securely remove files from
your computers hard drive and securely wipe free space so as to remove
the [residual data](residual_data.md) of previously deleted
files by overwriting with specially selected wiping paterns.

Eraser currently works with Windows 95, 98, ME, NT, 2000, XP, Windows
2003 Server and DOS and supports FAT and NTFS formatted IDE/SATA/SCSI
hard drives. Support for Vista was introduced in 5.83beta.

The software supports the scheduled wiping of files via its *Scheduler*
console as well as on demand file wiping which can be done via an
Explorer context menu or dragging files to the Eraser application. It
can attempt to wipe locked files (e.g. [index.dat](index.dat.md)
files) after the next reboot by forcing a wipe before Windows takes
control again.

# Methodology

Eraser overwrites the filename for each deleted file with zeros up to
the maximum filename length.

Supported wiping patterns include

| Erase File                           | Erase Free Space                     |
|--------------------------------------|--------------------------------------|
| Gutmann                              | Gutmann                              |
| US DoD 5220.22-M (8-306 /E, C and E) | US DoD 5220.22-M (8-306 /E, C and E) |
| US DoD 5220.22-M (8-306 /E)          | US DoD 5220.22-M (8-306 /E)          |
| Pseudorandom Data                    | Pseudorandom Data                    |
| First and Last 2kb                   | \-                                   |
| Schneier's 7 Pass                    | Schneier's 7 Pass                    |

# Authors

Eraser was originally developed by Sami Tolvanen and now maintained by
Garrett Trant of Heidi Computers Ltd.

# External Links

- [Official website](http://www.heidi.ie/eraser/)
- [Eraser Support Forums](http://bbs.heidi.ie/index.php)