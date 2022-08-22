The following indicators may indicate that the user of a computer system
is trying to hide their presence, implicate another individual, convey
erroneous information, or otherwise attempt to deceive a forensic
analysis or tool.

Unfortunately, many of the deception indicators are also indicators of
good security practice.

## File System Indicators

- Files having the wrong extension (e.g. file.jpg instead of file.doc).
- Very large files (may indicate use of cryptographic file systems,
  virtual machines, etc.)
- Virtual Machine Players (VMWare, VirtualBox, Parallels)
- TrueCrypt or RealCrypt
- PGP files or Volumes
- PointSec
- Encrypted email
- Date or time wrong
- Repeating data over the drive
- Truncated history files

## Log File Indicators

Log files that are:

- Missing
- Truncated
- With time gaps
- With one or more incomplete lines, or other lines that start midway
  (happens if the attacker removes the last 4K of a file without respect
  to line boundaries)
- Inconsistencies (e.g. email that is forwarded without being received.)

## Network Communications

- Presence or use of VPN software.
- Use of anonymity websites, such as:
  - anonymizer.com
  - hidemyass.com
  - Open Proxy Servers (got a list?)
- hushmail.com
- Setting a proxy server
- ssh

## Redaction Indicators

- Evidence Eliminator
- ccleaner
- list of Drive Cleaner tools; searches for drive cleaning software