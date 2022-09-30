---
tags:
  - No Category
---
**Bulk Extractor** (**bulk_extractor**) is a feature extraction tool
written in C++ for extracting features from media images. Extracted
features are stored in feature files that can be easily inspected,
parsed, or processed with automated tools. Some Python programs that
process feature files are available. Also, feature files may be browsed
using the [Bulk Extractor Viewer](bulk_extractor_viewer.md) User
Interface.

**Bulk Extractor** is fast. Rather than parsing file system structures,
it parallel-processes 16MiByte pages of media on multiple cores.

**Bulk Extractor** is thorough. It searches for multiple feature types.
Additionally, it recursively decompresses and reprocesses compressed
data.

## See Also

- [Bulk Extractor Viewer](bulk_extractor_viewer.md), the User
  Interface for browsing features that have been extracted via the
  **Bulk Extractor** tool.

## External Links

- [Official website](https://github.com/simsong/bulk_extractor/wiki)