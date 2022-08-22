The **Word Document (DOC) file format** has the **.doc** extension. This
file type originates from [Microsoft Word](Microsoft_Word "wikilink").
However, other word processing software can be used to display these
files as well. These include:

- [WordPad](WordPad "wikilink")
- [WordPerfect](WordPerfect "wikilink")
- [OpenOffice](OpenOffice "wikilink")
- [AbiWord](AbiWord "wikilink")
- [LibreOffice](LibreOffice "wikilink")

The Word DOC file format should not be confused with
[DOCX](DOCX "wikilink").

## MIME types

The following [MIME types](MIME_types "wikilink") apply to this [file
format](file_format "wikilink"):

- application/msword
- application/doc
- appl/text
- application/vnd.msword
- application/vnd.ms-word
- application/winword
- application/word
- application/x-msw6
- application/x-msword
- zz-application/zz-winassoc-doc

## File signature

[Microsoft Word](Microsoft_Word "wikilink") documents of version 97-2003
use the [OLE Compound File](OLE_Compound_File "wikilink") (OLECF). These
files therefore have the OLECF file signature

The object stream of the OLECF containing a Word document contains the
string "Word.Document" with some version.

## Word 97-2003 documents

The Word Binary File format is stored in the OLECF using multiple
streams:

- WordDocument stream
- Table stream (0Table, 1Table)
- Data stream

## Encryption

Versions 97/2000 encrypt documents with a very weak algorithm. This
password scheme can be broken easily by several different products and
it is possible to decrypt the contents without discovering the password.
This is done by testing all 1,099,511,627,776 possible keys. Ultimate
Zip Cracker by VDGSoftware is one utility that can perform this
decryption.

## Extracting Strings

On a unix-like machine try this command to extract strings from a .doc
file:

`cat /tmp/test.doc | tr -d \\0 | strings | more`

(where /tmp/test.doc is the path to your .doc file)

Note that a Word 97 and later document can contain both extended ASCII
with codepage 1252 (codepage 1252 compressed text) and UTF-16
little-endian text. Word document can also contain 'East Asian' or
'Complex script' languages. Also the text stream contains information
about all the parts of the Word document (header/footer, foot/endnote,
annotation, etc.) Therefore using basic Unix string is very rough
approach of finding data in a Word document. Use the wvtools or more
sophisticated tools instead.

## External Links

- [Word 97-2007 Binary File Format by
  Microsoft](http://download.microsoft.com/download/0/B/E/0BE8BDD7-E5E8-422A-ABFD-4342ED7AD886/Word97-2007BinaryFileFormat(doc)Specification.pdf)

[Category:File Formats](Category:File_Formats "wikilink")