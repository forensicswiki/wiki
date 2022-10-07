---
tags:
  - No Category
---
- AT and AT+ commands can be used to manually collect simple
  information. This is an ideal choice for "full control" over the
  communications that are sent and returned from the phone. These can
  also be used when there is no tool available to communicate with the
  phone. These commands were tested using a Motorola v551 GSM phone
  using Bluetooth and USB data cables. It is important to note that not
  all of these commands are supported by all phones, but the AT+CLAC
  command (usually) displays all of the available commands the GSM phone
  can respond to.
- With Motorola phones (and many others) there are **NO** AT commands
  that can be used to retrieve multimedia content. For these, OBEX
  commands must be issued to the phone to return directory contents,
  ringtones, pictures and video.
- Samsung GSM phones, on the other hand, **DO** have AT commands that
  allow access to the multimedia content.


To use these AT commands:

1.  Connect the phone and determine the number of the COM port that is
    associated with it.
2.  Open HyperTerminal, Realterm or any other terminal program that will
    communicate with a specified COM port.
3.  With the Motorola phone, type **AT+MODE=2**. This prepares the phone
    for an extended AT+ command set. (+Cxxx and +MPxx)


After following these steps, you can continue with any of the commands
below.

## **Phonebook**

**AT+CPBS=?**
Lists the phonebooks that the phone contains. (Choose phonebook
storage)
Returns: +CPBS:
("ME","SM","MT","ON","DC","MC","RC","EN","AD","QD","SD","FD")
+CPBS="ME" sets the "retrieve mode" to the internal phonebook.
+CPBS="SM" sets the "retrieve mode" to the SIM phonebook.

**AT+CPBR=?**
Describes the phonebook selected above. (Simple) This gives the max
number of entries the phone can contain. It also gives the maximum phone
number (or email address) length and name length.
**NOTE:** You can substitute +MPBR for any +CPBR command, but the phone
returns a much more specific (and less intelligible) response containing
more fields that may act as internal “programming” flags of some sort.
Returns: +CPBR: (1-1000),40,24

**AT+CPBR=\[beginning index\],\[ending index\]**
Returns a list of numbers with the index between the two numbers
entered. Also denotes what TYPE of phonebook entry was selected.
Returns: +CPBR: 9,"18005555555",129,"Contact Name" – 129 refers to a
phone number.
Returns: +CPBR: 18,"user@domain.net",128,"Contact Name" – 128 refers to
an email.

**AT+CPBR=\[index\]**
Returns the specified index.
Returns: +CPBR: 18,"user@domain.net",128,"Contact Nwikipedia

**AT+MPBR=?**
Similar to above, but a more verbose result is displayed.
Returns: +MPBR:
1-1000,40,24,8,0-1,50,(0,2,4,6,9-30,255),(0),(0-1),(1-30),(255),25,(0-1,255),264,(0),0,0,0,0,0,0,0

- 1-1000 denotes the number of entries that can be stored on the
  selected (+CPBS) phonebook.
- 40 represents the number of characters that the email or phone number
  can have.
- 24 indicates the number of characters the “friendly” name can have.
- The 8 refers to the different “types” of phonebook entry (i.e. Mobile,
  Main, Email, Home, Fax, Work … etc).
- The +CPBR command does not list anything after the 24 (as seen above),
  so there are times when the +MPBR may be useful.

**AT+MPBR=\[index\]**
Returns: +MPBR: 18,"user@domain.net",128,"Contact
Name",6,0,255,0,0,1,255,255,0,"",0,0,"","","","","","","",""

## **SMS Messages**

**AT+CMGF=1**
This tells the phone to display the entries as text rather than binary.
+CMFG=0 would display the data in binary format.

**AT+CPMS=?**
This displays all of the locations in which the phone can save the SMS
messages.
Returns: +CPMS: ("MT","IM","OM","BM","DM"),("OM","DM"),("IM")

**AT+CMGL=?**
Returns the options on which messages you wish to display.
Returns: +CMGL: ("REC UNREAD", "REC READ", "STO UNSENT", "STO SENT",
"ALL")

**AT+CMGL="ALL"**
Selects and displays all of the SMS messages on the selected source.

**AT#PMODE=1**
In order to retrieve text messages and other information, Samsung phones
must be in this mode.

**AT#PSRMR=?**
Returns the parameters to obtain text messages (Samsung).
Returns: \#PSRMR: (0-349)

## **Misc. Information**

**AT&F**
Controls local echo which enables the user to see the text they are
typing into HyperTerminal.

**ATi0, ATi1, ATi2, ATi3, or ATi4**
Returns various specs about the phone.
ATi0 Returns Manufacturer
ATi1 Returns IMEI
ATi2 Returns SW versions
ATi3 Returns Make and Model
ATi4 Returns HW Version
ATi4 Returns HW Version

'''AT+FSCD="

<DIR>

"'''
Changes to specific directories (Samsung)
If your phone is English, then it will be /Picture

'''AT+FSDI="

<DIR>

"'''
Returns directory information (Samsung)

'''AT+FSDL="

<DIR>

"'''
Returns a list of directories (Samsung)

**AT+FSFW=-1, "<FILENAME>", 0, "", <LEN>, <CRC>**
Send a file (Samsung)

**AT+FSFE=0, "<FILENAME>"**
Delete a file (Samsung)

**AT+CGSN**
Returns the IMEI of the phone.
Returns: +CGSN: IMEI356252000861622
Returns: +GSN: 299B5900 (Samsung)

**AT+CGMR**
Returns the manufacturer’s OS revision.
Returns: +CGMR: "R47_G_08.17.0FR_01"

**AT+GMI**
Returns the manufacturer name (Samsung).
Returns: +GMI: SAMSUNG

**AT+CGMM**
Returns the make, model and capabilities of the phones.
Returns: +CGMM: "GSM900","GSM1800","GSM1900","GSM850","MODEL=V551"
Returns: +GMM: SCH-A670 (Samsung)

**AT+CNUM**
Returns the subscriber name/number from the SIM, or internal memory for
CDMA phones.
Returns: +CNUM: Owner Name,15555555555,129

**AT+CLAC**
Lists AT commands that the phone supports.

**AT+MODE=22**
Prepares the phone (Motorola) for OBEX commands.

**AT+MODE=0**
This returns the phone to simple AT command mode.

**AT#PBDYN?**
This returns the phone number (Samsung).

## **Reference Links**

[Motorola AT Commands
Reference](http://jpirog.com/MOTO_AT_Commands_Reference.pdf)

[AT+C Command Set of
GSM](http://gatling.ikk.sztaki.hu/~kissg/gsm/index.html)

[Alexander Traud's GSM pages](http://www.traud.de/gsm/atex.htm)

[AT Test Commands](http://www.anotherurl.com/library/at_test.htm)

[AT Commands to Access the
Motorola](http://www.csparks.com/MotoBackup/MotorolaAT.xhtml)

[Gammu Phone Protocols](http://wammu.eu/docs/manual/protocol/index.html)

[ETSI-3GPP
Standards](http://webapp.etsi.org/key/key.asp?GSMSpecPart1=27&GSMSpecPart2=007)

[Nokia AT Commands](http://wiki.forum.nokia.com/index.php/AT_Commands)

[Support Guide for the Nokia Phones and AT
Commands](http://www.parallax.com/Portals/0/Education/custapps/Nokia_AThelp.pdf)

[Nokia 30 GSM Connectivity Terminal AT Command
Guide](http://www.daimi.au.dk/~jones/sms/packed/Nokia_30_AT_Command_Guide_2_0.pdf)

[Nokia PremiCell List of AT
Commands](http://nds1.nokia.com/phones/files/guides/at_commands.pdf)

[Samsung AT
Commands](http://webpages.charter.net/hideo_a310/downs/TechNotes/a310_atcommands.txt)

[More Samsung AT
Commands](http://ns.gentoogeek.org/portage-overlay/app-mobilephone/bitpim/bitpim-1.0.7/examples/vga1000notes.txt)

[Even more Samsung AT
Commands](http://gatling.ikk.sztaki.hu/~kissg/gsm/atscan/unprocessed/SamsungS105v1_6h.txt)