---
tags:
  -  Howtos
---
## Creating virtual machines from forensic images

After having no success with raw2vmdk, the Live View method has worked.

[Live View](http://liveview.sourceforge.net/index.html) requires:

-Java JRE

-VMWare Workstation 5.5+ or Server

-VMWare VDDK ([download](http://www.vmware.com/support/developer/vddk))

## Install

Install prerequisites followed by Live View (the installer will check
for pre-reqs).

*Tested: Win7-64 with VMWare Workstation 7.12, Live View 0.7b, and
VMWare VDDK 5.0*

![<File:LiveView.png>](LiveView.png "File:LiveView.png")

## VMX Creation

1\. Run Live View as Administrator. *(Messages pane will result in
errors otherwise)*

2\. Set memory and OS as closely as possible to target machine specs.
*(To maximize probability of success)*

3\. Click "Start". *(The screenshot error relates to maximums exceeded
based on client machine.)*

![<File:VMWareWorkstation.png>](VMWareWorkstation.png "File:VMWareWorkstation.png")

