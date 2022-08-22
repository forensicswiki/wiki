frag_find is a program for finding blocks of one or more MASTER files in
a disk IMAGE file. This is useful in cases where a MASTER file has been
stolen and you wish to establish that the file has been present on a
subject's drive. If most of the MASTER file's sectors are found on the
IMAGE drive---and if the sectors are in consecutive sector runs---then
the chances are excellent that the file was once there.

The idea of using individual sector hashes in this manner has been
discussed in the forensic community for several years. Frag_find is an
efficient and easy-to-use tool that perform this process.

frag_find relies on two observations about files and file systems:

1.  Most file systems tend to block-align files stored within the file
    system. So if you break up an 8K file into 16 different 512-byte
    blocks, then store that file in a file system, it's likely that
    those 16 different "file blocks" will be stored each in its own
    individual disk sector.
2.  Most 512-byte blocks within most files are "unique" --- that is,
    they do not appear by chance in other files. This is especially true
    for files that are compressed (like zip and docx files) and files
    that are encrypted. It is less true of files such as Microsoft Word
    doc files that are likely to have one or more blocks filled with
    NULLs or some other constant.

frag_find deals with the problem of non-unique blocks by looking for
runs of matching blocks, rather than individual blocks.

frag_find is fast because:

- Initial filtering of presence/absence is done using the NPS Bloom
  filter implementation, an efficient memory-mapped Bloom implementation
  designed to be used with hash functions.
- Hashes are stored in efficient C++ structures.
- All computations are done in binary, rather than hex.

## OPTIONS

The following options are available:

`  -b blocksize   - sets the blocksize (default is 512 bytes).`
`  -s `<start>`     - start the image scan at `<start>` (default is start`
`                   of image)`
`  -e `<end>`       - stop the image scan at `<end>` (default is end of image)         `
`  -r             - prints the raw association map, in addition to the cleaned one`

## MEMORY USAGE

frag_find uses 512MB of RAM for the Bloom filter, approximately 1MB of
RAM for bookkeeping, and roughly 64 bytes for every block of the target
file.

## AVAILABILITY

- Download: <http://digitalcorpora.org/downloads/frag_find>
- github: <https://github.com/simsong/frag_find>