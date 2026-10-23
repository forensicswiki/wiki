---
tags:
  - Concept
---
In digital forensics "what you see is rarely what you get". While analysts are trained to look
for traditional anti-forensic techniques-like standard steganography or file extension
manipulation, there a more subtler text-obfuscation vectors, such as **Control Codes and Invisible
Unicode Characters**.

These non-rendering characters can negatively impact standard text encoding. By inserting bytes
that remain completely invisible in standard user interfaces but are explicitly processed by
compilers, interpreters, and operating systems. Allowing malicious actors can actively deceive,
bypass, and influence digital forensic tools.

### The Anatomy of the Unicode Blindspot

To understand why these characters affect tools, one must look at how they function within the
Unicode standard (and other text encoding standards). Main categories of non-printing characters:

1. **C0/C1 Control Codes &amp; Private Use Areas (PUA):** Legacy control codes (like `U+0000-U+001F`)
   can alter how terminals parse strings, while the PUA block (`U+E000-U+F8FF`) allocates custom
   character slots that render as blank spaces if no custom font is provided.
2. **Zero-Width Space &amp; Formatting Characters:** Characters like the **Zero-Width Space
   (`U+200B`)**, **Zero-Width Non-Joiner (`U+200C`)**, and **Zero-Width Joiner (`U+200D`)** consume
   byte space but have no physical rendering width.
3. **Bidirectional (Bidi) Control Codes:** Explicit control characters like **Right-to-Left
   Override (`U+202E`)** and the newer **Isolate characters (`U+2066`, `U+2067`, `U+2068`)** override
   the text engine's rendering direction.
4. **Variation Selectors &amp; Tags (VS1-VS256 &amp; U+E0000):** Spanning the `U+FE00-U+FE0F`,
   `U+E0100-U+E01EF`, and `U+E0000-U+E007F` blocks, these characters act as invisible tags or
   alternate glyph instructions. A malicious actor can map the entire ASCII range to these hidden
   blocks to build out-of-band payloads.

Because modern platforms assume text integrity based on visual appearance, these invisible layers
create a perfect steganographic payload. The text looks benign to a human analysts, but the raw
byte stream tells a completely different story.

### How Invisible Unicode Influences Tools

The presence of variation selectors, formatting tokens, and control characters introduces severe
challenges to automated data parsing, static code analysis, and artifact indexing.

#### Breaking Keyword Searches and Regex Patterns

Numerous tools rely heavily on indexing engines, such as Lucene in [Autopsy](autopsy_forensic_browser.md),
and regular expressions to carve text strings out of memory dumps or unallocated space.

For example if software uses a **Zero-Width Binary Encoding** scheme-interspersing `U+200B` and
`U+200C` characters between letters to represent `0` and `1` bits-a standard keyword search for the
word "admin" will fail completely. The forensic tool sees the sequence of five letters
interspersed with invisible multi-byte Unicode characters, causing string-matching algorithms and
basic regex strings to miss critical evidence entirely.

#### Defeating Static Analysis, Diff Viewers, and Code Review

In incident response and malware analysis, forensic specialists review source code changes (diffs)
or application logs to trace backdoors. As documented in supply chain campaigns like the
**GlassWorm attacks**, invisible Unicode completely blinds Abstract Syntax Tree (AST) code parsers
and standard diff tools.

Because AST parsers tokenize text based on visible character boundaries, they often skip zero-width
tokens or treat variation selectors as benign whitespace. An attacker can hide an entire malicious
Command and Control (C2) payload or backdoor logic *inside* an innocuous comment or a variable
name. The code looks untouched in a repository review, yet the compiled binary executes the hidden
bytes.

## See Also

* [unpaired surrogates](unpaired_surrogates.md)
