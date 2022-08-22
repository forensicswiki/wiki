This page is for discussing ideas regarding next-generation (NG) imaging
tools.

Note that some of the ideas mentioned can be already used by imaging
tools, but the idea of this page is to determine how useful these
features could be for next-generation of imaging tools. The scope is
mainly a software-based imaging tools, but not limited to. Some features
might not be doable, because of limitations of certain image file
formats.

Please, do not delete text (ideas) here, use the discussion page if you
want to discuss the usefulness of a feature.

# License

# Features

- Compression
- Integrity checks
- Encryption
- Error correction (parity)
- Pre-processing during imaging
- User suspend/resume, resume after failure
- Remote imaging
- Error resistance in reading storage media, e.d. disks
  - maybe have different techniques, e.g. to use for heavily damaged
    storage media
- Support different types of storage media
  - disk
  - volume
  - optical discs
  - memory
  - files and directories
- Store relevant data about the storage media and the imaging process
  - read errors
- Support multiple image format
  - not all image formats have support for all the features
- Built-in write blocking (software write blocker)

## Compression

- Reduces the amount of data that needs to be written; improved the
  overall imaging speed.
  - hash-based imaging
  - detection of easy (emtpy-block) and hard (encrypted block) to
    compress data
  - multi-threaded compression
  - sparse ranges
  - de-duplication

### de-duplication

- hash-based imaging
- sparse or repeated ranges
- pattern-fill

## Integrity checks

- Integrity hash (MD5, SHA1, SHA256)
- piecewise hashing

# Supportive tooling

## Image conversion

## Image verification

- modes:
  - full verification and print a report at the end
  - stop on error (useful for automation?)

# Image format

Implied features for an image format

- High-speed imaging
- Compact storage
- Error-resistant storage (over a longer time)
- Minimal overhead on read
- Evidence bag
  - multiple images in one image format
  - support for additional information e.g. case data

# See Also

- [Disk Imaging](Disk_Imaging "wikilink")
- [Memory Imaging](Memory_Imaging "wikilink")
- [Piecewise hashing](Piecewise_hashing "wikilink")
- [Forensics File Formats](:Category:Forensics_File_Formats "wikilink")

# External Links

[Category:Research](Category:Research "wikilink")