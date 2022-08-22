    Subject: header test
    From: Username <username@sendinghost.com>
    To: Username <username@receivinghost.com>
    Content-Type: text/plain
    Date: Sat, 28 Jul 2007 11:52:35 +0200
    Message-Id: <1185616355.19231.0.camel@localhost>
    Mime-Version: 1.0
    X-Mailer: Evolution 2.10.1
    Content-Transfer-Encoding: 7bit

The Message id consists of five parts:

1.  The current time as returned by the `time` function followed by a
    period. The value is dislayed in decimal and is the number of
    seconds since midnight on 1 Jan 1970. In the example above,
    1185616355 refers to Sat, 28 Jul 2007 09:52:35 GMT.
2.  The process id number in decimal followed by a period
3.  The third value starts at zero but may increase as more messages are
    sent. It is also followed by a period
4.  The word `camel` followed by an '@'
5.  If the canonical hostname can found, it is used. Otherwise the
    hostname

The Message id format comes from the function
`camel_header_msgid_generate` in
`evolution-data-server/camel/camel-mime-utils.c`.

[Category:Email Analysis](Category:Email_Analysis "wikilink")