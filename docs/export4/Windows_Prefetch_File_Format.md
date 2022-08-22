A Windows Prefetch file consists of one file header and multiple file
sections with different content. Not all content has an obvious forensic
value.

As far as have been possible to ascertain, there is no official public
description of the format. The description below has been synthesized
from examination of multiple Prefetch files.

As of Windows 10 the Prefetch files are compressed using a similar
compression as used by the [Windows SuperFetch
Format](Windows_SuperFetch_Format "wikilink"). Preliminary findings
regarding Windows 10 Prefetch files are described in [Windows Prefetch
File (PF)
format](https://github.com/libyal/libscca/blob/master/documentation/Windows%20Prefetch%20File%20(PF)%20format.asciidoc).

## Characteristics

|                   |                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| <b>Integers</b>   | stored in little-endian                                                                                      |
| <b>Strings</b>    | Stored as [UTF-16 little-endian](http://en.wikipedia.org/wiki/UTF-16/UCS-2) without a byte-order-mark (BOM). |
| <b>Timestamps</b> | Stored as [Windows FILETIME](http://msdn2.microsoft.com/en-us/library/ms724284.aspx) in UTC.                 |
|                   |                                                                                                              |

## File header

The file header is 84 bytes of size and consists of:

| Field | Offset | Length | Type   | Notes                                                                                                                                                                                                                               |
|-------|--------|--------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| H1    | 0x0000 | 4      | DWORD  | Format version (see format version section below)                                                                                                                                                                                   |
| H2    | 0x0004 | 4      | DWORD  | Signature 'SCCA' (or in hexadecimal representation 0x53 0x43 0x43 0x41)                                                                                                                                                             |
| H3    | 0x0008 | 4      | DWORD? | Unknown - Values observed: 0x0F - Windows XP, 0x11 - Windows 7, Windows 8.1                                                                                                                                                         |
| H4    | 0x000C | 4      | DWORD  | Prefetch file size (or length) (sometimes referred to as End of File (EOF)).                                                                                                                                                        |
| H5    | 0x0010 | 60     | USTR   | The name of the (original) executable as a Unicode (UTF-16 litte-endian string), up to 29 characters and terminated by an end-of-string character (U+0000). This name should correspond with the one in the prefetch file filename. |
| H6    | 0x004C | 4      | DWORD  | The prefetch hash. This hash value should correspond with the one in the prefetch file filename.                                                                                                                                    |
| H7    | 0x0050 | 4      | ?      | Unknown (flags)? Values observed: 0 for almost all prefetch files (XP); 1 for NTOSBOOT-B00DFAAD.pf (XP)                                                                                                                             |
|       |        |        |        |                                                                                                                                                                                                                                     |

It's worth noting that the name of a carved prefetch file can be
restored using the information in field H5 and H6, and its size can be
determined by field H4.

### Format version

| Value     | Windows version                                                               |
|-----------|-------------------------------------------------------------------------------|
| 17 (0x11) | Windows XP, Windows 2003                                                      |
| 23 (0x17) | Windows Vista, Windows 7                                                      |
| 26 (0x1a) | Windows 8.1 (note this could be Windows 8 as well but has not been confirmed) |
| 30 (0x1e) | Windows 10                                                                    |
|           |                                                                               |

Yet unconfirmed are Windows 2008, differences between Windows 2003 and
2008 non-R2 and R2 versions, and Windows 8.0.

### File information

The format of the file information is version dependent.

Note that some other format specifications consider the file information
part of the file header.

#### File information - version 17

The file information – version 17 is 68 bytes of size and consists of:

| Field | Offset | Length | Type     | Notes                                                                                                                                                                                                                  |
|-------|--------|--------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       | 0x0054 | 4      | DWORD    | The offset to section A. The offset is relative from the start of the file.                                                                                                                                            |
|       | 0x0058 | 4      | DWORD    | The number of entries in section A.                                                                                                                                                                                    |
|       | 0x005C | 4      | DWORD    | The offset to section B. The offset is relative from the start of the file.                                                                                                                                            |
|       | 0x0060 | 4      | DWORD    | The number of entries in section B.                                                                                                                                                                                    |
|       | 0x0064 | 4      | DWORD    | The offset to section C. The offset is relative from the start of the file.                                                                                                                                            |
|       | 0x0068 | 4      | DWORD    | Length of section C.                                                                                                                                                                                                   |
|       | 0x006C | 4      | DWORD    | Offset to section D. The offset is relative from the start of the file.                                                                                                                                                |
|       | 0x0070 | 4      | DWORD    | The number of entries in section D.                                                                                                                                                                                    |
|       | 0x0074 | 4      | DWORD    | Length of section D.                                                                                                                                                                                                   |
|       | 0x0078 | 8      | FILETIME | Latest execution time (or run time) of executable (FILETIME)                                                                                                                                                           |
|       | 0x0080 | 16     | ?        | Unknown ? Possibly structured as 4 DWORD. Observed values: /0x00000000 0x00000000 0x00000000 0x00000000/, /0x47868c00 0x00000000 0x47860c00 0x00000000/ (don't exclude the possibility here that this is remnant data) |
|       | 0x0090 | 4      | DWORD    | Execution counter (or run count)                                                                                                                                                                                       |
|       | 0x0094 | 4      | DWORD?   | Unknown ? Observed values: 1, 2, 3, 4, 5, 6 (XP)                                                                                                                                                                       |
|       |        |        |          |                                                                                                                                                                                                                        |

#### File information - version 23

The file information – version 23 is 156 bytes of size and consists of:

| Field | Offset        | Length    | Type     | Notes                                                                       |
|-------|---------------|-----------|----------|-----------------------------------------------------------------------------|
|       | 0x0054        | 4         | DWORD    | The offset to section A. The offset is relative from the start of the file. |
|       | 0x0058        | 4         | DWORD    | The number of entries in section A.                                         |
|       | 0x005C        | 4         | DWORD    | The offset to section B. The offset is relative from the start of the file. |
|       | 0x0060        | 4         | DWORD    | The number of entries in section B.                                         |
|       | 0x0064        | 4         | DWORD    | The offset to section C. The offset is relative from the start of the file. |
|       | 0x0068        | 4         | DWORD    | Length of section C.                                                        |
|       | 0x006C        | 4         | DWORD    | Offset to section D. The offset is relative from the start of the file.     |
|       | 0x0070        | 4         | DWORD    | The number of entries in section D.                                         |
|       | 0x0074        | 4         | DWORD    | Length of section D.                                                        |
|       | <b>0x0078</b> | <b>8</b>  | <b>?</b> | <b>Unknown</b>                                                              |
|       | 0x0080        | 8         | FILETIME | Latest execution time (or run time) of executable (FILETIME)                |
|       | 0x0088        | 16        | ?        | Unknown                                                                     |
|       | 0x0098        | 4         | DWORD    | Execution counter (or run count)                                            |
|       | 0x009C        | 4         | DWORD?   | Unknown                                                                     |
|       | <b>0x00A0</b> | <b>80</b> | <b>?</b> | <b>Unknown</b>                                                              |
|       |               |           |          |                                                                             |

#### File information - version 26

The file information – version 26 is 224 bytes of size and consists of:

| Field | Offset        | Length            | Type            | Notes                                                                                   |
|-------|---------------|-------------------|-----------------|-----------------------------------------------------------------------------------------|
|       | 0x0054        | 4                 | DWORD           | The offset to section A. The offset is relative from the start of the file.             |
|       | 0x0058        | 4                 | DWORD           | The number of entries in section A.                                                     |
|       | 0x005C        | 4                 | DWORD           | The offset to section B. The offset is relative from the start of the file.             |
|       | 0x0060        | 4                 | DWORD           | The number of entries in section B.                                                     |
|       | 0x0064        | 4                 | DWORD           | The offset to section C. The offset is relative from the start of the file.             |
|       | 0x0068        | 4                 | DWORD           | Length of section C.                                                                    |
|       | 0x006C        | 4                 | DWORD           | Offset to section D. The offset is relative from the start of the file.                 |
|       | 0x0070        | 4                 | DWORD           | The number of entries in section D.                                                     |
|       | 0x0074        | 4                 | DWORD           | Length of section D.                                                                    |
|       | 0x0078        | 8                 | ?               | Unknown                                                                                 |
|       | 0x0080        | 8                 | FILETIME        | Latest execution time (or run time) of executable (FILETIME)                            |
|       | <b>0x0088</b> | <b>7 x 8 = 56</b> | <b>FILETIME</b> | <b>Older (most recent) latest execution time (or run time) of executable (FILETIME)</b> |
|       | <b>0x00C0</b> | <b>16</b>         | <b>?</b>        | <b>Unknown</b>                                                                          |
|       | 0x00D0        | 4                 | DWORD           | Execution counter (or run count)                                                        |
|       | <b>0x00D4</b> | <b>4</b>          | <b>?</b>        | <b>Unknown</b>                                                                          |
|       | <b>0x00D8</b> | <b>4</b>          | <b>?</b>        | <b>Unknown</b>                                                                          |
|       | <b>0x00DC</b> | <b>88</b>         | <b>?</b>        | <b>Unknown</b>                                                                          |
|       |               |                   |                 |                                                                                         |

## Section A - File metrics array

#### File metrics entry record - version 17

The file metrics entry records – version 17 is 20 bytes in size and
consists of:

<table>
<thead>
<tr class="header">
<th><p>Field</p></th>
<th><p>Offset</p></th>
<th><p>Length</p></th>
<th><p>Type</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Start time in ms</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Duration in ms</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Filename string offset<br />
The offset is relative to the start of the filename string section
(section C)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Filename string number of characters without end-of-string
character</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Unknown, flags?</p></td>
</tr>
</tbody>
</table>

#### File metrics entry record - version 23

The file metrics entry records – version 23 is 32 bytes in size and
consists of:

<table>
<thead>
<tr class="header">
<th><p>Field</p></th>
<th><p>Offset</p></th>
<th><p>Length</p></th>
<th><p>Type</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Start time in ms</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Duration in ms</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Average duration in ms?</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Filename string offset<br />
The offset is relative to the start of the filename string section
(section C)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Filename string number of characters without end-of-string
character</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>20</p></td>
<td><p>4</p></td>
<td><p>DWORD</p></td>
<td><p>Unknown, flags?</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>24</p></td>
<td><p>8</p></td>
<td></td>
<td><p>NTFS file reference<br />
0 if not set.</p></td>
</tr>
</tbody>
</table>

#### File metrics entry record - version 26

The file metrics entry record – version 26 appears to be similar to file
metrics entry record – version 23.

## Section B - Trace chains array

This section contains an array with 12 byte (version 17, 23 and 26)
entry records.

<table>
<thead>
<tr class="header">
<th><p>Field</p></th>
<th><p>Offset</p></th>
<th><p>Length</p></th>
<th><p>Type</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>0</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Next array entry index<br />
Contains the next trace chain array entry index in the chain, where the
first entry index starts with 0, or -1 (0xffffffff) for the
end-of-chain.</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>4</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Total block load count<br />
Number of blocks loaded (or fetched)<br />
The block size 512k (512 x 1024) bytes</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>8</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Unknown</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>9</p></td>
<td><p>1</p></td>
<td></td>
<td><p>Sample duration in ms?</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>10</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Unknown</p></td>
</tr>
</tbody>
</table>

## Section C - Filename strings

This section contains filenames strings, it consists of an array of
UTF-16 little-endian formatted strings with end-of-string characters
(U+0000).

At the end of the section there seems to be alignment padding that can
contain remnant values.

## Section D - Volumes information (block)

Section D contains one or more subsections, each subsection refers to
directories on a volume.

If all the executables and libraries referenced in the C section are
from one single disk volume, there will be only one section in the D
section. If multiple volumes are referenced by section C, section D will
contain multiple sections. (A simple way to force this situation is to
copy, say, NOTEPAD.EXE to a USB drive, and start it from that volume.
The corresponding prefetch file will have one D header referring to,
e.g. \DEVICE\HARDDISK1\DP(1)0-0+4 (the USB drive), and one to, e.g.
\DEVICE\HARDDISKVOLUME1\\ (where the .DLLs and other support files were
found).

In this section, all offsets are assumed to be counted from the start of
the D section.

### Volume information

The structure of the volume information is version dependent.

#### Volume information - version 17

The volume information – version 17 is 40 bytes in size and consists of:

| Field | Offset  | Length | Type     | Notes                                                                         |
|-------|---------|--------|----------|-------------------------------------------------------------------------------|
| VI1   | +0x0000 | 4      | DWORD    | Offset to volume device path (Unicode, terminated by U+0000)                  |
| VI2   | +0x0004 | 4      | DWORD    | Length of volume device path (nr of characters, including terminating U+0000) |
| VI3   | +0x0008 | 8      | FILETIME | Volume creation time.                                                         |
| VI4   | +0x0010 | 4      | DWORD    | Volume serial number of volume indicated by volume string                     |
| VI5   | +0x0014 | 4      | DWORD    | Offset to sub section E                                                       |
| VI6   | +0x0018 | 4      | DWORD    | Length of sub section E (in bytes)                                            |
| VI7   | +0x001C | 4      | DWORD    | Offset to sub section F                                                       |
| VI8   | +0x0020 | 4      | DWORD    | Number of strings in sub section F                                            |
| VI9   | +0x0024 | 4      | ?        | Unknown                                                                       |
|       |         |        |          |                                                                               |

#### Volume information - version 23

The volume information entry – version 23 is 104 bytes in size and
consists of:

| Field       | Offset         | Length    | Type     | Notes                                                                         |
|-------------|----------------|-----------|----------|-------------------------------------------------------------------------------|
| VI1         | +0x0000        | 4         | DWORD    | Offset to volume device path (Unicode, terminated by U+0000)                  |
| VI2         | +0x0004        | 4         | DWORD    | Length of volume device path (nr of characters, including terminating U+0000) |
| VI3         | +0x0008        | 8         | FILETIME | Volume creation time.                                                         |
| VI4         | +0x0010        | 4         | DWORD    | Volume serial number of volume indicated by volume string                     |
| VI5         | +0x0014        | 4         | DWORD    | Offset to sub section E                                                       |
| VI6         | +0x0018        | 4         | DWORD    | Length of sub section E (in bytes)                                            |
| VI7         | +0x001C        | 4         | DWORD    | Offset to sub section F                                                       |
| VI8         | +0x0020        | 4         | DWORD    | Number of strings in sub section F                                            |
| VI9         | +0x0024        | 4         | ?        | Unknown                                                                       |
| <b>VI10</b> | <b>+0x0028</b> | <b>28</b> | <b>?</b> | <b>Unknown</b>                                                                |
| <b>VI11</b> | <b>+0x0044</b> | <b>4</b>  | <b>?</b> | <b>Unknown</b>                                                                |
| <b>VI12</b> | <b>+0x0048</b> | <b>28</b> | <b>?</b> | <b>Unknown</b>                                                                |
| <b>VI13</b> | <b>+0x0064</b> | <b>4</b>  | <b>?</b> | <b>Unknown</b>                                                                |
|             |                |           |          |                                                                               |

#### Volume information - version 26

The volume information entry – version 26 appears to be similar to
volume information – version 23.

### Sub section E - NTFS file references

This sub section can contain NTFS file references.

For more information see [Windows Prefetch File (PF)
format](https://github.com/libyal/libscca/blob/master/documentation/Windows%20Prefetch%20File%20(PF)%20format.asciidoc).

### Sub section F - Directory strings

This sub sections contains directory strings. The number of strings is
stored in the volume information.

A directory string is stored in the following structure:

| Field | Offset | Length | Type  | Notes                                                                                                           |
|-------|--------|--------|-------|-----------------------------------------------------------------------------------------------------------------|
|       | 0x0000 | 2      | DWORD | Number of characters (WORDs) of the directory name. The value does not include the end-of-string character.     |
|       | 0x0002 |        | USTR  | The directory name as a Unicode (UTF-16 litte-endian string) terminated by an end-of-string character (U+0000). |
|       |        |        |       |                                                                                                                 |

In version 26 and 30 data trailing the directory strings section has
been seen. It is currently assumed that this is unused remnant data.

## See Also

- [Prefetch](Prefetch "wikilink")
- For tools see: [Prefetch#Tools](Prefetch#Tools "wikilink")

## External Links

- [Windows Prefetch File (PF)
  format](https://github.com/libyal/libscca/blob/master/documentation/Windows%20Prefetch%20File%20(PF)%20format.asciidoc),
  by the [libssca project](libssca "wikilink")

[Category:File Formats](Category:File_Formats "wikilink")