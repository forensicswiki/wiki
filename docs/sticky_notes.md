---
tags:
  - No Category
---
## Sticky Notes

Sticky Notes are a feature of Windows 7 that allows a user to create
sticky notes on their desktop. The functionality of this feature is
somewhat limited, in that the user can change the text, font, color,
location and size of the sticky notes, but not much else.

Sticky Notes are maintained in a single file (stickynotes.snt) located
in the user's profile ("%UserProfile%\AppData\Roaming\Microsoft\Sticky
Notes"). This file is based on the MS [OLE/compound
file](http://msdn.microsoft.com/en-us/library/dd942138%28v=prot.13%29.aspx)
binary format. The .snt file can be opened and viewed using the [MiTec
Structured Storage Viewer](http://www.mitec.cz/ssv.html).

When sticky notes files are created, an OLE storage stream using a name
similar to "e3a17883-cfd8-11e0-8" is added to the stickynotes.snt file.
Each storage stream has three file streams associated with it, and for
all sticky notes, they are named 0, 1, and 3. The 0 stream contains the
rich text format (RTF) "document" for the sticky note, and the 3 stream
contains the actual text of the sticky note, in Unicode format.

The forensic value of Sticky Notes has yet to be determined or
demonstrated. The Root Entry of the OLE format file will have a
modification time associated with it, and each of the storage streams
the contain the sticky notes will have creation and modification times
(M and B of the MACB times) associated with them. These times are
maintained in the
[FILETIME](https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime?redirectedfrom=MSDN)
format, and can be included in a timeline of system activity in order to
demonstrate user activity on the system.

When sticky notes are deleted, the storage streams associated with those
notes are removed from the stickynotes.snt file; however, the Version
and Metafile streams remain. The Metafile stream format is not
documented at this time; however, this stream appears to contain
references to the names of the storage streams that contain the sticky
notes.

### Tools

Tools that can be used to parse and view the contents of Sticky Notes
files include (but are not limited to):

[MiTeC Structured Storage Viewer](http://www.mitec.cz/ssv.html)

Sticky Notes Parser (found at this [Google
Code](http://code.google.com/p/winforensicaanalysis/downloads/list)
site; Win32 binary command line tool, all times are displayed in UTC
format. Output formats include a listing of the available notes, CSV,
and TLN format (for inclusion in a timeline). Also displays the
modification time of the Root Entry.