---
tags:
  -  File Formats
---
The [Kaspersky Anti-Virus](kaspersky_anti-virus.md) report files
are stored in a [propriety file format](file_formats.md).

The following information is based on the current understanding of the
Kaspersky Report File format.

## Overview

A Kaspersky Report File consists of:

- file header
- log record index
- array of log records

## File header

The file header is 80 bytes of size and consists of:

<table>
<thead>
<tr class="header">
<th><p>Offset</p></th>
<th><p>Size</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>"RPD2"</p></td>
<td><p>Signature</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>2</p></td>
<td><p>Unknown, version?</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown (empty values?)</p></td>
</tr>
<tr class="even">
<td><p>16</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown A<br />
Next available record number or 0?</p></td>
</tr>
<tr class="odd">
<td><p>20</p></td>
<td><p>4</p></td>
<td><p>0x1000</p></td>
<td><p>Unknown (record index size?)</p></td>
</tr>
<tr class="even">
<td><p>24</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (Record offset?)</p></td>
</tr>
<tr class="odd">
<td><p>28</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (empty value)</p></td>
</tr>
<tr class="even">
<td><p>32</p></td>
<td><p>4</p></td>
<td></td>
<td><p>File size</p></td>
</tr>
<tr class="odd">
<td><p>36</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (empty value)</p></td>
</tr>
<tr class="even">
<td><p>40</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown timestamp<br />
Creation time?</p></td>
</tr>
<tr class="odd">
<td><p>48</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown timestamp<br />
Last write time?</p></td>
</tr>
<tr class="even">
<td><p>56</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown timestamp<br />
Access time?</p></td>
</tr>
<tr class="odd">
<td><p>64</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown (empty values?)</p></td>
</tr>
<tr class="even">
<td><p>72</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Next available record number?</p></td>
</tr>
<tr class="odd">
<td><p>76</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (empty value)</p></td>
</tr>
</tbody>
</table>

## Log records index

### Log records index entry

The file header is 80 bytes of size and consists of:

<table>
<thead>
<tr class="header">
<th><p>Offset</p></th>
<th><p>Size</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Record offset<br />
The offset is relative to the start of the file</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (empty value)</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Record number</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Unknown (empty value)</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Log records

### Log record header

<table>
<thead>
<tr class="header">
<th><p>Offset</p></th>
<th><p>Size</p></th>
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Log record data size<br />
Log record size = Log record data size + 12</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Unknown timestamp<br />
Creation time?</p></td>
</tr>
<tr class="odd">
<td><p>12</p></td>
<td><p>...</p></td>
<td></td>
<td><p>Log record data</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Log record data

The record data contains some types, followed by the data. Currently it
is assumed that the record data format is (partially) dependent on the
subsystem, e.g. on-access scan (oas), that generated the log record
data.

## Date and time values

The date and time values are stored in intervals of 10 ns since January
1, 1 00:00:00 local time.

E.g. the timestamp: 0x582db22720fb9bc9

    import datetime

    print datetime.datetime(1, 1, 1) + datetime.timedelta(microseconds=0x582db22720fb9bc9 / 100)
    2014-06-25 15:01:44.164668

## See Also

- [Kaspersky Anti-Virus](kaspersky_anti-virus.md)
- [Kaspersky Quarantine File](kaspersky_quarantine_file.md)

