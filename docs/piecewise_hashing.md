---
tags:
  -  Articles that need to be expanded 
---
**Piecewise hashing** is a [hashing](hashing.md) technique to
divide an input into chunks and hash each chunk separately. It was
invented by [Nick Harbour](nick_harbour.md) in
[dcfldd](dcfldd.md) to improve the reliability of [disk
imaging](disk_imaging.md). The theory was that if one chunk
became corrupted, only the integrity of that chunk would be threatened.
The piecewise hashes of the other chunks, which hadn't changed, could be
used to prove their integrity.

## References

- [md5deep](md5deep.md), [hashdeep](hashdeep "wikilink"), etc.
- [dcfldd](dcfldd.md)

## See Also

- [Context Triggered Piecewise
  Hashing](context_triggered_piecewise_hashing.md)