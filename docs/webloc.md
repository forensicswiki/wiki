---
tags:
  - File Formats
---
This is Mac OS X's internet shortcut file, similar to the Microsoft
Windows .URL file. However, due to the heavy usage of
[AppleDouble](appledouble_header_file.md) resources, the
expected data is actually stored as metadata and not in the the expected
data file location.

On the file system itself, the shortcut file named `News.webloc`
pointing to `http://news.google.com` is
actually a zero byte file. The URL is instead stored in the
`._News.webloc` file in a field with resource type '`url`'.

The contents of this resource file are visible with the Apple Developer
Tool
[DeRez](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/DeRez.1.html)
