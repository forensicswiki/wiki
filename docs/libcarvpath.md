---
tags:
  -  File Analysis 
  -  Data Recovery
  -  Tools
  -  Opensource Software
---
LibCarvPath is a library designed to be used by carving and file system
analysis tools. LibCarvPath allows fragments represented by offset and
size to be combined in a [CarvPath
annotation](carvpath_annotation.md) that take the form of file
system paths. LibCarvPath addresses the limits of file system paths by
mapping extremely fragmented files to a uniquely identifying key in a
long-path database.

The following tools use LibCarvPath and/or CarvPath Annotations:

- [CarvFs](carvfs.md)
- [tsk-cp](tsk-cp.md)
- [scalpelcp](scalpelcp.md)
- Modules for the [Open Computer Forensics
  Architecture](open_computer_forensics_architecture.md) that
  use the [OCFA treegraph API](ocfa_treegraph_api.md).

Next to these, in [Photorec](photorec.md) work has started to
include LibCarvPath support.

## External Links

- [Project site](https://github.com/DNPA/libcarvpath)