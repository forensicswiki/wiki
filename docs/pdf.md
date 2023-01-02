---
tags:
  -  File Formats
---
The **Portable Document Format** (**PDF**) is a document format from
[Adobe](adobe.md) Inc. It is widely available on the web.
Originally developed as a propriety format, version 1.7 was released as
an open standard in 2008. The standard is published as ISO/IEC
32000-1:2008. Although an open standard, Adobe still owns patents and
copyrights related to the PDF standard. Adobe has granted a worldwide
royalty-free license to produce PDF software, but only if the software
complies with the PDF standard.

## Format

It is a common misconception that PDF files are simply a collection of
images, one per page. Certainly a PDF can be formed that way (which is
typical of document scanners), but in reality the document structure is
much more complex. A PDF file can contain text streams (which cam be
encoded and/or compressed in dozens of ways), vector and raster images,
fonts, and various interactive elements. A PDF file comprises sections
called "objects." Each object is numbered and can represent a page, a
font, a data stream, etc. Each file begins with the string `%PDF`. Each
file ends with the letters `%%EOF`, but there can be multiple `EOF`'s in
a single file (this often confuses programs like
[foremost](foremost.md).

Adobe's Acrobat software supports "incremental updates." The standard
allows this so that modifications can simply be appended to the file,
leaving the original data intact. Any new or altered object is simply
appended to the end of the original file. Deleted objects are left
intact and simply marked deleted. This can potentially cause inadvertent
disclosure of sensitive information.

## Metadata

PDF metadata can be stored in a document information dictionary or as a
metadata stream, sometimes both. A metadata stream can describe the
entire document or an individual component of a document. Thus, multiple
metadata streams may exist in a single document, making it difficult to
find all of it. Metadata streams are stored in Adobe's XML based XMP
(Extensible Metadata Platform) format. Even if a PDF document is
encrypted, the accompanying metadata is not required to be, and often is
not, encrypted.

The metadata (or parts of it) can be extracted with
[pdfinfo](pdfinfo.md), a utility which is part of the
[xpdf](xpdf.md) package.

## Embedded Objects

The PDF standard supports embedding many types of files such as images.
Embedded files may contain their own metadata. You can use
[pdfimages](pdfimages.md), part of the [xpdf](xpdf.md),
to extract all of the images out of a PDF file and put each in its own
file.

## Subformats

Several related standards exist that contain subsets or supersets of the
PDF standard features. These standards include

- PDF/A a simpler set of features for archiving documents, allowing for
  long-term reproducibility. Some scanning software saves documents in
  PDF/A by default.
- PDF/X for graphic arts.
- PDF/UA for universal accessibility.
- PDF/E for engineering drawings.

## PDF Software

Due to the popularity of the PDF format, there is much software
available for viewing and creating PDF documents. However, Adobe
maintains a de facto monopoly on software capable of editing PDF
documents. There are quite a few tools that merge or split pdf
documents, but few that can make meaningful edits. Software such as
OpenOffice.org and Inkscape can import PDF files into their native
formats, where the documents can be edited and then exported back to
PDF. Unfortunately, this option can be quite cumbersome.

### PDF Tools

These tools are useful for analyzing PDF files:

Belkasoft Evidence Center
<http://belkasoft.com/ec>

A powerful digital forensic product by
[Belkasoft](belkasoft.md), in particular allowing for searching
and carving documents, including PDF files. The product can show PDF
preview, plain text, metadata and extract embedded objects (including
batch extraction from all found PDF files).

<!-- -->

JEB2 PDF Analysis Plugin
<https://www.pnfsoftware.com/jeb2/pdfplugin>

Module for commercial versions of PNF Software's JEB2. Robust stream
extraction, decoding, tree/table visualizations, etc. The official
client offers interactive capabilities (such as navigating xrefs).
Strong parsing for malicious files. Reports notifications on
malformations and anomalies. API can also be used for tool/scanner
integration.

<!-- -->

Origami
<http://security-labs.org/origami/>

A powerful open source framework and GUI written in Ruby. It allows for
parsing and exploring pdf files and graphically browsing its contents.

<!-- -->

PDF Tools
<http://blog.didierstevens.com/programs/pdf-tools/>

Didier Stevens'
[pdf-parse](http://blog.didierstevens.com/2008/10/30/pdf-parserpy/) and
pdfid, written in Python

<!-- -->

PDF Stream Dumper
<http://sandsprite.com/blogs/index.php?uid=7&pid=57>

Free tool for the analysis of malicious PDF documents by David Zimmer.
([GitHub](https://github.com/dzzie/pdfstreamdumper))

<!-- -->

pdfresurrect
<http://www.757labs.com/projects/pdfresurrect/#downloads>

Retrieves previous versions of PDF files that have changes appended with
"incremental updates"

<!-- -->

PDFMiner
<http://www.unixuser.org/~euske/python/pdfminer/index.html>

"Python PDF parser and analyzer"

Includes **pdf2txt.py** command-line tool for extracting text from PDF
files, and **dumppdf.py** for dumping PDF objects.

<!-- -->

pyPdf
<http://pybrary.net/pyPdf/>

"A Pure-Python library built as a PDF toolkit."

Will encrypt and decrypt PDF files.

<!-- -->

QPDF
<https://sourceforge.net/projects/qpdf/>

Open source, cross-platform library and set of programs to inspect and
manipulate PDF files. Packaged in recent Debian based distributions.

These tools are useful for manipulating and generating PDF files:

ReportLab Open Source PDF Library
<http://www.reportlab.com/software/opensource/>

"our proven, industry-strength PDF generating software. Programmatically
create any kind of PDF document"

# See Also

- [Arabic PDFs](arabic_pdfs.md)
- [Document Metadata Extraction](document_metadata_extraction.md)

## External Links

- [Adobe PDF
  Reference](http://partners.adobe.com/public/developer/pdf/index_reference.html)
- [Wikipedia: PDF](http://en.wikipedia.org/wiki/PDF)
- [Portable Document Format: An Introduction for
  Programmers](http://www.mactech.com/articles/mactech/Vol.15/15.09/PDFIntro/),
  MacTech Magazine, Volume 15, (1999), Issue 9
- [ISO
  Standard](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=51502)
- [Patent
  Licenses](http://partners.adobe.com/public/developer/support/topic_legal_notices.html)
- [Quickpost: About the Physical and Logical Structure of PDF
  Files](http://blog.didierstevens.com/2008/04/09/quickpost-about-the-physical-and-logical-structure-of-pdf-files/),
  by Didier Stevens, April 9, 2008

