---
tags:
  - No Category
---
Digital evidence is the collective term used to describe information or
materials stored or transmitted in digital form that is to be tendered
as an exhibit in a court of law. The past few decades have seen an
explosion in the use of technology in all walks of life and industry.
From email to automated control systems for water supplies, information
systems and technology underpin our modern society. Perhaps
unsurprisingly, criminals have moved with the times, finding means by
which to leverage technology in the commission or support of offences.

The material in this article is heavily based on [RFC
3227](https://www.ietf.org/rfc/rfc3227.txt)

## Handling

Some principles of handling digital evidence:

- Custodianship; guaranteeing a chain of custody
- Documentation

<b>Avoid:</b>

- Unauthorized disclosure; Digital evidence is often sensitive also in
  certain cases it requires qualified persons to access digital evidence
- Misuse
- Alteration; Make sure no change of data while handling of the data,
  note that with very volatile data this often means after acquisition
  and due to failure of storage media this it is not always possible to
  guarantee.
- Destruction

### Collection

The methods used to collect evidence should be transparent and
reproducible. You should be prepared to reproduce precisely the methods
you used, and have those methods tested by independent experts.

#### Order of Volatility

When collecting evidence you should proceed from the volatile to the
less volatile. Here is an example order of volatility for a typical
system.

- registers, cache
- routing table, ARP cache, process table, kernel statistics, memory
- temporary file systems
- disk
- remote logging and monitoring data that is relevant to the system in
  question
- physical configuration, network topology
- archival media

### Chain of custody

You should be able to clearly describe how the evidence was found, how
it was handled and everything that happened to it.

The following need to be documented:

- Where, when, and by whom was the evidence discovered and collected.
- Where, when and by whom was the evidence handled or examined.
- Who had custody of the evidence, during what period. How was it
  stored.
- When the evidence changed custody, when and how did the transfer occur
  (include shipping numbers, etc.).

## Reconstruction

Types of reconstruction:

- Relational - how one finding is related to another: Correlation
- Functional - how one finding can be used/applied
- Temporal - events related to the timeline

## Evidentiary standards of proof

### Legal Considerations

Computer evidence needs to be:

- Admissible: It must conform to certain legal rules before it can be
  put before a court.
- Authentic: It must be possible to positively tie evidentiary material
  to the incident.
- Complete: It must tell the whole story and not just a particular
  perspective.
- Reliable: There must be nothing about how the evidence was collected
  and subsequently handled that casts doubt about its authenticity and
  veracity.
- Believable: It must be readily believable and understandable by a
  court.

## External Links

- [Principles of Evidence - Fifth
  edition](http://www.lexisnexis.com/supp/lawschool/study/texts/pdf/2011RevisedTM3562.pdf),
  by Irving Younger, Michael Goldsmith, David A. Sonenshein, 2011

### Hearsay

- [Wikipedia: Hearsay](https://en.wikipedia.org/wiki/Hearsay)

### Reasoning

- [Wikipedia: Thesis, antithesis,
  synthesis](https://en.wikipedia.org/wiki/Thesis,_antithesis,_synthesis)
- [Wikipedia: Reasoning - Logical reasoning methods and
  argumentation](https://en.wikipedia.org/wiki/Reasoning#Logical_reasoning_methods_and_argumentation)
- [Wikipedia: Deductive
  reasoning](https://en.wikipedia.org/wiki/Deductive_reasoning)
- [Wikipedia: Inductive
  reasoning](https://en.wikipedia.org/wiki/Inductive_reasoning)
- [Wikipedia: Five Ws](https://en.wikipedia.org/wiki/Five_Ws)

### Standards and best practices

- [IETF RFC 3227, Guidelines for evidence collection and
  archiving](https://www.ietf.org/rfc/rfc3227.txt), by The Internet
  Society, 2002
- [ACPO Good Practice Guide for Digital
  Evidence](http://www.acpo.police.uk/documents/crime/2011/201110-cba-digital-evidence-v5.pdf),
  by ACPO, 2012
- [ISO/IEC 27037:2012 - Information technology -- Security techniques --
  Guidelines for identification, collection, acquisition and
  preservation of digital
  evidence](https://www.iso.org/standard/44381.html), by
  International Organization for Standardization (ISO)
- [ISO/IEC DIS 27041 - Information technology -- Security techniques --
  Guidance on assuring suitability and adequacy of incident
  investigative
  methods](https://www.iso.org/standard/44405.html),
  by International Organization for Standardization (ISO)
- [ISO/IEC DIS 27042 - Information technology -- Security techniques --
  Guidelines for the analysis and interpretation of digital
  evidence](https://www.iso.org/standard/44406.html),
  by International Organization for Standardization (ISO)