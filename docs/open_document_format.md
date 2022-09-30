---
tags:
  -  File Formats
---
**Open Document Format** (ODF) is an open, XML-based file format
standard for word processing documents, spreadsheets, charts, and
presentations. The specification was originally developed by Sun
Microsystems, but has been standardized by the Organization for the
Advancement of Structured Information Standards (OASIS). ODF version 1.0
has been standardized as ISO/IEC 26300:2006. ODF is the primary format
for the OpenOffice.org office suite.

# File Extensions

The main file extensions for ODF documents are

- .odt for word processing documents
- .ods for spreadsheet documents
- .odp for presentation documents
- .odb for database documents
- .odg for graphical documents
- .odf for mathematical formulae

ODF also supports template files for each type of document. The 'd' in
file extension is replaced by a 't' for template files.

# File Structure

An ODF document can be as simple as a single XML file. However, this is
rarely practical. The standard specifies that an ODF file can also be
stored as a collection of several subdocuments. The latter is the most
common implementation.

A packaged ODF file will contain, at a minimum, six files and two
directories archived into a modified ZIP file. The structure of the
basic package is as follows

`|-- META-INF`
`` |   `-- manifest.xml ``
`|-- Thumbnails`
`` |   `-- thumbnail.png ``
`|-- content.xml`
`|-- meta.xml`
`|-- mimetype`
`|-- settings.xml`
`` `-- styles.xml ``

Again, this represents a minimal ODF file. The structure can become much
more complicated as directories can be added that contain embedded
images, macros, and the like.

An important caveat in the structure of the ZIP file is that the first
file must be the "mimetype" file and it must not be compressed.
[1](http://www.jejik.com/articles/2010/03/how_to_correctly_create_odf_documents_using_zip/)
The string "mimetype" should appear at position 30 and the actual MIME
type at position 38. This adaptation makes it possible for operating
systems to determine the MIME type of a file without relying on the file
extension.

## Main Sub-Files

The **manifest.xml** file contains a list of all files in the packages,
as well as their media type, path, and any information required for
decryption. The **content.xml** file contains the content of the
document (e.g., the text in a word processing document), while the
**styles.xml** file contains the information on how the content is to be
styled. The **settings.xml** file is self-explanatory.

## Metadata

Because ODF files are basically ZIP files, the files contain the same
meta-information about each file as that of a standard ZIP archive,
namely the name and size of each sub-file, compression information, and
creation date of each sub-file. In addition, much metadata is contained
within the xml files themselves. The **meta.xml** file contains metadata
for the entire document. The types of metadata contained in the file can
comprise pre-defined metadata, user defined metadata, as well as custom
metadata:

- which version of ODF is used by the document
- the document generator, that is, the user-agent software that
  generated or last modified the ODF document. This string is similar to
  the HTTP user agent string as described in RFC-2616. This can contains
  the name and version of the software as well as the name of the
  operating system.
- document title
- document description
- document subject
- keywords
- initial creator
- Creator (person who last modified the document)
- printed by
- creation date/time
- modification date/time
- print date/time
- document template, the path of the document template if one was used
  to generate the current document
- automatic reload
- hyperlink behavior
- language
- number of editing cycles stored as a string. The number is incremented
  each time the document is saved.
- editing duration -- amount of time spent editing the document. The
  specification is not clear as to how this value is to be calculated.
- document statistics -- this field varies by file type, but includes
  information such as page count, object count, paragraph count, cell
  count, etc.
- user-defined metadata -- allowable types: string, integer, float,
  boolean

Conforming applications are permitted to store non-standard fields in
this file, and the software should preserve any custom fields.

Not all metadata is stored in the meta.xml file. The content.xml file
can contain meta-information such as annotations and tracked changes, as
well as the creator and creation date time of those annotations or
tracked changes.

# External Links

[ODF
specification](http://docs.oasis-open.org/office/v1.1/OS/OpenDocument-v1.1-html/OpenDocument-v1.1.html)

