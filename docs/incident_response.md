---
tags:
  - Incident Response
---
Incident Response is a set of procedures for an investigator to examine
a computer security incident. This process involves figuring out what
was happened and preserving information related to those events. Because
of the fluid nature of computer investigations, incident response is
more of an art than a science.

## Tools

Incident response tools can be grouped into three categories. The first
category is **Individual Tools**. These are programs designed to probe
parts of the operating system and gather useful and/or volatile data.
The tools are self-contained, useful, discrete, and do not create a
large footprint on the victim system.

Standalone tools have been combined to create **Script Based Tools**.
These tools combine a number of standalone tools that are run via a
script or batch file. They require minimal interaction from the user and
gather a fixed set of data. These tools are good in that they automate
the incident response process and provide the examiner with a standard
process to defend in court. They also do not require the first responder
to necessarily be an expert with the individual tools. Their weakness,
however, is that they can be inflexible. Once the order of the tools is
set, it can be difficult to change. Some script based tools allow the
user to pick and choose which standalone tools will be used in a given
examination.

The final category of tools are **Agent Based Tools**. These tools
require the examiner to install a program on the victim which can then
report back to a central server. The upshot is that one examiner can
install the program on multiple computers, gather data from all of them,
and then view the results in the aggregate. Finding the victim or
victims can be easier if they stand out from the crowd.

## External Links

* [Preservation of Fragile Digital Evidence by First Responders](http://dfrws.org/2002/papers/Papers/Jesse_Kornblum.pdf),
  by [Jesse Kornblum](jesse_kornblum.md), DFRWS 2002
* [Journey to the Centre of the Breach](https://labs.withsecure.com/error/404),
  by Ben Downton, June 2, 2010
* [Keeping Focus During an Incident](https://www.hugedomains.com/domain_profile.cfm?d=handlerdiaries.com), by jackcr, January
  17, 2014

### Emergency Response

* [Addressing emergency response provider fatigue in emergency response preparedness, management, policy making, and research](http://www.mdchhs.com/sites/default/files/JEM-9-5-02-CHHS.pdf),
  Clark J. Lee, JD, September 2011

### Kill Chain

* [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf),
  by Eric M. Hutchins, Michael J. Clopperty, Rohan M. Amin, March 2011
* [Stalking the kill chain](http://www.emc.com/collateral/hardware/solution-overview/h11154-stalking-the-kill-chain-so.pdf),
  by RSA
* [APT Kill chain - Part 1 : Definition](https://www.cyber.airbus.com/cassidian-cybersecurity-blog-apt-kill-chain-part-1-definition/),
  by Cedric Pernet, April 28, 2014
* [APT Kill chain - Part 2 : Global view](https://www.cyber.airbus.com/de/apt-kill-chain-part-2-global-view/),
  by Cedric Pernet, May 7, 2014
* [APT Kill chain - Part 3: Reconnaissance](https://www.cyber.airbus.com/apt-kill-chain-part-3-reconnaissance/),
  by Cedric Pernet, May 23, 2014
* [APT Kill chain - Part 4 : Initial compromise](https://www.cyber.airbus.com/apt-kill-chain-part-4-initial-compromise/),
  by Cedric Pernet, June 20, 2014
* [APT Kill chain - Part 5 : Access Strenghtening and lateral movements](https://www.cyber.airbus.com/apt-kill-chain-part-5-access-strenghtening-lateral-movements/),
  by Cedric Pernet, December 2, 2014

### Incident Lifecycle

* [Expanding the Expanded Incident Lifecycle](http://www.itsmsolutions.com/newsletters/DITYvol5iss7.htm),
  by Janet Kuhn, February 18, 2009
* [Incident lifecycle](https://www.enisa.europa.eu/activities/cert/support/incident-management/browsable/workflows/incident-lifecycle),
  by [ENISA](enisa.md)

### Intrusion Analysis

* [The Diamond Model of Intrusion Analysis](http://www.threatconnect.com/files/uploaded_files/The_Diamond_Model_of_Intrusion_Analysis.pdf),
  by Sergio Caltagirone, Andrew Pendergast, Christopher Betz

### Product related

* [Palantir: A Framework for Collaborative Incident Response and Investigation](http://middleware.internet2.edu/idtrust/2009/papers/05-khurana-palantir.pdf),
  Himanshu Khurana, Jim Basney, Mehedi Bakht, Mike Freemon, Von Welch,
  Randy Butler, April 2009

## Tools

### Individual Tools

* [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)

### Script Based Tools

* [First Responder's Evidence Disk (fred)](first_responder's_evidence_disk.md)
* [Microsoft COFEE](cofee.md)
* [Windows Forensic Toolchest (wft)](windows_forensic_toolchest.md)
* [RAPIER](regimented_potential_incident_examination_report.md)

### Agent Based Tools

* [GRR](grr.md)
* Mandiant First Response (FIR), supersceded by FireEye agent

## Books

There are several books available that discuss incident response. For
[Windows](windows.md), *[Windows Forensics and Incident
Recovery](https://www.windows-ir.com/)* by [Harlan
Carvey](harlan_carvey.md) is an excellent introduction to
possible scenarios and how to respond to them.
