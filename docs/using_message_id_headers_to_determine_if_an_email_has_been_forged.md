---
tags:
  -  Howtos
---
According to the RFCs for email, [RFC
822](http://www.faqs.org/rfcs/rfc822.html) and [RFC
2822](http://www.faqs.org/rfcs/rfc2822.html), every email
[should](http://www.faqs.org/rfcs/rfc2119.html) have a message id field
that: "provides a unique message identifier that refers to a particular
version of a particular message. The uniqueness of the message
identifier is guaranteed by the host that generates it. ... This message
identifier is intended to be machine readable and not necessarily
meaningful to humans. A message identifier pertains to exactly one
instantiation of a particular message; subsequent revisions to the
message each receive new message identifiers."

The message id headers can prove useful when trying to determine if a
email is authentic. Although they can't always prove that message is
authentic, they can often show that a message has been forged.

## Repeated Message ID

In this case, the forger, when creating a fake email, reuses the headers
belonging to an earlier message. The examiner need only compare the
Message-ID from the email in question to all of the other email messages
in the world. Ok, probably not <em>all</em> of the other email messages
out there. Usually just the messages on the systems in question are good
enough. But finding the same message id on the "smoking gun" email
<em>and</em> an old guacamole recipe can be used as evidence that a
message was forged.

## Impossible Message ID

This case is more subtle, but can be used quite effectively. Although
the RFC states that the message id should be globally unique, it says
nothing about how it should be constructed. Most email programs have
their own format for generating the message id. For example, [Apple
Mail](apple_mail_header_format.md) uses a [Universally Unique
Identifier](universally_unique_identifier.md) and the sender's
domain. [Thunderbird](thunderbird_header_format.md), on the
other hand, uses a combination of the time the message was sent, a salt,
and the sender's domain.

Sample Apple Mail Message ID:

    38D1C1FD-3C35-4568-925C-FC46CAC0DE8A@sendinghost.com

Sample Thunderbird Message ID:

    41B5F981.5040504@sendinghost.com

If a message was purportedly sent by a certain email program but does
not have a message id created by that program, it has obviously been
forged. It would be like a round cookie-cutter making square holes; it
just can't happen. Thus, if somebody claims that they received an
authentic email, look at the message-id and the format of the headers.
If the message id does not match the format for that program, the
message has been forged!

## See Also

- [Email Headers](email_headers.md)
- [Using signature headers to determine if an email has been
  forged](using_signature_headers_to_determine_if_an_email_has_been_forged.md)

