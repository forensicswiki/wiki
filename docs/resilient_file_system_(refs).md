---
tags:
  - File Systems
---
The Resilient File System (ReFS) (AKA protogon) was introduced in
[Windows 8](windows.md), with the intention of eventually
replacing [NTFS](ntfs.md). It has been designed for use with
huge data sets, and provides improvements over NTFS with features such
as repairing errors "on-the-go" (automatic chkdsk) and preventing Torn
Writes by using a "Copy-On-Write" feature.

## External Links

* [Resilient File System overview](http://msdn.microsoft.com/en-us/library/hh831724.aspx)
* [Resilient File System (ReFS)](https://github.com/libyal/libfsrefs/blob/main/documentation/Resilient%20File%20System%20(ReFS).pdf),
  by the [libfsrefs project](https://github.com/libyal/libfsrefs), May 2012
* [Forensic Investigation of Microsoft's Resilient File System (ReFS)](http://resilientfilesystem.co.uk),
  by Andrew Head, April 2015
