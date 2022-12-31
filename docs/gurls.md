---
tags:
  - Linux
  - Tools
---
Gruls is a bash script and is short for grep urls :

`#!/bin/bash`
`protocol="(ftp|http|https|gopher|mailto|pop|smtp|news|nntp|telnet|whois|file|imap|prospero|peercast|ed2k|irc|aim|mime|ftam|pnm|rtsp|ldap)"`
`ip4="([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.((0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.){2}([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])"`
`fqdn="(\w(-?\w+)*\.)+[a-z]{2,}"`
`host="(${ip4}|${fqdn})"`
`port="(:[0-9]+)?"`
`urlregexp="${protocol}://${host}${port}/?"`

`(`
`if [ "$1" ]`
`then`
`   while [ "$1" ]`
`   do`
`       egrep -o "$urlregexp" "$1"`
`       shift`
`   done`
`else`
`   egrep -o "$urlregexp" /dev/stdin`
`fi`
`) | sed 's;/$;;g'`

Once saved in /usr/local/bin/gurls and made ​​executable, gurls can be
used like this :

`root@forensic# gurls a.file an.other.file`
[`https://forensics.wiki`](https://forensics.wiki)

`root@forensic# strings /mnt/forensic/partition/pagefile.sys | gurls | sort | uniq -c | sort -n`
`     10 `[`https://forensics.wiki`](https://forensics.wiki)

`root@forensic# strings /dev/sdb1 | gurls > /tmp/urls`

## See Also

- [bulk_extractor](bulk_extractor.md) provides similar
  functionality but on a much larger scale. Still, scripts like *gurls*
  are good for quickly searching through data.
