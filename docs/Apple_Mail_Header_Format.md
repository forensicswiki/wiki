[Apple Mail](Apple_Mail "wikilink") version 2.1 generates [email
headers](Email_Headers "wikilink") in the following format:

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
Identifier](Universally_Unique_Identifier "wikilink"). By default [Mac
OS X](Mac_OS_X "wikilink") includes a command line program `uuidgen`
that can be used to generate such values.