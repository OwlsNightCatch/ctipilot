---
schema: 1
kind: threat
horizon: operational
title: "JADEPUFFER returns with ENCFORGE — a Go ransomware built to destroy AI/ML model artifacts, not just extort data"
headline: "JADEPUFFER re-hits the same Langflow instance with ENCFORGE, purpose-built to encrypt trained models and their training data"
summary: >
  Sysdig reports (2026-07-20) that the JADEPUFFER operator returned to the same internet-exposed Langflow
  instance and staged ENCFORGE, a compiled, UPX-packed Go ransomware purpose-built for AI/ML
  infrastructure — encrypting roughly 180 file types across model checkpoints, weights, quantized models,
  vector indices and training datasets. The extortion contact matches the July run, confirming the same
  operator; the operational point for defenders is that encrypted model checkpoints and co-located
  training data cannot be restored from a vendor patch or a decryptor.
discovered_at: "2026-07-21T04:40:00Z"
event_date: "2026-07-20"
run_id: 2026-07-21T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, ai-abuse, cloud]
regions: [global]
sectors: [public-sector, education, finance]
entities: [actor:jadepuffer]
techniques: [T1190, T1611, T1486]
affected_products: ["Langflow"]
cves: []
sources:
  - url: "https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models"
    publisher: "Sysdig Threat Research Team"
    date: "2026-07-20"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/jadepuffer-ai-model-ransomware/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In a new development, the operator behind JADEPUFFER has doubled down on that bet, using ransomware to destroy the one thing an organization can't simply restore: a trained AI model."
    publisher: "Sysdig Threat Research Team"
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-07-04/jadepuffer-agentic-llm-ransomware-langflow-rce
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "For any Langflow or self-hosted AI-pipeline estate, confirm model checkpoints and training datasets are backed up to storage isolated from the compute host — ENCFORGE encrypts ~180 ML-artifact file types and any training data sitting on the same host, so a co-located backup is inside the blast radius and recovery would otherwise mean re-training from scratch."
migrated_from: null
---

**UPDATE (originally covered 2026-07-04):** The JADEPUFFER operator — the agentic-LLM extortion actor Sysdig first documented exploiting Langflow's missing-authentication code-execution flaw (CVE-2025-3248) — returned to the same Langflow instance with a materially upgraded payload. Where the original intrusion improvised Python and MySQL `AES_ENCRYPT()` to extort a downstream database, the new run deploys ENCFORGE (written to disk as `lockd`), a compiled, UPX-packed Go ransomware purpose-built for the machine-learning stack ([Sysdig, 2026-07-20](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models)). Sysdig ties it to the same actor — the extortion contact embedded in ENCFORGE matches the one disclosed in the prior report — assessing "the same operator with a materially upgraded toolkit." Infosecurity Magazine corroborates the campaign ([Infosecurity Magazine, 2026-07-20](https://www.infosecurity-magazine.com/news/jadepuffer-ai-model-ransomware/)).

ENCFORGE targets roughly 180 file extensions spanning the modern ML pipeline — PyTorch/TensorFlow checkpoints, HuggingFace SafeTensors weights, llama.cpp GGUF quantized models, FAISS vector indices, Apache Parquet/TFRecord training datasets, NumPy arrays and LoRA adapters — encrypting with AES-256-CTR under RSA-2048. Sysdig frames the significance bluntly: the operator is "using ransomware to destroy the one thing an organization can't simply restore: a trained AI model," because rebuilding a production fine-tuned model means re-running weeks-to-months of training, and if the training data sits on the same compromised host it is encrypted too. **Defender takeaway:** conventional ransomware playbooks assume restore-from-backup; for AI infrastructure that assumption fails when model artifacts and their training data are co-located on the encrypted host. Treat self-hosted AI-pipeline tooling (Langflow and peers) as ransomware-reachable internet-facing software, and keep model-checkpoint and training-data backups off the compute host. **Triage:** benign ML training jobs write these same artifact types continuously — the discriminator is a single non-training process walking and rewriting model/checkpoint/dataset directories across the tree in bulk, especially one spawned from an unexpected parent on an internet-exposed AI-pipeline host rather than the training scheduler.
