---
tags:
  - No Category
---
CarvPath annotations are a simple string-wise depiction of a
hierarchically nested designation of sub entities within parent entities
in what basically is a flat address space. The annotations are used in
both [CarvFs](carvfs.md) and [MattockFS](MattockFS "wikilink")
as a way to allow for [Zero storage
carving](zero_storage_carving.md) by different computer forensic
tools. Next to zero-storage carving, the annotations can also be used in
regular file-system forensics. CarvPath annotations use the visual
appearance of file-system paths and as such can be used by the above
user-space file-systems. A CarvPath with a file extension designates
actual data in the underlying address space. Without a file extension,
the CarvPath designates a pseudo directory or nesting level.

![<File:carvpath.png>](carvpath.png "File:carvpath.png")

The basic structure of a CarvPath annotation is defined as follows:

- CARVPATH : \[CPTOKEN "/" \]\* CPTOKEN ".' <extension>
- CPTOKEN : \[CPCHUNK "_" \]\* CPCHUNK
- CPCGUNK : CPFRAGMENT \| CPSPARSE \| CPDIGEST
- CPFRAGMENT : <offset> + <size>
- CPSPARSE : "S" <size>
- CPDIGEST : "D" digest(CPTOKEN)

An example of a CarvPath :

- 132048+42949672960/Dca7cda1bd637a30b8f4f1344b9e984713b7ca06ce5da80b953e616c56cc6c64a/0+73728_S57344_98304+4096.dat