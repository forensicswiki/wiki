---
tags:
  - File Formats
---
[Microsoft](microsoft.md) [Windows](windows.md) NT 4
(and later) uses the **Windows NT Registry File (REGF)** to store system
and application related data, e.g. configurations, most recently used
(MRU) files.

## MIME types

## File signature

REGF has the following file signature:

hexadecimal: 72 65 67 66

ASCII: regf

## File types

There are multiple types of REGF files:

* primary file (other names: normal file, data file)
* transaction log file
* external file
* backup file

Primary files, external files (created with the *RegSaveKey()* routine),
and backup files share exactly the same format.

## Transactional Registry (TxR)

In Vista the Transactional Registry (TxR) was introduced. TxR creates
transaction log files similar to:

* %FILE%{%GUID%}.TM.blf
* %FILE%{%GUID%}.TMContainer00000000000000000001.regtrans-ms
* %FILE%{%GUID%}.TMContainer00000000000000000002.regtrans-ms

Where %FILE% is the name of the REGF normal (data) file, e.g. NTUSER.DAT
and %GUID% a string representation of a GUID/UUID.

TxR is similar to [Transactional NTFS (txf)](ntfs.md) and uses
the [Common Log File System
(clfs)](common_log_file_system_(clfs).md).

## Contents

The REGF basically consists of a set of hive bins. These hive bins
contain cells that make up a hierarchy of keys and values.

### Artifacts

The on-disk format itself contains several artifacts:

* last written timestamp of a registry key;
* access bits of a registry key (starting from Windows 8 and Windows
  Server 2012);
* last written timestamp of a base block in a hive (before Windows 8.1
  and Windows Server 2012 R2);
* last reorganized timestamp (starting from Windows 8 and Windows Server
  2012).

## Also See

* [Windows Registry](windows_registry.md)
* [Windows 9x Registry File (creg)](windows_9x_registry_file_(creg).md)

## External Links

* [The Windows NT Registry File Format](http://www.sentinelchicken.com/research/registry_format/), by
  Timothy Morgan
* [Windows NT Registry File (REGF) format](https://github.com/libyal/libregf/blob/master/documentation/Windows%20NT%20Registry%20File%20(REGF)%20format.asciidoc),
  by the [libregf project](libregf.md)
* [Windows registry file format specification](https://github.com/msuhanov/regf/blob/master/Windows%20registry%20file%20format%20specification.md),
  by Maxim Suhanov, 2015-2016
