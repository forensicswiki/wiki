---
tags:
  - No Category
---
[Mozilla Thunderbird](mozilla_thunderbird.md) version 1.0
running on [Microsoft Windows](windows.md) generates
[headers](email_headers.md) in the following format:

    Message-ID: <41B5F981.5040504@sendinghost.com>
    Date: Tue, 07 Dec 2004 13:42:09 -0500
    From: User Name <username@sendinghost.com>
    User-Agent: Mozilla Thunderbird 1.0 (Windows/20041206)
    X-Accept-Language: en-us, en
    MIME-Version: 1.0
    To: username@receivinghost.com
    Subject: Testing
    Content-Type: text/plain; charset=ISO-8859-1; format=flowed
    Content-Transfer-Encoding: 7bit

Extensions such as enigmail may add extra headers.

The Message-ID field has three parts:

1.  The time the message was sent in seconds past the epoch in
    hexadecimal.
2.  A random value called a salt. The salt is of the format \#0#0#0#
    where \# is a random digit. Because Thunderbird treats the salt like
    a number, it may be shorter if the leading digits are zeros. For
    example, a salt of "0030509" would display as "30509".
3.  The fully qualified domain name of the sender.

<!-- -->

    Message-ID: [time].[salt]@[domain-name]

## References

Information on the Message-ID header was derived from the source code,
specifically the function `msg_generate_message_id` in
`mozilla/mailnews/compose/src/nsMsgCompUtils.cpp`.

## Tools

- [Thunderbird MSF Viewer](https://www.bitrecover.com/free/thunderbird-viewer/) to view
  Thunderbird email messages header, message body along-with
  attachments.