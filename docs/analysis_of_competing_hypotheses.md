---
tags:
  - Concept
---
In digital forensics and incident response (DFIR), investigators frequently face massive datasets
filled with ambiguous or incomplete artifacts. A natural human pitfall during these investigations
is **confirmation bias**, latching onto an initial hunch, such as *"the employee intentionally
stole the data"*, and selectively hunting for logs that confirm that narrative while explaining
away anomalies.

To counter this, forensic practitioners and threat intelligence analysts have increasingly adopted
**Analysis of Competing Hypotheses (ACH)**. Originally developed in the 1970s by CIA veteran
Richards J. Heuer Jr. and formalized in his seminal book *Psychology of Intelligence Analysis*
(1999), ACH shifts the investigative mindset from *proving* a favored theory to systematically
*disproving* alternatives.

### How ACH Works in a Forensic Investigation

Instead of evaluating artifacts one by one against a single narrative, ACH forces the examiner to
build an **evidence-consistency matrix** that tests every piece of digital evidence against all
plausible scenarios simultaneously.

Heuer's methodology typically follows an eight-step workflow adapted to digital evidence:

1. **Brainstorm All Hypotheses:** List every mutually exclusive explanation for the incident, e.g.
   *H1: Insider threat*, *H2: External malware/RAT*, *H3: Automated IT backup script*, *H4: System
   clock/artifact corruption*.
2. **List Evidence and Assumptions:** Catalog all acquired digital artifacts, Windows Registry keys,
   Prefetch files, firewall logs, memory dumps, alongside their reliability and credibility scores.
3. **Build the Matrix:** Place hypotheses across the top row and digital artifacts down the left
   column. Evaluate each artifact against each hypothesis as **Consistent (C)**,
   **Inconsistent (I)**, or **Not Applicable (N/A)**.
4. **Assess Diagnosticity:** Identify which artifacts actually differentiate between hypotheses. If
   a timestamp is consistent with *every* hypothesis, it has zero diagnostic value and should be set
   aside so it does not create false confidence.
5. **Refine the Matrix:** Identify missing evidence gaps and perform targeted forensic collection
   to fill them.
6. **Attempt to Disprove Hypotheses:** Tally the **inconsistencies** rather than the consistencies.
   The winning hypothesis is not the one with the most supporting artifacts, but the one with the
   *fewest contradictions*.
7. **Analyze Sensitivity:** Ask how the conclusion would change if one or two critical artifacts
   turned out to be spoofed, corrupted, or misinterpreted.
8. **Report All Outcomes:** Document the relative likelihood of *all* tested hypotheses, not just
   the top choice, creating a transparent audit trail for legal review.

### Example: Applying an ACH Matrix to Suspicious File Access

Consider a scenario where proprietary source code appears on an external USB drive:

| Digital Artifact / Evidence | H1: Manual Insider Theft | H2: Malware / RAT Exfiltration | H3: Automated Backup Script | Diagnostic Value |
| --- | --- | --- | --- | --- |
| **E1:** USB device connected (`USBSTOR` registry) | C | C | C | **Low** (Consistent with all) |
| **E2:** Files copied to USB drive | C | C | C | **Low** (Consistent with all) |
| **E3:** Windows Shellbags show folder traversal | **C** | **I** | **I** | **High** (Suggests GUI interaction) |
| **E4:** Outbound C2 beacon 2 mins prior | **I** | **C** | **I** | **High** (Contradicts normal user/IT) |
| **E5:** Process launched by `SYSTEM` account | **I** | **C** | **C** | **Medium** (Rules out standard user GUI) |

By focusing on the **inconsistencies (I)**, the investigator quickly spots contradictions, such
as standard GUI interaction (**E3**) clashes with a `SYSTEM`-level process (**E5**) and active
command-and-control traffic (**E4**), pointing toward either sophisticated malware simulating user
artifacts or a compromised administrative script rather than simple manual theft.

### Relevant Research and Empirical Findings

The application of ACH in forensics, cyber threat intelligence, and legal settings is backed by a
growing body of academic and industry research, along with important caveats regarding its
limitations:

* **Cyber Threat Intelligence &amp; Incident Attribution:** Industry frameworks, such as those
  analyzed by "How to Structure Analysis of Competing Hypotheses", demonstrate how ACH structures
  incident triage (such as evaluating threat actor attribution during the WannaCry outbreak) while
  noting that standard threat-sharing formats like STIX 2.1 historically lacked native objects to
  represent competing hypotheses simultaneously.
* **Criminal &amp; Cold Case Forensics:** Recent forensic science research published in "Applying
  the analysis of competing hypotheses framework to criminal investigations", illustrates how ACH
  prevents premature fixation on single pieces of evidence in complex investigations, successfully
  disentangling competing explanations (accidental contamination vs. intentional foul play) by
  scoring consistency across entire evidence sets.
* **Mitigating Adversarial Allegiance &amp; Cognitive Bias:** While ACH is widely championed for
  reducing cognitive bias, empirical testing urges caution against treating it as a silver bullet. A
  2019 study on intelligence analysts by "The analysis of competing hypotheses in intelligence
  analysis" found that analysts often struggle to follow ACH's strict evidence-integration rules
  without proper training. Similarly, a 2026 study in "The analysis of competing hypotheses and
  expert witness testimony", examining mock forensic expert witnesses found that ACH alone did not
  completely eliminate "adversarial allegiance" (bias toward the retaining legal party).

### Why It Matters for Modern DFIR

Despite its learning curve, ACH remains one of the most effective argumentation methods for
**disciplining forensic judgment**. Even when sparse or ambiguous data prevents a definitive single
answer, an ACH matrix provides an auditable, peer-reviewable record showing judges, opposing
counsel, and incident commanders that alternative explanations were rigorously tested rather than
ignored.

## External Links

* [How to Structure Analysis of Competing Hypotheses (ACH)](https://blog.eclecticiq.com/how-to-structure-analysis-of-competing-hypotheses-ach),
  by Caitlin Huey, October 29, 2018
* [Applying the analysis of competing hypotheses framework to criminal investigations and cold cases](https://www.sciencedirect.com/science/article/pii/S1355030625000929),
  by David A. Keatley, September 2025
* [The "analysis of competing hypotheses" in intelligence analysis](https://psycnet.apa.org/record/2019-30607-001),
  by M. K. Dhami, I. K. Belton, and D. R. Mandel, 2019
* [The analysis of competing hypotheses and expert witness testimony](https://doi.org/10.1371/journal.pone.0346891),
  by Jana Otzipka and Renate Volbert, April 20, 2026
