---
tags:
  -  Memory Analysis
  -  Tools 
  -  Windows
  -  Linux
  -  MacOS
  -  Opensource Software
---
The **Volatility Framework** is a completely open collection of tools,
implemented in Python under the GNU General Public License (GPL v2), for
the extraction of digital artifacts from volatile memory (RAM) samples.
The extraction techniques are performed completely independent of the
system being investigated but offer unprecedented visibility into the
runtime state of the system. The framework is intended to introduce
people to the techniques and complexities associated with extracting
digital artifacts from volatile memory samples and provide a platform
for further work into this exciting area of research.

The project was originally developed by and is now headed up by [AAron
Walters](aaron_walters.md) of [Volatile
Systems](volatile_systems.md).

## Plugins

See: [List of Volatility Plugins](list_of_volatility_plugins.md)

## Memory acquisition drivers

In 2012 [Michael Cohen](michael_cohen.md) contributed both a
Linux and a Windows Open Source memory (acquisition) driver to the
Volatility project as part of the Technology Preview (TP) version, aka
scudette branch. Since the scudette branch of Volatility has moved on as
a separate project, the drivers can now be found as part of the
[rekall](rekall.md) project.

## See Also

- [List of Volatility Plugins](list_of_volatility_plugins.md)

## External Links

- [Official web site](https://code.google.com/p/volatility/)
- [Code
  repository](http://code.google.com/p/volatility/source/checkout),
  direct link to
  [source](http://code.google.com/p/volatility/source/browse/)
- [Volatility Documentation](http://code.google.com/p/volatility/w/list)

### Third party documentation

- [Set Up to More Memory
  Forensics!](http://sketchymoose.blogspot.com/2011/10/set-up-to-more-memory-forensics.html),
  October 2011
- [Memory Forensics With Volatility (Technology
  Preview)](https://docs.google.com/presentation/d/1KsZGF6cQ-N8ngABFGCZf8pTQQ5CZ19VoAHq5cO5ZPdE/edit),
  by [Michael Cohen](michael_cohen.md), October 2012
- [Using Volatility: Suspicious Process
  (1/2)](http://www.youtube.com/watch?v=8HsZLge0wWc)
- [Using Volatility: Suspicious Process
  (2/2)](http://www.youtube.com/watch?v=XTZPNk-Esok)