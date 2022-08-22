LibCarvPath is a library designed to be used by carving and file system
analysis tools. LibCarvPath allows fragments represented by offset and
size to be combined in a [CarvPath
annotation](CarvPath_annotation "wikilink") that take the form of file
system paths. LibCarvPath addresses the limits of file system paths by
mapping extremely fragmented files to a uniquely identifying key in a
long-path database.

The following tools use LibCarvPath and/or CarvPath Annotations:

- [CarvFs](CarvFs "wikilink")
- [tsk-cp](tsk-cp "wikilink")
- [scalpelcp](scalpelcp "wikilink")
- Modules for the [Open Computer Forensics
  Architecture](Open_Computer_Forensics_Architecture "wikilink") that
  use the [OCFA treegraph API](OCFA_treegraph_API "wikilink").

Next to these, in [Photorec](Photorec "wikilink") work has started to
include LibCarvPath support.

## External Links

- [Project site](https://github.com/DNPA/libcarvpath)