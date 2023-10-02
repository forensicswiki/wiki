---
tags:
  - MacOS
  - File Formats
  - Articles that need to be expanded
  - Tools
  - Binary
---
Binary plists are the files that Apple products use to store
information. The easiest way to view them is to convert them to XML.
Note that binary data in XML plist are converted in base64 and therefore
strings in the binary data are not directly visible.

The program **plutil** is native to [Mac OS X](mac_os_x.md) (as
of 10.2), however it is also included when iTunes is installed on a
Windows PC. On linux libplist
[1](https://cgit.sukimashita.com/libplist.git) also provides an
equivalent of **plutil**.

plutil on a Windows PC is stored in:

    C:\Program Files (x86)\Common Files\Apple\Apple Application Support

Which can be added to the PATH in Environmental variables so plutil can
be run from anywhere If you could like to copy out the plutil executable
to another directory it requires a number of DLL's to function. These
dlls are: ASL, CFNetwork, CoreFoundation, Foundation, icudt46,
libdispatch, libicuin, libicuuc, libtidy, libxml2, objc, ptheadVC2,
SQLite3 and zlib. These are all found in the Apple Application Support
folder along with plutil.exe.

To convert Binary plists to XML run the command:

    plutil -convert xml1 file.plist

Or with libplist

    plutil -i file.plist > file.xml.plist

## External Links

* [A library to handle Apple Property List format in binary or XML](https://cgit.sukimashita.com/libplist.git/)
