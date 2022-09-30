---
tags:
  - No Category
---
**Data reduction** is the science of eliminating information from
consideration. Although that may sound counter to the goal of [computer
forensics](computer_forensics.md), today's computers contain too
much information for a single [investigator](investigator.md) to
completely evaluate. Thus, those data that can be eliminated from
consideration should be removed, freeing an investigator to concentrate
on the truly meaningful pieces.

## Hash Analysis

A [hash](hash.md) is a mathmatical transform that reduces an
input of arbitrary size to a fixed value. It has the property that any
two inputs that have the same hash are almost certainly the same. In
this vein, an investigator can compute hashes of known good and known
bad inputs (e.g. files) and use those hashes to search for those known
files in a set of unknown files. For example, the
[NIST](nist.md) [National Software Reference
Library](national_software_reference_library.md) provides
several million hashes of known good [operating
system](operating_system.md) files. If an invesigator can match
those known hashes into an unknown set of files, the matching files can
be eliminated from consideration.