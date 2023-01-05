---
tags:
  -  File Formats
  -  XML
  -  Windows
---
Microsoft's .reg format for representing MS Registry entries has many
limitations, such as the inability to represent where registry
information physically resides on the disk and the difficulty in
representing Unicode. As a result, a variety of approaches have been
implemented. Currently DFXML uses the [RegXML](regxml.md)
standard to represent Registry entries.

## See Also

There are several open source programs that use XML to represent the
Windows Registry:

- [registryasxml](registryasxml.md) is a Windows GUI program
  that exports and imports section of the Windows Registry as
  XML-foramtted files.
- [RegXML](regxml.md) is also a Windows command-line utility
  that exports sections of the Windows Registry as XML-formatted files.
- [hivexml](hivexml.md) is a command-line utility that is part
  of Red Hat's [libguestfs](https://libguestfs.org/) that converts
  Registry hives to XML.
- [Tracking Computer Use with the Windows® Registry
  Dataset](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl),
  Doug White, NIST.
- [The complete set of code and and a WiReD XML difference set for
  steganographic
  applications](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl).

There is one commercial program that we have found:

- [ComponentSource](https://www.componentsource.com/product/componentspace-registry-toolkit-component/prices)
  has a \$195 .NET too that allows management, importing and exporting
  of the registry via XML.