---
tags:
  -  Anti-Forensics
  -  File Analysis
  -  Articles that need to be expanded
---
![](timestomp_mace.jpg "timestomp_mace.jpg") **Timestomp** is a utility
co-authored by developers [James C. Foster](james_c._foster.md)
and [Vincent Liu](vincent_liu.md). The software's goal is to
allow for the deletion or modification of [timestamp-related
information](mac_times.md) on files.

Take for example the "Timestomp MACE Values" screenshot displaying a
command prompt window displaying the MACE values for a document file
titled "text.txt". There are (4) four date time and date stamps
displayed that are useful to Forensic Examiners in reconstructing when
data was last modified, accessed, created, or entered into the
[NTFS](ntfs.md) Master File Table by the operating system or
manually by the user.

![](timestomp_mace_change.jpg "timestomp_mace_change.jpg") Using the
Timestomp application, the modified date and timestamp can be completely
changed (i.e., evidenced by the "Timestomp MACE Change" screenshot). If
I were to change it, along with the other entries to more believable
dates and times, then the validity of the document falls into question
as does its ability to completely slip by an examiner's watchful eye if
looking for modified files in an entirely different year or date span.

![](timestomp_mace_change_proof.jpg "timestomp_mace_change_proof.jpg")
The "Timestomp MACE Change Proof" screenshot is a final shot of the
Operating System's interpretation of the Modified timestamp. It reflects
the aforementioned change exactly.

Note: Although this program is designed to frustrate forensic analysis,
it should be noted that its use can be easily detected. Because the
program can delete all timestamp information, the lack of timestamp
values would lead an examiner to the conclusion that something is amiss
on the system. Microsoft-based [Windows](windows.md) operating
system record at least some timestamp information. The total absence of
such is a dead giveaway that a user has tried to hide something. On the
flipside, if the values are simply changed to believable values, then
there is little chance of the change(s) being noticed at a casual
glance.

## A Practical Example

Timestomp cannot be used directly to modify all (on average) 8 timestamp
values in the MFT entry; 4 in \$STANDARD_INFORMATION attribute and 4 in
\$FILE_NAME attribute. The \$FILE_NAME attribute MACE values are
intended to be modified by Windows, but still there is an indirect
workaround to update those values in order to further frustrate
forensics.

1\) Create file (*c:\test.txt*)

`  `![`Image:1.jpeg`](1.jpeg "Image:1.jpeg")

2\) Change timestamps using Timestomp

`  timestomp.exe c:\test.txt -z "Saturday 10/08/2005 2:02:02 PM"`
`  timestomp.exe c:\test.txt -a "Saturday 10/08/2005 2:02:02 PM"`
`  `![`Image:2.jpeg`](2.jpeg "Image:2.jpeg")

3\) Move that file to another folder (*c:\argument\test.txt*)

`  `![`Image:3.jpeg`](3.jpeg "Image:3.jpeg")
`  `
`  $STANDARD_INFORMATION values are copied to $FN MACE values`

4\) Update accessed and modified timestamps in \$STANDARD_INFORMATION

`  timestomp.exe c:\argument\test.txt -m "Saturday 10/08/2005 2:02:02 PM"`
`  timestomp.exe c:\argument\test.txt -a "Saturday 10/08/2005 2:02:02 PM"`
`  `![`Image:4.jpeg`](4.jpeg "Image:4.jpeg")

## External Links

- [Download
  Timestomp.exe](http://metasploit.com/data/antiforensics/timestomp.exe)
- [Presentation at Blackhat
  2005](https://www.blackhat.com/presentations/bh-usa-05/bh-us-05-foster-liu-update.pdf)