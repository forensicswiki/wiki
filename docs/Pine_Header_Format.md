[Pine](Pine "wikilink") composes headers in the following format:

    Date: Tue, 6 Mar 2007 11:10:36 -0500 (EST)
    From: Sender Name <sender@host.com>
    To: Getter Name <getter@otherhost.com>
    cc: Other Person <somebody@somehost.com>
    Subject: The subject text
    Message-ID: <Pine.LNX.4.64.0703061056380.29699@host.com>

Using the function `generate_message_id` in the file `reply.c` we can
see that the format for the Message-ID line is a series of fields
separated by periods, followed by the `@` symbol and the hostname of the
sending machine. The fields are

1.  The word `Pine`
2.  A three letter version of the operating system name (e.g. `LNX` for
    Linux)
3.  The major version of Pine
4.  The minor version of Pine
5.  A number YYMMDDHHmmssX, Where YY is the last two digits of the year,
    MM the current month, DD the current day of the month, HH the
    current hour, mm the current minute, ss the current second, and X is
    either a zero or one depending on the number of seconds.
6.  The current process ID number

Note that the timestamp in the Message-Id may not necessarily match the
`Date` line.

The hostname can be [ROT-13](ROT-13 "wikilink") encrypted on some
configurations. If the hostname is not defined, the value `huh` will be
used.