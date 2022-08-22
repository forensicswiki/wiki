**Email Headers** are lines of [metadata](metadata "wikilink") attached
to each [email](email "wikilink") that contain lots of useful
information for a [forensic
investigator](forensic_investigator "wikilink"). However, email headers
can be easily forged, so they should never be used as the only source of
information.

## Making Sense of Headers

There is no single way to make sense of email headers. Some examiners
favor reading from the bottom up, some favor reading from the top down.
Because information in the headers can be put there by the user's
[MUA](Mail_User_Agent "wikilink"), a server in transit, or the
recipient's [MUA](Mail_User_Agent "wikilink"), it can be difficult to
determine when a line was added.

### Sender's IP Address

Some web-based email providers include the sender's IP address in the
message headers. Some do not.

### Mail User Agents

Every [MUA](Mail_User_Agent "wikilink") sets up the headers for a
message slightly differently. Although some headers are required under
the applicable [RFC](http://www.faqs.org/rfcs/rfc2822.html), their
format and ordering can vary by client. Almost all clients, however, add
their headers in a fixed format and order. The examiner can use the
format and order for each client to show that messages were forged, but
not that they were legitimate. For example, if a message purports to be
from [Apple Mail](Apple_Mail "wikilink") but the order or the headers do
not match the [Apple Mail Header
Format](Apple_Mail_Header_Format "wikilink"), the message has been
forged. If the headers of the message do match that format, however, it
does not guarantee that the message was sent by that program.

### Servers in Transit

Mail servers can add lines onto email headers, usually in the form of
"Received" lines, like this:

    Received: by servername.recipeienthost.com (Postfix, from userid 506)
        id 77C30808A; Sat, 24 Feb 2007 20:43:56 -0500 (EST)

## Message Id Field

. According to the current guidelines for email
[1](http://www.faqs.org/rfcs/rfc2822.html), every message should have a
Message-ID field. These id fields can be used to determine if a message
has been forged. It is harder, but sometimes possible, to show that a
message is authentic using the message id field. Where known, the
Message-ID algorithms for known programs are [given on the separate
pages for those programs](List_of_MUA_Header_Formats "wikilink").

## Signature Fields

. Some email programs allow users to sign messages. This gives the
recipient some assurance that the sender given in the message really
sent the message. Obviously these headers can be used by an examiner for
the same purpose.

## Sample Header

This is an (incomplete) excerpt from an email header:

`Received: from lists.securityfocus.com (lists.securityfocus.com [205.206.231.19])`
`        by outgoing2.securityfocus.com (Postfix) with QMQP`
`        id 7E9971460C9; Mon,  9 Jan 2006 08:01:36 -0700 (MST)`
`Mailing-List: contact forensics-help@securityfocus.com; run by ezmlm`
`Precedence: bulk`
`List-Id: <forensics.list-id.securityfocus.com>`
`List-Post: <`[`mailto:forensics@securityfocus.com`](mailto:forensics@securityfocus.com)`>`
`List-Help: <`[`mailto:forensics-help@securityfocus.com`](mailto:forensics-help@securityfocus.com)`>`
`List-Unsubscribe: <`[`mailto:forensics-unsubscribe@securityfocus.com`](mailto:forensics-unsubscribe@securityfocus.com)`>`
`List-Subscribe: <`[`mailto:forensics-subscribe@securityfocus.com`](mailto:forensics-subscribe@securityfocus.com)`>`
`Delivered-To: mailing list forensics@securityfocus.com`
`Delivered-To: moderator for forensics@securityfocus.com`
`Received: (qmail 20564 invoked from network); 5 Jan 2006 16:11:57 -0000`
`From: YJesus <yjesus@security-projects.com>`
`To: forensics@securityfocus.com`
`Subject: New Tool : Unhide`
`User-Agent: KMail/1.9`
`MIME-Version: 1.0`
`Content-Disposition: inline`
`Date: Thu, 5 Jan 2006 16:41:30 +0100`
`Content-Type: text/plain;`
`  charset="iso-8859-1"`
`Content-Transfer-Encoding: quoted-printable`
`Message-Id: <200601051641.31830.yjesus@security-projects.com>`
`X-HE-Spam-Level: /`
`X-HE-Spam-Score: 0.0`
`X-HE-Virus-Scanned: yes`
`Status: RO`
`Content-Length: 586`
`Lines: 26`

## External Links

- [Wikipedia entry on email
  headers](http://en.wikipedia.org/wiki/E-mail#Header)

### Tools

- [MailXaminer product page](http://www.mailxaminer.com/product/)
- [Wikipedia: MailXaminer](https://en.wikipedia.org/wiki/MailXaminer)