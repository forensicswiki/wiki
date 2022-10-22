---
tags:
  -  Articles that need to be expanded
---
This topic will cover current research in wireless communication
networks. These types of networks have been growing exponentially in the
past several years and include a host of different network types: ad
hoc, cell phone, access point, sensor, etc. This topic will build better
understanding with all layers of wireless networking and the
interactions between them (including: physical, data link, medium access
control, routing, transport, and application). The topics of security,
energy efficiency, mobility, scalability, and their unique
characteristics in wireless networks will be discussed.

## Wireless Security Introduction

A consideration on any computer network, security is especially
important on Wi-Fi wireless networks. Hackers can easily intercept Wi-Fi
network traffic over open air and extract information like passwords and
credit card numbers. Several Wi-Fi network security technologies have
been developed to combat hackers, of course, although some of these
technologies can be defeated more easily than others.

**Network Data Encryption** Network security protocols usually use
encryption technology. Encryption scrambles data sent over network
connections to hide information from humans while still allowing
computers to properly decipher the messages. Many forms of encryption
technology exist in the industry.

**Network Authentication** Authentication technology for computer
networks verifies the identity of devices and people. Network operating
systems like Microsoft Windows and Apple OS-X include built-in
authentication support based on user names and passwords. Home network
routers also authenticate administrators by requiring them to enter
separate login credentials.

**Ad Hoc Wi-Fi Network Security** Traditional Wi-Fi network connections
go through a router or other wireless access point. Alternatively, Wi-Fi
supports a mode called ad hoc wireless that allows devices to connect
directly to each other in peer to peer fashion. Lacking a central
connection point, the security of ad hoc Wi-Fi connections tends to be
low. Some experts discourage the use of ad-hoc Wi-Fi networking for this
reason.

**Common Wi-Fi Security Standards** Most Wi-Fi devices including
computers, routers and phones support several security standards. The
available security types and even their names vary depending on a
device's capabilities.

**WEP** stands for Wired Equivalent Privacy. It is the original wireless
security standard for Wi-Fi and is still commonly used on home computer
networks. Some devices support multiple versions of WEP security and
allow an administrator to choose one, while other devices only support a
single WEP option. WEP should not be used except as a last resort, as it
provides very limited security protection.

- WEP-64-bit key (sometimes called WEP-40)
- WEP 128-bit key (sometimes called WEP-104)
- WEP 256-bit key

**WPA** stands for Wi-Fi Protected Access. This standard was developed
to replace WEP. Wi-Fi devices typically support multiple variations of
WPA technology. Traditional WPA, also known as WPA-Personal and
sometimes also called WPA-PSK (for pre-shared key), is designed for home
networking while another version, WPA-Enterprise, is designed for
corporate networks. WPA2 is an improved version of Wi-Fi Protected
Access supported by all newer Wi-Fi equipment. Like WPA, WPA2 also
exists in Personal/PSK and Enterprise forms.

**802.1X** provides network authentication to both Wi-Fi and other types
of networks. It tends to be used by larger businesses as this technology
requires additional expertise to set up and maintain. 802.1X works with
both Wi-Fi and other types of networks. In a Wi-Fi configuration,
administrators normally configure 802.1X authentication to work together
with WPA/WPA2-Enterprise encryption. 802.1X is also known as RADIUS.

**Network Security Keys and Pass-phrases** WEP and WPA/WPA2 utilize
encryption keys, long sequences of hexadecimal numbers. Matching key
values must be entered into a Wi-Fi router (or access point) and all
client devices wanting to join that network. In network security, the
term passphrase can refer to a simplified form of encryption key that
only uses alphanumeric characters instead of hexadecimal values.
However, the terms passphrase and key are often used interchangeably.

**Configuring Wi-Fi Security on Home Networks** All devices on a given
Wi-Fi network must use matching security settings. On Windows 7 PCs, the
following values must be entered on the Security tab of Wireless Network
Properties for a given network:

- Security type refers to authentication options including Open, Shared,
  WPA-Personal and –Enterprise, WPA2-Personal and –Enterprise, and
  802.1X. The Open option utilizes no authentication, while Shared
  utilizes WEP for authentication.
- Encryption type options available depend on the Security type chosen.
  Besides None, which can be only used with Open networks, the WEP
  option can be used with either WEP or 802.1X authentication. Two other
  options, called TKIP and AES, refer to specialized encryption
  technologies usable with the WPA family of Wi-Fi security standards.
- An encryption key or passphrase can be specified in the Network
  security key field when required.
- The Key Index, a value between 1 and 4, refers to the position of the
  matching key stored on the wireless router (access point). Many home
  routers allow four different encryption keys numbered 1 through 4 to
  be configured in order to support legitimate clients without forcing
  them to all use a common key.