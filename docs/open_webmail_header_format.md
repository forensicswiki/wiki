---
tags:
  - No Category
---
    From: "Username" <username@sendinghost.com>
    To: "Username" <username@receivinghost.com>
    Subject: Header test
    Date: Thu, 2 Aug 2007 20:54:36 +0400
    Message-Id: <20070802165414.M43479@sendinghost.com>
    X-Mailer: Open WebMail 2.50 20050106
    X-OriginatingIP: 255.255.255.255 (username@sendinghost.com)
    MIME-Version: 1.0
    Content-Type: text/plain; charset=koi8-r

Message-ID format:

    openwebmail/openwebmail-tool.pl
       # fake a messageid for this message
       my $fakedid = ow::datetime::gmtime2dateserial().'.M'.int(rand()*100000);
       $fakedid="<$fakedid".'@'."${$config{'domainnames'}}[0]>";