---
tags:
  - No Category
---
## LZ-based

### Deflate/Inflate

Used in:

* [Expert Witness (Compression) Format (ewf)](encase_image_file_format.md)
* [gzip](gzip.md)
* [Personal Folder File (PAB, PST, OST)](personal_folder_file_(pab,_pst,_ost).md),
  in compressed Offline Storage Table (OST) files.
* [QCOW Image Format](qcow_image_format.md),
  in compressed images
* [VMWare Virtual Disk Format (vmdk)](vmware_virtual_disk_format_(vmdk).md),
  in compressed images

### LZNT1

Used in:

* [NTFS](ntfs.md)
* [Windows SuperFetch Format](windows_superfetch_format.md)

### LZSS

* [Wikipedia: Lempel–Ziv–Storer–Szymanski](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Storer%E2%80%93Szymanski)

### LZX

Used in:

* [Microsoft Cabinet Format](https://learn.microsoft.com/en-us/previous-versions/bb417343(v=msdn.10))

The Windows implementation of LZX can be found in lz32.dll and is used
by the WINAPI LZ functions e.g. LZOpenFile.

### LZXPRESS

Used in:

* [Extensible Storage Engine (ESE) Database File (EDB) format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)

### LZXPRESS Huffman

Variant of LZXPRESS that uses Huffman encoding.

Used in:

* [Windows SuperFetch Format](windows_superfetch_format.md),
  Windows 7

#### LZXPRESS Huffman stream

Variant of LZXPRESS Huffman that allows for LZ compression tuples that
refer to previous blocks of uncompressed data.

Used in:

* [Windows Prefetch File Format](windows_prefetch_file_format.md),
  Windows 10
* [Windows SuperFetch Format](windows_superfetch_format.md),
  Windows 8

## External Links

* [Wikipedia: Lempel-Ziv](https://en.wikipedia.org/wiki/Lempel-Ziv)
* [Microsoft Compression Formats](https://www.coderforlife.com/microsoft-compression-formats/)

### Deflate/Inflate

* [Wikipedia: DEFLATE](https://en.wikipedia.org/wiki/DEFLATE)
* [RFC1950 - ZLIB Compressed Data Format Specification](https://www.rfc-editor.org/rfc/rfc1950),
  by IETF
* [RFC1951 - DEFLATE Compressed Data Format Specification](https://www.rfc-editor.org/rfc/rfc1951),
  by IETF

### LZXpress

* [MS-XCA: Xpress Compression Algorithm](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-xca/a8b7cb0a-92a6-4187-a23b-5e14273b96f8),
  by Microsoft
