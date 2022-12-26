---
tags:
  -  Howtos
---
Email signatures, designed for authentication, non-repudiation, and spam
control, can also be used to determine if an email has been forged. In
the most common case, the forger copies headers from an existing email
message to a new one. He could also attempt to change the content of a
signed message. Regardless, the signature no longer corresponds to the
message and it can be shown that the message is not authentic.

## Sender Policy Framework

Sender Policy Framework, or SPF records, can be used to enumerate which
hosts are allowed to send mail for that domain. If a message purports to
be from *example.com* but came from an IP address that is not
authorized, under SPF, to send mail for that domain, it has been forged.
As an example, let's say we have an email purporting to be from
`lexluthor@mit.edu` using the IP address `4.61.91.6`. An investigator
can query the DNS records from that domain, in this case `mit.edu` to
see the SPF senders.

    $ host -t txt mit.edu
    mit.edu descriptive text "v=spf1 ip4:18.7.7.0/24 ip4:18.7.21.0/24  ip4:18.72.0.0/16 ~all"

Here we see that there are three computers authorized to send mail for
the `mit.edu` domain. None of them have the IP address found on the
message, so the email in question may be forged.

## DomainKeys Identified Mail

These headers, included by the mail server, provide a signature of each
message. See [Gmail Header Format](gmail_header_format.md). The public keys are
distributed via DNS.

## Signed mail

Some other programs can be used by the sender to sign an email message.
Programs such as [PGP](pgp.md), [GnuPG](gnupg.md).

### PGP Messages

Messages sent using PGP, or its free equivalents such as GnuPG, have the
signature in the message body itself. Each message can be signed,
encrypted, or both. Encrypted messages begin with the header

    -----BEGIN PGP MESSAGE-----

followed by some optional headers. The optional headers may include the
character set of the decoded message, the program and version that
created the message, and an optional comment. The end of the message is
noted with

    -----END PGP MESSAGE-----

Between these two lines are a series of ASCII characters that represent
the encrypted or signed message.

A signed message has the header

    -----BEGIN PGP SIGNATURE-----

at the *end* of the signed message followed by the same optional headers
as encrypted messages. The signature is usually three lines of ASCII
characters.

## See Also

- [Using message id headers to determine if an email has been
  forged](using_message_id_headers_to_determine_if_an_email_has_been_forged.md)

