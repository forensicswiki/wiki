---
tags:
  - Knowledge Base
  - Open Source Software
  - Quality Assurance
  - Tools
---
Systematic Objective-based Listing of Various Established (Digital) Investigation Techniques (or
SOLVE-IT) is a knowledge base for and by the digital forensic community, supported by
[DFRWS.org](digital_forensic_research_workshop.md), that describes and indexes techniques available
to digital forensic analysts during an examination.

Uniquely, it also describes potential weakness at each stage of a digital forensic investigation,
including in digital forensic tools. It also provides Python tooling to compile the contents of the
knowledge base into different formats, making it useful for a number of different applications.

## Data model

The high-level concepts are:

* Objectives: based on ATT&amp;CK tactics, objectives are "the goal that one might wish to achieve
  in a digital forensic investigation", e.g. acquire data, or extract information from a file
  system.
* Techniques: "how one might achieve an objective in digital forensics by performing an action",
  e.g. for the objective of 'acquire data', the technique 'create disk image' could be used.
* Weaknesses: these represent potential problems resulting from using a technique. They are
  classified according to the error categories in ASTM E3016-18, the Standard Guide for Establishing
  Confidence in Digital and Multimedia Evidence Forensic Results by Error Mitigation Analysis.
* Mitigations: something that can be done to attempt to prevent a weakness from occurring, or to
  attempt to minimise its impact.

## TRWM

TRWM in the context of SOLVE-IT is short for Technique, Results, Weaknesses, and Mitigations.

It represents the 4 sequential steps used to document and analyze a digital forensic method in the
SOLVE-IT knowledge base:

* Technique. Defines what the forensic method is and how it works.
* Results. Lists the concrete outputs or findings the technique produces.
* Weaknesses. Identifies the errors, failures, or limitations that could affect those results.
* Mitigations. Specifies the safeguards or verification steps that reduce the risk of each weakness.

When extended to TRWM-AR, the AR stands for ASTM-guided failure effects and Root cause enumeration,
which breaks the Weaknesses step into two sub-steps.

### Example

```text
1. TECHNIQUE (T)
First, define the discrete, tool-agnostic forensic action being performed.
* Technique Name: File Carving from Unallocated Space
* Description: Scanning raw storage media or unallocated disk clusters for known file headers and
  footers (magic bytes) to reconstruct files without relying on file system metadata.

2. RESULTS (R)
Next, list every concrete output (Digital Forensic Technique Result) that the technique produces.
* Result 1 (DFTR-1): A set of reconstructed files extracted from raw disk space.
* Result 2 (DFTR-2): An absence of carved files for a specific file type (a negative result).

3. WEAKNESSES VIA ASTM-GUIDED FAILURE EFFECTS & ROOT CAUSES (W-AR)
Instead of guessing weaknesses at random, TRWM-AR splits this stage into two steps for each Result,
using ASTM E3016-18 error prompts (such as incompleteness, inaccuracy, or false positives) to guide
the analysis.

Analyzing Result 1: Reconstructed Files Extracted
* Step A – ASTM Failure Effect (What goes wrong):
  * Effect 1.1 (Inaccuracy / Corruption): A carved file is partially corrupted or contains mixed
    data from unrelated files.
  * Effect 1.2 (False Positive): A non-file data block is falsely identified and extracted as a
    valid file.
* Step R – Root Cause Enumeration (Why it happens):
  * Cause for Effect 1.1: File fragmentation on the storage medium causes the carver to read
    contiguous clusters that actually belong to a different file.
  * Cause for Effect 1.2: Random binary data within compressed or encrypted blocks happens to match
    a short file header signature by coincidence.

Analyzing Result 2: Absence of Carved Files
* Step A – ASTM Failure Effect (What goes wrong):
  * Effect 2.1 (Incompleteness / False Negative): Relevant deleted files present on the disk are
    missed and not extracted.
* Step R – Root Cause Enumeration (Why it happens):
  * Cause for Effect 2.1a: The carving tool lacks the specific header/footer signature definition
    for a proprietary or newer file format.
  * Cause for Effect 2.1b: The target file is encrypted or compressed at the file level, obscuring
    its internal magic bytes.

4. MITIGATIONS (M)
Finally, map each specific Weakness (the paired Failure Effect + Root Cause) to concrete safeguards
or complementary techniques.

* Weakness: Effect 1.1 + Fragmentation
  Mitigation: Manual Hex & Structural Inspection
  How It Reduces Risk: Inspecting cluster boundaries and file structure verifies whether data
  blocks genuinely belong together.

* Weakness: Effect 1.2 + Signature Collision
  Mitigation: File Format Validation / Parsing
  How It Reduces Risk: Running strict format parsers confirms whether the extracted file has valid
  internal syntax beyond the header.

* Weakness: Effect 2.1a + Missing Signature
  Mitigation: Custom Signature Configuration
  How It Reduces Risk: Reviewing and adding custom header/footer definitions ensures the carver
  searches for all case-relevant formats.

* Weakness: Effect 2.1b + File Encryption
  Mitigation: Entropy Analysis
  How It Reduces Risk: Scanning unallocated space for high-entropy regions flags potential
  encrypted blobs that standard carving missed.
```

## Use

The many potential applications of SOLVE-IT include:

* strengthen tool testing by scoping error-focused data sets for a technique
* reinforce techniques by cataloguing available mitigations for weaknesses
* bolster quality assurance by identifying potential weaknesses in a specific processes
* structure consideration of potential uses of AI in digital forensics
* augment automation by highlighting relevant CASE ontology classes
* prioritize innovation by identifying academic research opportunities
* standardizing language and terminology in teaching using the indexed techniques
* conducting capability assessments of labs or individuals against the techniques

One of the most interesting and immediate applications of SOLVE-IT is to avoid missed or
unmitigated errors in digital forensic processes. This can be undertaken to review either standard
processes, tool workflows, or even individual investigations.

## External Links

* [SOLVE-IT GitHub repositories](https://github.com/SOLVE-IT-DF?tab=repositories)
* [SOLVE-IT: A proposed digital forensic knowledge base inspired by MITRE ATT&amp;CK](https://dfrws.org/presentation/solve-it-a-proposed-digital-forensic-knowledge-base-inspired-by-mitre-attck/)
  from the Proceedings of the [DFRWS EU 2025 Conference](digital_forensic_research_workshop.md)
* ASTM E3016-18: Standard Guide for Establishing Confidence in Digital and Multimedia Evidence
  Forensic Results by Error Mitigation Analysis
  [based on SWGDE document](https://drive.google.com/file/d/1jBAjohuntNCLUzgV_x7aINf_JycfVddu/view)
* [Adding genAI-assisted techniques to SOLVE-IT](https://www.solveit-df.org/2026/10/01/adding-genai-assisted-techniques-to-solve-it.html),
  by Chris Hargreaves, Eoghan Casey, October 1, 2026
