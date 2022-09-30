---
tags:
  - Digital Forensics XML 
---
**fileobject** is an XML [Forensics XML](forensics_xml.md) tag
which is used to describe information about a file.

The file object can contain information about:

- The file's name
- The file's hash code(s)
- The file's location on the disk.
- Embedded metadata
- Block hashes, a Bloom Filter, or a Similarity Digest for the file.

Other objects can be embedded in a **fileobject** object:

- The **byte_runs** object specifies where the file is located on the
  disk.
- A **sector_hash** object is a list of sector hash codes.
- The sector_hash object could contain a **nsrl_bloom** object, which
  would be a bloom filter that contains all of the sector hashes.

## XML Sample


        <fileobject>
          <filename>README.txt</filename>
          <id>2</id>
          <filesize>43</filesize>
          <partition>1</partition>
          <alloc>1</alloc>
          <used>1</used>
          <inode>6</inode>
          <type>1</type>
          <mode>511</mode>
          <nlink>1</nlink>
          <uid>0</uid>
          <gid>0</gid>
          <mtime>1258916904</mtime>
          <atime>1258876800</atime>
          <crtime>1258916900</crtime>
          <byte_runs>
           <run[:Category:Operating systems](:Category:Operating_systems "wikilink") file_offset='0' fs_offset='37376' img_offset='37888' len='43'/>
          </byte_runs>
          <hashdigest type='md5'>2bbe5c3b554b14ff710a0a2e77ce8c4d</hashdigest>
          <hashdigest type='sha1'>b3ccdbe2db1c568e817c25bf516e3bf976a1dea6</hashdigest>
        </fileobject>

|                                                                               |                                                                                                                                                                |     |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| XML Tag                                                                       | Meaning                                                                                                                                                        |     |
| <fileobject>                                                                  | Every file is inside a <fileobject>                                                                                                                            |     |
| <orphan>YES</orphan>                                                          | YES means that the file is an ""orphan,"" with no file name.                                                                                                   |     |
| <filesize>3210</filesize>                                                     | The file size in bytes.                                                                                                                                        |     |
| <unalloc>1</unalloc>                                                          | A "1" means that the file was not allocated in the file system. This may mean that the file was deleted.                                                       |     |
| <used>1</used>                                                                | Not sure what this means.                                                                                                                                      |     |
| <mtime>1114172320</mtime>                                                     | The file's modification time, as a Unix timestamp (number of seconds since January 1, 1970 UTC).                                                               |     |
| <ctime>1195819392</ctime>                                                     | The file's inode's creation time, as a Unix timestamp.                                                                                                         |     |
| <atime>1195794000</atime>                                                     | The file's access time, as a unix timestamp.                                                                                                                   |     |
| <byte_runs>121130496:3210</byte_runs>                                         | The file's fragments. Each fragment is represented as the byte offset from the beginning of the disk image (the first byte is byte \#0) and a number of bytes. |     |
| <fragments>1</fragments>                                                      | The number of fragments in the file.                                                                                                                           |     |
| <hashdigest type='md5'>c27c0730b858bc60c8894300a98bba55</hashdigest>          | The file's MD5, as a hexadecimal hash.                                                                                                                         |     |
| <hashdigest type='sha1'>0277680d624e609f23aec9e4265c2d7d24bd3824</hashdigest> | The file's SHA1, as a hexadecimal hash.                                                                                                                        |     |
| <partition>1</partition>                                                      | The partition number in which the file was found.                                                                                                              |     |
