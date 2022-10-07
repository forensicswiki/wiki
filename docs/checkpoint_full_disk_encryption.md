---
tags:
  -  Tools
  -  Windows
  -  Disk Encryption
  -  Encryption 
---
Checkpoint Disk Encryption, formerly known as Pointsec, aka End Point
Encryption is a package for encrypting Windows PC disks. See the
Checkpoint site for all current information.

## Items of interest to Forensics people

\- It comes in two flavors, boot password protect and Windows
Pass-through. Boot protect means you're going to need the key. Windows
pass-through means you can attack the OS to get to the underlying data
(on a working copy, of course). Once you have an OS key, you can use a
fresh copy to assemble evidence.

\- Checkpoint(sec) does supply boot drivers that allow you to mount a
pass-through volume inside a BartPE environment. Very useful. Drivers
are available from Checkpoint.

--[Digitaltrustllc](user:digitaltrustllc.md) 19:42, 2 November
2009 (UTC)