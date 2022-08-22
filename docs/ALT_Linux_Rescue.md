**ALT Linux Rescue** is yet another sysadmin's [Live
CD](Live_CD "wikilink") with some forensic capabilities and features.

## Intro

This weekly-updated image is intended to be text-only toolchest for data
analysis and recovery.

It will not try to use swap partitions or autodetect and automount file
systems unless requested explicitly.

Forensic mode is available via a separate boot target for BIOS users and
a rescue boot option (via F2) for UEFI users. This will skip activating
MDRAID/LVM too.

Build profile suitable for ALT Linux `mkimage` tool is included as
`.disk/profile.tgz`.

## Tools included

Most of the usual rescue suspects should be there;
[biew](biew "wikilink"), [chntpw](chntpw "wikilink"),
[dc3dd](dc3dd "wikilink")/[dcfldd](dcfldd "wikilink"),
[foremost](foremost "wikilink"), [john](john "wikilink"),
[md5deep](md5deep "wikilink"), [nmap](nmap "wikilink"),
[scalpel](scalpel "wikilink"), [sleuthkit](sleuthkit "wikilink"),
[ssdeep](ssdeep "wikilink"), [wipefreespace](wipefreespace "wikilink")
to name a few are available either; [libevt](libevt "wikilink"),
[libevtx](libevtx "wikilink"), [liblnk](liblnk "wikilink"),
[libpff](libpff "wikilink"), [libregf](libregf "wikilink"),
[libuna](libuna "wikilink"), [libvshadow](libvshadow "wikilink"),
[libwrc](libwrc "wikilink") tools have been added since 20140514.

X11-based software is being considered for an extended version.

## Platforms

i586 (BIOS) and x86_64 (BIOS/UEFI); SecureBoot might be left enabled in
most occasions (Hyper-V gen.2 is a notable exception, looks like
Microsoft's "3rd party driver" key is lacking there; just turn SB off).

## Deliverables

Two separate 32/64-bit hybrid ISO images suitable for direct writing
onto USB Flash media (or CD-R by chance).

## Forensic issues

Hardening against rootfs spoofing has been implemented as of 20140423
(stage2 squashfs SHA256 check has been contributed by Maxim Suhanov);
previous images are vulnerable to ISO9660-on-device containing a
squashfs file with predefined name and specially crafted contents.

MDRAID/LVM2/swaps activation might occur with images before 20140416 or
when booted via the default "Rescue" target; booting into "Forensic
mode" will skip that (for both early userspace and final environment as
of 20140416) and switch `mount-system` script to use `ro,loop,noexec`
mount options (as of 20140423).

Physical device write blocking hasn't been considered so far.

## Credits

- [User:.FUF](User:.FUF "wikilink") for [Forensic Live CD
  issues](Forensic_Live_CD_issues "wikilink") page, sound advice and
  early userspace patch

## External Links

- [Project site](http://en.altlinux.org/Rescue) (also available in
  [Russian](http://www.altlinux.org/Rescue))
- Part of [Regular Builds](http://en.altlinux.org/Regular) based on ALT
  Linux Sisyphus
- Rescue image within [ALT Linux
  Starterkits](http://en.altlinux.org/Starterkits) based on stable
  branch has gained the same features as of 20140612