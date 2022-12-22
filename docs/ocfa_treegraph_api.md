---
tags:
  - No Category
---
The OCFA treegraph API is a more advanced API for the [Open Computer
Forensics
Architecture](open_computer_forensics_architecture.md). The
basic [OcfaLib API](ocfalib_api.md) allows for the fast and
simple creation of simple dissector and extractor modules for OCFA, but
has some limitations. To overcome these limitations, the 2.2 version of
OCFA re-vectored and promoted an API that was previously used internally
by th OCFA library to an API available to module builders. The OCFA
treegraph API defines an interface that a loadable library must
implement in order to be usable as an advanced dissector module bu the
Open Computer Forensics Architecture. Basically it defines an interface
'TreeGraphNode' that a treegraph module will need to derive one or many
classes from. A TreeGraphNode can contain data, meta-data and sub node's
that are also TreeGraphNode implementations. The data interface of the
TreeGraphNode also allows treegraph modules that are
[CarvFs](carvfs.md) aware, to return a carvpath as so called
soft linkable path'. Doing so allows OCFA to use substantially less
storage resources.

An example of a treegraph module for OCFA is included in the 2.2 release
of OCFA. This example is the OCFA mmls module. The ocfa mmls module
reproduces the functionality of the [The Sleuth Kit](the_sleuth_kit.md)
mmls tool. It does this using the OCFA treegraph library, the
[LibCarvPath](libcarvpath.md) library, and the
[The Sleuth Kit](the_sleuth_kit.md) library.
