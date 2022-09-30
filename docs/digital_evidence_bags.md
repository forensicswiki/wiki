---
tags:
  -  File Formats
---
The **Digital Evidence Bag** (**DEB**) format mimics in a digital
environment the bags, tags and seals used to traditionally wrap
evidence.

When a DEB is created three files are generated:

1.  A **.tag** file which is [plain text](plain_text.md) and
    stores case specific [metadata](metadata.md) such and
    evidence reference identifier, examiner, location, timestamps and
    tag continuity blocks that record DEB access activity. In addition
    to this the tag file contains the cryptographic
    [hashes](hash.md) that are used to maintain and
    assure the integrity of the DEB structure.
2.  An **.index** file is a plain text file that records device, file or
    data source metadata.
3.  A **.bag** file that holds the evidential data e.g. the raw device
    bit stream, logical files, network packet capture data.

