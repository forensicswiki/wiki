---
tags:
  - No Category
---
[Apple Mail](apple_mail.md) version 2.1 generates [email
headers](email_headers.md) in the following format:

    Mime-Version: 1.0 (Apple Message framework v752.2)
    Content-Transfer-Encoding: 7bit
    Message-Id: <38D1C1FD-3C35-4568-925C-FC46CAC0DE8A@sendinghost.com>
    Content-Type: text/plain;
        charset=US-ASCII;
        format=flowed
    To: Other User <otheruser@receivinghost.com>
    From: User Name <username@sendinghost.com>
    Subject: Subject Line
    Date: Mon, 26 Feb 2007 20:21:57 -0500

The message-id appears to be a random, or version 4, [Universally Unique
Identifier](universally_unique_identifier.md). By default [Mac
OS X](mac_os_x.md) includes a command line program `uuidgen`
that can be used to generate such values.