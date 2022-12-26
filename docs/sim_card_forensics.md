---
tags:
  - Mobile
---
## Procedures

Acquire [SIM Card](sim_cards.md) and analyze the following:

- ICCID - Integrated Circuit Card Identification
- MSISDN - Subscriber phone number
- IMSI - International Mobile Subscriber Identity
- LND - Last Dialed numbers
- [LOCI](loci.md) - Location Information
- LAI - Location Area Identifier
- ADN - Abbreviated Dialing Numbers (Contacts)
- FDN - Fixed Dialing Numbers (Provider entered Numbers)
- SMS - (Short Messages)
- SMSP - Text Message parameters
- SMSS - Text message status
- Phase - Phase ID
- SST - SIM Service table
- LP - Preferred languages variable
- SPN - Service Provider name
- EXT1 - Dialing Extension
- EXT2 - Dialing Extension
- GID1 - Groups
- GID2 - Groups
- CBMI - Preferred network messages
- PUCT - Calls per unit
- ACM - Accumulated Call Meter
- ACMmax - Call Limit
- HPLMNSP - HPLMN search period
- PLMNsel - PLMN selector
- FPLMN - Forbidden PLMNs
- CCP - Capability configuration parameter
- ACC - Access control class
- BCCH - Broadcast control channels
- Kc - Ciphering Key

## Hardware

### Serial

- [MicroDrive 120](microdrive_120.md) with SmartCard Adapter

### USB

- [ACR 38T](acr_38t.md)
- [SCR3311](http://www.scmmicro.com/products-services/smart-card-readers-terminals/smart-card-reader/scr3311.html)
- [SCR335](http://www.scmmicro.com/products-services/smart-card-readers-terminals/smart-card-reader/scr335.html)
- [Dekart SIM Card reader](http://www.dekart.com/products/hardware/sim_card_reader/)

## Software

Wiki Links

- [ForensicSIM](forensicsim.md)
- [Paraben SIM Card Seizure](paraben_sim_card_seizure.md)
- [SIMiFOR](simifor.md)
- [SIMIS](simis.md)
- [SIM Explorer](sim_explorer.md)

External Links

- [SIMiFOR](http://www.forensicts.co.uk)
- [SIMcon](http://www.simcon.no/)
- [USIM Detective](http://www.quantaq.com/usimdetective.htm)
- [SIM Explorer](http://www.dekart.com/products/card_management/sim_explorer/),
  [video demo of SIM Explorer](http://www.youtube.com/watch?v=P5dJS7g1o_c)
- [Pro Data Doctor](http://www.data-recovery-mobile-phone.com/)
- [Forensic Card Reader (FCR) - German](http://www.becker-partner.de/index.php?id=17)
- [SIM Manager](http://www.txsystems.com/sim-manager.html)
- [SIMQuery](http://vidstrom.net/otools/simquery/)
- [SimScan](http://users.net.yu/~dejan/)
- [SIMSpy](http://www.nobbi.com/download.htm)
- [UnDeleteSMS](http://vidstrom.net/stools/undeletesms/)
- [Forensic SIM Card Reader](http://www.bkforensics.com/FCR.html)
- [Dekart SIM Manager](http://www.dekart.com/products/card_management/sim_manager/),
  [video tutorial on how to recover a deleted SMS](http://www.youtube.com/watch?v=VaBaqZiNW4U)
- [Cell Phone SIM Card Spy](http://www.brickhousesecurity.com/cellphone-spy-simcardreader.html)
- [SIM Card Reader](http://www.mobile-t-mobile.com/mobile-network/SIM-card-reader.html)
- [Sim Card Reader Software](http://www.download3000.com/download_46892.html)
- [Sim Card Recovery](http://www.freedownloadscenter.com/Utilities/Backup_and_Copy_Utilities/Sim_Card_Recovery.html)
- [Sim Recovery Pro](http://www.spytechs.com/phone-recorders/sims-card-reader.htm)

## Recovering SIM Card Data

* [Damaged SIM Card Data Recovery](damaged_sim_card_data_recovery.md)

## Security

SIM cards can have their data protected by a PIN, or Personal
Identification Number. If a user has enabled the PIN on their SIM card,
the SIM will remain locked until the PIN is properly entered. Some
phones provide the option of using a second PIN, or PIN2, to further
protect data. If a user incorrectly enters their PIN number multiple
times, the phone may request a PUK, or Personal Unblocking Key. The
number of times a PIN must be incorrectly entered before the phone
requests the PUK will vary from phone to phone. Once a phone requests a
PUK, the SIM will remain locked until the PUK is correctly entered. The
PUK must be obtained from the SIM's network provider. If a PUK is
incorrectly entered 10 times the SIM will become permanently locked and
the user must purchase a new SIM card in order to use the phone. In some
cases the phone will request a PUK2 before it permanently locks the SIM
card.

## See also

* [SIM Cards](sim_cards.md)
* [Troubleshooting the installation of a PC/SC smart card reader (video tutorial)](http://www.youtube.com/watch?v=w_tcwmzUH6o)

## External Links

* [E-evidence Info](http://www.e-evidence.info/cellular.html)
* [Purdue Phone Phorensics Knowledge Base](http://mobileforensicsworld.com/p3/)
* [SIM Forensics: Part 1](http://www.forensicmag.com/articles/2011/04/sim-forensics-part-1),
  by John J. Barbara, April 25, 2011
* [SIM Forensics: Part 2](http://www.forensicmag.com/articles/2011/06/sim-forensics-part-2),
  by John J. Barbara, June 15, 2011
* [SIM Forensics: Part 3](http://www.forensicmag.com/articles/2011/08/sim-forensics-part-3),
  by John J. Barbara, August 5, 2011
