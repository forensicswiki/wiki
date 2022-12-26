---
tags:
  -  File Formats
  -  Windows
  -  Database
---
[Microsoft Outlook](microsoft_outlook.md) uses the **Personal Folder File
(PFF)** to store e-mails, appointments, tasks, contacts, notes, etc.

Three different types of the PFF are known:

- The **Personal Address Book (PAB)**, which contains the address book
  of contacts. These files have the extension **.pab**.
- The **Personal Storage Table (PST)**, which contains items like
  e-mails, appointments, tasks, notes, etc. and is used as current and
  archived mailbox files. These files have the extension **.pst**. The
  PST format is also referred to as the **Personal Folder File (PFF)**
  format.
- The **Offline Storage Table (OST)**, which contains items like
  e-mails, appointments, tasks, notes, etc. and is used as off line
  mailbox files in conjunction with [Microsoft](microsoft.md)
  [Exchange](exchange.md). These files have the extension
  **.ost**. The OST format is also referred to as the **Offline Folder
  File (OFF)** format.

The underlying file format of these files is the same of which the
actual name is unknown but has been dubbed the **Personal Folder File
(PFF)** format, because of its most common usage.

## MIME types

The actual mime type of the PFF format is unspecified however some
sources claim the following [MIME types](mime_types.md) apply to
this [file format](file_format.md):

- application/vnd.ms-outlook (for PST files)

## File signature

PFF has the following file signature:

hexadecimal: 21 42 44 4e

ASCII: !BDN

## File types

There are a 32-bit and a 64-bit version of the PFF. These have the same
file signature but can be identified by the version in the file header.

## Contents

The PFF basically contains a hierarchy of items. The attributes of these items
are defined by the [Microsoft Outlook](microsoft_outlook.md) Message API (MAPI).

## Encryption

The PFF format allows the file to be encrypted. Two types of encryptions
are currently known these are referred to as compressible and high
encryption. The compressible encryption is a basic substitution cypher
and the high encryption is a little more complex substitution cypher.
From a cryptographic point of view this is more a way of obfuscation
than a means to protect confidentiality.

## PST

PST or Personal Storage File is an open proprietary file format which
stores email messages, contacts, calendar entries, tasks, and other
items belonging to Microsoft software like MS Exchange Client, Microsoft
Outlook, and Windows Messaging. The open file format is organized &
structured by Microsoft who provide free specifications and free stable
technology licensing.

PST file is a self-contained, stand-alone, structured binary file format
which represents a message store comprising an arbitrary hierarchy of
Folder objects holding Message objects holding attachment objects. The
file format can also be known as; Personal Folder File or, Personal
Address Book (.pab). When this file is functioning as a cache for
Microsoft Outlook's Cached Exchange Mode feature, it can also be
referred as; Off-line Storage Table (.ost), or Off-line Folder File.

### Overview

PST file format is primarily related to “Outlook” application and
comprises data of Outlook 97, 2000, 2003, or any higher version.
Microsoft Exchange server stores messages and other data items on
server. These items are stored locally on computer by MS Outlook
application as offline storage table (.ost file). When this offline data
is archived in Outlook application, messages are archived and stored as
PST file.

PST file utilizes a fixed-block-based scheme for allocating memory. The
file is enlarged by pre-defined sum of bytes and file preserves the
information internally regarding allocated and non-allocated blocks. So
when email messages are added to PST file, file size is adjusted
accordingly by Outlook application. When any message is removed or
deleted, file size remains unchanged marking space as unallocated where
future items will be saved. Thus it has become easier to recover deleted
data from PST files.

### Types of Format

PST file format is currently of two types; ANSI and Unicode. Unicode PST
is an advance format for PST and is available in Outlook 2003 and all
above versions. It has storage capacity of 20 GB in Outlook 2007 and
50GB in Outlook 2010 & 2013. Whereas ANSI PST is legacy format which has
2GB storage space limitation and is part of Outlook 2002 and below
versions.

### PST Logical Architecture

PST file architecture is structured in three layers: NDB, LTP, and
Messaging layer. The NDB (Node Database) layer comprises of database of
nodes denoting the lower-level objects for storage function. It endures
header, blocks, file allocation details, nodes, and BTrees (Node BTree &
Block BTree). The LTP (Lists, Tables, and Properties) layer comprises
higher-level notions comprises elements like Property Context
(collection of properties) and Table Context (two-dimensional table).
Messaging layer comprises of higher-level rules, it also connects the
elements of LTP and NDB to be construed as high-level objects; Message
objects, Folder objects, Attachment and Properties objects.

## Outlook Offline Storage Table (OST)

Offline Storage Folders (OST) is the data file of MS Outlook. It is the
replica of Exchange Server mailbox on local machine with .ost file
extension and is automatically created when a user profile is configured
with Exchange Server.

MAPI clients (like MS Outlook) can use OST file to store and access the
folder information without being connected to the Server. It can be
considered as snapshots of Server folders and this is the reason the OST
file is also known as Slave Replica of Server. This file is
automatically synced with the mailbox on server, provided there is
unflawed connectivity between the client and the server.

### Access Specification of OST File

An OST file can be accessed only through a MAPI profile that originally
created it. If the OST file is not authenticated through its original
profile, it will refuse to open. This happens because an OST file has an
encrypted cookie that is created from the unique ID of the mailbox.

This unique ID can be only accessed when connection to the Server is
made and this same encryption key gets saved into the registry settings
of the profile. Every time Outlook is started to access an OST file, the
encryption key at the server and the system registry is checked and if
it matches at both the ends, access to the OST file is granted.

The common reason why OST file cannot be opened in Outlook is using a
different profile to access the database. Also, deleting the mailbox or
changing its location on Server will also result in OST file
inaccessibility.

### Location of OST File on Windows OS

| Outlook Version   | Windows Version        | OST Location                                                                              |
|-------------------|------------------------|-------------------------------------------------------------------------------------------|
| Windows XP        | Outlook 2000/2003/2007 | C:\Documents and Settings\\%username%\Local Settings\Application Data\Microsoft\Outlook\\ |
| Windows Vista/7/8 | Outlook 2007           | C:\Users\\%username%\AppData\Local\Microsoft\Outlook\\                                    |
| Windows XP        | Outlook 2010           | C:\Documents and Settings\\%username%\My Documents\Outlook Files                          |
| Windows Vista/7/8 | Outlook 2010/2013      | C:\Users\\%username%\Documents\Outlook Files                                              |
|                   |                        |                                                                                           |

## Also see

- [libpff](libpff.md)
- [libpst](libpst.md)

## External Links

- [outlook.pst — format of MS Outlook .pst
  file](http://www.five-ten-sg.com/libpst/rn01re05.html), by the [libpst
  project](libpst.md)
- [Personal Folder File format
  specifications](https://googledrive.com/host/0B3fBvzttpiiScU9qcG5ScEZKZE0/Personal%20Folder%20File%20(PFF)%20format.pdf),
  by the [libpff project](libpff.md)
- [MAPI
  definitions](https://googledrive.com/host/0B3fBvzttpiiSRlR1QkU5Vk43ZWs/MAPI%20definitions.pdf),
  by the [libpff project](libpff.md)
- \[<http://msdn.microsoft.com/en-us/library/ff385210(v=office.12>).aspx
  MS-PST: Outlook Personal Folders (.pst) File Format\], by
  [Microsoft](microsoft.md)

### Tools

- [Aid4Mail](aid4mail.md)
- [libpff](libpff.md)
- [libpst](libpst.md)
- Microsoft Exchange Client
- Microsoft Outlook
- [Free OST File Viewer](http://datahelp.in/ost/viewer.html)
- [Free PST File Viewer](http://datahelp.in/pst/viewer.html)
- [Free PST Email Viewer](http://www.bitrecover.com/free/pst-viewer/)
- MVCOM
- [MailXaminer](mailxaminer.md)
- [Outlook PST Viewer](outlook_pst_viewer.md)
- [Pst file viewer](pst_file_viewer.md)
- PST Scanner
- Windows Messaging