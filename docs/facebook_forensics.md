---
tags:
  - Articles that need to be expanded
---
When a user views a JPEG or PNG from Facebook (from a profile, album,
etc.) the URLs tend to have "fbcdn" or "facebook" in the hostname.
Profile pictures tend to contain "profile" in the hostname as well. To
that subset of URLs you can apply all of these regular expressions to
capture the user ID who owned that particular image. The a, s, n, and q
characters in the URL refer to the size of the image. There are a few
main varieties of image URLs, and these three expressions should help
you parse them.

* "/\d+\_(\d+)\_\d+\_\[qs\]\\.", where "q" represents small and "s" large
* "\[as\](\d+)\_\d+\_\d+\\.", where "s" represents small andd "a" large
* "\d+\_\d+\_(\d+)\_\d+\_\d+\_\[asnq\]\\.", where "s" represents small, "a"
  medium, "n" large and "q" square

## External Links

### Residual Data

* [Facebook Chat Forensics](http://forensicsfromthesausagefactory.blogspot.com/2009/03/facebook-chat-forensics.html),
  March 20, 2009, details of how to recover chat from the JavaScript and
  JSON entries.
* [Facebook Forensics](https://sites.google.com/site/valkyriexsecurityresearch/announcements/facebookforensicspaperpublished),
  Valkyrie-X Security Research Group, July 5, 2011. Notes the groups
  successes and failures in recovering Facebook artifacts from RAM and
  storage.

### Network Forensics

* Thoughts about the impact of Facebook's SSL decision on network forensics,
  by Netresec, January 30, 2011

### Tools

* [Facebook Forensic Toolkit](http://www.google.com) eDiscovery
  toolkit to identify and clone full profiles; including wall posts,
  private messages, uploaded photos/tags, group details, graphically
  illustrate friend links, and generate expert reports.
* [Belkasoft Evidence Center](https://belkasoft.com/) allows for carving
  Facebook data such as chats, wall posts and photos from Live RAM
  dumps, hibernation and pagefiles.
