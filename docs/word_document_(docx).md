---
tags:
  - File Formats
---
DOCX is the file format for Microsoft Office 2007 and later.

DOCX should not be confused with [DOC](doc.md), the format used
by earlier versions of Microsoft Office.

# Container Format

DOCX is written in an XML format, which consists of a [ZIP archive](zip.md)
file containing [XML](xml.md) and binaries. Content can be analysed without
modification by unzipping the file (e.g. in WinZIP) and analysing the contents
of the archive.

The file _rels/.rels contains information about the structure of the
document. It contains paths to the metadata information as well as the
main XML document that contains the content of the document itself.

Metadata information are usually stored in the folder docProps. Two or
more XML files are stored inside that folder, app.xml that stores
metadata information extracted from the Word application itself and
core.xml that stores metadata from the document itself, such as the
author name, last time it was printed, etc.

Another folder contains the actual content of the document, in a Word
document, or an .docx document the folder's name is word. A XML file
called document.xml is the main document, containing most of the content
of the document itself.

# Relationship to OOXML

Office Open XML is an open XML standard developed by Microsoft for word
processing documents, spreadsheets, presentations and charts. The OOXML
standard was submitted to the ISO for approval. After initially being
rejected over technical concerns, the ISO approved a modified version as
ISO/IEC 29500:2008. Microsoft intended to use the OOXML standard for its
Office suite. However, Office does not support the standard that the ISO
approved, it only supports the standard that was originally rejected by
the
ISO[1](http://arstechnica.com/microsoft/news/2010/04/iso-ooxml-convener-microsofts-format-heading-for-failure.ars).
As of Office 2010, Microsoft has still not brought its software into
compliance with the standard.

For most purposes OOXML may be considered a subset of DOCX (DOCX
contains additional features, like OLE serialization).

Documentation on OOXML may provide a guide to analysing a DOCX file.

# Metadata

## Content types

    [Content_Types].xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Types ns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="emf" ContentType="image/x-emf"/>
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
    <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
    <Override PartName="/word/stylesWithEffects.xml" ContentType="application/vnd.ms-word.stylesWithEffects+xml"/>
    <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
    <Override PartName="/word/webSettings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml"/>
    <Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
    <Override PartName="/word/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
    <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
    <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
    </Types>

## Relationships

    _rels/.rels

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Relationships ns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
    <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail" Target="docProps/thumbnail.emf"/>
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
    <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
    </Relationships>

Other relationship files:

    word/_rels/document.xml.rels

## Document properties - core

    docProps/core.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <cp:coreProperties
        xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:dcterms="http://purl.org/dc/terms/"
        xmlns:dcmitype="http://purl.org/dc/dcmitype/"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <dc:creator>User 1</dc:creator>
    <cp:lastModifiedBy>User 2</cp:lastModifiedBy>
    <cp:revision>3</cp:revision>
    <dcterms:created xsi:type="dcterms:W3CDTF">2012-11-07T23:29:00Z</dcterms:created>
    <dcterms:modified xsi:type="dcterms:W3CDTF">2013-08-25T22:18:00Z</dcterms:modified>
    </cp:coreProperties>

## Document properties - extended: application

    docProps/app.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Properties
        ns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
        xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
    <Template>Normal.dotm</Template>
        <TotalTime>1385</TotalTime>
        <Pages>1</Pages>
        <Words>2</Words>
        <Characters>13</Characters>
        <Application>Microsoft Office Word</Application>
        <DocSecurity>0</DocSecurity>
        <Lines>1</Lines>
        <Paragraphs>1</Paragraphs>
        <ScaleCrop>false</ScaleCrop>
        <HeadingPairs>
            <vt:vector size="2" baseType="variant">
                <vt:variant>
                    <vt:lpstr>Title</vt:lpstr>
                </vt:variant>
                <vt:variant>
                    <vt:i4>1</vt:i4>
                </vt:variant>
            </vt:vector>
        </HeadingPairs>
        <TitlesOfParts>
            <vt:vector size="1" baseType="lpstr">
                <vt:lpstr></vt:lpstr>
            </vt:vector>
        </TitlesOfParts>
        <Company></Company>
        <LinksUpToDate>false</LinksUpToDate>
        <CharactersWithSpaces>14</CharactersWithSpaces>
        <SharedDoc>false</SharedDoc>
        <HyperlinksChanged>false</HyperlinksChanged>
        <AppVersion>14.0000</AppVersion>
    </Properties>

# External Links

* [Introducing the Office (2007) Open XML File Formats](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2007/aa338205(v=office.12)),
  by [Microsoft](microsoft.md), May 2006
* [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/2012-06-14/)
* [The new XML Office Document Files: Implications For Forensics](https://simson.net/clips/academic/2009.IEEE.DOCX.pdf),
  [Simson L. Garfinkel](simson_l._garfinkel.md) and James Migletz
* [Office 2007 Metadata](https://www.sans.org/blog/office-2007-metadata/),
  by [Kristinn Gudjonsson](kristinn_gudjonsson.md), July 10, 2009
