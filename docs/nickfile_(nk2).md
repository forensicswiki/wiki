---
tags:
  - File Formats
---
[Microsoft Outlook](microsoft_outlook.md) uses the **Nickfile (NK2)** to store
e-mail address aliases.

The file type is also known as the Outlook AutoComplete File or the Nickname
file.

## MIME types

The actual mime type of the NK2 format is unspecified

## File signature

The NK2 has the following file signature: hexadecimal: 0D F0 AD BA

Note that other sources claim that the file signature is hexadecimal: 0D
F0 AD BA 0A 00 00 00

## Contents

The NK2 basically contains a list of items. The attributes of these
items are defined by the [Microsoft Outlook](microsoft_outlook.md) Message
API (MAPI).

## External Links

* [Nickfile (NK2) format specification](https://github.com/libyal/libnk2/blob/main/documentation/Nickfile%20(NK2)%20format.asciidoc),
  by the [libnk2 project](libnk2.md)
* [MAPI definitions](https://github.com/libyal/libfmapi/blob/main/documentation/MAPI%20definitions.asciidoc),
  by the libfmapi project
