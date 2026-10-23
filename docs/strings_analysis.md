---
tags:
  - Analysis Techniques
---
String analysis is the technique of extracting the printable strings
embedded in a file and examining them to learn what the file is up to.
Although it is most often applied to [executables](executable.md) and
process memory dumps, it can also be used on archives, databases and log
files. Because most of a binary file is unreadable noise, string analyzers
sift through the file and pull out only the strings that are most likely to
include pertinent information, using the criteria set by the examiner.

It is a basic part of the
[content analysis](file_analysis.md#content-analysis) category of
[file analysis](file_analysis.md), and is often the first pass over an
unknown or suspicious file.

## Choosing criteria

Two criteria matter most when extracting strings:

* **Minimum string length.** Short strings rarely contain useful
  information and mostly add noise. Most string analyzers allow setting a
  minimum string length: requiring strings of at least 8 consecutive
  characters, for example, surfaces strings more likely to contain
  filenames or starting parameters, while filtering out most of the noise.
* **Character set.** Strings in a file can be stored as ASCII or Unicode.
  Many analyzers search only ASCII and equivalent characters by default and
  require an explicit option to also search for Unicode strings, so both
  encodings should be checked - particularly for Windows binaries and
  memory dumps.

## What to look for

The extracted strings are then examined for clues about the file's
behavior:

* File paths and filenames the program uses or references
* Command lines and starting parameters, showing how a program was invoked
  and configured
* User prompts, error messages and status messages, which suggest the
  functionality of a program
* Version banners and help output, which can identify a program that was
  renamed or repurposed, such as a disguised backdoor
* URLs, host names and other network endpoints

[strings](strings.md#use) contains a concrete example in which string analysis of a process memory
dump identified a disguised [Netcat](netcat.md) backdoor.

## Interpreting findings

The presence or absence of a string is not proof, or evidence of the
absence, of any functionality: a string can be present in a file even if
the feature it suggests is never used, and functionality can be present
without any identifying string at all, for example when the code is packed,
encrypted or dynamically generated. Strings therefore provide hints that
should be corroborated by other techniques, such as static or dynamic
[analysis of program execution](analyzing_program_execution.md).

## See Also

* [Strings](strings.md)
* [File analysis](file_analysis.md)
* [Memory analysis](memory_analysis.md)
* [Malware analysis](malware_analysis.md)

## External Links

* [Wikipedia: Strings (Unix)](https://en.wikipedia.org/wiki/Strings_(Unix))
