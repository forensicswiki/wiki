---
tags:
  - Email Analysis
  - File Analysis
  - Commercial Software
  - Tools
  - Windows
  - Linux
  - macOS
---

## Introduction

Mailward is a proprietary, browser-based email archive viewer and converter.
It opens PST, OST, OLM, MBOX, EML and MSG files without an installed copy of
Microsoft Outlook. Its interface provides folder browsing, message reading,
attachment saving and search by subject, sender or message body.

The [developer's documentation](https://pst.aivismonitor.com/) describes
local file reading with the browser File API and parsing in a Web Worker.
Email archive contents are processed on the user's device rather than
uploaded for server-side conversion. Local archive processing should not be
interpreted as a claim that the website makes no network requests.

## Usage

1. Open the website in a browser and select or drop an email archive.
2. Browse its folder tree and select a message to view its contents and
   attachments.
3. Search the archive by subject, sender or body text.
4. Save an individual message or attachment, or use the paid batch-export
   functions to export folders or the archive to MBOX or EML.

The browser interface can be used on macOS, Windows and Linux. It also
accepts a batch of EML or MSG files as a combined message list.

## Licensing

The service has free and paid functionality. Reading, searching and
single-message export are available in the free tier. For MBOX files, free
message reading is limited to the first 500 MB, although larger files can
be listed and searched in full. Bulk export and reading MBOX messages
beyond that limit require a paid license. The pricing page listed a
one-time US$19 license on 7 September 2026.

## Limitations

Mailward reads existing email files; it does not repair damaged PST files
or write new PST files. The developer's
[format reference](https://pst.aivismonitor.com/email-archive-formats)
describes conversion losses, including Outlook-specific categories, flags
and some calendar or contact fields that do not map directly to MIME
messages. Exports should therefore not be treated as lossless copies of
every property in the original archive.

Its documented workflow concerns browsing, searching and exporting email
files. This article does not establish the tool's suitability for evidence
acquisition or forensic validation of its output.

## External Links

* [Official website and pricing](https://pst.aivismonitor.com/)
* [Email archive formats and conversion limitations](https://pst.aivismonitor.com/email-archive-formats)
