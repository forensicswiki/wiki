---
tags:
  - Linux
  - FreeBSD
  - MacOS
  - Tools
  - Windows
  - XML
  - Disk Analysis
  - Data Carving
---
fiwalk is a batch forensics analysis program written in C that uses
SleuthKit. The program can output in XML or ARFF formats.

## Temporary Distribution Point

fiwalk has been integrated with SleuthKit and can be downloaded from
Github at <https://github.com/sleuthkit/sleuthkit>.

## Legacy Distribution

**fiwalk** is a program that processes a disk image using the SleuthKit
library and outputs its results in Digital Forensics XML, the Attribute
Relationship File Format (ARFF) format used by the Weka Datamining
Toolkit, or an easy-to-read textual format.

The fiwalk source code comes with fiwalk.py, a Python module that makes
it easy to create digital forensics programs. Also included are several
demonstration programs that use fiwalk.py:

iblkfind.py
Given a disk block in a disk image, this program tells you which file(s)
map that sector.

icarvingtruth.py
Given two or more images of the same disk at different points in time,
this program files that are present in the earlier images that can only
be recovered from the later images using file carving techniques.

idifference.py
Given two or more images of the same disk at different points in time,
this program tells you what changes took place between each one.

iextract.py
Allows the extraction of files that match a particular pattern.

igrep.py
Searches every file in a disk image for a particular string. When found,
prints, the file and the offset within the file that the string was
found.

ihistogram.py
Prints a histogram of file types found in the disk image.

imap.py
Displays a “map” of where files are present in the disk image.

imicrosoft_redact.py
Modifies a disk image of a bootable Microsoft operating system so that
the image can no longer be boot and so that any Microsoft copyrighted
file in the \Windows directory cannot be executed. This allows the disk
image of a Microsoft operating system to be distributed without
implicitly violating Microsoft’s copyright.

iredact.py
An experimental disk redaction program which allows the removal of
specific files matching specific criteria.

iverify.py
Given a disk image and a previously created XML file, verifies that each
file in the DFXML file is still present in the disk image.

sanitize_xml.py
Given a DFXML file, sanitize file names so that no personally
identifiable information is leaked if the DFXML file is distributed.

## XML Example

    <?xml version='1.0' encoding='ISO-8859-1'?>
    <fiwalk xmloutputversion='0.2'>
      <metadata
      ns='http://example.org/myapp/'
      xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
      xmlns:dc='http://purl.org/dc/elements/1.1/'>
        <dc:type>Disk Image</dc:type>
      </metadata>
      <creator>
        <program>fiwalk</program>
        <version>0.5.7</version>
        <os>Darwin</os>
        <library name="tsk" version="3.0.1"></library>
        <library name="afflib" version="3.5.2"></library>
        <command_line>fiwalk -x /dev/disk2</command_line>
      </creator>
      <source>
        <imagefile>/dev/disk2</imagefile>
      </source>
    <!-- fs start: 512 -->
      <volume offset='512'>
        <Partition_Offset>512</Partition_Offset>
        <block_size>512</block_size>
        <ftype>2</ftype>
        <ftype_str>fat12</ftype_str>
        <block_count>5062</block_count>
        <first_block>0</first_block>
        <last_block>5061</last_block>
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
           <run file_offset='0' fs_offset='37376' img_offset='37888' len='43'/>
          </byte_runs>
          <hashdigest type='md5'>2bbe5c3b554b14ff710a0a2e77ce8c4d</hashdigest>
          <hashdigest type='sha1'>b3ccdbe2db1c568e817c25bf516e3bf976a1dea6</hashdigest>
        </fileobject>
      </volume>
    <!-- end of volume -->
    <!-- clock: 0 -->
      <runstats>
        <user_seconds>0</user_seconds>
        <system_seconds>0</system_seconds>
        <maxrss>1814528</maxrss>
        <reclaims>546</reclaims>
        <faults>1</faults>
        <swaps>0</swaps>
        <inputs>56</inputs>
        <outputs>0</outputs>
        <stop_time>Sun Nov 22 11:08:36 2009</stop_time>
      </runstats>
    </fiwalk>

## Availability

fiwalk can be downloaded from
<https://downloads.digitalcorpora.org/downloads/fiwalk>

## See Also

* [fileobject](fileobject.md)
