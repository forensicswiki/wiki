---
tags:
  - Concept
---
Various concepts central to digital forensics.

## Legal & Procedural Concepts

* [Chain of custody](chain_of_custody.md)
* Data Integrity: evidence must remain entirely unaltered throughout the investigation. To uphold
  this, investigators typically work on a copy instead of the original device.
* Forensic Soundness: A standard or concept stating that tools and methods used during an
  investigation must be scientifically validated, reliable, and independently verifiable.
* [Ipse Dixit](ipse_dixit.md) or why "because the tool/vendor/expert/artificial intelligence said
  so" is not evidence.
* Hearsay, see: [Wikipedia: Hearsay](https://en.wikipedia.org/wiki/Hearsay)
* [Reproducibility](reproducibility.md)
* [Traits of evidence](traits_of_evidence.md)

## Investigation (or Analysis or Examination) Concepts

* [Digital evidence](digital_evidence.md)
* [(Digital) forensic tooling](forensic_tooling.md)
* [Observation errors](observation_errors.md)
* [Rhetoric of Proof](rethoric_of_proof.md)

## Storage & Data Concepts

* Allocated Space: Storage space currently reserved by the operating system for active files, e.g.
  your documents or photos.
* Host Protected Areas (HPA) and Device Configuration Overlays (DCO): These are hidden, reserved
  regions on hard drives or SSDs that sit outside the master boot record (MBR) or GUID partition
  table addresses. Standard operating systems and basic forensic imagers cannot see these zones.
  Investigators must use specialized hardware or write-blockers that issue direct ATA commands to
  unhide and image these areas, where data can easily be cached away from sight.
* Metadata: "data about data." This includes hidden file attributes like camera GPS coordinates on
  a photo, original authors of a document, or exact file creation and modification timestamps.
* Slack Space: The leftover, unused space at the end of a fixed data cluster. If a file is smaller
  than the space the computer allocates for it, fragments of old deleted data can often be found
  trapped in this "slack" space.
* Unallocated Space: "Empty" space on a hard drive. When you delete a file, the computer does not
  instantly erase it; it simply marks that file's location as unallocated (free to overwrite).

## Operational & Technical Concepts

* Forensic Imaging (Bit-by-Bit Copy): Unlike a standard file copy (like dragging a folder to a USB
  drive), a forensic image is a complete, mathematical clone of every single bit on a storage
  medium-including its deleted files, hidden partitions, and unallocated space.
* Write Blocking: A concept implemented via hardware or software that strictly prevents a computer
  from writing data to a piece of evidence. When a suspect's drive is plugged into a "write blocker",
  the investigator's computer can only read the data, ensuring the original device is completely
  untouched. See also: [write blockers](write_blockers.md).
* Hashing (Cryptographic Verification): A process that passes a file or drive image through an
  algorithm (like SHA-256) to generate a unique alphanumeric string. Think of it as a digital
  fingerprint. If even a single letter inside a file is altered, the hash value changes completely,
  alerting investigators that the evidence has been tampered with. See also: [hashing](hashing.md).
* [Order of Volatility](digital_evidence.md#order-of-volatility)

## Data recovery

* [Data recovery](data_recovery.md) - restoring data that was deleted, made inaccessible by damage
  to a file system, partition table or storage media, or that is on failing media; see also
  [Tools: Data Recovery](tools_data_recovery.md).
* [File carving](file_carving.md) - recovering files based on their content (headers, footers,
  internal structure) rather than on file system metadata.

## Analysis Concepts

* [Cell Site Analysis (CSA)](cell_site_analysis.md)

### Data Format Analysis

* [Non-rendering characters](non_rendering_characters.md), also referred to as non-printable
  characters.
* Polyglot Files: A polyglot is a single file that is structurally valid as two or more distinct
  file types simultaneously, such as a file that functions as both a valid JPG image and a valid ZIP
  archive depending on the interpreter used). If a forensic analysis tool relies strictly on a
  single header validation technique, it will catalog only one side of the polyglot, leaving a
  hidden archive or script fully functional yet unparsed.
* [Unpaired surrogates](unpaired_surrogates.md)

### Intrusion Analysis

Digital forensics and intrusion analysis overlap significantly in their shared reliance on
analyzing technical artifacts like system logs, memory captures, and network traffic to reconstruct
a threat actor's timeline.

They differ sharply in their primary objectives and operational contexts. Intrusion analysis
operates near "real-time", focusing on rapid threat detection, live containment, and determining
how a system was actively compromised to eradicate the adversary. In contrast to digital forensics,
which is typically a post-incident, deep-dive methodology that prioritizes strict chain-of-custody
documentation and absolute data preservation to ensure findings are legally defensible.

* Threat hunting, in the context of intrusion analysis, is the proactive, hypothesis-driven practice
  of searching through networks, endpoints, and datasets to detect malicious activity that has
  evaded existing security controls. Unlike traditional reactive analysis, which triggers only after
  an automated alert fires, hunting operates under the assumption that a breach has already occurred.

### Timeline Analysis

* [epoch](epoch.md)
* [MAC(B) and MACE times](mac_times.md)
