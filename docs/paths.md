---
tags:
  - Concept
---
In digital forensics, file and Window Registry paths are the primary maps used to locate evidence,
trace malicious actor activity, and establish a timeline of events.

While paths are often taken for granted, underlying operating system quirks, normalization
routines, and character encoding schemes introduce significant edge cases. Misunderstanding how a
system processes or records a path can lead to missed Indicators of Compromise (IoCs), failed
script execution, and a lack of [forensic reproducibility](reproducibility.md).

## The Anatomy of Windows Path Formats

Windows systems utilize several distinct path formats to reference file system resources and object
models. Forensics examiners must recognize each type to properly interpret artifacts:

* **Traditional DOS Paths:** The standard format consisting of a drive letter volume specifier,
  directory separators, and a filename (e.g., `C:\Windows\System32`). These can be absolute or
  relative, which frequently leads to logic bugs if a script assumes a path is fully qualified when
  it is actually drive-relative (e.g., `C:Modules\file.dll`).
* **Universal Naming Convention (UNC) Paths:** Used to access network shares, formatted as
  `\\Server\Share\Directory\File`. UNC paths must always be fully qualified.
* **DOS Device Paths:** Exposed through a special folder of symbolic links in the Windows unified
  object model. They bypass standard entry points using the prefixes `\\.\` or `\\?\`. They can
  target volumes directly via GUIDs (e.g., `\\?\Volume{GUID}\File`).

## Windows Path Normalization: A Double-Edged Sword

Before a path is passed to Windows APIs, the operating system undergoes an implicit **normalization
process**. This standardizes separators, applies the current directory to relative paths, and trims
trailing dots or spaces.

When a path begins precisely with the literal device specifier `\\?\`, **Windows skips path
normalization**. This allows for paths that exceed the historical 260-character `MAX_PATH` limit.

A malicious actor can exploit normalization bypasses to hide files. By appending a trailing space
or dot via `\\?\C:\Hidden \`, they create files that "normal" Windows applications cannot access,
read, or delete. Forensics tools must be evaluated to ensure they can handle un-normalized paths
during automated triage or collection.

## Caution

Naive handling of paths by tooling introduces reproducibility errors due to character encoding
nuances and environment abstractions:

* **Troublesome Codepoints (Unpaired Surrogates):** Modern Unicode applications require strict
  surrogate pairs. However, the NTFS file system allows legacy,
  [unpaired surrogates](unpaired_surrogates.md), such as `U+d800`, to exist in file names. When
  automated scanners find these paths, strict Python or XML parsers throw encoding errors, crash, or
  replace the invalid character with `U+FFFD`, rendering the path un-reproducible.
* **Ambiguous Path Separators:** While Windows treats backslashes (`\`) as segment separators and
  forward slashes (`/`) case-insensitively during standard API calls, underlying file systems like
  NTFS allow a forward slash (`/`) to exist as part of a file entry name if created outside normal
  operating system APIs. This obfuscates path boundaries during string splits.
* **Encoding Assumptions:** Older file systems like `ext2` handle file names as raw byte sequences
  rather than structured Unicode. Parsing an old Linux image assuming `UTF-8` can drop or distort
  non-standard characters, mutating the actual evidence path.
* **Environment Variables and Placeholders:** Artifacts, like LNK files, Prefetch, or registry
  configurations, often store abstracted paths like `%USERNAME%\Documents` or Known Folder GUIDs.
  Reconstructing the runtime reality requires mapping these placeholders back to the specific system
  configuration present in the hive at the time of execution.

## Takeaways for Examiners

To ensure high-fidelity automation and reporting, digital forensics professionals should:

1. **Verify Tool Behavior:** Validate whether your forensic suite silently drops or strips
   un-normalized characters, trailing spaces, or unpaired surrogates during logical imaging.
2. **Anchor with Unique Identifiers:** Combine path strings with absolute file system records, such
   as an **NTFS File Reference / MFT Entry number** or an **inode number**, to preserve path integrity
   even if the string encoding is corrupted.
3. **Account for Case Insensitivity:** Remember that while Windows is case-insensitive for file
   routing, it preserves case string styling upon creation. Discrepancies between expected and actual
   case structure can serve as a subtle indicator of unauthorized file manipulation or masquerading.

## External Links

* [File path formats on Windows systems](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats),
  by Microsoft
* [What's in a (file) path?](https://osdfir.blogspot.com/2023/07/whats-in-file-path.html),
  by Joachim Metz, July 19, 2023
