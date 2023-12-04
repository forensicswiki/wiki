---
tags:
  - Articles that need to be expanded
  - Papers
  - Research
  - Secure Deletion
---
Here are some of the standards by country that we have been able to find
regarding the disk sanitization problem:

### Australia

- ASCI 33: 5 pass wipe, 1 pass with character, 1
  pass with inverse of character, repeat first two passes, 1 pass
  random.

### Canada

- [RCMP TSSIT OPS-II](http://www.rcmp-grc.gc.ca/tsb/pubs/it_sec/g2-003_e.pdf):
  8 pass wipe.

### Germany

- VSItR: Verschlusssachen-IT-Richtlinien, 7 pass wipe followed by verification.

### Russia

- [Gostechcommission management directive](http://www.internet-law.ru/standarts/safety/gtk009.doc):
  2 pass with random data.

### UK

- BHMG Infosec Standard no.5: Three pass wipe followed by verification.

### USA

- [NIST 800-88](https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final):
  Guidelines for Data Sanitation, Sept 2006.
- [DoD Destruction](http://simson.net/ref/2001/ASD_HD_Disposition_memo060401.pdf):
  Disposition of Unclassified DoD Computer Hard Drives, Assistant
  Secretary of Defence, June 4, 2001.
- [DoD 5200.28-STD](https://irp.fas.org/nsa/rainbow/std001.htm):
  Department of Defence Trusted Computer System Evaluation Criteria,
  December 26, 1985.
- [DoD 5220.22-M](http://simson.net/ref/2001/DoD_5220.22-M.pdf):
  National Industrial Security Program Operating Manual, January 1995,
  incorporating Change One (July 1997) and Change Two (February 2001).
- NAVSO P-5239-26: US Navy standards for RLL and MFM encoded drives.

### Other

- [Gutmann Wipe](http://www.cs.auckland.ac.nz/~pgut001/pubs/secure_del.html):
  Secure Deletion of Data from Magnetic and Solid-State Memory by
  [Peter Gutmann](peter_gutmann.md). Overwrite process using a sequence
  of 35 consecutive writes. First published in the Sixth USENIX Security
  Symposium Proceedings, San Jose, Ca, July 22-25, 1996.
- Schneier Wipe: Two pass of specific characters followed by five passes of
  Pseudo Random Data. Published by [Bruce Schneier](bruce_schneier.md) in
  [Applied Cryptography](https://www.schneier.com/books/applied-cryptography),
  1996
