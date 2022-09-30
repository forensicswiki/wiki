---
tags:
  - No Category
---
AFFLIB has been depreciated. As a result, this page is now obsolete.

## High Priority

- When afinfo -a is run on a non-AFF file, it notes it is a "Raw" file,
  but continues to attempt to process segments. It should exit if it
  does not find valid AFF segments. For example, running it against a
  raw image of a 40GB disk created with aimage, afinfo -a reported 2,386
  segments then finished with the error message "Cannot calculate
  missing pages."

<!-- -->

- The library does not compile on 64-bit versions of Fedora Core 7
  Linux.

<!-- -->

- Create man pages and/or documentation for AFF toolkit. To wit:

`* `[`aimage`](aimage.md)
`* `[`ident`](ident.md)
`* `[`afcat`](afcat.md)
`* `[`afcompare`](afcompare.md)
`* `[`afconvert`](afconvert.md)
`* `[`affix`](affix.md)
`* `[`affuse`](affuse.md)
`* `[`afinfo`](afinfo.md)
`* `[`afstats`](afstats.md)
`* `[`afxml`](afxml.md)
`* `[`afsegment`](afsegment.md)

- Add a usage description to [afcat](afcat.md). When run with no
  arguments the output should say what the program does.

<!-- -->

- Create man pages and/or documentation for AFF library functions (e.g.
  ,`af_open`, `af_get_imagesize`)

<!-- -->

- Build library as a shared library using libtool. This will allow
  developers using the library to just link to the AFF. Without it,
  developers must link to the static library and the individual
  libraries necessary <em>on that machine</em>. There is no good way to
  determine those extra libraries.

<!-- -->

- Document that `af_write` may not be called without first setting the
  `image_pagesize` value inside of the `AFFILE` structure. Not doing so
  causes a divide by zero error. Perhaps we should 1. Check that
  `image_pagesize` is not zero and 2. Set `image_pagesize` to a known
  good default value when opening a new AFF file for writing.

<!-- -->

- Check aimage ability to write a file of 1,073,741,825 bytes
  ((2\*\*30)+1). Correctly reported reading/writing a file that was a
  1,073,741,824 random byte stream, but did not pick up the extra byte
  when it was added to the file. ls -la correctly shows the size with
  the extra byte. Also, added 42 additional bytes which were not
  apparently read or written. UPDATE - With 511 bytes added, still
  didn't read/write full file, however, adding 512 bytes did cause the
  whole file (1,073,742,336 bytes) to be read/written.

## Medium Priority

- Is there a set of segment names that must be defined to have a *valid*
  AFF file?

<!-- -->

- Document that `af_open` (when writing a file) does more than a
  standard `fopen` command. The command writes an AFF stub of some kind
  to the output file. Users should be cautioned not to use this function
  as a test, lest they overwrite data.

<!-- -->

- Does `af_open` refuse to open a file for writing if it already exists?
  If so, what kind of error does it return?

<!-- -->

- Document how to programmatically enumerate all segments and values in
  a file. That is, explain how to get the output of `$ afinfo -a`.

## Low Priority

- Add library function to open standard input. Perhaps:

<!-- -->

    AFFILE * af_open_stdin(void);