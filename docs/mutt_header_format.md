---
tags:
  - No Category
---
    Date: Sat, 28 Jul 2007 18:29:15 +0200
    To: Username <username@receivinghost.com>
    Subject: header test
    Message-ID: <20070728162915.GA2046@localhost>
    MIME-Version: 1.0
    Content-Type: text/plain; charset=us-ascii
    Content-Disposition: inline
    User-Agent: Mutt/1.5.13 (2006-08-11)
    From: Username <username@sendinghost.com>

The format of the Message id field is:

1.  Four digits for the current year
2.  Two digits for the current month
3.  Two digits for the current day of the month
4.  Two digits for the current hour
5.  Two digits for the current minute
6.  Two digits for the current second
7.  A period followed by the capital letter 'G'
8.  A capital letter. The first message sent will have the letter 'A',
    the next 'B', and then 'C' until the 26th message will have 'Z'. The
    27th message sent starts again with 'A'.
9.  The current process id number
10. The '@' symbol
11. The fully qualified domain name of the sending computer.

The above was based on the function `mutt_gen_msgid` in
`mutt/sendlib.c`.