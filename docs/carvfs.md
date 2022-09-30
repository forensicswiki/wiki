---
tags:
  - No Category
---
CarvFs is a modular [Fuse](fuse.md) based user space file system
on top of [LibCarvPath](libcarvpath.md). CarvFS makes CarvPath
style annotations as used by LibCarvPath available as files. Using
CarvFs makes it possible to process carved entities using [zero storage
carving](zero_storage_carving.md).

CarvFs is modular with respect to access to image files. The CarvFs
distribution comes with a default module for access to [(split) raw
files](raw_image_format.md).

A separate [Libewf](libewf.md) module is available for access to
[EWF images](encase_image_file_format.md).

For use in computer forensic frameworks, CarvFS is superseded by the
closely related [MattockFS](mattockfs.md).

## External Links

- [Project site](https://github.com/DNPA/carvfs)