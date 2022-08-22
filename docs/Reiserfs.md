## Detecting ReiserFS in a forensics environment

![Image:Superblock.png](Superblock.png "Image:Superblock.png")

Note: These are in
[little-endian](http://en.wikipedia.org/wiki/Little_endian) format.
[Pmow](User:Pmow "wikilink") 18:21, 17 July 2008 (UTC)

<table border="0">
<tr>
<th>

**Name**

</th>
<th>

Size

</th>
<th>

Description

</th>
</tr>
<tr>
<td>

Block count

</td>
<td align="center">

4

</td>
<td>

The number of blocks in the partition

</td>
</tr>
<tr>
<td>

Free blocks

</td>
<td align="center">

4

</td>
<td>

The number of free blocks in the partition

</td>
</tr>
<tr>
<td>

Root block

</td>
<td align="center">

4

</td>
<td>

The block number of the block containing the root node

</td>
</tr>
<tr>
<td>

Journal block

</td>
<td align="center">

4

</td>
<td>

The block number of the block containing the first journal node

</td>
</tr>
<tr>
<td>

Journal device

</td>
<td align="center">

4

</td>
<td>

Journal device number (not sure what for)

</td>
</tr>
<tr>
<td>

Orig. journal size

</td>
<td align="center">

4

</td>
<td>

Original journal size. Needed when using partition on systems with
different default journal sizes.

</td>
</tr>
<tr>
<td>

Journal trans. max

</td>
<td align="center">

4

</td>
<td>

The maximum number of blocks in a transaction

</td>
</tr>
<tr>
<td>

Journal magic

</td>
<td align="center">

4

</td>
<td>

A random magic number

</td>
</tr>
<tr>
<td>

Journal max batch

</td>
<td align="center">

4

</td>
<td>

The maximum number of blocks in a transaction

</td>
</tr>
<tr>
<td>

Journal max commit age

</td>
<td align="center">

4

</td>
<td>

Time in seconds of how old an asynchronous commit can be

</td>
</tr>
<tr>
<td>

Journal max trans. age

</td>
<td align="center">

4

</td>
<td>

Time in seconds of how old a transaction can be

</td>
</tr>
<tr>
<td>

Blocksize

</td>
<td align="center">

2

</td>
<td>

The size in bytes of a block

</td>
</tr>
<tr>
<td>

OID max size

</td>
<td align="center">

2

</td>
<td>

The maximum size of the object id array

</td>
</tr>
<tr>
<td>

OID current size

</td>
<td align="center">

2

</td>
<td>

The current size of the object id array

</td>
</tr>
<tr>
<td>

State

</td>
<td align="center">

2

</td>
<td>

State of the partition: valid (1) or error (2)

</td>
</tr>
<tr>
<td>

Magic string

</td>
<td align="center">

12

</td>
<td>

The reiserfs magic string, should be "ReIsEr2Fs"

</td>
</tr>
<tr>
<td>

Hash function code

</td>
<td align="center">

4

</td>
<td>

The hash function that is being used to sort names in a directory

</td>
</tr>
<tr>
<td>

Tree Height

</td>
<td align="center">

2

</td>
<td>

The current height of the disk tree

</td>
</tr>
<tr>
<td>

Bitmap number

</td>
<td align="center">

2

</td>
<td>

The amount of bitmap blocks needed to address each block of the file
system

</td>
</tr>
<tr>
<td>

Version

</td>
<td align="center">

2

</td>
<td>

The reiserfs version number

</td>
</tr>
<tr>
<td>

Reserved

</td>
<td align="center">

2

</td>
<td>

 

</td>
</tr>
<tr>
<td>

Inode Generation

</td>
<td align="center">

4

</td>
<td>

Number of the current inode generation.

</td>
</tr>
</table>

The following is the start of the superblock of a 256MB reiserfs
partition on an Intel based system:

    00000000 66 00 01 00 93 18 00 00 82 40 00 00 12 00 00 00  f........@......
    00000010 00 00 00 00 00 20 00 00 00 04 00 00 ac 34 11 57  ..... ......¬4.W
    00000020 84 03 00 00 1e 00 00 00 00 00 00 00 00 10 cc 03  ..............Ì.
    00000030 08 00 02 00 52 65 49 73 45 72 32 46 73 00 00 00  ....ReIsEr2Fs...
    00000040 03 00 00 00 04 00 03 00 02 00 00 00 dc 52 00 00  ............ÜR..

![Image:superblock_example.png](superblock_example.png "Image:superblock_example.png")


Block count: 65638
Free blocks: 6291
Root block: 16514
Journal block: 18
Journal device: 0
Original journal size: 8192
Journal trans. max: 1024
Journal magic: 1460745388
Journal max. batch: 900
Journal max. commit age: 30
Journal max. trans. age: 0
Blocksize: 4096
OID max. size: 972
OID current size: 8
State: 2 (error)
Magic String: ReIsEr2Fs
Hash function code: 3
Tree height: 4
Bitmap number: 3
Version: 2
Inode generation: 21212

## External Links

- [ReiserFS on Wikipedia](http://en.wikipedia.org/wiki/Reiserfs)
- [The structure of the Reiser file
  system](http://homes.cerias.purdue.edu/~florian/reiser/reiserfs.php)

[Category:File Systems](Category:File_Systems "wikilink")