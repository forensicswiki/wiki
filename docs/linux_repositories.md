---
tags:
  - No Category
---
There are a number of linux distributions.

In general they have primary repositories which are setup for every
installation of the operating system and they have special purpose
repositories which require specific setup.

# Repository Setup

## openSUSE

For current openSUSE 11.4 and 12.1 users it is necessary to have the
following repositories configured:

- security
- devel:languages:perl
- devel:languages:python

This is most easily done from the command line via (assumes openSUSE
12.1):

`sudo zypper ar -f http://download.opensuse.org/repositories/security/openSUSE_12.1 security`
`sudo zypper ar -f http://download.opensuse.org/repositories/devel:/languages:/perl/openSUSE_12.1 perl`
`sudo zypper ar -f http://download.opensuse.org/repositories/devel:/languages:/python/openSUSE_12.1 python`

`zypper lr               # used to verify you have the repos installed`

## fedora

[CERT](https://forensics.cert.org/) maintains a fedora security
repository with a large number of DFIR applications.

## debian

You can search for debian packages at [debian's search
page](http://packages.debian.org/search)

## ubuntu

## altlinux

[ALT Linux packages](http://packages.altlinux.org/) (interesting things
from autoimports tend to be integrated into main repository)

# Computer Forensic Tools

Below is a list of computer forensic tools. For each tool the repository
it can be found in and the version in the repository is shown.

As an example, aimage is in the openSUSE security repository and it is
version 3.2.5

## Imaging Tools

|                                            |                       |            |                           |            |                                                        |                                                                                                      |
|--------------------------------------------|-----------------------|------------|---------------------------|------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Tool**                                   | **openSUSE**          | **fedora** | **debian**                | **ubuntu** | **comment**                                            | **General Remarks**                                                                                  |
| [adepto](http://www.e-fense.com/helix/)    | N/A                   | ?          | N/A                       | ?          |                                                        | adepto is included in the helix boot cd                                                              |
| [aimage](aimage.md) are recommended for creating aff images. |
| [AIR](air.md)                      | N/A                   | ?          | N/A                       | ?          | Automated Image and Restore                            | a GUI front-end to dd and dc3dd designed for easily creating forensic bit images                     |
| [dc3dd](dc3dd.md)                  | security\*/7.1.614    | ?          | sid/7.1.614               | ?          | DoD Cyber Crime Center DD                              | This tool was formerly known as dcfldd. When released as dc3dd it was totally rewritten.             |
| [ddrescue](ddrescue.md)            | Base/1.14             | ?          | squeeze/1.14 sid/1.23     | ?          | Also known as GNU ddrescue                             | This tool is different than dd_rescue.                                                               |
| [dd_rescue](dd_rescue.md)          | N/A                   | ?          | N/A                       | ?          |                                                        | This tool is different than GNU ddrescue.                                                            |
| [ewfacquire](libewf.md)            | security\*/20100226   | ?          | squeeze/20100226          | ?          | a imaging tool to create ewf format images             | ewfacquire is part of ewftools in some distributions.                                                |
| [IXimager](iximager.md)            | N/A                   | ?          | N/A                       | ?          | A law enforcement only imager                          | used in conjunction with ILook Investigator                                                          |
| [LinEn](linen.md)                  | N/A                   | ?          | N/A                       | ?          | a proprietary imaging tool to create ewf format images | included on the Helix boot CD                                                                        |
| [guymager](guymager.md)            | N/A                   | ?          | Squeeze/0.4.2 Sid/0.5.9-3 | ?          | a imaging tool to create aff format images             | Guymager is an open source forensic imager. It focuses on user friendliness and high speed.          |
| [rdd](http://sourceforge.net/projects/rdd) | N/A                   | ?          | 2.0.7-2                   | ?          | a dd-like tool, with forensic imaging features         | Rdd is robust with respect to read errors                                                            |
| [sdd](ftp://ftp.berlios.de/pub/sdd/)       | Archiving:Backup/1.52 | ?          | lenny/1.52 deprecated     | ?          | a dd-like tool                                         | Designed to work well when IBS != OBS. Working with tape is an example.                              |

- package will appear in the base release with the next full
  distribution release.

## File Inventory Tools

|                                 |                    |            |                         |            |             |                                                          |
|---------------------------------|--------------------|------------|-------------------------|------------|-------------|----------------------------------------------------------|
| **Tool**                        | **openSUSE**       | **fedora** | **debian**              | **ubuntu** | **comment** | **General Remarks**                                      |
| [exiftool](exiftool.md) | base/v8.65         | ?          | squeeze/v8.15 sid/v8.60 | ?          |             | exiftool has superior metadata reporting capability --\> |
| [fiwalk](fiwalk.md)     | security\*/v0.6.15 | ?          | N/A                     | ?          |             | fiwalk is a robust \$MFT walker                          |

- package will appear in the base release with the next full
  distribution release.