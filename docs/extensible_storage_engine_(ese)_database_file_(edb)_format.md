---
tags:
  - Database File Formats
  - File Formats
---
[Microsoft](microsoft.md) Exchange Server database uses
Extensible Storage Engine (ESE) which is designed for single
client-server architecture. The Exchange Server directly accesses the
data from ESE and the database here is stored in hierarchical storage
format which includes the messages, folders, attachments, message
properties etc. The data stored in each table may have varying property.
The Information Store and ESE collaboratively makes up client-server
based messaging service for small and large enterprises.

In many of its technologies like Access or FoxPro, Microsoft uses the
Joint Engine Technology (JET). There are two variants of JET engine: JET
Red and JET Blue. Microsoft Office applications like Access uses JET Red
that provides a standalone single user database. Since it was not
developed for a multi-user access and thus considering this limitation,
the JET Blue was developed that suited the multi-user requirement like
Exchange Server. From the time this technology is used in Exchange
server, it has evolved to large extent and is incomparable to its
original form. Microsoft renamed this JET technology as Extensible
Storage Engine (ESE).

## MIME types

The actual mime type of the ESDEB format is unspecified

## File signature

The ESEDB has the following file signature: hexadecimal: ef cd ab 89 (at
offset 4)

## File types

The ESEDB has the following file signature:

- hexadecimal: ef cd ab 89 (at offset 4)

ESEDB distinguishes between the following types:

- database (.edb, .sdb, ...)
- streaming file (.stm)

### Database (.edb)

The EDB file stores rich text data of Exchange Server and is known as
its proprietary store. MAPI, HTTPS, and SMTP messages are stored in the
EDB file with database arranged in B-Tree structure. The data gets saved
into 4 KB pages (or multiple of 4 depending upon version of Exchange
Server used) and these pages contain data, checksum, pointers, headers
etc.

### Streaming File (.stm)

The Streaming data file (STM) is introduced with Exchange 2000 Server.
This file stores the Internet MIME formatted content like video, images,
audio, or other multimedia. There are also multiple versions of the
ESEDB format. Basically the database that needs to be streamed is saved
here. This file format was provided by Microsoft in addition to EDB in
order to optimize the application performance for the type of database
it stores. STM is excluded from database structure after Exchange 2003
edition.

There are also multiple versions of the ESEDB format.

## Contents

The ESEDB basically is an ISAM database file format.

The ESEDB format is used by many Microsoft applications to store data
such as:

- Active Directory (NTDS)
- [Cortana](cortana.md)
- File Replication service (FRS)
- Windows Internet Name service (WINS)
- DHCP
- Security Configuration Engine (SCE)
- Certificate Server
- Terminal Services Session folder
- Terminal Services Licensing service
- Catalog database
- Help and Support Services
- Directory Synchronization service (MSDSS)
- Remote Storage (RSS)
- Phone Book service
- Single Instance Store (SIS) Groveler
- Windows NT Backup/Restore
- Exchange store
- Microsoft Exchange folder (SRS and DXA)
- Key Management service (KMS)
- Instant Messaging
- Windows (Vista) Mail
- [Content Indexing/Windows (Desktop) Search](windows_desktop_search.md)

## External Links

- [Extensible Storage Engine (ESE) Database File (EDB) format](https://github.com/libyal/libesedb/blob/master/documentation/Extensible%20Storage%20Engine%20(ESE)%20Database%20File%20(EDB)%20format.asciidoc),
  by the [libesedb project](libesedb.md)
- [Wikipedia on Extensible Storage Engine](https://en.wikipedia.org/wiki/Extensible_Storage_Engine)
- [Exchange .EDB File Extension](https://www.whatisfileextension.com/edb/)
- [Forensic examination of Windows Live Messenger 2009 Extensible Storage Engine](https://www.os3.nl/_media/2008-2009/students/willem_toorop/wlm2009_ese_fin.pdf),
  by Wouter van Dongen, Willem Toorop, Joeri Blokhuis, May 2009

### Tile Data Layer database

- [Management of Start Menu and Tiles on Windows 10 and Server 2016, part \#2](https://james-rankin.com/articles/management-of-start-menu-and-tiles-on-windows-10-and-server-2016-part-2/),
  by James Rankin, August 30, 2018

## Tools

- [EsEDbViewer](https://github.com/woanware)
- [ESE Database Viewer](http://www.systoolsgroup.com/ese-database-viewer/)
- [Free EDB Viewer](https://datahelp.in/edb/viewer.html)
- [libesedb](libesedb.md)
- [Logpresso Mini](https://github.com/logpresso/community)

Tools that are provided with the ESE engine:

- **eseutil** (comes with [Microsoft Exchange Server](microsoft_exchange_server.md) or **esentutl** (comes
  with a [Windows NT](windows.md) variant which has the ESE
  engine)

### Exchange

- [Exchange EDB Viewer](exchange_edb_viewer.md)
