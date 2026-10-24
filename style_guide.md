# Style Guide

This document captures the style conventions for writing and maintaining articles in the Forensics
Wiki. It covers:

* Markdown lint rules
* expected article structure
* conventions regarding content

## Markdown style

Forensics Wiki uses MkDocs therefore all Markdown in the docs directory must be MkDocs compatible.
Since MkDocs does not come with linter, pymarkdown is used to lint Markdown files.

You can run pymarkdown locally via:

```bash
tox -e pymarkdown
```

Conventions pymarkdown checks for:

* Text and headings must not exceed 100 characters. A single long link may occupy its own line
  (treat_links_as_single_words). Table rows and code blocks are exempt from the line length limit
  (tables: false, code_blocks: false).
* Leave a blank line before and after each heading.
* Bulleted list use the asterisk style, never hyphens or alternatives, and list elements with
  text longer than 100 characters are continue at the start of the text after the bullet.
* Code blocks are fenced and must declare a language.
* Do not use special characters (!, &, etc.) in headings that other pages link to by anchor;
  pymarkdown and MkDocs generate different [slugs](https://en.wikipedia.org/wiki/Clean_URL#Slug)
  for them. Use plain words instead.
* Renaming a heading changes its anchor slug. Before renaming, make sure that no other
  article links to the old slug.
* Use the native Markdown notation for strikethrough, `~~text~~`, instead of HTML tags such
  as `<s>` or `<del>`.
* There is no native notation for underline in Markdown, use *italics* or **bold** to make
  text stand out instead of HTML tags like `<u>`.
* Files end with exactly one trailing newline.

When prose needs a literal `<`, `>` or `&`, write the HTML entity instead: `&lt;`, `&gt;` and
`&amp;`. An unescaped `<word>` in prose is treated as an HTML tag and disappears from the
rendered page, and the Markdown engine used by MkDocs does not consume backslash escapes for
these characters (a `\<` or `\&` in the source shows up as a literal backslash), so HTML
entities are the reliable way to escape them. This rule is enforced in CI by
`check_escaping.py`; run `tox -e check-escaping` locally, or
`python check_escaping.py --fix docs` to correct files automatically.

Limit inline HTML to tags that Markdown cannot render natively, such as `<sup>` or `<sub>`
for superscripts and subscripts. Use standard Markdown syntax (bold, italics, lists, links,
tables) for everything else; the topics table on the homepage is an existing exception.

## Article structure

Wiki articles are topic pages without a top level heading (heading level 1), MkDocs will add one.
Note that index.md is an exception to the rule. Articles start with a MkDocs YAML front matter for
example:

```yaml
tags:
  - Network Forensics
```

The tags list holds the topic tags. Articles that still need work also list "Articles that need to
be expanded".

All articles should start with an introduction that summarizes what is discussed in the article,
e.g. `Wireless forensics is the process of ...`

The body follows, then additional sections in this order:

1. subsections part of the description of the topic, which are at minimum heading level 2 (`##`).
2. `## See Also`, which contains references to articles within Forensics Wiki relevant for the
   topic.
3. `## External Links`, which contain references to external articles, relevant for the topic.
4. `## Tools` or equivalent sections such as `## Services` or `## Training`

There is no requirement for the length of an article, but it should be long enough to explain the
topic.

## Naming

The file name of the article should be in all lowercase and use underscores to connect words. For
example, `forensics.md` for an article about "forensics" and `forensic_artifacts.md` for an
article about "forensic artifacts".

## Writing style

Using standardized (or normalized) terminology is essential for an international audience because
it eliminates ambiguity, ensures accurate and culturally nuanced translations, and creates a
unified baseline of communication across diverse languages and borders.

* Do not assume every reader is a native English speaker, avoid uncommon terms or metaphors.
* Do not assume every reader has the same expertise or background, avoid non-standard
  abbreviations or jargon. If unavoidable explain them in the concepts article (concepts.md).
* Use unlocalized date and time notations, e.g. ISO 8601 (2020-01-01) or the "Month day, year"
  format as in "January 1, 2020", instead of localized notations such as "DD/MM/YYYY" or
  "MM/DD/YYYY".
* Use unambiguous notations, e.g. USD instead of Dollar or $.
* Use the adjective "forensic" before a noun ("forensic analysis", "forensic investigation"), not
  the noun "forensics" ("forensics analysis").
* American spelling such as analyze, analyzed, analyzing, is preferred over British variants,
  such as analyse, analysed, analysing; corrections are welcome but not required.
* Use the ASCII character set for punctuation as much as possible, such as "-" instead of "—".

### Names

* Capitalize the names of operating systems, software and other proper nouns, e.g. `Windows`
  instead of `windows`.
* For Mac OS, prefer `Mac OS` when the text is about the operating system in general. Use
  `macOS`, `Mac OS X`, or `MacOS` when it is the official name of a specific version of Mac OS,
  e.g. `macOS 15 Sequoia`.
* Use `Windows Registry` instead of the more general `registry`, to disambiguate from, e.g.,
  the domain name registry.

### Preferred terminology

See Also: [terminology](docs/terminology.md)

#### Analysis, Examination and Investigation

Use the term that matches the scope of the work being described.

* *analysis* - the data-level work: interpreting specific artifacts and tool output. The
  most technical and granular term.
* *examination* - the inspection of the evidence itself, forensically sound, documented
  and court-facing.
* *investigation* - the whole case: scoping, acquisition, examination, analysis and
  reporting, ending in a legally defensible answer.

To decide, look at what the work acts on.

* Work on *data* - artifacts, log files, tool output - is *analysis*.
* Work on the *evidence itself*, documented and ready for court, is *examination*.
* Work on the *case as a whole* - the question, the acquisition, the reporting - is *investigation*.

Where the scope spans more than one level, prefer the narrowest term that fully covers the
work being described.

Sub-discipline names and tags are fixed terminology that contain *analysis* by design should
remain as-is. This includes names such as *memory analysis*, *malware analysis*, *timeline
analysis*, *file analysis*, *log analysis*, *cell site analysis* and *flow-based analysis*, as well
as the tags listed in the Tags section.

Common English uses of these words are not governed by this rule: professional examinations,
such as "pass the CFAP examination", legal proceedings, such as "cross-examination" and fixed
organization or product names, such as "LiveWire Investigator".

#### Analyst, examiner or investigator

* *analyst*, for the person who analyzes the data
* *examiner*, for the person who performs the examination
* *investigator*, for the person who owns the investigation

**Please do not use forensicator. It is [slang](https://en.wikipedia.org/wiki/Slang).**

## References and external links

Put most external links at the bottom of an article to prevent littering it with them.

* For references use `[title](url), by author(s), date` in chronological order.
* A reference should have a link (URL) that points to a relevant site. References without a link,
  or those that point to a non-relevant site, will be removed.
* For references without a link, use a citation block and reference the source from which the
  citation came.
* Make sure external links are publicly accessible. Links with signup or paywalls, or that are
  geo-restricted, will be removed. The exception are vendor related articles where one can link to
  a vendor site that uses signup or paywalls, but explicitly call this out.

## Category articles

Category articles cover one analysis category and link back to their umbrella topic article.
Such as session_reconstruction.md linking back to network_forensics.md

Category articles follow the following structure:

* definition paragraph
* optional subsections
* see also
* external link
* tools

## Vendor articles

A vendor article is to inform the reader about the organization, its products and most important
its role in the digital forensics process.

Vendor articles should include the following structure:

* A short profile of the vendor.
* `## Products`: a bullet list of the vendor's products (anchors), then a `###` section per product
  with `####` sub-features.
* `## External Links` at the end, with a link to its company site.

Commercial software and training should be part of the vendor article and include:

* A description of the product.
* The digital forensics tradeoffs of the product.
* Descriptive prose follows the preferred terminology and uses the term that fits the scope:
  *analysis* for data-level work, *examination* for court-facing inspection of the evidence,
  and *investigation* for the case as a whole. Direct quotes from the vendor, official
  product names and quoted feature names are preserved as-is.
* References to individual external product pages can be included in the `## External Links`.
  **Note that the vendor is expected to keep their information up to date and outdated information
  such as links will be removed.**
* Other pages that reference a product should link to the vendor article, using an anchor to the
  specific product where possible.
* If two vendors have similar names, both articles carry a cross-link noting that they are separate
  companies in the profile section, see systools.md and sysinfotools_software.md.

## Tool articles

If you are writing an article that includes tooling, first read
[(digital) forensic tooling](https://forensics.wiki/forensic_tooling).
An article about tooling should include the following headings:

* **Introduction**: This section may include the history of the tool and its supported operating
  systems and file systems.
* **Caution**: The digital forensic tradeoffs to be aware of. Make sure to include the pros and
  cons of tool use for different digital forensics use cases. Highlight the dependency on other
  tooling, which is relevant for cross-tool validation
  (reproducibility.md#cross-tool-validation).
* **Use**: This section may include the common uses of a tool. A tool could contain one or more
  common uses. For example, the dd Unix utility could image drives as well as wipe drives so that
  data is not recoverable.
* **See Also**: This section may include links to Forensics Wiki articles with related content,
  complementary tools, or forks of the tool. For example, an article about the Sleuth Kit (TSK) may
  include a link to an article about Autopsy.
* **External Links**: Any external links, such as references to support the information provided,
  or links to the project page or official website.

## Command line examples

If you want to include command line examples, use a code block.

<!--pyml disable md048-->
For Linux/Unix:

~~~text
```bash
$ whoami
user
```
~~~

For Windows:

~~~text
```cmd
whoami
desktop\user
```
~~~
<!--pyml enable md048-->

## Images

Images or illustrations are not required, but if they help explain the topic they could be added.
Any images must be placed in the `docs/assets/images` directory. The simplest way to add an image
to a document is using HTML:

```text
![myimage.jpg](assets/images/myimage.jpg){width="200"}
```

## Tags

Tags help make content more discoverable. They appear at the top of the page and should help the
user know what the content is related to. Tags are searchable and clickable, so you could easily
see other articles that have the same tag.

### How to add tags

After you write your article, you can place tags at the top of the page using the following
syntax:

```yaml
---
tags:
  - Commercial Software
  - Disk Analysis
  - Tools
  - Windows
---
```

> Note that tags are formatted in [YAML](https://www.mkdocs.org/user-guide/writing-your-docs/#yaml-style-meta-data)

### Tag guidelines

Tags should describe the content of the article and should be applied uniformly across all the
content. This will help users discover the content more easily. Multiple topics could apply to one
article. For example, a page tagged with `Tool` would also likely benefit from a tag denoting the
appropriate Operating System, Software type, and Analysis type.

See examples below the table.

| Tag | Description |
| --- | --- |
| Android | Mobile Operating Systems |
| Anti-Forensics | Analysis Types |
| Archive | File Types |
| Audio | File Types |
| Binary | File Types |
| BlackberryOS | Mobile Operating Systems |
| BSD | Operating Systems |
| Cell Phone Analysis | Analysis Types |
| Commercial Software | Software Type |
| Computer Bus | Hardware Types |
| Concept | Concept |
| Database | File Types |
| Data Carving | Analysis Types |
| Data Recovery | Analysis Types |
| Discontinued | Abandoned, deprecated or discontinued tools |
| Disk Analysis | Analysis Types |
| Disk Encryption | Encryption |
| Disk Image | File Types |
| Disk Imaging | Analysis Types |
| Email Analysis | Analysis Types |
| Encryption | Encryption |
| File Analysis | Analysis Types |
| File Format | File Types |
| File System | Analysis Types |
| Free Software | Software Type |
| GPS | Hardware Types |
| Hard Drive | Hardware Types |
| iOS | Mobile Operating Systems |
| Knowledge Base | Repository of factual information |
| Legal | Law, Legal |
| Linux | Operating Systems |
| Log Analysis | Analysis Types |
| macOS | Operating Systems |
| Malware Analysis | Analysis Types |
| Memory Analysis | Analysis Types |
| Memory | Hardware Types |
| Memory Imaging | Analysis Types |
| Microprocessor | Hardware Types |
| Mobile | Mobile |
| Mobile Networks | Mobile |
| Network Analysis | Analysis Types |
| Network Encryption | Encryption |
| Open Source Software | Software Type |
| Operating System | Operating Systems |
| Organizations | Non-vendor companies, Government |
| OS Component | OS Components |
| PalmOS | Mobile Operating Systems |
| People | People |
| Personal Device | Hardware Types |
| Photo | File Types |
| Publications | Blogs, Books, Journals, Magazines, Papers, Websites |
| Public Domain Software | Software Type |
| Registry Analysis | Analysis Types |
| Reports | Knowledge |
| Secure Deletion | Analysis Types |
| SIM | Mobile |
| Symbian | Mobile Operating Systems |
| System Analysis | Analysis Types |
| System Monitoring | Analysis Types |
| Text | File Types |
| Timeline Analysis | Analysis Types |
| Tools | Tools |
| Training | Training |
| Unix | Operating Systems |
| Vendor | Software Vendors, Training Vendor |
| Windows Mobile | Mobile Operating Systems |
| Windows | Operating Systems |
| Write Blockers | Hardware Types |

### Tagging examples

Let's run through some examples to see how tags would be applied to articles.

#### Example 1: An article about Windows

An article about the Windows operating system in general.

```yaml
---
tags:
  - Operating System
  - Windows
---
```

#### Example 2: An article about an open source Linux/macOS tool that parses logs in /var/messages

An article about a tool should contain the operating systems it supports (Linux and macOS), what
the tool is used for (in this case, Log Analysis), and the software type: Open Source Software.

```yaml
---
tags:
  - Linux
  - Log Analysis
  - MacOS
  - Open Source Software
  - Tools
---
```

#### Example 3: An article about Bitlocker encryption

An article about Bitlocker should contain the following tags:

```yaml
---
tags:
  - Anti-Forensics
  - Encryption
  - Windows
---
```

Bitlocker is a type of "Encryption", available only for "Windows", and might be relevant during
"Anti-Forensics" analysis.

#### Example 4: An article about the ZIP file format

File types are tagged with File Format and the file type. In this case, ZIP files are Archive
files.

```yaml
---
tags:
  - Archive
  - File Format
---
```

#### Example 5: An article about Windows System Restore Points

Windows System Restore Points are part of the operating system ("OS Component") of Windows.

```yaml
---
tags:
  - OS Component
  - Windows
---
```
