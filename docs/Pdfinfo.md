**pdfinfo** is a small utility which shows (parts of) the metadata
stored in [PDF](PDF "wikilink") files. It is part of the
[xpdf](xpdf "wikilink") package.

## Example

`$ pdfinfo nsa-redact.pdf`
`Title:          Redacting with Confidence:  How to Safely Publish Sanitized Reports Converted from Word to PDF`
`Subject:        I333-015R-2005`
`Keywords:       word, pdf, redaction, metadata`
`Author:         SNAC`
`Creator:        activePDF DocConverter`
`Producer:       5D PDFLib`
`CreationDate:   Tue Jan 10 11:15:26 2006`
`ModDate:        Fri Jan 20 09:05:43 2006`
`Tagged:         no`
`Pages:          14`
`Encrypted:      no`
`Page size:      612 x 792 pts (letter)`
`File size:      681417 bytes`
`Optimized:      yes`
`PDF version:    1.3`

The `-meta` command line option shows some more metadata (in
[XML](XML "wikilink") format).