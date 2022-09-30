---
tags:
  - No Category
---
The OcfaLib API is a C++ API that is meant for usage by modules in the
[Open Computer Forensics
Architecture](open_computer_forensics_architecture.md). The C++
class ocfa::module::OcfaModule defines the base class of what all OCFA
modules are derived. Depending on the type of module, the ocfa::facade
namespace provides different convenient subclasses. The OcfaModule class
defines a virtual function named ProcessEvidence that the final module
class must implement. A typical module implementation implements a
subclass by implementing a constructor and a ProcessEvidence method. The
main function of the module program will create an instance of the
module class and call the run method on the object. The module will
connect and register itself to the OCFA Anycast Relay and thus be
connected into the Open Computer Forensics Architecture. For each piece
of evidence data the module receives, the ProcessEvidence method will
get invoked. The implementation of the ProcessEvidence method can
depending on the type of facade used as baseclass can:

- Gain read access to the input evidence data.
- Use its own private workdir for derived and temporary data
- Derive evidence from the input evidence.
- Access meta data created by other modules.
- Add additional metadata to the input evidence or child evidences.

For a simple example of a module that derives data from data look at the
tar module in OcfaModules/dissector/tar. For a simple example of a
module that extracts metadata from data look at the pgp module in
OcfaModule/extractor/pgp.

Next to simple OCFA modules, the ocfa::treegraph namespace provides an
aditional sub API for building treegraph loadable modules, that can be
used to create modules that map evidence data to a tree graph of data
and meta data.

The only API available currently is the C++ API. Work is currently being
done to also create a Java API and plans exist to build a Perl API to
OCFA in the future.

## See Also

- [Open Computer Forensics
  Architecture](open_computer_forensics_architecture.md)