---
tags:
  - No Category
---
How do tools handle imaging tools with bad sectors?

To find this out, you need (for starters) disks that can reliably
generate faculty sectors. The NIST computer forensic tool testing
program has some of them.

They found that IXimager did a pretty good job.

But sometimes, when it encountered a disk with a single faculty sector,
it would miss the next 7.

Encase 5 & 6 let you set an error granularity. But if they find an error
in their window, they won't get any of the blocks.

What's the right thing to do? For starters, the programs should document
how they handle bad blocks.