---
tags:
  - Tools
  - Memory Analysis
---
> This article was copied from the Rekall Forensics blog, but was never posted given it was not
> finalized. Copied with permission for historical preservation.

Providing a way to accurately determine the profile of a running operating system is at the core of
Rekall's ability to analyze memory images.

Trying to analyze an entire fleet of machines in an unattended way (such as via GRR) presents an
additional challenge. Recovering from profile detection errors as we would do when manually
analyzing an image is infeasible, because it's a manual debugging process that doesn't scale. A
profile detection method that is robust is paramount to its succes.

But how does profile detection really work on each operating system? At a glance:

* For Windows, to find the exact kernel version we use a unique identifier that's present in the
  kernel image itself (the UUID). We scan physical memory to find PE headers that contain this UUID.
  Fortunately, Windows publishes debug information for almost all of their kernels. We obtain symbol
  data from Microsoft by UUID, store this information and we're done.
* On Mac OS X, there's a small enough number of versions of the XNU kernel that a certain string is
  always present at unique locations, relative to the kernel start. We maintain
* Linux distributions publish new kernels every so often. Given the prevalence of many different
  versions of several Linux distributions, thousands of kernels exist that can be widely used at one
  time.

As an example, take the kernel releases for anyone Ubuntu flavor.

This iterative, repeated release of updated kernels means the differences between one version to
the next may simply be a couple of lines added and removed to the code. This means that sometimes
we deal with kernels that are almost exactly the same, except for a few differences.

Up until now we only had one method of identifying Linux kernels. We scanned memory looking for a
string called the linux_proc_banner (cat /proc/banner will show it to you) and we used it to decide
which profile to choose. An example of an Ubuntu 14.04 (trusty) string: "Linux version
3.13.0-71-generic (buildd@lgw01-09) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #114-Ubuntu SMP
Tue Dec 1 02:34:22 UTC 2015". We take the 3.13.0-71-generic string to find the profile in our
repository.

The reality of this method is that it's insufficient. First of all, the string is not strictly tied
to the contents of the kernel. I could take the kernel sources for this version, change the
"3.13.0-71-generic" string to "9.99-9-99-generic" and it would virtually be the same. The
generated profile would essentially be the same.

The second problem is that even if you assume the version string won't be tampered with, version
string clashes can happen. For example, Ubuntu trusty (14.04) and precise (12.04) use the same
kernel version string but the kernels are actually different. Alinux-image-3.13.0-71-generic
package exists both on trusty and precise, but they are different kernels.

So we need a new, better method of identification.

## First idea: symbol names

The first idea was to use symbol names alone. Symbols are the public information exported by a
binary program that help the linked how to glue a piece of code that requests usage of an external
resource (for example a library function) to the code that holds it (the library). Symbols are
identified by a name and have a value.

We use these symbols profusely within Rekall, to access things like the head of the processes
linked list or the list of loaded kernel modules by knowing their virtual address. Because each new
kernel version changes code, there should be some symbols added and other removed here and there,
correct?

Not entirely. The fine granularity at which new kernel packages are released by different Linux
distributions produce kernels that have the exact same symbol names... but at differet locations.

So the presence of a set of symbol names alone does not uniquely identify a kernel:

Here's the number of different profiles only by symbol. We use a function that orders all the
symbol names for a profile and does a sha256 of it.

```text
ipdb> symbols_hash = [(index.CalculateRawSymbolsHash(p[1]), p[0], p[1]["$CONSTANTS"]) for p in new_profile_candidates]
ipdb> len(set([x[0] for x in symbols_hash]))
363

( with filtering )
ipdb> symbols_hash_f = [(index.CalculateRawSymbolsHash({"$CONSTANTS":index.FilterSymbols(p[1]["$CONSTANTS"])}), p[0], index.FilterSymbols(p[1]["$CONSTANTS"])) for p in new_profile_candidates]

ipdb> len(set([x[0] for x in symbols_hash_f]))
336

And here's the number of different profiles by symbol-offset combination

ipdb> symboloffsets_hash = [(profile_index.SymbolOffsetIndex.CalculateRawProfileHash(p[1]), p[0], p[1]["$CONSTANTS"]) for p in new_profile_candidates]

ipdb> len(set([x[0] for x in symboloffsets_hash]))
396

( with filtering )
ipdb> symboloffsets_hash_f = [(profile_index.LinuxSymbolOffsetIndex.CalculateRawProfileHash(p[1]), p[0], profile_index.LinuxSymbolOffsetIndex.FilterSymbols(p[1]["$CONSTANTS"])) for p in new_profile_candidates]
ipdb> len(set([x[0] for x in symboloffsets_hash_f]))
381
```

First extract all hashes that are dupped on each:

```bash
awk '{print $1}' symbols_hash  | sort | uniq -c | grep -v " 1 " > symbols_hash.dups
awk '{print $1}' symboloffsetss_hash  | sort | uniq -c | grep -v " 1 " > symboloffsetss_hash.dups
```

Then find the actual dupped profiles:

```bash
for i in `awk '{print $2}' symboloffsetss_hash.dups`; do grep $i symboloffsetss_hash; done | awk '{print $2}' > symboloffsetss_hash.dups_profiles

for i in `awk '{print $2}' symbols_hash.dups`; do grep $i symbols_hash; done | awk '{print $2}' > symbols_hash.dups_profiles
```

And this is the list of profiles that are different by symbol-offset but not by symbol name (that
is, they have exactly the same symbol names, but different offsets on these symbols):

```bash
$ grep -Fv -f  symboloffsetss_hash.dups_profiles symbols_hash.dups_profiles | sort | uniq
./Linux/Ubuntu/12.04/x86_64/3.2.0-41-generic.gz
./Linux/Ubuntu/12.04/x86_64/3.2.0-41-virtual.gz
./Linux/Ubuntu/12.04/x86_64/3.2.0-43-generic.gz
./Linux/Ubuntu/12.04/x86_64/3.2.0-43-virtual.gz
...
./Linux/Ubuntu/14.04/x86_64/3.19.0-39-generic.gz
./Linux/Ubuntu/14.04/x86_64/3.19.0-39-lowlatency.gz
```

Taking an example:

```bash
$ grep -F ./Linux/Ubuntu/12.04/x86_64/3.2.0-41-generic.gz symbols_hash
8b303725ea36d3be5e9fdf1b28118aafbf2a04c3cd4403afe3cc286dc4b39ed8        ./Linux/Ubuntu/12.04/x86_64/3.2.0-41-generic.gz

$ grep 8b303725ea36d3be5e9fdf1b28118aafbf2a04c3cd4403afe3cc286dc4b39ed8 symbols_hash
8b303725ea36d3be5e9fdf1b28118aafbf2a04c3cd4403afe3cc286dc4b39ed8        ./Linux/Ubuntu/12.04/x86_64/3.2.0-41-generic.gz
8b303725ea36d3be5e9fdf1b28118aafbf2a04c3cd4403afe3cc286dc4b39ed8        ./Linux/Ubuntu/12.04/x86_64/3.2.0-43-generic.gz
```

Even if we take the source and filter by code symbols, that still holds true:

```bash
$ unzip 3.2.0-41-generic.zip
$ unzip 3.2.0-43-generic.zip
$ grep ' [tT] ' boot/System.map-3.2.0-41-generic | sort > boot/System.map-3.2.0-41-generic.sorted.filtered
$ grep ' [tT] ' boot/System.map-3.2.0-43-generic | sort > boot/System.map-3.2.0-43-generic.sorted.filtered
$ diff -u System.map-3.2.0-41-generic.sorted.filtered System.map-3.2.0-43-generic.sorted.filtered | wc -l
48859
```

## Second idea: symbols

So, we thought: how about we just add symbol value information. This way, instead of comparing just
the presence of symbol names, we check their value. Would we be able to uniquely identify a set of
known linux kernels by their symbols?
