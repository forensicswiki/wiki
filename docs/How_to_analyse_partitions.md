A How-to for dealing with partitions.

[Sleuth Kit Informer
\#12](http://www.sleuthkit.org/informer/sleuthkit-informer-12.html)
suggests using the *mmls* program to display the contents of partitions.

For example:

` # mmls -t dos disk.dd`
`   Slot    Start   End Length  Description`
` 00:   -----    0000000000 0000000000  0000000001  Primary Table (#0)`
` 01:   -----   0000000001  0000000062  0000000062  Unallocated`
` 02:   00:00   0000000063  0002056319  0002056257  Win95 FAT32 (0x0B)`
` 03:   00:01   0002056320  0008209214  0006152895  OpenBSD (0xA6)`
` 04:   00:02   0008209215  0019999727  0011790513  FreeBSD (0xA5)`

You can use mmls to examine the OpenBSD and FreeBSD partitions that are
inside the DOS partition:

` # mmls -t bsd -o 2056321 disk.dd`
` Length    Description`
` 00:   02  0000000000  0019999727  0019999728  Unused (0x00)`
` 01:   08  0000000063  0002056319  0002056257  MSDOS (0x08)`
` 02:   00  0002056320  0002260943  0000204624  4.2BSD (0x07)`
` 03:   01  0002260944  0002875823  0000614880  Swap (0x01)`
` 04:   03  0002875824  0003080447  0000204624  4.2BSD (0x07)`
` 05:   04  0003080448  0003233663  0000153216  4.2BSD (0x07)`
` 06:   07  0003233664  0004257791  0001024128  4.2BSD (0x07)`
` 07:   06  0004257792  0008209214  0003951423  4.2BSD (0x07)`
` 08:    09 0008209215  0019984859  0011775645  Unknown (0x0A)`

(Examples from [Sleuth Kit Informer
\#12](http://www.sleuthkit.org/informer/sleuthkit-informer-12.html))

## External Links

- [Sleuth Kit Informer \#12: Using mmls from The Sleuth
  Kit](http://www.sleuthkit.org/informer/sleuthkit-informer-12.html)

[Category:Howtos](Category:Howtos "wikilink")