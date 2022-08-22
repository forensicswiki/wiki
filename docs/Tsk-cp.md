Tsk-cp is a set of [LibCarvPath](LibCarvPath "wikilink") aware versions
of [Sleuthkit](Sleuthkit "wikilink") tools, that are for use together
with the normal versions of the other sleuthkit tools in the process of
doing [zero storage carving](zero_storage_carving "wikilink").

The tools are:

- mmls-cp : A CarvPath based version of mmls for listing a partitioned
  carvpath disk images as a list of partition carvpaths.
- dls-cp : A CarvPath based version of dls for listing all continuous
  unallocated fragments of a carvpath partition holding a filesystem as
  a list of unallocated block carvpaths.
- icat-cp : A CarvPath based version of icat that instead of copying out
  the data of an inode within a carvpath partition holding a filesystem
  as the carvpath of the file and the carvpath of the [file
  slack](file_slack "wikilink").

The carvpaths output by dls-cp can be used as the input of a CarvPath
aware carving tool.

## See Also

- [Open Computer Forensics
  Architecture](Open_Computer_Forensics_Architecture "wikilink")