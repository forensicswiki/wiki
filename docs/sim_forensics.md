---
tags:
  - Articles that need to be expanded
  - Mobile
---
*Under Construction*

The [SIM Card](sim_cards.md) is the basic memory device inside of
many mobile phones in use today. This small piece of hardware has been
key to solving many cases in the world of [SIM Card
Forensics](sim_card_forensics.md). However, without the proper
knowledge of the SIM card's filesystem, the user will be missing out on
all the valuable information the SIM Card holds.

## Getting Started

<figure>
<img src="What_you_need.jpg" title="What_you_need.jpg" width="250"
alt="What_you_need.jpg" />
<figcaption aria-hidden="true">What_you_need.jpg</figcaption>
</figure>

This is a list of items to get you started on reading SIM Cards and
their information:

1.  [Windows](windows.md) operating system
2.  [SIMCon](simcon.md)[1](https://www.simcon.no/)
    - Program used to read SIM Cards
3.  SIM Cards
4.  SIM Card Reader

## Quick Guide for SIMCon

1.  Make sure the SIM Card Reader with SIM Card is connected
2.  Open [SIMCon](simcon.md)
3.  Click File \> Read SIM or Click
    ![<File:Simcon.png>](Simcon.png "File:Simcon.png") in the upper left
    corner of [SIMCon](simcon.md)
4.  Click OK when the next dialog box pops up
    - **Note**, some SIM cards are locked. This is where the PIN needs
      to be entered if known.
    - If the PIN is unknown, the SIM cannot be read.
5.  Click OK again when the next dialog box pops up

## Definitions

### MF

- Only **one** MF
- The Master File (MF)
- Root of the SIM Card file system
- Equivalent to the root directory or "/" in the Linux filesystem

### DF

- Dedicated Files (DF)
- Equivalent to a folder in a Windows/Linux filesystem
- Usually three DF's
  - DF_GSM / DF_DCS1800 / DF_TELECOM

#### DF_DCS1800 / DF_GSM

- Contains network related information
- Specifying data in DF_GSM writes only to DF_GSM on the SIM
- The SIM is expected to mirror GSM and DCS1800

#### DF_TELECOM

- Contains the service related information

### EF

- Elementary Files (EF)
- Holds one to many records
- Represent the leaf node of the filesystem
- EF's sit below the DF's in the filesystem hierarchy

### PLMN

- Public Land Mobile Network
  - A PLMN is a network that is established and operated by an
    administration or by a recognized operating agency (ROA) for the
    specific purpose of providing land mobile telecommunications
    services to the public.
    [2](https://en.wikipedia.org/wiki/Public_land_mobile_network)

### LAI

- Location Area Identity
  - Each location area of a public land mobile network (PLMN) has its
    own unique identifier which is known as Location Area Identity
    (LAI). [3](https://en.wikipedia.org/wiki/Location_Area_Identity)

## Filesystem

### EF_ICCID

This displays the ID or Card Identity of the SIM Card, this can also be
found on the SIM card itself.

<figure>
<img src="Ef_iccid.png" title="Ef_iccid.png" width="350"
alt="Ef_iccid.png" />
<figcaption aria-hidden="true">Ef_iccid.png</figcaption>
</figure>










----

### DF_GSM

#### EF_IMSI

- International Mobile Subscriber Identity
  (IMSI)[4](https://en.wikipedia.org/wiki/IMSI)
- 310 - 260 - 653235860
- MCC - MNC - MSIN
  - MCC[5](https://en.wikipedia.org/wiki/List_of_mobile_country_codes) (3
    Digits)
    - Mobile Country Code
  - MNC[6](https://en.wikipedia.org/wiki/Mobile_Network_Code) (2 Digits
    EU / 3 Digits NA)
    - Mobile Network Code
  - MSIN[7](https://en.wikipedia.org/wiki/MSIN) (Remaining Digits)
    - Mobile Subscription Identification Number
    - Within the network's customer base

<figure>
<img src="Ef_imsi.png" title="Ef_imsi.png" width="350"
alt="Ef_imsi.png" />
<figcaption aria-hidden="true">Ef_imsi.png</figcaption>
</figure>










----

#### EF_PLMNSEL

- List of all PLMN's (see
  [Sim_Filesystem#PLMN](sim_forensics.md#plmn)

<figure>
<img src="Plmnsel.png" title="Plmnsel.png" width="350"
alt="Plmnsel.png" />
<figcaption aria-hidden="true">Plmnsel.png</figcaption>
</figure>










----

#### EF_LOCI

- Location Information
  - Contains Location Area Identity (see
    [Sim_Filesystem#LAI](sim_forensics.md#lai)
    - LAI Network Code (see
      [Sim_Filesystem#PLMN](sim_forensics.md#plmn) /
      [Sim_Filesystem#LAI](sim_forensics.md#lai)

<figure>
<img src="Ef_loci.png" title="Ef_loci.png" width="350"
alt="Ef_loci.png" />
<figcaption aria-hidden="true">Ef_loci.png</figcaption>
</figure>










----

### DF_TELECOM

#### EF_ADN

<figure>
<img src="EF_adn.png" title="EF_adn.png" width="350" alt="EF_adn.png" />
<figcaption aria-hidden="true">EF_adn.png</figcaption>
</figure>










----
