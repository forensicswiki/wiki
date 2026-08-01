---
tags:
  - Digital Forensics XML
---

## Schemas

The Digital Forensics XML schemas are somewhat in flux, in that new elements
will be added as necessary. However, the basic structure is unlikely to change.

* fileobject schema
* filehashset schema

### Encoding

Encoding is assumed to be base10, except for hash codes, which are assumed to
be base16.

### File object (fileobject)

The file object (**fileobject**) is used to describe information about a file.

The file object can contain information about:

* The file's name
* The file's hash code(s)
* The file's location on the disk.
* Embedded metadata
* Block hashes, a Bloom Filter, or a Similarity Digest for the file.

Other objects can be embedded in a **fileobject** object:

* The **byte_runs** object specifies where the file is located on the disk.
* A **sector_hash** object is a list of sector hash codes.
* The sector_hash object could contain a **nsrl_bloom** object, which would be
  a bloom filter that contains all of the sector hashes.

| XML Tag | Meaning |
| --- | --- |
| `<fileobject>` | Every file is inside a `<fileobject>` |
| `<orphan>YES</orphan>` | YES means that the file is an "orphan," without a name. |
| `<filesize>3210</filesize>` | The size of the file content in bytes. |
| `<unalloc>1</unalloc>` | A "1" means that the file was not allocated in the file system. This may mean that the file was deleted. |
| `<used>1</used>` | Not sure what this means. |
| `<mtime>1114172320</mtime>` | The file's modification time, as a POSIX (time_t) timestamp (number of seconds since January 1, 1970 UTC). |
| `<ctime>1195819392</ctime>` | The file's inode's creation time, as a POSIX (time_t) timestamp. |
| `<atime>1195794000</atime>` | The file's access time, as a unix timestamp. |
| `<byte_runs>121130496:3210</byte_runs>` | The file's fragments. Each fragment is represented as the byte offset from the beginning of the disk image (the first byte is byte #0) and a number of bytes. |
| `<fragments>1</fragments>` | The number of fragments in the file. |
| `<hashdigest type='md5'>c27c0730b858bc60c8894300a98bba55</hashdigest>` | The file's MD5, as a hexadecimal hash. |
| `<hashdigest type='sha1'>0277680d624e609f23aec9e4265c2d7d24bd3824</hashdigest>` | The file's SHA1, as a hexadecimal hash. |
| `<partition>1</partition>` | The partition number in which the file was found. |

## Examples

### Piecewise Hashing

Digital Forensics XML can be used to represent the results of piecewise hashing
of individual files. The [md5deep](md5deep.md) suite now generates piecewise
hashing results in DFXML when the `-d` option is provided. For example:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<md5deep>
  <fileobject>
    <filename>sample/bar.txt</filename>
    <filesize>46</filesize>
    <mtime format='time_t'>1296497502.0</mtime>
    <byte_runs>
      <byte_run file_offset='0' len='46'>
        <hashdigest type='MD5'>0e886f6b08986269af98aedde53df23f</hashdigest>
        <hashdigest type='SHA256'>21c35b5698f1e54d11ca8a41321d40d75797425013dfa1b640ab34d7efa7f1ac</hashdigest>
      </byte_run>
    </byte_runs>
    <hashdigest type='MD5'>0e886f6b08986269af98aedde53df23f</hashdigest>
    <hashdigest type='SHA256'>21c35b5698f1e54d11ca8a41321d40d75797425013dfa1b640ab34d7efa7f1ac</hashdigest>
  </fileobject>
  <fileobject>
    <filename>sample/foo.txt</filename>
    <filesize>193</filesize>
    <mtime format='time_t'>1296497462.0</mtime>
    <byte_runs>
      <byte_run file_offset='0' len='193'>
        <hashdigest type='MD5'>06f63e03ed5e1770a2ff753a76d04906</hashdigest>
        <hashdigest type='SHA256'>82a217a76ebe5e6c0f768576a3e8fd9ba6de504c42360c23e08ddfa22e711ba0</hashdigest>
      </byte_run>
    </byte_runs>
    <hashdigest type='MD5'>06f63e03ed5e1770a2ff753a76d04906</hashdigest>
    <hashdigest type='SHA256'>82a217a76ebe5e6c0f768576a3e8fd9ba6de504c42360c23e08ddfa22e711ba0</hashdigest>
  </fileobject>
  <fileobject>
    <filename>sample/somedir/baz.txt</filename>
    <filesize>19</filesize>
    <mtime format='time_t'>1296497486.0</mtime>
    <byte_runs>
      <byte_run file_offset='0' len='19'>
        <hashdigest type='MD5'>362aa248563e453588755f280387a3d4</hashdigest>
        <hashdigest type='SHA256'>7a7c62947561b0b00c213d37d04edbe0c8de46282098b7216a23b25fa336f150</hashdigest>
      </byte_run>
    </byte_runs>
    <hashdigest type='MD5'>362aa248563e453588755f280387a3d4</hashdigest>
    <hashdigest type='SHA256'>7a7c62947561b0b00c213d37d04edbe0c8de46282098b7216a23b25fa336f150</hashdigest>
  </fileobject>
</md5deep>
```

### Source Tag

The `source` tag is used to describe the source of forensic data. It currently
is used for disk images, for example:

```xml
<source type='Disk Image'>
  <imagefile>/corp/images/nus/1040.aff</imagefile>
  <sectorsize>512</sectorsize>
  <device_model>SEAGATE ST32550W SUN2.1G 0418</device_model>
  <device_sn>01806486</device_sn>
  <acquisition_commandline>aimage scsi1 /project2/b28.aff</acquisition_commandline>
  <acquisition_device>/dev/sda1</acquisition_device>
  <device_capabilities>pass2: &gt;SEAGATE ST32550W SUN2.1G 0418&lt; Fixed Direct Access SCSI-2 device
pass2: Serial Number 01806486
pass2: 20.000MB/s transfers (10.000MHz, offset 15, 16bit), Tagged Queueing Enabled
  </device_capabilities>
  <sectorsize coding='base10'>512</sectorsize>
  <devicesectors coding='base10'>4194995</devicesectors>
  <acquisition_macaddr>00:0f:b5:42:6a:fe</acquisition_macaddr>
  <acquisition_date>2006-07-25T10:56:42</acquisition_date>
</source>
```

### Volume Grouping

After the **source** tag you may find some **fileobject** tags. They may be
grouped within a **volume** tag, for example:

```xml
<volume offset='32256'>
  <byte_runs>
    <byte_run offset='0' img_offset='114688' len='32768'>
    <byte_run offset='0' img_offset='1523712' len='32768'>
    <byte_run offset='0' img_offset='6356992' len='39659'>
  </byte_runs>
  <ftype>1</ftype>
  <ftype_str>ntfs</ftype_str>
  <block_size>4096</block_size>
  <block_count>4980142</block_count>
  <first_block>0</first_block>
  <last_block>4980141</last_block>
  <fileobject>
  ...
  </fileobject>
</volume>
```

### File Object

```xml
<fileobject>
  <filename>RAW/report02-3.pdf</filename>
  <id>19</id>
  <filesize>1421998</filesize>
  <partition>1</partition>
  <alloc>1</alloc>
  <used>1</used>
  <inode>39</inode>
  <type>1</type>
  <mode>511</mode>
  <nlink>2</nlink>
  <uid>0</uid>
  <gid>0</gid>
  <mtime>1230764913</mtime>
  <ctime>1230764913</ctime>
  <atime>1230764978</atime>
  <crtime>1230764978</crtime>
  <seq>1</seq>
  <byte_runs>
    <run file_offset='0' fs_offset='241542144' img_offset='241542144' len='1421998'/>
  </byte_runs>
  <hashdigest type='MD5'>dede94f84fb2d00dc93ed00fda272a18</hashdigest>
  <hashdigest type='SHA1'>3c078d039398c44611b6365e8afdeadeb61967d4</hashdigest>
</fileobject>
```

## External links

* [Project site](https://github.com/dfxml-working-group/dfxml_schema)
