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

- [ASCI 33](asci_33.md): 5 pass wipe, 1 pass with character, 1
  pass with inverse of character, repeat first two passes, 1 pass
  random.

### Canada

- [RCMP TSSIT OPS-II](rcmp_tssit_ops-ii.md)
  ([pdf](http://www.rcmp-grc.gc.ca/tsb/pubs/it_sec/g2-003_e.pdf)): 8
  pass wipe.

### Germany

- [VSItR](vsitr.md): Verschlusssachen-IT-Richtlinien, 7 pass
  wipe followed by verification.

### Russia

- Gostechcommission management directive
  ([doc](http://www.internet-law.ru/standarts/safety/gtk009.doc)): 2
  pass with random data.

### UK

- [BHMG Infosec Standard no.5](bhmg_infosec_standard_no.5.md):
  Three pass wipe followed by verification.

### USA

- [AFSSI-5020](afssi-5020.md)
  ([pdf](http://jya.com/afssi5020.htm)): USAF Data Sanitization
  Standard.
- [NIST 800-88](nist_800-88.md)
  ([pdf](https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final)):
  Guidelines for Data Sanitation, Sept 2006.
- [DoD Destruction](dod_destruction.md)
  ([pdf](http://simson.net/ref/2001/ASD_HD_Disposition_memo060401.pdf)):
  Disposition of Unclassified DoD Computer Hard Drives, Assistant
  Secretary of Defence, June 4, 2001.
- [DoD 5200.28-STD](dod_5200.28-std.md)
  ([pdf](http://security.isu.edu/pdf/d520028.pdf)): Department of
  Defence Trusted Computer System Evaluation Criteria\], December 26,
  1985.
- [DoD 5220.22-M](dod_5220.22-m.md)
  ([pdf](http://simson.net/ref/2001/DoD_5220.22-M.pdf)): National
  Industrial Security Program Operating Manual\], January 1995,
  incorporating Change One (July 1997) and Change Two (February 2001).
- [NAVSO P-5239-26](navso_p-5239-26.md): US Navy standards for
  RLL and MFM encoded drives.

### Other

- [Gutmann Wipe](gutmann_wipe.md)
  ([pdf](http://www.cs.auckland.ac.nz/~pgut001/pubs/secure_del.html)):
  Secure Deletion of Data from Magnetic and Solid-State Memory by [Peter
  Gutmann](peter_gutmann.md). Overwrite process using a sequence
  of 35 consecutive writes. First published in the Sixth USENIX Security
  Symposium Proceedings, San Jose, Ca, July 22-25, 1996.
- [Schneier Wipe](schneier_wipe.md): Two pass of specific
  characters followed by five passes of Pseudo Random Data. Published by
  [Bruce Schneier](bruce_schneier.md) in [Applied
  Cryptography](https://www.schneier.com/books/applied-cryptography), 1996
