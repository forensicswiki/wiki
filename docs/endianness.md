---
tags:
  - Articles that need to be expanded
---
Endianness refers to the way that a computer processor or file format
stores numbers.

Big endian numbers are stored in such a way that the most significant
digit appears first in the number as it is read from left to right. This
is familiar to most people as it is the way that nubers are represented
in most languages. For example, in the number 1337 the first digit is
the most significant digit because it represents 1000 units. The last
digit is the least significant because it only represents 7 units.

Little endian numbers are stored in such a way that the most significant
digit appears last in the number as it is read from left to right. When
the number 1337 is stored in a little endian system, the seven is the
most significant digit and represents 7000 units. The one is now the
least significant digit representing only one unit.

When examining numbers in hexadecimal form on a little-endian system,
the byte order must be reversed before converting to decimal. Note that
the individual characters within the byte are not reversed because the
whole byte represents one number. For example, the hexadecimal number 39
05 must be reversed to 05 39 before being converted to the decimal 1337.

Intel based processors like the x86 usually represent numbers in little
endian form. Motorola based processor architectures like the PowerPC
tend to be big endian.

Middle endian (PDP).

Network endian (big endian).

## External Links

* [Wikipedia: Endianness](https://en.wikipedia.org/wiki/Endianness)
