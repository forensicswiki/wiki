---
tags:
  - File Formats
  - Articles that need to be expanded
---
## Cache files

The cache is stored in multiple:

| Filename | Description |
| --- | --- |
| index | The index file |
| data_# | Data block files |
| f_###### | (Separate) data stream file |

## Cache address

The cache address is 4 bytes in size and consists of:

| offset | size | value | description |
| --- | --- | --- | --- |
| *If file type is 0 (Separate file)* | | | |
| 0.0 | 28 bits | | File number. The value represents the value of # in f_###### |
| *Else* | | | |
| 0.0 | 16 bits | | Block number |
| 2.0 | 8 bits | | File number (or file selector). The value represents the value of # in data_# |
| 3.0 | 2 bits | | Block size. The number of contiguous blocks where 0 represents 1 block and 3 represents 4 blocks. |
| 3.2 | 2 bits | | Reserved |
| *Common* | | | |
| 3.4 | 3 bits | | File type |
| 3.7 | 1 bit | | Initialized flag |

### File types

| Value | Description |
| --- | --- |
| 0 | (Separate) data stream file |
| 1 | (Rankings) block data file (36 byte block data file) |
| 2 | 256 byte block data file |
| 3 | 1024 byte block data file |
| 4 | 4096 byte block data file |
| | |
| 6 | Unknown; seen on Mac OS X 0x6f430074 |

#### Examples

| Value | Description |
| --- | --- |
| 0x00000000 | Not initialized |
| 0x8000002a | Data stream file: f_00002a |
| 0xa0010003 | Block data file: data_1, block number 3, 1 block of size |

## Index file format (index)

Overview:

* File header
* least recently used (LRU) data (or eviction control data)
* index table

### File header

The index file header (struct IndexHeader) is 256 bytes in size and
consists of:

| offset | size | value | description |
| --- | --- | --- | --- |
| 0 | 4 | "\xc3\xca\x03\xc1" | Signature |
| 4 | 2 | | Minor version |
| 6 | 2 | | Major version |
| 8 | 4 | | Number of entries |
| 12 | 4 | | Stored data size |
| 16 | 4 | | Last created file number. The value represents the value of # in f_###### |
| 20 | 4 | | Dirty flag. Identifier for all entries being changed |
| 24 | 4 | | Usage statistics data cache address |
| 28 | 4 | | Table size. Where 0 represents 0x10000 (is this the same as the file size?) |
| 32 | 4 | | Signals a previous crash |
| 36 | 4 | | Identifier of an ongoing test or experiment |
| 40 | 8 | | Creation time |
| 48 | 52 x 8 = 208 | | Padding. Contains 0-byte values |

#### Format versions

| Value | Description |
| --- | --- |
| 2.0 | |
| 2.1 | |

### Least recently used (LRU) data

The least recently used (LRU) data (struct LruData) is 112 bytes in size
and consists of:

| offset | size | value | description |
| --- | --- | --- | --- |
| 0 | 2 x 4 = 8 | | Padding |
| 8 | 4 | | Filled flag. Value to indicate if when the cache was filled |
| 12 | 5 x 4 = 20 | | Array of sizes |
| 32 | 5 x 4 = 20 | | Array of head cache addresses |
| 52 | 5 x 4 = 20 | | Array of tail cache addresses |
| 72 | 4 | | Transaction cache address. Value to indicate an in-flight operation |
| 76 | 4 | | Operation. The in-flight operation |
| 80 | 4 | | Operations list. The in-flight operations list |
| 84 | 7 x 4 = 28 | | Padding. Contains 0-byte values |

### Array indexes

The array indexes correspond to the file types.

| Value | Description |
| --- | --- |
| 0 | Separate file |
| 1 | (Rankings) block data file |
| 2 | 256 byte block data file |
| 3 | 1024 byte block data file |
| 4 | 4096 byte block data file |

### Index table

The index table is an array of cache addresses.

## Data block file format (data_#)

Overview:

* File header
* array of blocks

### File header

The index file header (struct BlockFileHeader) is 8192 bytes in size and
consists of:

| offset | size | value | description |
| --- | --- | --- | --- |
| 0 | 4 | "\xc3\xca\x04\xc1" | Signature |
| 4 | 2 | | Minor version |
| 6 | 2 | | Major version |
| 8 | 2 | | File number (or file index). The value represents the value of # in data_# |
| 10 | 2 | | Next file number (or next file index). The value represents the value of # in data_# |
| 12 | 4 | | Block size (or cache entry) size |
| 16 | 4 | | Number of entries |
| 20 | 4 | | Maximum number of entries |
| 24 | 4 x 4 = 16 | | Array of empty entry counters. The counters of empty entries for each type |
| 40 | 4 x 4 = 16 | | Array of last used position (hints). The last used position for each type |
| 56 | 4 | | Updating. Value to keep track of updates to the header |
| 60 | 5 x 4 = 20 | | User |
| 80 | 2028 x 4 = 8112 | | Block allocation bitmap |

#### Format versions

| Value | Description |
| --- | --- |
| 2.0 | |
| 2.1 | |

### Cache entry

The cache entry (struct EntryStore) is 256 bytes in size and consists
of:

| offset | size | value | description |
| --- | --- | --- | --- |
| 0 | 4 | | Hash. The hash of the key |
| 4 | 4 | | Next entry cache address. The next entry with the same hash or bucket |
| 8 | 4 | | Rankings node cache address |
| 12 | 4 | | Reuse count. Value that indicates how often this entry was (re-)used |
| 16 | 4 | | Refetch count. Value that indicates how often this entry was (re-)fetched (or downloaded) |
| 20 | 4 | | Cache entry state |
| 24 | 8 | | Creation time |
| 32 | 4 | | Key data size |
| 36 | 4 | | Long key data cache address. The value is 0 if no long key data is present |
| 40 | 4 x 4 = 16 | | Array of data stream sizes |
| 56 | 4 x 4 = 16 | | Array of data stream cache addresses |
| 72 | 4 | | Cache entry flags |
| 76 | 4 x 4 = 16 | | Padding |
| 92 | 4 | | Self hash. The hash of the first 92 bytes of the cache entry is this used as a checksum? |
| 96 | 160 | | Key data. Contains an UTF-8 encoded string with an end-of-string character with the original URL |

#### Array indexes

The data stream array indexes correspond to:

| Value | Description |
| --- | --- |
| 0 | HTTP response headers |
| 1 | Page contents (Payload) |
| 2 | |
| 3 | |

#### Cache entry state

| Value | Identifier | Description |
| --- | --- | --- |
| 0 | ENTRY_NORMAL | Normal cache entry |
| 1 | ENTRY_EVICTED | The cache entry was recently evicted |
| 2 | ENTRY_DOOMED | The cache entry was doomed |

#### Cache entry flags

| Value | Identifier | Description |
| --- | --- | --- |
| 0x00000001 | PARENT_ENTRY | Parent cache entry |
| 0x00000002 | CHILD_ENTRY | Child cache entry |

### Rankings node

The rankings node (struct RankingsNode) is 36 bytes in size and consists
of:

| offset | size | value | description |
| --- | --- | --- | --- |
| 0 | 8 | | Last used. Contains LRU information? |
| 8 | 8 | | Last modified. Contains LRU information? |
| 16 | 4 | | Next rankings node cache address |
| 20 | 4 | | Previous rankings node cache address |
| 24 | 4 | | Cache entry cache address |
| 28 | 4 | | Is dirty flag |
| 32 | 4 | | Self hash. The hash of the first 32 bytes of the rankings node is this used as a checksum? |

## Data stream

The data stream is stored inside the data block file (data_#), for
small amounts of data, or stored as a separate file (f_######). The
data stream is stored as a [gzip file](gzip.md).

Note that the last modification time of the gzip file is set to 0.

## Hash

The hash algorithm used is referred to as SuperFastHash. A pseudo C
implementation:

```C
uint32_t SuperFastHash(
          const uint8_t *key,
          size_t key_size )
{
    size_t key_index    = 0;
    size_t remainder    = 0;
    uint32_t hash_value = 0;
    uint32_t temp_value = 0;

    if( ( key == NULL ) || ( key_size == 0 ) )
    {
       return( 0 );
    }
    remainder = key_size % 4;
    key_size -= remainder;

    for( key_index = 0;
         key_index < key_size;
         key_index += 4 )
    {
        hash_value += key[ key_index ] + ( key[ key_index + 1 ] << 8 );
        temp_value  = key[ key_index + 2 ] + ( key[ key_index + 3 ] << 8 );

        temp_value = ( temp_value << 11 ) ^ hash_value;

        hash_value  = ( hash_value << 16 ) ^ temp_value;
        hash_value += hash_value >> 11;
    }

    switch( remainder )
    {
        case 3:
            hash_value += key[ key_index ] + ( key[ key_index + 1 ] << 8 );
            hash_value ^= hash_value<< 16;
            hash_value ^= key[ key_index + 2 ] << 18;
            hash_value += hash_value >> 11;
            break;

        case 2:
            hash_value += key[ key_index ] + ( key[ key_index + 1 ] << 8 );
            hash_value ^= hash_value << 11;
            hash_value += hash_value >> 17;
            break;

        case 1:
            hash_value += key[ key_index ];
            hash_value ^= hash_value << 10;
            hash_value += hash_value >> 1;
            break;
    }

    /* Force "avalanching" of final 127 bits */
    hash_value ^= hash_value << 3;
    hash_value += hash_value >> 5;
    hash_value ^= hash_value << 4;
    hash_value += hash_value >> 17;
    hash_value ^= hash_value << 25;
    hash_value += hash_value >> 6;

    return hash_value;
}
```

## See Also

* [Google Chrome](google_chrome.md)
* [gzip](gzip.md)

## External Links

* [Disk Cache](https://www.chromium.org/developers/design-documents/network-stack/disk-cache/),
  The Chromium Projects
* [Chrome Cache file format](https://github.com/libyal/dtformats/blob/main/documentation/Chrome%20Cache%20file%20format.asciidoc),
  originally by the [Plaso project](plaso.md) transitioned to the dtFormats project, April 2014
