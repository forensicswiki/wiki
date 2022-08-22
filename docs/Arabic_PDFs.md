Documents in [PDF](PDF "wikilink") format that contain Arabic text may
present problems for examiners. This page presents the difference
between a glyph and a character and how PDF documents can commingle
them.

## Glyphs vs. Characters

The term *chracter* describes an abstract concept of a letter. The term
*glyph* describes how a character prints. A single character can have
multiple glyphs (for example, glyphs with serifs and those without). A
single glyph can have multiple characters. For example, in the font
Helvetica the same shape is used to represent a lower case 'l' (ell) and
a capital 'I' (eye).

Unicode is set up as a catalog of nominal characters, independent and
irrespective of the (computer) typographical consequences. For example,
the English/US Unicode page has an entry for the character 'lower case
a', but does not define how that letter should be displayed.

PDF documents can contain both glyphs and characters. Modern PDFs
emulate the 19th century-style metal-based typesetting process. Ideally
PDFs should encode characters, not glyphs<sup>citation needed</sup>.
When typesetting Arabic, Unicode is used as a glyph list, rather than a
character list. The glyphs are used as indexes into a huge font book.

By interpreting the Unicode standard as a look-up for glyph indexes,
Unicode is abused as if it were a huge font book. This confuses
multi-lingual encoding with computer typography.

An underlying cause for this error is the idea that there can be such a
thing as a Character-Glyph model. However, in the real world there is no
connection between abstract characters and the glyphs used to represent
them.

Increasingly font designers are discovering the enormous conceptual
freedom one gets without any Character-Glyph constraint. But Adobe still
uses the Unicode standard to extract the nominal character values from
the font glyph numbers used to represent them. That is why more advanced
Arabic fonts that do not use the Unicode Presentation Blocks produce
gibberish when text is extracted from the PDF.

Future versions of PDF are planned to embed Unicode as text in addition
to the font information, which would resolve this issue.

Part of the problem is that Unicode’s Arabic Presentation Blocks are
officially deprecated by the Unicode Consortium. Their inclusion was at
the time – late 1980’s - a technical compromise to allow the ISO 10646
to join Unicode. As such the compromise was incomplete, as only 400 out
of originally 4000 requested Arabic ligatures we allowed to remain in
the Unicode Standard. Ironically, all the printed examples in the
Unicode standard were designed by Thomas Milo based on
computer-generated synthesis of the underlying letter block fusions of
traditional Arabic "Script Grammar". This was done using DecoType’s
famous ACE technology, that eventually became the working model for
Microsoft’s True Type Open, the precursor of today's OpenType.

Arabic Presentation Forms should never be encoded, such a practice
amounts to reverting to Font Pages, whose very proliferation caused the
development of a more intelligent alternative: Unicode.

## References

- <http://www.river-valley.tv/conferences/arabic_typography_2008/>
- <http://www.river-valley.tv/conferences/non_latintypefacedesign/>