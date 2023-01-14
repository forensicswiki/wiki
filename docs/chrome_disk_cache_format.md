---
tags:
  - File Formats
  - Articles that need to be expanded
  - Cache
---
## Cache files

The cache is stored in multiple:

| Filename  | Description                 |
|-----------|-----------------------------|
| index     | The index file              |
| data_#   | Data block files            |
| f_###### | (Separate) data stream file |

## Cache address

The cache address is 4 bytes in size and consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><i>If file type is 0 (Separate file)</i></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>0.0</p></td>
<td><p>28 bits</p></td>
<td></td>
<td><p>File number<br />
The value represents the value of # in f_######</p></td>
</tr>
<tr class="odd">
<td><p><i>Else</i></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>0.0</p></td>
<td><p>16 bits</p></td>
<td></td>
<td><p>Block number</p></td>
</tr>
<tr class="odd">
<td><p>2.0</p></td>
<td><p>8 bits</p></td>
<td></td>
<td><p>File number (or file selector)<br />
The value represents the value of # in data_#</p></td>
</tr>
<tr class="even">
<td><p>3.0</p></td>
<td><p>2 bits</p></td>
<td></td>
<td><p>Block size<br />
The number of contiguous blocks where 0 represents 1 block and 3
represents 4 blocks.</p></td>
</tr>
<tr class="odd">
<td><p>3.2</p></td>
<td><p>2 bits</p></td>
<td></td>
<td><p>Reserved</p></td>
</tr>
<tr class="even">
<td><p><i>Common</i></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>3.4</p></td>
<td><p>3 bits</p></td>
<td></td>
<td><p>File type</p></td>
</tr>
<tr class="even">
<td><p>3.7</p></td>
<td><p>1 bit</p></td>
<td></td>
<td><p>Initialized flag</p></td>
</tr>
</tbody>
</table>

### File types

| Value | Description                                          |
|-------|------------------------------------------------------|
| 0     | (Separate) data stream file                          |
| 1     | (Rankings) block data file (36 byte block data file) |
| 2     | 256 byte block data file                             |
| 3     | 1024 byte block data file                            |
| 4     | 4096 byte block data file                            |
|       |                                                      |
| 6     | Unknown; seen on Mac OS X 0x6f430074                 |

#### Examples

| Value      | Description                                              |
|------------|----------------------------------------------------------|
| 0x00000000 | Not initialized                                          |
| 0x8000002a | Data stream file: f_00002a                               |
| 0xa0010003 | Block data file: data_1, block number 3, 1 block of size |

## Index file format (index)

Overview:

- File header
- least recently used (LRU) data (or eviction control data)
- index table

### File header

The index file header (struct IndexHeader) is 256 bytes in size and
consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>"\xc3\xca\x03\xc1"</p></td>
<td><p>Signature</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Minor version</p></td>
</tr>
<tr class="odd">
<td><p>6</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Major version</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Number of entries</p></td>
</tr>
<tr class="odd">
<td><p>12</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Stored data size</p></td>
</tr>
<tr class="even">
<td><p>16</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Last created file number<br />
The value represents the value of # in f_######</p></td>
</tr>
<tr class="odd">
<td><p>20</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Dirty flag<br />
Identifier for all entries being changed</p></td>
</tr>
<tr class="even">
<td><p>24</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Usage statistics data cache address</p></td>
</tr>
<tr class="odd">
<td><p>28</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Table size<br />
Where 0 represents 0x10000 (is this the same as the file size?)</p></td>
</tr>
<tr class="even">
<td><p>32</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Signals a previous crash</p></td>
</tr>
<tr class="odd">
<td><p>36</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Identifier of an ongoing test or experiment</p></td>
</tr>
<tr class="even">
<td><p>40</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Creation time</p></td>
</tr>
<tr class="odd">
<td><p>48</p></td>
<td><p>52 x 8 = 208</p></td>
<td></td>
<td><p>Padding<br />
Contains 0-byte values</p></td>
</tr>
</tbody>
</table>

#### Format versions

| Value | Description |
|-------|-------------|
| 2.0   |             |
| 2.1   |             |

### Least recently used (LRU) data

The least recently used (LRU) data (struct LruData) is 112 bytes in size
and consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>2 x 4 = 8</p></td>
<td></td>
<td><p>Padding</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Filled flag<br />
Value to indicate if when the cache was filled</p></td>
</tr>
<tr class="odd">
<td><p>12</p></td>
<td><p>5 x 4 = 20</p></td>
<td></td>
<td><p>Array of sizes</p></td>
</tr>
<tr class="even">
<td><p>32</p></td>
<td><p>5 x 4 = 20</p></td>
<td></td>
<td><p>Array of head cache addresses</p></td>
</tr>
<tr class="odd">
<td><p>52</p></td>
<td><p>5 x 4 = 20</p></td>
<td></td>
<td><p>Array of tail cache addresses</p></td>
</tr>
<tr class="even">
<td><p>72</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Transaction cache address<br />
Value to indicate an in-flight operation</p></td>
</tr>
<tr class="odd">
<td><p>76</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Operation<br />
The in-flight operation</p></td>
</tr>
<tr class="even">
<td><p>80</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Operations list<br />
The in-flight operations list</p></td>
</tr>
<tr class="odd">
<td><p>84</p></td>
<td><p>7 x 4 = 28</p></td>
<td></td>
<td><p>Padding<br />
Contains 0-byte values</p></td>
</tr>
</tbody>
</table>

### Array indexes

The array indexes correspond to the file types.

| Value | Description                |
|-------|----------------------------|
| 0     | Separate file              |
| 1     | (Rankings) block data file |
| 2     | 256 byte block data file   |
| 3     | 1024 byte block data file  |
| 4     | 4096 byte block data file  |

### Index table

The index table is an array of cache addresses.

## Data block file format (data_#)

Overview:

- File header
- array of blocks

### File header

The index file header (struct BlockFileHeader) is 8192 bytes in size and
consists of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>"\xc3\xca\x04\xc1"</p></td>
<td><p>Signature</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Minor version</p></td>
</tr>
<tr class="odd">
<td><p>6</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Major version</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>2</p></td>
<td></td>
<td><p>File number (or file index)<br />
The value represents the value of # in data_#</p></td>
</tr>
<tr class="odd">
<td><p>10</p></td>
<td><p>2</p></td>
<td></td>
<td><p>Next file number (or next file index)<br />
The value represents the value of # in data_#</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Block size (or cache entry) size</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Number of entries</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Maximum number of entries</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>4 x 4 = 16</p></td>
<td></td>
<td><p>Array of empty entry counters<br />
The counters of empty entries for each type</p></td>
</tr>
<tr class="even">
<td><p>40</p></td>
<td><p>4 x 4 = 16</p></td>
<td></td>
<td><p>Array of last used position (hints)<br />
The last used position for each type</p></td>
</tr>
<tr class="odd">
<td><p>56</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Updating<br />
Value to keep track of updates to the header</p></td>
</tr>
<tr class="even">
<td><p>60</p></td>
<td><p>5 x 4 = 20</p></td>
<td></td>
<td><p>User</p></td>
</tr>
<tr class="odd">
<td><p>80</p></td>
<td><p>2028 x 4 = 8112</p></td>
<td></td>
<td><p>Block allocation bitmap</p></td>
</tr>
</tbody>
</table>

#### Format versions

| Value | Description |
|-------|-------------|
| 2.0   |             |
| 2.1   |             |

### Cache entry

The cache entry (struct EntryStore) is 256 bytes in size and consists
of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Hash<br />
The hash of the key</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Next entry cache address<br />
The next entry with the same hash or bucket</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Rankings node cache address</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Reuse count<br />
Value that indicates how often this entry was (re-)used</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Refetch count<br />
Value that indicates how often this entry was (re-)fetched (or
downloaded)</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Cache entry state</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Creation time</p></td>
</tr>
<tr class="even">
<td><p>32</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Key data size</p></td>
</tr>
<tr class="odd">
<td><p>36</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Long key data cache address<br />
The value is 0 if no long key data is present</p></td>
</tr>
<tr class="even">
<td><p>40</p></td>
<td><p>4 x 4 = 16</p></td>
<td></td>
<td><p>Array of data stream sizes</p></td>
</tr>
<tr class="odd">
<td><p>56</p></td>
<td><p>4 x 4 = 16</p></td>
<td></td>
<td><p>Array of data stream cache addresses</p></td>
</tr>
<tr class="even">
<td><p>72</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Cache entry flags</p></td>
</tr>
<tr class="odd">
<td><p>76</p></td>
<td><p>4 x 4 = 16</p></td>
<td></td>
<td><p>Padding</p></td>
</tr>
<tr class="even">
<td><p>92</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Self hash<br />
The hash of the first 92 bytes of the cache entry is this used as a
checksum?</p></td>
</tr>
<tr class="odd">
<td><p>96</p></td>
<td><p>160</p></td>
<td></td>
<td><p>Key data<br />
Contains an UTF-8 encoded string with an end-of-string character with
the original URL</p></td>
</tr>
</tbody>
</table>

#### Array indexes

The data stream array indexes correspond to:

| Value | Description             |
|-------|-------------------------|
| 0     | HTTP response headers   |
| 1     | Page contents (Payload) |
| 2     |                         |
| 3     |                         |

#### Cache entry state

| Value | Identifier    | Description                          |
|-------|---------------|--------------------------------------|
| 0     | ENTRY_NORMAL  | Normal cache entry                   |
| 1     | ENTRY_EVICTED | The cache entry was recently evicted |
| 2     | ENTRY_DOOMED  | The cache entry was doomed           |

#### Cache entry flags

| Value      | Identifier   | Description        |
|------------|--------------|--------------------|
| 0x00000001 | PARENT_ENTRY | Parent cache entry |
| 0x00000002 | CHILD_ENTRY  | Child cache entry  |

### Rankings node

The rankings node (struct RankingsNode) is 36 bytes in size and consists
of:

<table>
<thead>
<tr class="header">
<th><p>offset</p></th>
<th><p>size</p></th>
<th><p>value</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Last used<br />
Contains LRU information?</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>8</p></td>
<td></td>
<td><p>Last modified<br />
Contains LRU information?</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Next rankings node cache address</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Previous rankings node cache address</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Cache entry cache address</p></td>
</tr>
<tr class="even">
<td><p>28</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Is dirty flag</p></td>
</tr>
<tr class="odd">
<td><p>32</p></td>
<td><p>4</p></td>
<td></td>
<td><p>Self hash<br />
The hash of the first 32 bytes of the rankings node is this used as a
checksum?</p></td>
</tr>
</tbody>
</table>

## Data stream

The data stream is stored inside the data block file (data_#), for
small amounts of data, or stored as a separate file (f_######). The
data stream is stored as a [gzip file](gzip.md).

Note that the last modification time of the gzip file is set to 0.

## Hash

The hash algorithm used is referred to as SuperFastHash. A pseudo C
implementation:

    uint32_t SuperFastHash(
              const uint8_t *key,
              size_t key_size )
    {
        size_t key_index    = 0;
        size_t remainder    = 0;
        uint32_t hash_value = 0;
        uint32_t temp_value = 0;

        if( ( key == NULL ) || ( key_siz 0 ) )
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

## See Also

- [Google Chrome](google_chrome.md)
- [gzip](gzip.md)

## External Links

- [Disk Cache](https://www.chromium.org/developers/design-documents/network-stack/disk-cache/),
  The Chromium Projects
- [Chrome Cache file format](https://github.com/libyal/dtformats/blob/main/documentation/Chrome%20Cache%20file%20format.asciidoc),
  orignally by the [Plaso project](plaso.md) transitioned to the dtFormats project, April 2014
