---
tags:
  - Network Forensics
---
Network forensics is the process of identifying, capturing, and preserving volatile data
transmitted across a network to reconstruct events, establish timelines, and uncover actionable
digital evidence.

The scope of network forensics encompasses the monitoring, interception, and analysis of network
traffic across internal and external boundaries to identify security anomalies, trace policy
violations, and reconstruct information security incidents. This operational domain extends from
localized local area network (LAN) activity and wide area network (WAN) perimeters to virtualized
cloud environments and software-defined networks. Rather than focusing on static storage media,
investigators target data in motion using two primary methodologies:

* Deep-Analysis Systems: Utilize Full Packet Capture (FPC) and Deep Packet Inspection (DPI) to
  record every byte passing through a network monitoring point (via TAPs or SPAN ports), allowing
  investigators to reconstruct entire transmissions down to the application layer.
* Flow-Based Systems: Aggregate traffic into compact, structured metadata records based on a unique
  "5-tuple" identity (Source/Destination IP, Source/Destination Port, and Protocol) to provide
  long-term behavioral visibility without inspecting payload contents.

By combining these packet-level and flow-level capture capabilities with the evaluation of network
device logs (such as firewall and IDS records), advanced hybrid systems establish an authenticated,
end-to-end timeline of how an attacker accessed, navigated, and exfiltrated data from an enterprise
ecosystem.

## Categories of Analysis

The analysis of captured network data is commonly broken down into the following categories:

* **Session reconstruction** - Rebuilding complete user sessions by
  recovering application-layer content (files, email, web pages) from
  captured packets; see also [Session reconstruction](session_reconstruction.md).
* **Flow-based analysis** - Examining compact 5-tuple records (volume,
  duration, timing) to find unusual peers, tunneling, exfiltration, and
  beaconing patterns; see also [Flow-based analysis](flow_based_analysis.md).
* **Intrusion and anomaly detection** - Matching traffic against
  signature rules or behavioral baselines to identify attacks and
  malware; see also [Intrusion detection](intrusion_detection.md).
* **Data leakage analysis** - Combining flow volumes with inspection of
  unencrypted payloads and DNS queries to identify sensitive data
  leaving the network.
* **DNS analysis** - Inspecting queries and responses for tunneling,
  domain generation algorithms, and indicators of compromise.
* **Wireless and Radio Frequency (RF) analysis** - Analysis of 802.11 and other
  radio-based traffic; see also [Wireless forensics](wireless_forensics.md).
* **TLS/SSL analysis** - Examining handshake and certificate metadata,
  or the payload when keys are available; see also
  [SSL forensics](ssl_forensics.md).
* **Geolocation and path analysis** - Using TTL values, traceroutes,
  and address data to map routes; see also
  [IP geolocation](ip_geolocation.md).
* **Timeline correlation** - Aligning network events with host and log
  evidence to build an end-to-end incident timeline; see also
  [Timeline analysis](timeline_analysis.md) and
  [Logfile analysis](logfile_analysis.md).

## See also

* [Flow-based analysis](flow_based_analysis.md)
* [Intrusion detection](intrusion_detection.md)
* [IP geolocation](ip_geolocation.md)
* [Logfile Analysis](logfile_analysis.md#tools)
* [Session reconstruction](session_reconstruction.md)
* [SSL forensics](ssl_forensics.md)
* [Tools: Network Forensics](tools_network_forensics.md)
* [Wireless forensics](wireless_forensics.md)

## External Links

* [http2 explained](https://daniel.haxx.se/http2/), by Daniel Stenberg,
  February 18, 2015
