---
schema: 1
kind: research
horizon: operational
title: Cisco Talos maps the DICOM-format attack surface against Orthanc PACS — network-ingested medical images as a heap out-of-bounds-write primitive
headline: Cisco Talos maps the DICOM-format attack surface against Orthanc PACS — network-ingested medical images as a heap out-of-bounds-write primitive
summary: "Cisco Talos published a technical study of the DICOM image-format attack surface against Orthanc, the open-source PACS server widely deployed in CH/EU hospital radiology — auto-ingestion of network-received DICOM files turns a malformed study into a heap out-of-bounds write primitive (Cisco Talos, 2026-05-28). No CVE/PoC in the public post; relevant to hospital-segmentation and modality-allowlisting posture."
discovered_at: "2026-05-31T05:00:03Z"
event_date: 2026-05-28
run_id: 2026-05-31-d742bed9
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - ot-ics
regions:
  - global
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/"
    publisher: Cisco Talos
    role: primary
closed_sources: []
evidence:
  - quote: "Hospitals rely on DICOM-based PACS systems, and those systems often automatically ingest files received over the network. That means malformed data could directly trigger vulnerable decoders — the holy grail of attack surfaces for those studying robustness"
    publisher: Cisco Talos
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-31.md
---

Cisco Talos published a technical study on 2026-05-28 examining how the DICOM medical-imaging file format yields heap out-of-bounds-write conditions across three parsers — the Python `pydicom` library, GDCM (Grassroots DICOM), and the parser inside Orthanc, the open-source PACS (Picture Archiving and Communication System) server widely deployed in hospital radiology ([Cisco Talos, 2026-05-28](https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/)). Talos frames the upload/ingestion pathway as the highest-concern surface: hospital PACS routinely auto-ingest DICOM studies received over the network from imaging modalities (CT, MRI, X-ray) via DICOM C-STORE, so a malformed study from any connected modality or compromised upstream institution can directly reach the vulnerable decoder without user action. The write primitive arises from the format's variable-length Value Representation (VR) tag structure combined with lax bounds-checking in heap allocation. The public blog post discloses no CVE identifiers and no exploit code — the underlying technique class is `T1190` (exploit public-facing application) where a PACS endpoint is network-reachable, or delivery via a malicious study over DICOM networking. `[SINGLE-SOURCE]` (Cisco Talos primary research).

**Why it matters to us:** Swiss cantonal and university hospitals and EU healthcare providers — NIS2 critical entities — universally run PACS/DICOM infrastructure, and Orthanc is common in academic medical centres. The attack surface is structural to how PACS operate (mandatory DICOM connectivity to vendor equipment), so it cannot be closed by patching a single product alone. Defender posture from the research: review network segmentation between PACS servers and clinical workstations; restrict DICOM C-STORE acceptance to known modality Application Entity (AE) titles via the PACS ACL; confirm Orthanc instances run a supported version; treat studies arriving from referring institutions as untrusted input.
