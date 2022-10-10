---
tags:
  -  Registry Analysis
  -  Windows 
---
The OpenSaveMRU key exists in the [Windows
Registry](windows_registry.md) and tracks files that have been
opened or saved within a Windows shell dialog box. It is part of a set
of keys recording information from the Windows Common Dialog. The Common
Dialog libraries can be used by any Windows application and Microsoft
highly recommends that developers use them instead of creating novel
user interface elements
[1](http://msdn.microsoft.com/en-us/library/windows/desktop/aa511274.aspx).
Data is commonly found in this key from web browsers, document viewers,
archiving utilities, and image viewers.

## Registry Key Location

The key is present in each user's NTUSER.DAT hive in the
\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDIg32\OpenSaveMRU
[location](list_of_windows_mru_locations.md). The values stored
in the key itself are items that do not have file extensions associated
with them
[2](http://computer-forensics.sans.org/blog/2010/04/02/openrunsavemru-lastvisitedmru).
Since most files in Windows have extensions, what often ends up here is
auto-complete information. Consider an OpenSave dialog box that allows
you to choose a file type from a list (e.g. .jpg, .png, .bmp). User
input into this dialog will typically be the name of the file without
the extension, since the dropdown filetype menu takes care of filling in
the extension. Thus what will be stored in the OpenSaveMRU value is
auto-complete information for that transaction, and the full filename is
not stored.

## Sub-Keys

The possibility for a large number of subkeys exist within the
OpenSaveMRU key. All but one of the sub-keys correspond to file
extensions and store full path information for files of that extension
that have been opened or saved. Each subkey keeps its own Most Recently
Used (MRU) list and last write time.

One outlier is the \* subkey. This key tracks the last ten files of any
extension (including no extension) that have been input into the
OpenSave dialog
[3](http://www.forensicfocus.com/index.php?name=Content&pid=73&page=8).

## OpenSaveMRU in Windows 7

Starting with Windows Vista, the key has been renamed to
[OpenSavePidlMRU](opensavepidlmru.md)

## External Links

Harlan Carvey, Windows Forensic Analysis DVD Toolkit, 2009