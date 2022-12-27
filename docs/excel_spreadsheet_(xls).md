---
tags:
  - File Formats
---
The **Excel Spreadsheet (XLS) file format** has the **.xls** extension. This
file type originates from Microsoft Excel. However, other spreadsheet software
can be used to display these files as well. These include:

* OpenOffice
* WordPerfect

The XLS file format should not be confused with [XLSX](excel_spreadsheet_(xlsx).md)
and [XSLB](excel_spreadsheet_(xlsb).md).

## MIME types

The following MIME types apply to this [file format](file_formats.md):

* application/msexcel
* application/xls

## File signature

Microsoft Excel spreadsheets of version 97-2003 use the
[OLE Compound File](ole_compound_file.md) (OLECF). These files therefore have
the OLECF file signature.

The object stream of the OLECF containing a Excel spreadsheet contains
the string "..." with some version.

## Excel 97-2003 spreadsheets

The Excel 97-2007 Binary File format is stored in the OLECF using
multiple streams:

* Workbook stream

## Encryption

See [Word Document (doc)](word_document_(doc).md). Note: perhaps
this section should be moved to a separate section about Microsoft
Office encryption

## See Also

## External Links

* [Excel 97-2007 Binary File format by Microsoft](https://download.microsoft.com/download/5/0/1/501ED102-E53F-4CE0-AA6B-B0F93629DDC6/Office/Excel97-2007BinaryFileFormat(xls)Specification.pdf)
* [Excel 2007 Binary File format by Microsoft](http://download.microsoft.com/download/0/B/E/0BE8BDD7-E5E8-422A-ABFD-4342ED7AD886/Excel2007BinaryFileFormat(xlsb)Specification.pdf)
