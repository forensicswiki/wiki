---
tags:
  - Concept
  - Legal
---
In the field of digital forensics, a critical distinction exists between an investigative
**finding** and **legal evidence**. While a forensic analyst may uncover technical artifacts that
perfectly reconstruct an information security incident, those findings do not automatically qualify
as evidence in a court of law. For data to cross the threshold into legally admissible evidence, it
must possess specific structural and procedural traits.

### The Core Traits of Digital Evidence

To withstand legal scrutiny, digital artifacts must exhibit five foundational characteristics:

* **Admissibility:** The data must comply with established legal statutes and rules of evidence. It
  must be collected legally, often requiring specific authorization like a search warrant or clear
  terms of service agreements.
* **Authenticity:** Investigators must prove that the data is genuine and tied directly to the
  incident. This is typically achieved through cryptographic hashing (e.g., SHA-256), which creates a
  unique digital fingerprint of the data at the moment of capture.
* **Integrity:** The evidence must remain unaltered from its original state. Maintaining an
  unbroken **chain of custody**, a meticulously detailed log tracking who handled, stored, or
  analyzed the media, is mandatory to prove no tampering occurred.
* **Reliability:** The tools, methodologies, and forensic processes used to extract and analyze the
  data must be scientifically validated, repeatable, and widely accepted by the technical community.
* **Completeness:** The evidence cannot be presented in a vacuum or cherry-picked. Investigators
  must provide a comprehensive view, including any exculpatory evidence that might favor the defense
  or offer alternative explanations.

### Why a "Finding" Is Not Always Evidence

A forensic **finding** is an empirical observation. It is a line in a firewall log, a Windows
Registry key modification, an unallocated file fragment, or a timeline correlation discovered
during an investigation. **It is a technical fact, but it is not inherently a legal proof.**

The transition from a finding to legal evidence fails if any of the core traits are violated:

1. **Procedural Flaws:** If an investigator discovers a definitive "smoking gun" file on a
   corporate laptop but accessed that laptop without proper authorization or authorization protocols,
   the finding may be suppressed in court.
2. **Chain of Custody Breaks:** If a hard drive snapshot is left unattended on an unencrypted
   network share, its integrity is compromised. Even if the data inside is completely accurate, it
   ceases to be legally sound evidence because the opportunity for tampering was introduced.
3. **The Problem of Attribution:** Finding a malicious command inside a user's profile is a clear
   technical finding. However, without corroborating network flow records or physical access logs to
   prove *who* was sitting at the keyboard, that finding may fail the trait of authenticity required
   to prove culpability.

Ultimately, digital forensics is as much a legal discipline as it is a technical one. Analysts do
not just solve technical riddles; they build [legally resilient narratives](rethoric_of_proof.md).
Understanding that findings are merely raw material, and that strict adherence to evidentiary traits
is what transforms them into legal evidence, is what separates an intrusion assessment from a
rigorous forensic investigation.

## External Links

* [How two new rules for self-authentication will save you time and money](https://judicature.duke.edu/wp-content/uploads/sites/3/2021/05/Haried_Winter2016.pdf),
  by John M. Haried, March 2021
