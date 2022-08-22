Version 6 of [Outlook Express](Outlook_Express "wikilink") running on
[Microsoft Windows](Microsoft_Windows "wikilink") generates headers in
the format:

    Message-ID: <000f10c7183d$abe4d510$6031a8c0@hostname>
    From: "Username" <username@sendinghost.com>
    To: "Username" <username@receivinghost.com>
    Subject: Testing
    Date: Wed, 4 Apr 2007 14:11:45 +0100
    MIME-Version: 1.0
    Content-Type: text/plain;
        charset="iso-8859-1"
    Content-Transfer-Encoding: 7bit
    X-Priority: 3
    X-MSMail-Priority: Normal
    X-Mailer: Microsoft Outlook Express 6.00.2800.1807
    X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1807

## Message ID Field

The Message-ID have 4 parts: \[hex
time\]\$\[random?\]\$\[hw-hash?\]@\[hostname\]