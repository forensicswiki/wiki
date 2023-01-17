---
tags:
  - No Category
---
### URL Signatures

When a user views a JPEG or PNG from Facebook (from a profile, album,
etc.) the URLs tend to have "fbcdn" or "facebook" in the hostname.
Profile pictures tend to contain "profile" in the hostname as well. To
that subset of URLs you can apply all of these regular expressions to
capture the user ID who owned that particular image. The a, s, n, and q
characters in the URL refer to the size of the image. There are a few
main varieties of image URLs, and these three expressions should help
you parse them.

- /\d+_(\d+)_\d+_\[qs\]\\. *q is small, s is large*
- \[as\](\d+)_\d+_\d+\\. *s is small, a is large*
- \d+_\d+_(\d+)_\d+_\d+_\[asnq\]\\. ''s is small, a is medium, n is
  large, q is square'

## See also

### Residual Data

- ["Facebook
  Forensics"](https://www.sans.org/digital-forensics-incident-response/),
  SANS Computer Forensics and Incident Response Blog Entry, June
  11, 2009. A few musings and links (that are reported above). Mostly
  with tracking photos to facebook.
- ["Facebook Memory
  Forensics"](https://www.sans.org/digital-forensics-incident-response/),
  SANS Computer Forensics Incident Response Log, Nov. 20, 2009.
  Discussion about facebook details left in memory.
- [Facebook Chat
  Forensics](http://forensicsfromthesausagefactory.blogspot.com/2009/03/facebook-chat-forensics.html),
  March 20, 2009, details of how to recover chat from the JavaScript and
  JSON entries.
- ["Facebook
  Forensics"](https://sites.google.com/site/valkyriexsecurityresearch/announcements/facebookforensicspaperpublished),
  Valkyrie-X Security Research Group, July 5, 2011. Notes the groups
  successes and failures in recovering Facebook artifacts from RAM and
  storage.

### Network Forensics

- [Netresec](https://www.netresec.com/?page=Bloghttp://www.netresec.com/?page=Blog&month=2011-01&post=Facebook-SSL-and-Network-Forensicsmonth=2011-01http://www.netresec.com/?page=Blog&month=2011-01&post=Facebook-SSL-and-Network-Forensicspost=Facebook-SSL-and-Network-Forensics),
  January 30, 2011, thoughts about the impact of Facebook's SSL decision
  on network forensics.

### Tools

- [Facebook Forensic Toolkit](http://www.google.com) eDiscovery
  toolkit to identify and clone full profiles; including wall posts,
  private messages, uploaded photos/tags, group details, graphically
  illustrate friend links, and generate expert reports.
- [Belkasoft Evidence Center](https://belkasoft.com/) allows for carving
  Facebook data such as chats, wall posts and photos from Live RAM
  dumps, hibernation and pagefiles.
- [Belkasoft Facebook Profile
  Saver](https://belkasoft.com/x) is a free
  utility to download Facebook wall posts and photoalbums to a local
  computer.
- [WebPreserver](https://webpreserver.com/facebook-forensics/) captures
  Facebook wall posts and about information as well as metadata in a
  legally authenticated manner.