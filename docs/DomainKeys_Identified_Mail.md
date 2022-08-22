**DomainKeys Identified Mail** (**DKIM**) is a method for signing email
messages to help eliminate spam.

The signature in each message should give the domain (`d=`) and selector
(`s=`). The appropriate key can be retrived as a TXT
[DNS](Domain_Name_System "wikilink") record from the host
*`selector`*`._domainkey.`*`domain`*
[1](http://www.elandsys.com/resources/sendmail/dkim.html). A sample
message from Gmail had the following DKIM header:

    DKIM-Signature: a=rsa-sha1; c=relaxed/relaxed;
            d=gmail.com; s=beta;

We can thus retrieve the Gmail key with:

    $ host -t txt beta._domainkey.gmail.com
    beta._domainkey.gmail.com descriptive text "t=y\; k=rsa\; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC69TURXN3oNfz+G/m3g5rt4P6nsKmVgU1D6cw2X6BnxKJNlQKm10f8tMx6P6bN7juTR1BeD8ubaGqtzm2rWK4LiMJqhoQcwQziGbK1zp/MkdXZEWMCflLY6oUITrivK7JNOLXtZbdxJG2y/RAHGswKKyVhSP9niRsZF/IBr5p8uQIDAQAB"

## External Links

- [Official website](http://www.dkim.org/)
- [Wikipedia entry on
  DKIM](http://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)
- [Dan Kegel's mini-howto on checking a DKIM
  signature](http://kegel.com/validating-email-with-dkim.html)