---
tags:
  - Analysis
  - Linux
  - Live CD
  - Open Source Software
  - Tools
---
Caine (an acronym for Computer Aided Investigative Environment) is a
distribution [live](live_cd.md) oriented to [computer forensics](computer_forensics.md)
historically conceived by Giancarlo Giustini, within a project of Digital
Forensics* Interdepartmental Research Center for Security'' (CRIS) of the
University of Modena and Reggio Emilia see [Official Site](http://www.caine-live.net/page4/history.html).
Since the end of the **2009** and currently the project is maintained by Nanni
Bassetti.

## Features

The latest version of Caine is based on the [Ubuntu](ubuntu.md) 12.04 LTS, MATE and LightDM. Compared to
its original version, the current version has been modified to meet the
standards forensic reliability and safety standards laid down by the
[NIST](nist.md) View [the methodologies of Nist](Http://www.cftt.nist.gov/Methodology_Overview.htm).

Caine includes:

- Caine Interface - a user-friendly interface that brings together a
  number of well-known forensic tools, many of which are open source;
- Updated and optimized environment to conduct a forensic analysis;
- Report generator semi-automatic, by which the investigator has a
  document easily editable and exportable with a summary of the
  activities;
- Adherence to the investigative procedure defined recently by Italian
  Law 48/2008, [Law 48/2008,](Http://www.parlamento.it/parlam/leggi/08048l.htm).

In addition, Caine is the first distribution to include forensic
Forensics inside the Caja/Nautilus Scripts and all the patches of
security for not to alter the devices in analysis.

The distro uses several patches specifically constructed to make the
system "forensic", ie not alter the original device to be tested and /
or duplicate:

- Root file system spoofing: patch that prevents tampering with the
  source device;
- No automatic recovery corrupted Journal patch: patch that prevents
  tampering with the device source, through the recovery of the Journal;
- Mounter and RBFstab: mounting devices in a simple and via graphical
  interface.

RBFstab is set to treat an ext3 file system as an ext4 file system *noload with
the option* to avoid automatic recovery of any corrupt Journal of ext3;

- Swap file off: patch that avoids modifying the file swap in systems with
  limited memory [RAM](ram.md), avoiding the alteration of the original
  artifact computer and overwrite data useful for the purposes of investigation.

Caine and Open Source == == Patches and technical solutions are and have
been all made in collaboration with people (Professionals, hobbyists,
experts, etc..) from all over the world.
CAINE represents fully the spirit of the Open Source philosophy, because
the project is completely open, anyone could take the legacy of the
previous developer or project manager.
The distro is open source, the Windows side (Nirlauncher/Wintaylor) is
open source and, last one but not least important, the distro is
installable, so as to give the possibility to rebuild in a new version,
in order to give a long life to this project.

## Caine Interface

Caine Interface - a user-friendly interface that brings together a
number of well-known forensic tools.
Environment updated and optimized for digital investigations.
Report Semi-automatic - the final production of a complete document and
easily editable exported by the investigator. Maximum adherence to the
Italian investigative procedure.
The first distribution to include forensic inside the Caja Forensics /
Nautilus/Caja Scripts and all security patches, not to alter the devices
in the analysis.
The basic interface of the distribution called Caine Interface, was
performed using the known GTK2-Perl wrapper that implements the Perl
language instruction set and commands made available from the Gtk +
toolkit.

Caine Interface allows you not only to select the various forensic
software, it automatically generates the final report, due to the
modules offered by Perl Template Toolkit, and DocBook.

Inside contains the following software.

, Acquisition

- Grissom Analyzer (mmls, img_stat, fsstat)
- LRRP
- AIR
- Guymager
- Terminal with saving the output
- DC3DD

Analysis

- Autopsy
- [The Sleuth Kit](the_sleuth_kit.md)
- [Sfdumper 2.2](selective_file_dumper.md)
- Fundl 2.0
- Scalpel
- Foremost
- Stegdetect
- Ophcrack
- Nautilus scripts
- And many others

Reporting semiautomatic == ==

Every contribution in the form of output and local report for each
program involved in an investigation is saved in a report file, easily
manageable by the investigator. The generation of the final report is
done through the creation of temporary log file, that is to contain the
output products for implementing the programs used by the
investigator.
The generation process is achieved through the use of Perl, bash
scripts, variables Perl Template Toolkit and the DocBook file that acts
as a container to the final report.
All set within the Perl program.

The Project Caine == ==

The project was initially inserted into the priorities of the CRIS
(Centre for Research Interdepartmental Security) Research Centre
Interpardimentale Security - University of Modena, in this way the
distribution has benefited from essential contributions on the technical
computing, together to the latest "best practices" legal investigation
digital.

The project Caine was also the subject of a scientific paper accepted
and published inside the first Workshop on Computer & Network Forensics
held in Milan September 10th 2008 - OSSCoNF.

In followed all close collaboration with Denis Frati (spilled by the
project at end 2009) and Nanni Bassetti, prominent figures in the
panorama of Italian Digital Forensics, allowed a constant improvement of
investigative standards proposed. The work carried out together with the
staff ConoscereLinux allowed to enter Caine within the Italian community
of programmers of open-source software.

Caine is very much the spirit of Open Source OSSConf 2008 Open Source
Day 2012, precisely because the various inputs planning and operational
were provided by so many employees scattered across the globe, using
only the network to communicate and many have our utmost to provide
hosting, mirror and suggestions, scripts and everything that can serve
to improve the project, then a full and free.

Currently the project manager and a team of international figures treat
the project Caine since the 1.0 release to date that has arrived at
version 4.0 (18-March-2013) and achieving praise from law enforcements
of several foreign nations.

November 24, 2012 The Caine 3.0 was presented at the [Opens Source Day 2012](http://www.opensourceday.org/2012/?mid=20)
at the University of Udine.

## Bibliography

- Andrea Ghirardini, Gabriele Faggioli, *Computer Forensics*, Apogeo,
  2009, ISBN 9788850328161
- E. Huebner, S. Zanero, *Open Source Software for Digital Forensics*,
  Springer, 2010, ISBN 978-1-4419-5802-0
- Diane Barrett, Greg Kipper, *Virtualization and Forensics: A Digital
  Forensic Investigator's Guide to Virtual Environment*, Syngress, 2010,
  ISBN 978-1-59749-557-8
- Sean Philip Oriyano and Michael Gregg, *Hacker Techniques, Tools, And
  Incident Handling*, Jones and Bartlett Learning, 2011, ISBN
  978-0-7637-9183-4
- Michael Jang, *Security Strategies in Linux Platforms and
  Applications*, Jones and Bartlett Learning, 2011, ISBN
  978-0-7637-9189-6

## External links

- [Open Source Live Distributions for Computer Forensics- by Springer](http://link.springer.com/chapter/10.1007/978-1-4419-5803-7_5)
- [Google books](http://books.google.it/books?id=jQVgWaF3pJwC&pg=PT304&lpg=PT304&dq=Andrea+Ghirardini;+Gabriele+Faggioli,+Computer+Forensics+caine&source=bl&ots=mf8-Def6uF&sig=88ydFgTv05M2Q45B4FSvwqhBXKk&hl=it&sa=X&ei=W2voUOD3Lcrk4QSVlIDoDQ&ved=0CEMQ6AEwAQ)
- [Linux-Mazin.de](http://www.linux-magazin.de/Ausgaben/2010/12/Italienische-Aufklaerung)
- [Linux-Magazine.com](http://www.linux-magazine.com/Issues/2011/122/Caine)
- [Opens Source Day 2012](http://www.opensourceday.org/2012/?mid=20)
- [TechTarget.it](http://searchsecurity.techtarget.it/articoli/0,1254,18_ART_103282,00.html)
- [Softpedia](https://news.softpedia.com/news/CAINE-3-0-a-Tool-for-Digital-Forensics-297461.shtml)
- [gustavopimental.com.ar](http://www.gustavopimentel.com.ar/)
- [concise-courses.com](http://www.concise-courses.com/security/top-ten-distros/#)
- [ilsoftware.it](http://www.ilsoftware.it/articoli.asp?tag=CAINE-progetto-italiano-per-la-computer-forensics_5656)
- [dragonjar.org](http://www.dragonjar.org/distribucion-live-cd-analisis-forense.xhtml)
- [Attestato Marenostrum V.F.F.](http://www.nannibassetti.com/dblog/articolo.asp?articolo=156)
- [LinuxFormat](http://www.linuxformat.com/archives?issue=151)
- [TechRepublic](http://www.techrepublic.com/blog/10things/10-obscure-linux-distributions-and-why-you-should-know-about-them/2334)
- [Forensics Wiki](http://www.forensicswiki.org/wiki/CAINE_Live_CD)
- [Sito ufficiale](http://www.caine-live.net)
