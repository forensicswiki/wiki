---
tags:
  - No Category
---
The **Open Computer Forensics Architecture** (**OCFA**) is a modular
[computer forensics framework](computer_forensics_framework.md)
built by the [Dutch National Police Agency](klpd.md). The main
goal is to automate the digital forensic process to speed up the
investigation and give tactical [investigators](investigator.md)
direct access to the seized data through an easy to use search and
browse interface.

The architecture forms an environment where existing forensic
[tools](tools.md) and libraries can be easily plugged into the
architecture and can thus be made part of the recursive extraction of
data and [metadata](metadata.md) from digital evidence.

The Open Computer Forensics Architecture aims to be highly modular,
robust, fault tolerant, recursive and scalable in order to be usable in
large investigations that spawn numerous terabytes of evidence data and
covers hundreds of evidence items.

Modules in OCFA for reasons of fault tolerance are processes. The basic
[OcfaLib API](ocfalib_api.md) makes it possible and relatively
easy to build an OCFA module out of any data processing library or tool.
OCFA comes with numerous such modules that are mostly wrappers around
libraries like [libmagic](libmagic.md) or tools such as those
found in the [The Sleuth Kit](the_sleuth_kit.md).

The 2.2 version of OCFA (released April 2009) makes the previously
internal [OCFA treegraph API](ocfa_treegraph_api.md) available
for OCFA module development. The OCFA treegraph API allows more advanced
dissectors that produce data and meta-data for a treegraph
representation of an input file. The OCFA treegraph API also allows
dissectors that are programed to be [CarvFs](carvfs.md) aware to
use [zero storage carving](zero_storage_carving.md).

Communication between modules within OCFA is governed by a two layered
communication infrastructure as provided by OCFA. At the lowest layer is a
messaging system with at is center the OCFA AnyCast-relay. The Anycast Relay
provides the facilities of module crash resistance, distributed processing load
balancing and flow control. At a higher level of communication, the OCFA XML
Router provides for the routing of individual pieces of evidence through the
most appropriate tool chain for its particular type of content.

Although OCFA contains a rudimentary user interface, most of its power
is in the backend architecture. The last and final module in the tool
chain of any evidence will be the OCFA Data Store Module. This module
processes the evidence XML (that contains all of the evidence data its
meta data) and stores relevant parts into a postgesql database.
Extending the apache based user interface with interfaces for your own
case bound queries is something that should proof very useful in most
investigations.

Development and maintenance of OCFA by the Dutch National Police has
been discontinued in 2012. The latest version of the orphaned code is
available as the seperate github repositories
[ocfaLib](https://github.com/DNPA/OcfaLib) ,
[OcfaArch](https://github.com/DNPA/OcfaArch),
[OcfaJavaLib](https://github.com/DNPA/OcfaJavaLib),
[OcfaModules](https://github.com/DNPA/OcfaModules) and
[OcfaDocs](https://github.com/DNPA/OcfaDocs) on the Dutch National
Police [Github](https://github.com/DNPA) page.

## External Links

- [Project site](http://sourceforge.net/projects/ocfa/)
- [Linux Magazine article on
  OCFA](http://www.linux-magazine.com/Issues/2008/93/OCFA)
- [Open Computer Forensic Architecture a Way to Process Terabytes of
  Forensic Disk
  Images](https://www.researchgate.net/publication/226554617_Open_Computer_Forensic_Architecture_a_Way_to_Process_Terabytes_of_Forensic_Disk_Images)
