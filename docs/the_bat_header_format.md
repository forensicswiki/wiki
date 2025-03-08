---
tags:
  -  File Formats
  -  Articles that need to be expanded
---
The Bat! v3

    Date: Mon, 6 Aug 2007 00:41:44 +0200
    From: Username <username@sendinghost.com>
    X-Mailer: The Bat! (v3.95.8) Professional
    X-Priority: 3 (Normal)
    Message-ID: <1398886086.20070806004144@sendinghost.com>
    To: Username <username@receivinghost.com>
    Subject: header test. the bat
    MIME-Version: 1.0
    Content-Type: text/plain; charset=us-ascii
    Content-Transfer-Encoding: 7bit
    Content-Type: multipart/mixed; boundary="----------069134143049E2085"

    
Message-ID format:

`Message-ID` consists of 4 parts

* A random string of numbers
* A timestamp of the format YYYYmmDDHHMMSS
* The `@` symbol
* The domain of the sending host

As at March 2025, there is [an interesting nuance](https://www.bentasker.co.uk/posts/blog/security/seducing-a-romance-scammer.html#scheduled-sending) in `Message-ID` when used with the mail agent's [Postponed Sending](https://www.ritlabs.com/en/products/thebat/postponed.php) feature. When a mail's sending is postponed, the `Date` header will be updated accordingly, but the timestamp within the Message ID _will not_.

    
## External Links

## Tools

- [Aid4Mail](aid4mail.md) - convert The Bat! email messages to
  other formats
- [The Bat! Viewer &
  Converter](https://www.bitrecover.com/bat-converter/) View and convert
  your The Bat! tbb email messages stored in messages.tbb
- [The Bat! MailXaminer
  support](https://www.mailxaminer.com/blog/the-bat-mailbox-forensic-analysis/)
  The Bat! related file extensions and logs

