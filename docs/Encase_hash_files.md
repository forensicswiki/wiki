The [EnCase](EnCase "wikilink") forensics suite uses a proprietary file
format to store sets of known hashes called the **EnCase hash file
format**. The format stores a set of [MD5](MD5 "wikilink") hashes and
[metadata](metadata "wikilink") about the set as a whole. That is,
individual hashes do not contain any information specific to them, but
the set as a whole can contain some information. In particular, the
filename corresponding to each hash is not stored.

Version 3 of [EnCase](EnCase "wikilink") used a slightly different
format than versions 4 and 5. Both versions start with the header, in
hexadecimal:

    48 41 53 48 0d 0a ff 00

In ASCII, this looks like `HASH` followed by a newline.

The hashes begin at offset 0x480 in the file.

A quick look at a hash file created by Encase 6.8.1.8 revealed the
following structure (to be verified):

**Offset 0x0000**

A header that consists of the following 16 bytes:

    48 41 53 48 0D 0A FF 00 02 00 00 00 01 00 00 00

**Offset 0x0010**

Count: The number of MD5 sums contained in this file, written as a 4
byte integer in Intel litle endian format (i.e. least significant byte
first).

**Offset 0x0014**

The range from 0x0014 to 0x0407 is filled by zero-bytes. The purpose of
this area is unknown.

**Offset 0x0408**

HashSet: The text that EnCase shows in its column "Hash Set". The
maximum string length is 39 characters. Characters are stored in
Unicode. (*Based on hash file form EnCase v. 6.17*)

**Offset 0x0458**

Category: The text that Encase shows in its column "category". The
maximum string length is 19 characters. Each character is written as a
2-byte-Unicode-number. Examples:

The latin letter A is represented by the 2 bytes

    41 00

The cyrillic letter Д is represented by the 2 bytes

    14 04

Again, Intel little endian format is used. The unused space is filled up
by zero-bytes.

**Offset 0x047E**

Two zero-bytes.

**Offset 0x0480**

Start of the hash entries. Each entry occupies 18 bytes: The hash value
itself (16 bytes) followed by 2 zero-bytes. The next entry follows
immediately.

The file ends with the last hash entry.

## See also

- [EnCase](EnCase "wikilink")

[Category:Forensics File
Formats](Category:Forensics_File_Formats "wikilink")