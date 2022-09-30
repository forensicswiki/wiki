---
tags:
  -  Email Analysis
---
The **Yahoo! Web Mail** header format has changed over time, but
currently includes the [sender's IP
address](ip_addresses_in_webmail_messages.md), a domain key
signature, and some other helpful information.

DomainKey-Signature

    DomainKey-Signature: a=rsa-sha1; q=dns; c=nofws;
      s=s1024; d=yahoo.com;
      h=Received:Date:From:Subject:To:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID;
      b=ql3kRKrhner1LTFFVBgCYI1uqK4+8hrb6d/Fefr/HkLuObQwIrIpEXA1OiagbuFZU+H+ue1anFvm1cHQ4hjpdUcjpIIPL7ldNL9YnOxauugdVW+
      OpbTvAu0XaGf2t7eBqOWJF0Y5gM7TE27WdElgVRikunfCQca1VFV6KSuQP0o=;

Here is a sample mail header. Note that the 'date' field will change
from (PDT) to (PST) depending on the status of daylight savings time in
California, USA. The sender's IP address is represented as a.b.c.d in
the example below.

Mail Header

    Received: from [a.b.c.d] by web53409.mail.re2.yahoo.com via HTTP; Sat, 14 Feb 2009 05:42:03 PST
    X-Mailer: YahooMailWebService/0.7.260.1
    Date: Sat, 14 Feb 2009 05:42:03 -0800 (PST)
    From: Sender Name <sender@yahoo.com>
    Reply-To: sender@yahoo.com
    Subject: Test Message
    To: recipient@domain.com
    MIME-Version: 1.0
    Content-Type: text/plain; charset=us-ascii
    Message-ID: <695976.86300.qm@web53409.mail.re2.yahoo.com>

## Message IDs

The Message-ID header in yahoo emails is a good identifier for the
device that sent the message. Below are some samples:

Sent via Yahoo!® Mail for Android application on Android (Jelly Bean):

    Message-ID: <1332714176.54741.androidMobile@web141101.mail.bf1.yahoo.com>

Sent via Yahoo Webmail from Chrome:

    Message-ID: <1332793663.59921.YahooMailNeo@web121601.mail.bf1.yahoo.com>

Sent via Android browser on via mobile webmail interface:

    Message-ID: <1332792527.64712.BPMail_high_noncarrier@web121601.mail.bf1.yahoo.com>

Sent via Android email application configured for SMTP (jelly bean):

    Message-ID: <gf4yxl2u7us2lp89xkgbty9u.1342797846221@email.android.com>

Sent via iPod (IOS 5.0.1)

    Message-ID: <1341798412.80181.YahooMailMobile@web124306.mail.ne1.yahoo.com>

## Also See

- [Yahoo Forensics](https://www.systoolsgroup.com/forensics/yahoo/)
- [Yahoo Backup](https://www.systoolsgroup.com/yahoo-backup.html)

