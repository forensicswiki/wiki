---
tags:
  - No Category
---
Optimistic decompression is a digital forensics technique in which each
byte of an input buffer is examined for the possibility of compressed
data. If data is found that *might* be compressed, a decompression
algorithm is invoked to perform a *trial decompression.* If the
decompressor does not produce an error, the decompressed data is
processed. The decompressor is thus called *optimistically*---that is,
with the hope that it might be successful.

Optimistic decompression is used as a tool to validate JPEGs that are
produced by [file carving](file_carving.md). The approach can
also be used for fragment reassembly carving by attempting to combine
different combinations of fragments, looking for a combination that
produces neither decompression errors nor visual discontinuities. This
is the approach used by the [Adroit](adroit_photo_forensics.md) file carver.
