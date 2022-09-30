---
tags:
  - No Category
---
We have installed the BibTeX mediaWiki Extension. Even better, Simson
Garfinkel has started fixing it!

Here's how it works.

You can insert BibTeX entries into any mediawiki page by enclosing them
in <bibtex> tags, like this:

` `<bibtex>
` @inproceedings{garfinkel:carving07,`
`   title="Carving Contiguous and Fragmented Files with Fast Object Validation",`
`   author="Simson Garfinkel",`
`   booktitle={Proceedings of the 7th Annual Digital Forensic Research Workshop (DFRWS)},`
`   journal="Digital Investigation",`
`   year=2007,`
`   month=Aug,`
`   location="Pittsburgh, PA",`
`   url="`[`http://www.simson.net/clips/academic/2007.DFRWS.pdf`](http://www.simson.net/clips/academic/2007.DFRWS.pdf)`"`
` }`
` `</bibtex>

This produces:

<bibtex> @inproceedings{garfinkel:carving07,

` title="Carving Contiguous and Fragmented Files with Fast Object Validation",`
` author="Simson Garfinkel",`
` booktitle={Proceedings of the 7th Annual Digital Forensic Research Workshop (DFRWS)},`
` journal="Digital Investigation",`
` year=2007,`
` month=Aug,`
` location="Pittsburgh, PA",`
`   url="`[`http://www.simson.net/clips/academic/2007.DFRWS.pdf`](http://www.simson.net/clips/academic/2007.DFRWS.pdf)`"`

} </bibtex>

If you have any comments about this, please contact [Simson
Garfinkel](simson_garfinkel.md). Thanks!