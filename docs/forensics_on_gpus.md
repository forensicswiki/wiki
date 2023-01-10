---
tags:
  - No Category
---
Using a **Graphical Processing Unit** (**GPU**) for forensics analysis
attempts to make use of the significant, parallel processing power
available on these high cards for a different purpose than their
original intent. The idea of forensic analysis on a GPU was first
proposed by Marziale, Richard and Roussev in 2007 with a version of
[Scalpel](scalpel.md) that utilized a GPU.

## Password Cracking

Password cracking process accelerated by using GPU is several times
faster than in CPU-only mode.

For example, password recovering speed for [MD5](md5.md) hash
using Core2 Duo is about 4,7 millions passwords per second. By using
8800GTX it is possible to reach 265 millions passwords per second.

- [ElcomSoft Distributed Password
  Recovery](https://www.elcomsoft.com/edpr.html)
- [ElcomSoft Password Recovery
  Bundle](https://www.elcomsoft.com/edfb.html)
- [Extreme GPU Bruteforcer](http://www.insidepro.com/eng/egb.shtml)
- [Passware Kit
  Forensic](https://www.passware.com/)
- [Passcovery
  Suite](https://passcovery.com/products/passcoverysuite.htm)

## Bibliography

<bibtex> @inproceedings{p73-marziale,

` author="Lodovico Marziale and  Golden G. Richard III and Vassil Roussev",`
` title="Massive Threading: Using GPUs to Increase the Performance of Digital Forensics Tools",`
` booktitle="DFRWS: Proceedings of the 7th Annual Digital Forensics Research Workshop",`
` year=2007,`
` url="`[`http://dfrws.org/2007/proceedings/p73-marziale.pdf`](http://dfrws.org/2007/proceedings/p73-marziale.pdf)`"`

} </bibtex>

<bibtex> @inproceedings{1191892,

`author = {Nigel Jacob and Carla Brodley},`
`title = {Offloading IDS Computation to the GPU},`
`booktitle = {ACSAC '06: Proceedings of the 22nd Annual Computer Security Applications Conference on Annual Computer Security Applications Conference},`
`year = {2006},`
`isbn = {0-7695-2716-7},`
`pages = {371--380},`
`doi = {`[`http://dx.doi.org/10.1109/ACSAC.2006.35`](http://dx.doi.org/10.1109/ACSAC.2006.35)`},`
`publisher = {IEEE Computer Society},`
`address = {Washington, DC, USA},`
` url="`[`https://www.acsac.org/2006/papers/74.pdf`](https://www.acsac.org/2006/papers/74.pdf)`"`
`}`

</bibtex>