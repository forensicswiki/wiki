---
tags:
  - Encryption
---
## Overview

Rainbow tables are large pre-computed tables that make it fast to
determine what word produced a particular hash. Rainbow tables only work
if the following conditions are true:

* The hash algorithm was known when the rainbow table was created;
* No salt was used in the individual password.

## Free Rainbow Tables

*These rainbow tables are free for download.*

### Windows XP & Vista passwords (LM & NT hashes)

* <http://ophcrack.sourceforge.net/tables.php>

### WPA/WPA2-PSK passwords

* <http://www.renderlab.net/projects/WPA-tables/> (only for top 1000 SSID list)

### [DOC](doc.md), [PDF](pdf.md), etc

## See Also

* [Hashing#MD5_Reverse_Hash_Services](hashing.md#md5-reverse-hash-services)

# References

* [Wikipedia's Rainbow table entry](http://en.wikipedia.org/wiki/Rainbow_table)
