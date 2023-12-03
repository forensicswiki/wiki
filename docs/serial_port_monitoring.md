---
tags:
  - Hardware
---
## Serial Port Monitoring

**Overview**

Examiners should be aware how all the tools on the market work. It is
crucial not to change the evidence that may reside on a cell phone, PDA,
or other small scale digital device. Forensic examinations on cell
phones are currently not possible if used with a USB write blocker like
in computer forensics. How do examiners know the evidence is not being
changed when "forensic" tools are used to extract the data from a cell
phone.

A step in the right direction is to monitor the data being transferred
in between the phone and the forensic workstation. Most of the devices
make use of a USB cord to transfer the data. It would be advised to
monitor that port to see what commands the workstation is asking the
cell phone to execute. A serial port monitor would be able to
independently monitor the data transferred.

Cell phone manufacturers use different command languages to communicate
with the cell phone. Three of the most common types of commands are AT
Commaands, Obex, and Jtag. By using a serial port monitor it may be able
to see what commands the "forensic tool" is sending to the cell phone to
execute. It can also be used to see if the tool automatically filters
out any information that the examiner might actually need for the
investigation.

------------------------------------------------------------------------

**Tools** Here are some tools used to monitor the data transfer between
COM devices.

* [AGGSoftware](https://www.aggsoft.com/)
* [HHD USB/Serial Port Monitoing Software](https://www.hhdsoftware.com/)
* [Serial Port Monitoring tool](https://www.com-port-monitoring.com/)
