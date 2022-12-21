---
tags:
  - No Category
---
**SIMCon** is a program that securely images all files on a [GSM](gsm.md) [SIM
Card](sim_card.md) with a standard PC-SC [smart card](smart_card.md) reader,
either [serial](serial.md) or [USB](usb.md). After imaging, the forensic
investigator can then analyze the contents of the card.  Specific information
regarding stored numbers, call history, and text messages are available.

SIMCon is now Paraben's SIM Card Seizure

## Features

- Acquire all available files on a [SIM Card](sim_card.md) and
  store in an archive file
- Analyze and interpret content of files
- Recover deleted text messages stored on the card
- Manage PIN and PUK codes
- Compatible with [SIM Cards](sim_cards.md) and [USIM
  Cards](usim_cards.md)
- Print reports of evidence
- Secure file archive using hashing
- Export items to popular spreadsheet programs
- Supports international charsets
- Contains a "content" view for plain text viewing of data, as well as a
  hexadecimal view for more specific analysis.

## Data Acquisition

[SIMCon](http://www.simcon.no) is also capable of aquiring the following
data from a [SIM Card](sim_card.md):

- Abbreviated Dialing Numbers (ADN),
- Last Dialed Numbers (LDN)
- Short Message Service (SMS)
- Public Land Mobile Network (PLMN) selector
- Forbidden PLMNs, Location Information (LOCI)
- General Packet Radio Service (GPRS) location
- International Mobile Subscriber Identity (IMSI)
- Integrated Circuit Card Identifier (ICCID)
- Mobile Subscriber ISDN (MSISDN)
- Service Provider Name (SPN)
- Phase Identification
- SIM Service Table (SST)
- Language Preference (LP)
- Card Holder Verification (CHV1) and (CHV2)
- Broadcast Control Channels (BCCH)
- Ciphering Key (Kc)
- Ciphering Key Sequence Number
- Emergency Call Code
- Fixed Dialing Numbers (FDN)
- Forbidden PLMNs
- Local Area Identitity (LAI)
- Own Dialing Number
- Temporary Mobile Subscriber Identity (TMSI)
- Routing Area Identifier (RIA) netowrk code
- Service Dialing Numbers (SDNs)
- Service Provider Name
- Depersonalizatoin Keys

All [GSM](gsm.md) cell phones today have a subscriber identity
module (SIM) to identify the phone onto the network.
[SIMCon](http://www.simcon.no) is an application to acquire all of the
information from the [SIM Card](sim_card.md).

The [SIM Card](sim_card.md) provides secure storing of the key
identifying a mobile phone service subscriber, subscription information,
preferences and text messages. Network state information, such as the
current location area identity (LAI), is also stored on the card. When a
handset is turned off and then back on, it will search for the LAI that
it was in, rather than having to search all frequencies that the phone
operates in. This saves time when trying to log on to the network.
(Subscriber, 2006, para. 1)

By using [SIMCon](http://www.simcon.no) and a smart card reader, all of
the above information and more can be pulled off of the card without
knowing the PIN or the PUK of the card. The PIN and the PUK are ways to
keep the information on the card secure. They also can be used as a
security feature on the phone, not allowing anyone to use a phone to
access the [SIM Card](sim_card.md) without knowing the codes.

[SIMCon](http://www.simcon.no) is an application developed by Inside Out
Forensics in Norway. It is designed for use by the law enforcement
community, and it can be obtained free of charge by emailing
[SIMCon](http://www.simcon.no) and identifying the officers and unit.
However, for anyone outside the law enforcement community, it is not
free.

## Review

- [SIMCon](http://www.simcon.no) makes the acquisition of data very
  easy, simply inserting the [SIM Card](sim_card.md) to the
  appropriate [SIM Card](sim_card.md) reader, and clicking
  acquire is all that is needed to start analyzing evidence. After the
  acquisition of the data is complete SimCon will show the user a screen
  with two halves.

<!-- -->

- On the left panel is the different data sectors of the [SIM
  Card](sim_card.md) that can either be checked on or off
  depending on what is needed. After choosing what data sectors are
  needed, the right panel will be populated with the selected data. Some
  of the most useful pieces of information that are shown are: the
  International Mobile Subscriber Identity number, every contacts name
  and number, and all SMS messages sent and received both stored and
  deleted.

<!-- -->

- SIMCon also comes with two more handy features that are key to an
  investigation and in a court of law. The first is
  [SIMCon](http://www.simcon.no)s' feature that allows the printing of a
  report. [SIMCon](http://www.simcon.no) will format and populate a
  report with the contents of the users’ choosing. This can list all the
  key pieces to an investigation and is an excellent piece of evidence
  to be used in a court of law. The second feature is the exportation of
  the acquired data. [SIMCon](http://www.simcon.no) allows the
  exportation of all SMS messages and also of all contacts. When these
  exported files are opened in a program such as Microsoft Excel the
  data can be read, sorted, and analyzed in a format of the users
  design.

<!-- -->

- When SMS messages are exported [SIMCon](http://www.simcon.no)
  automatically adds the following information about every message:
  file, item, status, service center, message type, number, time stamp,
  and text. When the contacts are exported
  [SIMCon](http://www.simcon.no) automatically adds the following
  information about every contact: file, item, identifier, and number.
  For reference a report of an acquired [SIM Card](sim_card.md)
  is enclosed as well as a document that tells what information is added
  into an exported file at the end of this document.

<!-- -->

- [SIMCon](http://www.simcon.no) is known to have issues while imaging
  multiple cards in the same session of the program. These issues
  include the appearance of random characters in both the contacts list
  and in the [SMS](sms.md). These complications are outlined in
  the paper [Running head: SIM CARD FORENSICS WITH SIMCON
  SOFTWARE](:image:huser_timothy_simcon_paper.doc.md) by
  [Timothy D. Huser](user:thuser.md).

<!-- -->

- Currently there is no "data-dump" mode in which one can simply dump
  data exactly as it is on the card in order to have a more pure
  investigation of the contents. This has proven to be a major setback
  up to version 1.1, as the automatic parsing of information from the
  card sometimes leaves certain details unseen, especially in the
  content view.

## External Links

- [Wikipedia: Subscriber Identity
  Module](http://en.wikipedia.org/wiki/Subscriber_Identity_Module)
- [InsideOut Forensics](http://www.simcon.no/)
