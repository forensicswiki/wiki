---
tags:
  - No Category
---
Because Gmail is a web based application and can be changed at any time, the
information in this article may not reflect the current state of Gmail headers.
In general Gmail headers have a [DomainKeys Identified Mail](domainkeys_identified_mail.md)
signature line that contains a signature for the message in question. These
lines appear above the standard Message-ID fields. These signatures are of the
format:

    DKIM-Signature: a=rsa-sha1; c=relaxed/relaxed;
            d=gmail.com; s=beta;
            h=domainkey-signature:received:received:message-id:date:from:to:subject:mime-version:content-type;
            b=OITvzFGKQQUjywUQB7U8dQypDAeOGqBIhfcb8VKioP2UU5P2aJL3l2adoyRqSp9h/Fo9A6wY5EIRsfaCWM9ge+EzCob/
    4p85jcEn3uW8dpRyBFQXMuK2q0RMIk3FznrXAM4W5FvoJIPP04qgXErar+/hZq03vEUIErV1v6p2Fy4=
    DomainKey-Signature: a=rsa-sha1; c=nofws;
            d=gmail.com; s=beta;
            h=received:message-id:date:from:to:subject:mime-version:content-type;
            b=oC+hlWhBboQ+RlsKCL4r2pQxpgKRM9iUgCBmw9wZqlEcxj+A3q+fJkDXgLKmI1twfvTHj7GQ3HDzSLzw982UD
    +CPh1bPQxkhNbylUBRtwpoFeixIk7OmR2YE1iYrYpQXf3dEcXNfKs7ffoeY18plJNJG0S8RRmXLaR6XqXFVUoo=

Note that some of the `Received` lines will contain hosts with IP
addresses like 10.x.x.x. These addresses are non-routable but part of
the Gmail system. The remaining headers look like:

    Message-ID: <f6a363400703050910y7d591d42raf015fcef16f95ea@mail.gmail.com>
    Date: Mon, 5 Mar 2007 09:10:41 -0800
    From: UserName <address@gmail.com>
    To: OtherUserName <address@system.com>
    Subject: Subject Line
    MIME-Version: 1.0

## Message Id Field

Although the message id format is not completely understood, it contains the 
date and time the message was sent, in pacific time, starting at the ninth 
digit, in the form YYMMDDHHMM. In the example above, the time/date is 
`0703050910`, 0910 PDT on 5 Mar 2007. This has been confirmed by experimental 
testing. If you are [trying to determine if a message has been forged](using_signature_headers_to_determine_if_an_email_has_been_forged.md), 
you should verify that the time in the Message Id field matches the time in the 
Date field for the message. Don't forget that the time in the Date field should 
be in the Sender's local time and the Message Id will be in Google's local 
time, US Pacific Time.

## See Also

- [Using message id headers to determine if an email has been forged](using_message_id_headers_to_determine_if_an_email_has_been_forged.md)

## External Links

- [Gmail](https://www.google.com/gmail/about/)
- [DKIM Signatures](http://www.elandsys.com/resources/sendmail/dkim.html)
