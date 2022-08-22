**Piecewise hashing** is a [hashing](hashing "wikilink") technique to
divide an input into chunks and hash each chunk separately. It was
invented by [Nick Harbour](Nick_Harbour "wikilink") in
[dcfldd](dcfldd "wikilink") to improve the reliability of [disk
imaging](Disk_Imaging "wikilink"). The theory was that if one chunk
became corrupted, only the integrity of that chunk would be threatened.
The piecewise hashes of the other chunks, which hadn't changed, could be
used to prove their integrity.

## References

- [md5deep](md5deep "wikilink"), [hashdeep](hashdeep "wikilink"), etc.
- [dcfldd](dcfldd "wikilink")

## See Also

- [Context Triggered Piecewise
  Hashing](Context_Triggered_Piecewise_Hashing "wikilink")