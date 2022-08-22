**Helix3** is a [Live CD](Live_CD "wikilink") built on top of
[Ubuntu](Ubuntu "wikilink"). It focuses on [incident
response](Incident_Response "wikilink") and [computer
forensics](computer_forensics "wikilink").

According to Helix3 Support Forum, e-fense is no longer planning on
updating the free version of Helix.

## Tools Included

Helix focuses on Incident Response and forensics tools. It is meant to
be used by individuals who have a sound understanding of Incident
Response and forensic techniques.

### Bootable Side

- [The Sleuth Kit](The_Sleuth_Kit "wikilink") (3.0.0)
- [dc3dd](dc3dd "wikilink")
- [dcfldd](dcfldd "wikilink")
- [LinEn](LinEn "wikilink")
- [aimage](aimage "wikilink")

*and others.*

### Windows Side

- [FTK Imager](FTK_Imager "wikilink")
- [mdd](mdd "wikilink")
- [win32dd](WinDD "wikilink")
- [winen](winen "wikilink")
- [WFT](WFT "wikilink")
- [IRCR](IRCR "wikilink")

*and others.*

Windows side can be used to scan for pictures on a live system.

## Forensic Issues

- Helix3 will automount [Ext3](Ext3 "wikilink") /
  [Ext4](Ext4 "wikilink") file systems during the boot process and
  recover them if required (bug in *initrd* scripts);
- Helix3 can automount some storage devices like firewire devices and
  MMC in read/write mode;
- Helix3 relies on file system drivers to provide write protection,
  mounting some file system types (e.g. [XFS](XFS "wikilink")) will
  result in several data writes to the original media.

## See Also

- [Helix3 Pro](Helix3_Pro "wikilink")

## External Links

- [Helix3 CE Forum](http://forum.charlestendell.com)