---
tags:
  - Concept
  - Legal
---
Digital evidence is the collective term used to describe information or materials stored or
transmitted in digital form that is to be tendered as an exhibit in a context of law, such as
court. The past few decades have seen an explosion in the use of technology in all walks of life
and industry. From email to automated control systems for water supplies, information systems and
technology underpin our modern society. Perhaps unsurprisingly, criminals have moved with the
times, finding means by which to leverage technology in the commission or support of offences.

Note that this article is based on [RFC 3227](https://www.ietf.org/rfc/rfc3227.txt).

## Handling

Some principles of handling digital evidence:

* Custodianship; guaranteeing a [chain of custody](chain_of_custody.md)
* Documentation

**Avoid:**

* Unauthorized disclosure; Digital evidence is often sensitive also in certain cases it requires
  qualified persons to access digital evidence
* Misuse
* Alteration; Make sure no change of data while handling of the data, note that with very volatile
  data this often means after acquisition and due to failure of storage media this it is not always
  possible to guarantee.
* Destruction

### Collection

The methods used to collect evidence should be transparent and reproducible. You should be prepared
to reproduce precisely the methods you used, and have those methods tested by independent experts.

#### Order of Volatility

When collecting evidence you should proceed from the volatile to the less volatile. Here is an
example order of volatility for a typical system.

* CPU (or equivalent processing units) registers, cache
* routing table, ARP cache, process table, kernel statistics, memory
* temporary file systems
* disk
* remote logging and monitoring data that is relevant to the system in question
* physical configuration, network topology
* archival media

## Reconstruction

Types of reconstruction:

* Relational - how one finding is related to another: Correlation
* Functional - how one finding can be used/applied
* Temporal - events related to the timeline

## Evidentiary standards of proof

To be legally defensible in a court of law, computer evidence must satisfy
[traits of evidence](traits_of_evidence.md) by being admissible, authentic to the incident,
contextually complete, reliable in its forensic handling, and easily believable to a judge and/or
jury.

## See Also

* [Chain of custody](chain_of_custody.md)
* [Rethoric of proof](rethoric_of_proof.md)
* [Traits of evidence](traits_of_evidence.md)

## External Links

* [IETF RFC 3227, Guidelines for evidence collection and archiving](https://www.ietf.org/rfc/rfc3227.txt),
  by The Internet Society, 2002
* [ISO/IEC 27037:2012 - Information technology -- Security techniques -- Guidelines for
  identification, collection, acquisition and preservation of digital
  evidence](https://www.iso.org/standard/44381.html),
  by International Organization for Standardization (ISO)
* [ISO/IEC DIS 27041 - Information technology -- Security techniques -- Guidance on assuring
  suitability and adequacy of incident investigative
  methods](https://www.iso.org/standard/44405.html),
  by International Organization for Standardization (ISO)
* [ISO/IEC DIS 27042 - Information technology -- Security techniques -- Guidelines for the analysis
  and interpretation of digital evidence](https://www.iso.org/standard/44406.html),
  by International Organization for Standardization (ISO)
