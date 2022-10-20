# How to contribute

The Forensicswiki has moved to Github.  In order to contribute you will need to follow the instructions below:

## Setup 
1.  Fork the Forensicswiki project
2.  git clone https://github.com/[your-github-user-id]/wiki.git
3.  git remote add upstream https://github.com/forensicswiki/wiki.git
4.  cd wiki
5.  git checkout -b new-article

## Prepare a Article

### Naming Convenation 
The name of the article be in all lowercase and an underscore should connect words.  For exmaple if you write an article around forensics then the name should be `forensics.md`.  If you are writing an article about forensic artifacts then the name should be `forensics_artifacts.md`

## TAG Configuraiton

### How to create TAGS
In order to help make content discoverable, TAGS are being used.  TAGS are placed at the top of the page and should help the user know what the content is related to.  TAGS are searchable and clickable so you could see other articles that have the same TAG.  

After you write you article, you must place TAGS at the top of the page using the following syntax.  

```
---
tags:
  -  Tools 
  -  Windows
  -  Disk Analysis
  -  Commercial Software 
---
```
### TAG Guidelines 

TAGS should describe the content of the article and should be applied uniformally across all of the content.  This will help the user discover the content more easily.  The table below has topics along with possible tags for the each topic.  Different topics could apply to one article.  For example a Tools would also need an Operating System, Software Type, Analysis type tags.  See examples below.

| Topcis | TAGS |
| ------ | ---- |
| Operating Systems | Windows, Linux, MacOS, BSD, Unix, Operating System |
| Mobile Operating Systems | Android, Ios, Windows Mobile, BlackberryOS, PalmOS, Symbian |
| Analysis Types | Disk Analysis, File Analysis, Disk Imaging, Data Recovery, Registry Analysis, Log Analysis, Data Recovery, Data Carving, Live CD, Reversing, Secure Deletion, Disk Imaging, Cell Phone Analysis, System Monitoring, System Analysis, Email Analysis, File System, Network Analysis, Memory Analysis, Memory Imaging, Anti-Forensics |
| Software Type  |  Opensource Software, Public Domain Software, Commercial Software, Free Software |
| OS Components  |  OS Component |
| File Types     |  File Format, Archive, Database, Disk Image, Binary, Audio, Text, Photo |
| Legal |  Law |
| Hardware Types | Computer Bus, Microprocessor, Hard Drive, Memory, Personal Device, Write Blockers, GPS |
| People |  People |
| Encryption | Encryption, Network Encryption, Disk Encryption
| Tools | Tools |
| Knowledge | Books, Papers, Reports, Journals, Websites, Blogs, Training |
| Companies / Government | Organizations |
| Mobile | Mobile Networks, Mobile, Sim |

Let's run through some examples to see how we would apply tags to articles.

Example 1:  An article about of Windows.

```
---
tags:
  -  Operating System
  -  Windows
---
```

Example 2:  An article about a opersouce linux/MacOS tool that parses logs in /var/messages.

A article about tools should contain the OSes that it supports (Linux, and MacOS), what the tool is used for, in this case Log Analysis, and the software type; Opensource Software

```
---
tags:
  -  Tools
  -  Linux
  -  MacOS
  -  Log Analysis
  -  Opensource Software
---
```

Example 3:  An article about Bitlocker encryption.

A article about bitlocker should contain the following tags:

```
---
tags:
  -  Disk Encryption
  -  Anti-Fornesics
  -  Windows
---
```

Bitlocker is a Disk Encryption.  In this case it is only for Windows so we labeled it with the Windows tag.  

Example 4:  An article about the zip file format.

File Types are tagged with File Format and the file type.  In this case Zip files are Archive files.  

```
---
tags: 
  -  File Format
  -  Archive
---
```

Exmaple 5:  An article about Windows restore point.

Windows restore point is an OS Component of Windows

```
---
tags:
  -  OS Component
  -  Windows
---
```


### How to suggest new TAGS

There might be an article that does not fit into the TAG Guildlines.  If you want to suggest a new tag then please open a [Github Issue](https://github.com/forensicswiki/wiki/issues).


## Create PR

1.  git push origin new-article
2.  Create PR for review