---
tags:
  - Concept
---
Various terms widely used in connection to digital forensics.

## Acquisition and imaging

**Acquisition** is the act of lawfully obtaining digital evidence. It is a stage of the
*investigation*, see [concepts](concepts.md), and precedes the *examination* and *analysis*
of the evidence.

**Imaging** is the creation of a bit-by-bit copy of the storage medium, so that the copy can
be worked on without altering the original; see [disk imaging](disk_imaging.md) and
[memory imaging](memory_imaging.md).

## Analysis, Examination and Investigation

*Analysis*, *examination* and *investigation* all describe work performed on digital evidence.
They differ in scope, as described in the sections below; their usage throughout the wiki is
prescribed by the [style guide](https://github.com/forensicswiki/wiki/blob/main/style_guide.md).

### Analysis

*Analysis* is the most technical and granular of the three terms: processing specific
digital data to extract meaning from it. It is the default word for the sub-disciplines and
techniques of the field.

Analysis is also where tool quality matters most, [forensic tooling](forensic_tooling.md)
states that "an analysis or parsing tool must always yield the exact same output" for the same
input. At the same time, analysis can be fast and reactive, in [concepts](concepts.md) "Intrusion
analysis operates near "real-time"", while digital forensics is "a post-incident, deep-dive
methodology".

### Examination

*Examination* is the middle of the three terms: the stage of the investigation where the
evidence itself is inspected, between acquisition and reporting.

Note that the word is also used in ordinary English in ways that are not defined here, such
as a professional examination (e.g. a CFAP examination) or the cross-examination of a witness.
[Pillars of forensics](pillars_of_forensics.md) combines it with analysis as one stage of the
methodology, "Examination &amp; Analysis": "Sifting through system logs, registries, and
artifacts to reconstruct timelines and discover malicious activity".

Examination is also the most court-facing of the three terms:

* [Computer forensics](computer_forensics.md) lists what is key to all forensics
  examinations: maintaining integrity and authenticity, preventing contamination, proper
  and comprehensive documentation, and a systematic, scientific methodology.
* [Incident response](incident_response.md) wants scripts that "provide the examiner with
  a standard process to defend in court".

### Investigation

*Investigation* is the broadest of the three terms: it spans the case, from the question
and the evidence to the legally defensible answer. It is the subject of
[investigator](investigator.md).

* "evidence must remain entirely unaltered throughout the
  [investigation]" ([concepts](concepts.md)).
* [Traits of evidence](traits_of_evidence.md) separates "an intrusion assessment" from "a
  rigorous forensic investigation".
* [Incident response](incident_response.md) notes that "the fluid nature of computer
  investigations" makes the discipline "more of an art than a science".

### Overlap and differences

The words all name work done on digital evidence. Where the terms differ is scope, and they nest in
one another: an *investigation* contains one or more *examinations*, and an *examination* contains
many *analyses*.

* **analysis** - the data-level work: interpreting specific artifacts and tool output. The
  most technical and granular term.
* **examination** - the inspection of the evidence itself, forensically sound, documented
  and court-facing.
* **investigation** - the whole case: scoping, acquisition, examination, analysis and
  reporting, ending in a legally defensible answer.

## Analyst, Examiner and Investigator

*Analyst*, *examiner* and *investigator* all describe the people who perform that work on
digital evidence. Each role matches the scope of the work described in the sections above.

### Analyst

The *analyst* is the practitioner who analyzes digital data: someone who runs tools, performs
experiments and interprets the technical findings. The term is predominantly used in analytical and
technical articles.

*Analyst* is the preferred term for roles adjacent to digital forensics.

### Investigator

The *investigator* is the individual who owns the forensic investigation from start to
finish. The [investigator](investigator.md) article defines the role:

> A computer forensics investigator is the individual responsible for the practice of
> identifying, extracting and considering evidence from digital media, such as computer hard
> drives.

## Attacker and Malicious actor

An **"attacker"** acts as the technical, data-level equivalent of an *analyst*, representing the
specific entity orchestrating a discrete, highly tactical intrusion or exploit thread at the
micro-level. Typically used in the context of a concrete attack.

In contrast, a **"malicious actor"** is a broader, macro-level concept analogous to an
*investigator*; it encompasses the entire identity, strategic alignment, and overall narrative
footprint of the hostile entity behind the campaign, spanning multiple combined attacks, human
motivations, and systemic risks.

## Evidence, Fact, Findings and Traces

These terms form a chain from residue to legal proof: *traces* are what activity leaves
behind in digital media, a *finding* is the technical fact that *analysis* observes in
them, a *fact* is a finding that the work has verified, and *evidence* is the material
a court may admit.

A **trace** is a mark or residue left behind by an action or a presence. The principle
behind it is [Locard's exchange principle](locard's_exchange_principle.md); in the words
of its [Wikipedia entry](https://en.wikipedia.org/wiki/Locard%27s_exchange_principle):

> Every contact leaves a trace.

In digital media, traces are what [residual data](residual_data.md) is: data
"unintentionally left behind on computer media" - after deletion attempts, forgotten
copies, or decommissioned media - and, at the limit, [remnant data](remnant_data.md):
data still recoverable after new information has been written to it.
[Anti-forensic techniques](anti_forensic_techniques.md) target such traces: they aim to
"negatively affect the existence, amount and/or quality" of the evidence.

A **finding** is a technical fact observed during the work - a log entry, a registry
modification, an unallocated file fragment or a timeline correlation. It is what *analysis*
produces, but it is not legal proof. Per [traits of evidence](traits_of_evidence.md):

> A forensic **finding** is an empirical observation. It is a line in a firewall log, a
> Windows Registry key modification, an unallocated file fragment, or a timeline correlation
> discovered during an investigation. **It is a technical fact, but it is not inherently a
> legal proof.**

A **fact** is an established, verified state of affairs - a finding that the work has
confirmed. [computer forensics](computer_forensics.md) makes accuracy a professional
duty: "Present facts accurately", and "Not withhold any findings as such actions may
distort or misrepresent the facts". Per [ipse Dixit](ipse_dixit.md): the record must ensure
that "justice relies on verifiable facts rather than assumptions". In court, *evidence*
is tendered so that the *facts* of the case can be established from it.

**Evidence** (legal evidence) is a finding that has been made admissible: collected legally,
authentic, unaltered, reliable and complete, so that it can be tendered as an exhibit in a
court of law. Per [digital evidence](digital_evidence.md):

> Digital evidence is the collective term used to describe information or materials stored or
> transmitted in digital form that is to be tendered as an exhibit in a context of law, such
> as court.

A finding and legal evidence do not coincide automatically - "those findings do not
automatically qualify as evidence in a court of law" ([traits of
evidence](traits_of_evidence.md)). The traits a finding must exhibit to cross that
threshold - admissibility, authenticity, integrity, reliability and completeness - are
listed there. Per [RFC 3227](https://www.ietf.org/rfc/rfc3227.txt), evidence collected
correctly "stands a much greater chance of being admissible in the event of a
prosecution".

### Examiner

The *examiner* performs the forensic *examination* of the evidence: the technical stage
between acquisition and reporting where the "Examination &amp; Analysis" work happens.
The duties listed in [computer forensics](computer_forensics.md) apply to "All professionals
involved in a forensics examination".

*Examiner* is also part of professional titles and organizations.

### Forensicator

The *forensicator* is informal jargon for [a forensic investigator](investigator.md):

> The vernacular of digital or computer *forensics investigator* is *forensicator*.

### Overlap and differences

Where the terms differ is mostly scope and context:

* **investigator** - owns the whole investigation: scoping, acquisition, reporting and the
  legal narrative. The broadest term in this wiki; also used for the field officer:
  "law enforcement investigators in the field".
* **examiner** - performs the *examination* of the evidence, i.e. the lab/technical stage.
  Associated with credentials (EnCE) and trade bodies (ISFCE).
* **analyst** - analyzes and interprets data and tool output. The most technical of the
  three, and the term of choice for roles adjacent to forensics (incident response,
  malware, memory forensics).

## Artifact

The term artifact (or artefact) is widely used within computer forensics, though there is no
official definition of this term.

The definition closest to the meaning of the word within computer forensics is that of the word
artifact within [archaeology](https://en.wikipedia.org/wiki/Artifact_(archaeology)). The term
should not be confused with the word artifact used within
[software development](https://en.wikipedia.org/wiki/Artifact_(software_development)).

If archaeology defines an artifact as:

> something made or given shape by man, such as a tool or a work of art, esp an object of
> archaeological interest

The definition of artifact within computer forensics could be:

> An object of digital archaeological interest.

Where digital archaeological roughly refers to computer forensics without the forensic (legal)
context.

## Binary, Executable, Object File and Source Code

These terms trace the lifecycle of a software program from human-readable text to
machine-executable code. In reverse engineering and malware analysis, these distinctions help
examiners identify the compilation state and structural readiness of a file.

A **binary** is a broad term with two meanings. Generally, a binary file is any file that contains
data not formatted as plain text, such as an image, an encrypted log, or a database. Informally in
digital forensics, "a binary" is often used as a catch-all noun for any compiled piece of code,
including executables and shared libraries (`.dll` or `.so`), to contrast them against plaintext
source code.

An **executable** (or executable file) is a complete, fully linked program that an operating system
can load and run, such as an `.exe` file in Windows or an ELF file in Linux. A linker combines one
or more object files and system libraries, resolving all memory addresses and establishing a clear
execution entry point.

An **object file** is an intermediate product of the compilation process (typically with a `.o` or
`.obj` extension). A compiler translates source code into machine language for a specific
architecture, creating an object file. While it contains machine instructions, it cannot be run on
its own because references to external functions, variables, or libraries have not yet been
resolved.

A **source code** file contains human-readable programming instructions written in a high-level
language, such as C, C++, or Go. It cannot be directly processed by a computer's Central
Processing Unit (CPU) and serves as the blueprint before compilation.

### Overlap and differences

Where these terms differ is their level of compilation, structural readiness, and context:

* **binary** - The data-level format (non-text); colloquially used to describe any compiled
  artifact encountered during an investigation.
* **executable** - Machine-readable and complete; a fully functional program ready to be executed
  by an operating system.
* **object file** - Machine-readable but incomplete; isolated fragments of compiled code requiring
  linking.
* **source code** - Human-readable text; the uncompiled design logic.

## Code points and characters

* A **code unit** is the smallest chunk of bit data, such as an 8-bit byte for UTF-8 or a 16-bit word
  for UTF-16, that an encoding uses to represent text.
* A **code point** is a specific numerical value assigned to an abstract symbol by a character set
  standard, such as Unicode. When written to a storage medium via an encoding like UTF-16, it is
  mapped into one or more code units (e.g. a surrogate pair), acting as a data-level artifact or trace.
* A **character** is the abstract unit of textual information that humans actually perceive. A
  character represents the interpreted, run-time (or "real-world") information reconstructed from
  those underlying data structures.

## Digital forensics and computer forensics

Both names are used in the field and in this wiki for the same discipline. This wiki
canonicalizes [computer forensics](computer_forensics.md);
[digital forensics](digital_forensics.md) is a redirect to it.

[Computer forensics](computer_forensics.md) is also distinguished from the more generic term
*forensic computing*, which covers the analysis and study of all types of digital media and
materials, of a computing or telecommunication nature. In a strict sense, computer forensics
applies specifically to the evaluation of computers and their data storage or data processing
devices.

## Forensically sound

Per [when is digital evidence forensically sound?](https://link.springer.com/content/pdf/10.1007/978-0-387-84927-0_1.pdf):

> The application of a transparent digital forensic process that preserves the original meaning of
> the data for production in a court of law.

## Method and Technique

*Method* (or methodology) and *technique* describe how forensic tasks are structured and executed.
They differ in abstraction, rigidity, and their relationship to legal admissibility.

### Method

A *method* is the overarching, structured framework or standard operating procedure that guides the
lifecycle of an investigation. It defines the strategic "how" to ensure that the entire process is
repeatable, transparent, and legally defensible.

Methods are generally rigid and scale across the entire macro-level workflow. They rely on
validated, standardized models, such as the NIST Digital Forensics Process or ISO/IEC 27037, to
govern the sequence of acquisition, examination, analysis, and reporting. The primary objective of
a method is to preserve the integrity of the evidence and maintain a flawless chain of custody.

### Technique

A *technique* (specifically an *analysis technique*) is a discrete, highly tactical technical
action or mechanism deployed to extract, parse, or interpret data from a specific digital artifact.

Techniques operate at the micro-level and are highly flexible; practitioners select them
dynamically based on the target operating system, hardware, or file types. Examples of techniques
include file carving, reverse steganography, live memory extraction, and registry timeline
correlation. A technique is executed *within* the boundaries prescribed by the broader forensic
method.

### Overlap and differences

While both terms dictate how work is performed on a case, they exist at different tiers of
execution. A *method* establishes the global rules of engagement to keep the investigation
forensically sound, whereas a *technique* is the practical technical utility used to solve a
data-level puzzle.

* **method** - the strategic framework; a standardized, phased process designed to withstand legal
  scrutiny and prevent data contamination.
* **technique** - the tactical action; the specific tool-driven or manual mechanism used to examine
  and decode abstract digital traces.

## See Also

* [Anti-forensic techniques](anti_forensic_techniques.md)
* [Computer forensics](computer_forensics.md)
* [Concepts](concepts.md)
* [Digital evidence](digital_evidence.md)
* [Investigator](investigator.md)
* [Ipse Dixit](ipse_dixit.md)
* [Locard's exchange principle](locard's_exchange_principle.md)
* [Remnant data](remnant_data.md)
* [Residual data](residual_data.md)
* [Rethoric of proof](rethoric_of_proof.md)
* [Traits of evidence](traits_of_evidence.md)
