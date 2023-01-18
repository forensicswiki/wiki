---
tags:
  - Data Carving 
  - Data Recovery 
---
**GuidedCarving** is a [File Carving](file_carving.md) technique
to recover fragmented files introduced in [Adroit Photo
Forensics](adroit_photo_forensics.md). GuidedCarving allows a
user to attempt to recover a fragmented file that failed to fully
recover using [SmartCarving](file_carving_smartcarving.md).

## Process

* The user opens a photo that has failed to recover properly.
* The user identifies the first error on a photo by clicking on it.
* Adroit Photo Forensics then presents the user with the best possible block
  matches.
* The user cycles through the presented blocks to find the correct continuation
  block.
* User can then choose to either manually build the rest of the file or allow
  SmartCarving to take over again.
