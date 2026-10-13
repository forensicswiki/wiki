---
tags:
  - Concept
---
Various concepts central to digital forensics are:

## Legal & Procedural Concepts

* [Chain of custody](digital_evidence.md#chain-of-custody)
* Data Integrity: evidence must remain entirely unaltered throughout the investigation. To uphold
  this, investigators typically work on a copy instead of the original device.
* Forensic Soundness: A standard or concept stating that tools and methods used during an
  investigation must be scientifically validated, reliable, and independently verifiable.

## Storage & Data Concepts

* Allocated Space: Storage space currently reserved by the operating system for active files, e.g.
  your documents or photos.
* Unallocated Space: "Empty" space on a hard drive. When you delete a file, the computer does not
  instantly erase it; it simply marks that file's location as unallocated (free to overwrite).
* Slack Space: The leftover, unused space at the end of a fixed data cluster. If a file is smaller
  than the space the computer allocates for it, fragments of old deleted data can often be found
  trapped in this "slack" space.
* Metadata: "data about data." This includes hidden file attributes like camera GPS coordinates on
  a photo, original authors of a document, or exact file creation and modification timestamps.

## Operational & Technical Concepts

* Forensic Imaging (Bit-by-Bit Copy): Unlike a standard file copy (like dragging a folder to a USB
  drive), a forensic image is a complete, mathematical clone of every single bit on a storage
  medium—including its deleted files, hidden partitions, and unallocated space.
* Write Blocking: A concept implemented via hardware or software that strictly prevents a computer
  from writing data to a piece of evidence. When a suspect's drive is plugged into a "write blocker",
  the investigator's computer can only read the data, ensuring the original device is completely
  untouched.
* Hashing (Cryptographic Verification): A process that passes a file or drive image through an
  algorithm (like SHA-256) to generate a unique alphanumeric string. Think of it as a digital
  fingerprint. If even a single letter inside a file is altered, the hash value changes completely,
  alerting investigators that the evidence has been tampered with.
* [Order of Volatility](digital_evidence.md#order-of-volatility)

## Data recovery

* File Carving: A data recovery concept used when file allocation tables are broken or missing.
  Forensic software bypasses the operating system entirely and reads the raw binary data to identify
  specific file "headers" and "footers" (like finding the specific binary code that dictates where a
  JPEG begins and ends) to piece the file back together.

## Timeline Analysis Concepts

* [epoch](epoch.md)
* [MAC(B) and MACE times](mac_times.md)

## See Also

* [Digital Evidence](digital_evidence.md)
