---
tags:
  - Concept
---
In digital forensics, a timeline is often the outline of the entire story. It ties together system
actions, user behaviors, and security incidents into a cohesive chronological narrative. However,
timestamp analysis is rarely as straightforward as sorting a list from oldest to newest. For a
forensic analyst, understanding the underlying **mechanisms of date and time values, specifically
their formats, accuracy, precision, and granularity, is critical to preventing misinterpretation
and flawed conclusions**.

## Storage vs. Value Granularity: The Analyst's Blindspot

When exploring temporal artifacts, analysts must establish a clear distinction between how a system
*stores* time and the *actual resolution* of the data within it:

* **Accuracy &amp; Precision:** **Accuracy** reflects how close a timestamp is to the actual, true
  time of the event. **Precision** refers to the consistency or closeness of agreement among a set
  of recorded results.
* **Storage Granularity:** This is the upper bound of a timestamp format's capacity based on its
  technical design. For example, a format might be capable of tracking time down to the nanosecond.
* **Value Granularity:** Just because a format *can* store nanoseconds does not mean the
  operating system or application updates it at that frequency. For instance, a system might record
  a file access timestamp using a highly precise structure, but the operating system may only update
  that specific artifact once every hour or day.

## A Tale of Two Formats: FILETIME vs. POSIX `time_t`

Different operating systems and file systems rely on wildly distinct structures to track time. Two
of the most common formats encountered in digital forensics highlight these vast engineering
differences:

### Windows FILETIME

Used natively within the NTFS file system, a **FILETIME structure stores date and time values as a
64-bit integer representing the number of 100-nanosecond intervals since January 1, 1601 UTC**.

**Forensic Caveat:** While its *storage granularity* is incredibly high (100-ns intervals), its
*value granularity* varies wildly. For example, the NTFS last access time historically has a value
granularity of 1 hour, or may be entirely disabled via system configuration
(`NtfsDisableLastAccessUpdate`). Furthermore, certain FILETIME values possess **overloaded
semantics**; a value of `0` typically means the time is unset, while `{0xffffffff, 0xffffffff}`
might be used to indicate a value should be preserved or carry a special meaning in specific
protocols like Kerberos.

### POSIX `time_t` (Unix Timestamp)

Natively used across Unix-like systems (Linux, macOS), a standard **POSIX timestamp tracks time as
an integer representing the number of seconds elapsed since the Unix Epoch (January 1, 1970 UTC)**.

**Forensic Caveat:** Historically bounded as a 32-bit integer, standard POSIX time suffers from
a much lower storage granularity (1 second) compared to Windows. This low granularity can mask the
true sequence of events, forcing forensic tools to smash separate, sub-second actions into a single
timeline entry. Modern variants alter this format by extending it to 64 bits to avoid the "Year
2038" overflow, and related file systems (like APFS) scale the precision up to 1-nanosecond
intervals.

### Comparison

The table below details how these formats stack up against other common structures:

| Timestamp Format | Epoch (Reference Point) | Storage Granularity | Key Forensic Trap |
| --- | --- | --- | --- |
| **FILETIME** | Jan 1, 1601 UTC | 100 nanoseconds | Overloaded values (e.g., 0 or 0xFFFFFFFF) change meaning. |
| **POSIX `time_t`** | Jan 1, 1970 UTC | 1 second (Standard) | 32-bit versions will overflow in the Year 2038. |
| **APFS** | Jan 1, 1970 UTC | 1 nanosecond | High granularity can mask low value-resolution data. |
| **FAT Time** | Jan 1, 1980 (Local) | 2 seconds (10ms for timestamp) | Stored in local time; access dates only have a 1-day granularity. |

## The Normalization Trap: Information Underflow and Overflow

To build "super timelines," forensic data processing tools typically normalize all incoming
timestamps into a unified standard, such as microseconds since the Unix epoch. While normalization
is essential for comparing disparate logs, it introduces analytic risks, such as:

* Up-Sampling (Artificially High Granularity)
* Down-Sampling (Loss of Granularity)

> Note that this is not intended as a comprehensive list of risks.

### Up-Sampling (Artificially High Granularity)

When a tool forces a low-granularity timestamp (like a 1-day FAT file access date) into a
microsecond timeline, it must infer a time, often padding it out to midnight (`00:00:00.000000`). If
an analyst searches a timeline for an event that happened at 14:30, a naive query will completely
miss this FAT record, creating an **information underflow** condition where the analyst assumes no
activity took place.

### Down-Sampling (Loss of Granularity)

Conversely, reducing a high-granularity 100-nanosecond Windows FILETIME down to a 1-second format
forces distinct sub-second events to merge. This can make three separate file alterations look like
a single grouped action, causing the analyst to misinterpret causality or the absolute order of
execution.

## Conclusion

Timestamps are not self-explanatory facts; they are artifacts of specific system designs. Modern
frameworks (like Plaso) are moving toward **dynamic time representation** via specialized libraries
like `dfDateTime` to preserve original granularity and semantic constraints during processing. For
the human analyst, maintaining a deep skepticism of normalized timelines and verifying the native
format's value granularity remains the ultimate safeguard against a flawed investigation.

## External Links

* [dfDateTime: Date and time values](https://dfdatetime.readthedocs.io/en/latest/sources/Date-and-time-values.html)
* [Pearls and pitfalls of timeline analysis](https://osdfir.blogspot.com/2021/10/pearls-and-pitfalls-of-timeline-analysis.html),
  by Joachim Metz October 20, 2021
