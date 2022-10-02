---
tags:
  - Database File Formats 
---
PFC files are files associated with America Online (AOL). PFC (Personal
Filing Cabinet) is a database file that enables the users to save AOL
emails locally on the computer’s hard drive. It also stores all the
received and sent emails of America Online email client. The PFC file
enables the user to manage and access the AOL mails when the user needs
to work without the presence of internet connectivity. PFC file enables
to create custom folders in it for making it easier for the user to
identify the mails. Each username in AOL has only one PFC file
associated with it, which can be viewed only via AOL. In addition to
this, the PFC file cannot be accessed from any other computer or even if
the user signs as a guest in his own computer.

## File Signature

- **Hexadecimal**: 41 4F 4C 56 4D 31 30 30
- **ASCII** : AOLVM100

## Contents

It contains attributes like emails, URLs, bookmarks, preferences,
configuration data, etc. When it comes to the attachments associated
with the AOL emails, the attachments are not stored in the PFC file.
Thus, the attachments embedded in the AOL emails cannot be opened
manually. These inline body attachments of AOL emails are stored in
encoded 64 bit structure.

## Location

The location of the AOL PFC mail store is:

1.  **In Windows XP(AOL 9.0)** - C:\Documents and Settings\All
    Users\Application Data\AOL\C_AOL9.0\Organize
2.  **In Windows 7(AOL 9.7)** - C:\ProgramData\AOL\C_AOL Desktop
    9.7\backup
3.  **In Windows 10(AOL 9.7)** - C:\ProgramData\AOL\C_AOL Desktop
    9.7\backup

## Tools

- [Free AOL PFC Viewer](http://www.systoolsgroup.com/aol-pfc-viewer/)
- [PFC File Viewer](http://datahelp.in/pfc/viewer.html)
- [AOL PFC Converter](https://www.systoolsgroup.com/aol-pfc-converter/)
- [Digital Detective Blade®
  Professional](http://www.digital-detective.net/digital-forensic-software/blade/)