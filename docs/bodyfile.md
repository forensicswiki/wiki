---
tags:
  -  Timeline Analysis
---
Bodyfile (or body file) is an output format (as far as known) introduced
by the [SleuthKit](sleuthkit.md).

The bodyfile is typically an intermediate file generated by fls or ils
which are then provided as input to the mactime tool.

The bodyfile uses a delimiter-separated value format, with the
pipe-character (\|) as the delimiter.

Different versions of the SleuthKit use different versions of the
bodyfile format.

The following fields are defined for SleuthKit 3.0 and later:

    MD5|name|inode|mode_as_string|UID|GID|size|atime|mtime|ctime|crtime

## Known issues

- date and time values do not indicate a time zone or if daylight
  savings applies
- the encoding is not specified, UTF-8 is assumed
- the name field can contain (\$FILE_NAME) to indicate the bodyfile
  entry was derived from a NTFS \$FILE_NAME attribute instead of
  \$STANDARD_INFORMATION and \$DATA attributes. Note that the exact
  behavior is not documented by the SleuthKit project.
- the name field can contain -\> symbolic_link_target but fls does not
  appear to support this for NTFS. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/2645>
  - it is unclear if the symbolic link target can be used in combination
    with the "(\$FILE_NAME)" suffix
- it is unclear which characters should be escaped, by observation \|
  and \\ are both escaped with \\ in the name field by fls but mactime
  is unable to handle a name that contains the \| character
  <https://github.com/sleuthkit/sleuthkit/issues/2124>.
  - other implementations are known to not escape \\
- It is unclear from the specification if control characters should be
  escaped. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/1989>
  - other implementations are known to escape control characters as \x##
    where \## contains the hexadecimal byte value of the control
    character
- the format of the inode field is unclear for file systems like NTFS,
  the documentation indicates that it uses [a TSK Metadata
  Address](https://wiki.sleuthkit.org/index.php?title=Metadata_Address)
  however by observation the implementation is TSK specific and does not
  seem to match what is documented. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/1809>
  - other implementations are known to store the 64-bit NTFS file
    reference value as the inode field
- the format of the mode_as_string field is unclear for file systems
  like NTFS, this likely can be derived from the source code. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/1810>
  - Note that the SleuthKit currently does not correctly identifies
    symbolic links for NTFS in the bodyfile output. Also see:
    <https://github.com/sleuthkit/sleuthkit/issues/2645>
- the atime, mtime, ctime and crtime typically contain the number of
  seconds since January 1, 1970. It is unknown if a fractional part is
  allowed by specification. The corresponding mactime tool does allow
  for a fractional part to be present but ignores it. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/1810>
  - this limits the usefulness of the format for timelines with a vast
    amount of sub-second activity
- the format of the MD5 field is undefined, it seems to be '0' if
  "hashing" is disabled, '00000000000000000000000000000000' if "hashing"
  is enabled but no MD5 was calculated, otherwise it contains the MD5
  that was calculated. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/2058>
- duplicate entries for the same NTFS ADS. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/2644>

## Observations

- the name field can contain a symbolic link target. Also see:
  <https://github.com/sleuthkit/sleuthkit/issues/2043>
- on HFS+ the / character in a file name will be replaced by :, which
  corresponds with the behavior of Mac OS Terminal. Also see:
  <https://github.com/sleuthkit/sleuthkit/blob/3d16b8bc293ba13a5674fe9ce6a35f867ccc945d/tsk/fs/hfs_dent.c#L110>
- for hard links on HFS+ the Catalog Node Identifier (CNID) of the link
  target (indirect node) file record is used instead as the "inode"
  value instead of the CNID of the (hard link) file record itself. This
  matches the behavior of Mac OS (file) stat as described in
  <https://developer.apple.com/library/archive/technotes/tn/tn1150.html>
  section "Hard Links".
- For ext2 the MD5 calculation of fls includes: regular files,
  directories (contents of the directory entries data stream), symbolic
  links (content of the data stream of the symbolic link not its
  target), "virtual metadata files/directories" like \$OrphanFiles
- For HFS+ the MD5 calculation of fls includes: regular files, symbolic
  links (content of the data stream of the symbolic link not its
  target), "virtual metadata files" like \$CatalogFile

## External Links

- [Body file -
  SleuthKit](https://wiki.sleuthkit.org/index.php?title=Body_file)
- [Bodyfile
  format](https://dfimagetools.readthedocs.io/en/latest/sources/Bodyfile-format.html),
  by dfImageTools project
