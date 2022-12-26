---
tags:
  - No Category
---
MattockFS is a computer forensics actor-framework component, computer
forensic data-repository and message-bus implemented as
[Fuse](https://en.wikipedia.org/wiki/Filesystem_in_Userspace) based user
space file system. It is based partially on [CarvFs](carvfs.md)
and the AnyCast-relay from the [Open Computer Forensics Architecture](open_computer_forensics_architecture.md).
MattockFS uses [CarvPath annotations](carvpath_annotations.md)
to designate frozen repository data in the same way that
[CarvFs](carvfs.md) does. MattockFS was designed to address some
of the shortcomings of OCFA in respect to disk-cache misses and access
control, and as such aims to become an essential foundational component
in future actor-model based computer forensic frameworks. MattockFS is
not a complete computer forensics framework, rather MattockFS provides
essential features that a computer forensics framework may build upon.

MattockFS provides the following facilities to future actor-model based
computer forensic frameworks:

- **Lab-side privilege-separation equivalent of [Sealed Digital Evidence
  Bags](sealed_digital_evidence_bags.md).** After creation,
  repository data is made immutable, thus guarding the integrity of the
  data from unintended write access by untrusted modules.
- **Trusted provenance logs.** Actors/workers roles in the processing of
  digital evidence chunks are logged to a provenance log, leaving no
  opportunity for untrusted modules to falsify or corrupt provenance
  logs.
- **CarvPath based access to frozen (immutable) data.** Multi-layer
  CarvPath based access in the same way as provided by
  [CarvFs](carvfs.md).
- **Domain specific actors oriented localhost message bus.** MattockFS
  provides sparse-capability based access to an Anycast message bus
  aimed specifically at use by a computer forensics framework and the
  concept of toolchains. This is basically the same functionality that
  used to be provided by the Anycast-Relay in the [Open Computer
  Forensics
  Architecture](open_computer_forensics_architecture.md).
- **CarvPath based opportunistic hashing.** MattockFS maps all low-level
  reads and writes to reads and writes on all active (either open files
  or or part of an active tool-chain) CarvPaths and will
  opportunisticaly calculate BLAKE2 hashes for these CarvPaths when
  possible.
- **Page-cache friendly archive interaction.** MattockFS keeps track of
  CarvPaths belonging to tool-chains that are not yet completely done.
  It will communicate with the kernel when a toolchain completes and as
  a result part of the archive should be considered to be no longer
  active (and thus can be flushed from page cache).
- **Actor Job picking policies**: MattockFS implements multiple job
  CarvPath based picking policies aimed either at opportunistic hashing
  or page-cache load optimized strategies.
- **Load balancing support**: MattockFS allows a special actor, a
  load-balancer, to steal jobs from other (overloaded) actors in order
  to redistribute the job to an other node in a multi-host setup.
- **Throttle information**: MattockFS provides the overlaying computer
  forensic framework with meta-data concerning potential page-cache load
  and per Actor queue size and volume. Based on this information, actors
  should throttle their new-data output in order to avoid spurious
  page-cache misses caused by to much active evidence data at a time.
- **Hooks for a distributed FIVES router**. In the [Open Computer
  Forensics
  Architecture](open_computer_forensics_architecture.md) a
  stateless router process was responsible for dynamic toolchain-path
  routing based on meta-data extracted from the evidence data. Later,
  the FIVES project created an alternative router
  process. This router carried state regarding the current location
  within a routing rule-list over to the next time the same data was
  processed by a router process. MattockFS provides a simple hook for
  use by an envisioned distributed version of FIVES-router like
  functionality.

MattockFS is not a complete forensic framework, it is a component that
can be used as foundation for a complete forensic framework. Currently
MattockFS is in beta. MattockFS comes with a Python API aimed at usage
by an overlaying computer forensics framework. Future API's for other
programming languages (C++ and others) are planned.

## External Links

- [Github page](https://github.com/pibara/MattockFS)
- [YouTube Presentation](https://www.youtube.com/watch?v=hJCqBLfEN7Y)
