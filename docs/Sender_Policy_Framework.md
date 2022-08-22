**Sender Policy Framework** (**SPF**) is a system to eliminate spam
based on the idea that only certain computers should be allowed to send
mail for a given domain. SPF allows a domain's owner to specify which
hosts may send mail purporting to be from that domain by creating
**TXT** type records in the DNS for the domain. Unlike [DomainKeys
Identified Mail](DomainKeys_Identified_Mail "wikilink"), only source
hosts/addresses may be specified, meaning that should a host/ip address
be compromised (such as by [Address Resolution
Protocol](Address_Resolution_Protocol "wikilink") spoofing on an
ethernet segment, or system compromise), unauthorized messages may still
be sent originating from the given source address and would be accepted
based on the SPF record. Any number of hosts may be specified in the TXT
record for a given domain, and pointers to SPF records in other DNS
zones may be included as well.

## External Links

- [Sender Policy Framework project website](http://www.openspf.org/)
- [RFC 4408 - "Sender Policy Framework (SPF) for Authorizing Use of
  Domains in E-Mail, Version 1"](http://www.ietf.org/rfc/rfc4408.txt)
- [Wikipedia entry on Sender Policy
  Framework](http://en.wikipedia.org/wiki/Sender_Policy_Framework)