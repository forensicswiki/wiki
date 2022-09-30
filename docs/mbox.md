---
tags:
  -  Email
---
MBOX is a generic name to the family of related files that holds a
collection of email messages in a single file. MBOX files are simple
flat text files that have individual email messages concatenated to the
end of file.

mbox (RFC 4155) stores mailbox messages in their original Internet
Message (RFC 2822) format, usually in files directly accessible to users

## Overview

Traditionally, the MBOX file structure follows a rule of keeping all the
mail messages assigned to a single folder and preserves the indexes of
the email messages. The MBOX mailbox format stores messages in
accordance with the RFC2822 file format. MBOX files were primarily used
in UNIX but are now used for storing email messages in several email
clients like Mozilla thunderbird, Envoy, Eudora, Entourage.

## File Structure

The starting of each mailbox message is with a line that consists of
“From” followed by a space and then the email address of sender. In
order to differentiate one message from another, a blank line is
appended at the end of each message. Because of its plain text format, a
number of text processing utilities can be employed on the MBOX file
format.

## MBOX File Variants

There are four different forms of MBOX file format that are discussed as
follows

1.  mboxo
2.  mboxrd
3.  mboxcl
4.  mboxcl2

### mboxo File Format

The mboxo file format employs the original System V format. It follows
an irreversible “From quoting” that usually corrupts a message. To
locate the beginning of a message in mboxo mailbox format, one has to
scan ahead to find the next “From” line. If on reaching the end of file
there are no email messages then there are no next messages.

### mboxrd File Format

The idea for mboxrd file format was coined by Rahul Dhesi and so the
mailbox format has been named according to his name. It follows a
reversible “From quoting” that is used to resolve the corruption
problems found in mboxo mailbox format. To locate the starting point of
a message in mboxrd file format, on starts moving in the forward
direction of “From” line till it reaches the end of the file.

### mboxcl File Format

The mboxcl message format employs irreversible “From quoting” that
generally corrupts a message. To locate the starting of each message, it
does not use From_ line-scanning rather it uses Content: Length which
presents the length of the message body after it is converted into
octets. One can use the header of the message to trace for the next
message.

### mboxcl2 File Format

The mboxcl2 file format does not use “From” quoting. It does not use
From_line to scan a line in the message .Instead, it consists of a
Content-Length: header which describes the message length in octets.
This header is appended to the email message when it is added to the
mailbox and can be used to trace the beginning of each message.

## Support

As mbox is a cross-platform email storage medium, it is accessible on
Operating System besides Windows i.e. in Linux and Mac OS X. However,
the similar requirements apply to access an MBOX folder on other
Operating System as well i.e. the supported email application(s).

## External Links

- [Wikipedia: Mbox](http://en.wikipedia.org/wiki/Mbox)
- [RFC 4155: The application/mbox Media
  Type](http://tools.ietf.org/html/rfc4155), by E. Hall, September 2005
- [RFC 2822: Internet Message
  Format](http://tools.ietf.org/html/rfc2822), by P. Resnick, April 2001

## Tools

- [MBOX Forensics Wizard](https://forensiksoft.com/mbox-forensics.html)
  View and convert mbox files. Forensically analyze a MBOX file and also
  perform search inside MBOX emails to locate a particular evidence.
- [Aid4Mail](aid4mail.md)
- [mbox-extract-attachments.py](https://raw.githubusercontent.com/PabloCastellano/pablog-scripts/master/mbox-extract-attachments.py)
- [Windows MBOX Converter](http://www.bitrecover.com/mbox-converter/)
  Converts mbox email messages from Thunderbird, Postbox, Netscape,
  Evolution, SeaMonkey, Sylpheed, Mulberry, GyazMail, Claws Mail, Gnu,
  Sparrow, the Bat, Apple Mail, Entourage, PowerMail, PocoMail, Eudora,
  Spicebird, WebMail or Opera Email client into PDF, PST, EML, MSG,
  EMLX, RTF, HTML.
- [MBOX File Viewer](http://datahelp.in/mbox/viewer.html)
- [FREE MBox Viewer](http://www.freeviewer.org/mbox/)
- [MBOX Viewer](mbox_viewer.md)
- [Paraben's Email Examiner](paraben's_email_examiner.md)

[Category:Email](category:email.md) [Category:File
