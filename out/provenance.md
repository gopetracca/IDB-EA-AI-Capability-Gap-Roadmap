# Provenance — where the capability map comes from

**Inter-American Development Bank** · generated 2026-09-05 · register `facts/sources.json`, access date 3 September 2026

> **The rule (ADR-0010):** provenance is graded by whether a reviewer can open it, not by prestige. **A grade-D source cannot support a claim in anything that leaves the Bank**, whatever its quality.

| Grade | Meaning | Sources |
|---|---|:-:|
| **A** | openly available, dated, versioned, standards body or public authority | 10 |
| **B** | openly available and dated, but vendor-published or non-normative | 11 |
| **C** | available but undated / superseded / flagged historical / paywalled | 12 |
| **D** | non-public, or not a publication at all - unusable as evidence externally | 7 |

| | |
|---|---|
| Sources in the register | 40 |
| Capability–source citations | 143 |
| Citations resolving to a registered source | 143 |
| Citations pinned to a locus (clause, section, control) | 15 |

A citation without a locus says *this source informed the capability*; it does not say where. Under ADR-0010 a capability whose loci are never pinned is reclassified as **synthesized** — assembled by us — rather than left claiming a source it cannot point into.

---

## Capabilities resting partly on a grade-D source

These 14 capabilities cite at least one source a reviewer outside the Bank cannot open. Each still has other sources; the grade-D citation must be replaced or the claim restated as ours before anything containing it circulates externally.

| ID | Capability | Grade-D citation | Register entry | What would close it |
|---|---|---|---|---|
| `1.2` | AI Portfolio & Investment Management | Gartner (analyst, non-public) | Gartner `S34` | Licensed material |
| `1.5` | AI Ecosystem & Alliance Management | Institutional practice | IDB institutional practice `S36` | Legitimate as an origin, but 'institutional practice' names nothing a reviewer can open |
| `2.4` | Business Process & Service Redesign | Consultancy transformation patterns (non-public) | Consultancy transformation patterns `S35` | REMOVE or replace |
| `2.6` | AI Innovation & Incubation | Institutional practice | IDB institutional practice `S36` | Legitimate as an origin, but 'institutional practice' names nothing a reviewer can open |
| `3.1` | Data Governance & Stewardship for AI | EDM Council DCAM/ADAC | EDM Council ADAC `S26` | REMOVE |
| `3.2` | Data Sourcing, Licensing & Provenance | EDM Council DCAM/ADAC | EDM Council ADAC `S26` | REMOVE |
| `3.3` | Data Quality & Preparation for AI | EDM Council DCAM/ADAC | EDM Council ADAC `S26` | REMOVE |
| `3.4` | Metadata, Lineage & Cataloging for AI | EDM Council DCAM/ADAC | EDM Council ADAC `S26` | REMOVE |
| `6.5` | AI Cost Management | Gartner (analyst, non-public) | Gartner `S34` | Licensed material |
| `7.5` | Privacy & Data Protection for AI | Institutional data protection framework | IDB data protection framework `S37` | Data Governance to confirm the instrument name, version and the specific provision relied on. |
| `7.6` | Legal, Regulatory & Contractual Compliance for AI | Institutional legal framework | IDB legal framework `S38` | Legal to confirm which instrument is relied on |
| `7.8` | AI Assurance & Evidence Management | Institutional internal audit standards | IDB internal audit standards `S39` | Internal Audit to confirm which standards are relied on and whether the IIA Global Internal Audit Standards (2024) are adopted directly. |
| `8.5` | AI Change Management & Workforce Transition | Consultancy transformation patterns (non-public) | Consultancy transformation patterns `S35` | REMOVE or replace |
| `8.6` | AI Community & Reuse Culture | Institutional practice | IDB institutional practice `S36` | Legitimate as an origin, but 'institutional practice' names nothing a reviewer can open |

---

## The register

| ID | Grade | Source | Publisher | Edition · date | Status | Cited by |
|---|:-:|---|---|---|---|:-:|
| `S01` | **C** | [ISO/IEC 42001](https://www.iso.org/standard/42001) | ISO / IEC (JTC 1/SC 42) | First edition · 2023-12 | Current | 14 |
| `S02` | **C** | [ISO/IEC 5338](https://www.iso.org/standard/81118.html) | ISO / IEC (JTC 1/SC 42) | First edition · 2023-12 | Current | 9 |
| `S03` | **C** | [ISO/IEC 38507](https://www.iso.org/standard/56641.html) | ISO / IEC (JTC 1/SC 40) | First edition · 2022-04 | Current | 3 |
| `S04` | **C** | [ISO/IEC 23894](https://www.iso.org/standard/77304.html) | ISO / IEC (JTC 1/SC 42) | First edition · 2023-02 | Current | 2 |
| `S05` | **C** | [ISO/IEC 42005](https://www.iso.org/standard/42005) | ISO / IEC (JTC 1/SC 42) | First edition · 2025-05 | Current | 2 |
| `S06` | **C** | [ISO/IEC 27001](https://www.iso.org/standard/27001) | ISO / IEC (JTC 1/SC 27) | Third edition + Amd 1:2024 · 2022-10 / 2024 | Current | 2 |
| `S07` | **C** | [ISO/IEC 27701](https://www.iso.org/standard/27701) | ISO / IEC (JTC 1/SC 27) | Second edition · 2025-10 | Restructured — old loci invalid | 1 |
| `S08` | **A** | [NIST AI RMF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) | NIST, U.S. Department of Commerce | NIST AI 100-1, Version 1.0 · 2023-01-26 | Current | 8 |
| `S09` | **A** | [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | NIST, U.S. Department of Commerce | NIST AI 600-1 · 2024-07-26 | Current | 4 |
| `S10` | **A** | [OECD AI Principles](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) | OECD | Adopted 2019; amended 2023-11 and 2024-05 · 2024-05-03 | Current | 3 |
| `S11` | **A** | [GAO AI Accountability Framework](https://www.gao.gov/assets/gao-21-519sp.pdf) | U.S. Government Accountability Office | GAO-21-519SP · 2021-06-30 | Current | 5 |
| `S12` | **C** | [AWS CAF-AI](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html) | Amazon Web Services | Whitepaper · 2024-02-13 | Flagged historical by AWS | 11 |
| `S13` | **B** | [Microsoft CAF for AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/) | Microsoft | Living document — no version number · Accessed 3 September 2026 | Current | 5 |
| `S14` | **C** | [Google AI Adoption Framework](https://services.google.com/fh/files/misc/ai_adoption_framework_whitepaper.pdf) | Google Cloud | Undated whitepaper · UNDATED | Undated, pre-GenAI | 4 |
| `S15` | **B** | [IBM GenAI Capability Model](https://www.ibm.com/architectures/patterns/genai-capability-model) | IBM (Think — Architecture patterns) | Living page · Last updated 2025-04-30 | Current | 11 |
| `S16` | **B** | [NVIDIA Enterprise AI Factory](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/) | NVIDIA Corporation | White paper · Last updated 2026-05-27 | Current | 4 |
| `S17` | **B** | [SAP AI-native North Star](https://architecture.learning.sap.com/docs/ai-native-north-star-architecture) | SAP (SAP Architecture Center) | Living document · Last updated 2026-05-13 | Current | 4 |
| `S18` | **C** | [Salesforce ADLC](https://architect.salesforce.com/docs/architect/fundamentals/guide/agent-development-lifecycle.html) | Salesforce (Salesforce Architects) | Living document — undated · UNDATED, accessed 3 September 2026 | Undated | 1 |
| `S19` | **B** | [WEF AI-First Operating System](https://www.weforum.org/publications/the-ai-first-operating-system-a-blueprint-for-operating-and-business-model-innovation/) | World Economic Forum, in collaboration with Kearney | Report · 2026-06 | Current | 7 |
| `S20` | **B** | [TOGAF Standard](https://pubs.opengroup.org/togaf-standard/) | The Open Group | 10th Edition · 2022-04-25 | Current | 2 |
| `S21` | **B** | [TOGAF G193 Capability-Based Planning](https://publications.opengroup.org/g193) | The Open Group | Series Guide G193 · Current | Current | 1 |
| `S22` | **B** | [Open Agile Architecture](https://www.opengroup.org/AgileArchitecture) | The Open Group | Version 2.0 · 2026-04 (confirm from cover) | Current | 5 |
| `S23` | **B** | [IT4IT Standard](https://pubs.opengroup.org/it4it/3.0.1/standard/) | The Open Group | Version 3.0.1 · 2024-10 | Current | 3 |
| `S24` | **C** | [ITIL 4](https://www.peoplecert.org/) | PeopleCert International Ltd (acquired AXELOS 2021) | ITIL 4; practice guidance refreshed from 2023 · 2019 onward | Superseded in part | 3 |
| `S25` | **C** | [EDM Council DCAM](https://edmcouncil.org/frameworks/dcam/) | EDM Council | Version 3 · 2025-06-30 | Current but members-only | 0 |
| `S26` | **D** | [EDM Council ADAC](https://edmcouncil.org/forums-workgroups/adac-workgroup/) | EDM Council | NOT A PUBLICATION · n/a | Not a publication | 4 |
| `S27` | **A** | [FinOps Framework](https://www.finops.org/framework/) | FinOps Foundation (a Linux Foundation project) | FinOps Framework 2026 · 2026-03-19 | Current | 2 |
| `S28` | **A** | [IIA Three Lines Model](https://www.theiia.org/globalassets/site/resources/statements-of-position/tlm_assurance_advice_support_effective_gov_en.pdf) | The Institute of Internal Auditors | Statement of Position · 2026-07-08 | Current | 1 |
| `S29` | **B** | [MITRE AI Maturity Model](https://aimaturitymodel.mitre.org/) | The MITRE Corporation | Guide · 2022-11-17 | Ageing | 2 |
| `S30` | **B** | [MIT CISR](https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer) | MIT Sloan Center for Information Systems Research | Research Briefing Vol. XXV No. 8 · 2025-08-21 | Current | 1 |
| `S31` | **A** | [IMDA Model AI Governance Framework](https://aiverifyfoundation.sg/wp-content/uploads/2024/05/Model-AI-Governance-Framework-for-Generative-AI-May-2024-1-1.pdf) | IMDA Singapore and AI Verify Foundation | Final · 2024-05-30 | Current — but our citation was ambiguous | 5 |
| `S31b` | **A** | [IMDA Agentic AI Framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | IMDA Singapore | Version 1.0 · 2026-01-22 | Current | 0 |
| `S32` | **A** | [OWASP GenAI Security Project](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | OWASP Foundation | 2026, Version 1.0 · 2026-08 / launch 2026-09-02 | Current | 2 |
| `S33` | **A** | [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) | Agentic AI Foundation (Linux Foundation); originated at Anthropic | Revision 2026-07-28 · 2026-07-28 | Current | 2 |
| `S34` | **D** | [Gartner](https://www.gartner.com/) | Gartner, Inc. | Subscription research · Various | Non-public | 2 |
| `S35` | **D** | [Consultancy transformation patterns](n/a) | Various consultancies | n/a · n/a | Not a publication | 2 |
| `S36` | **D** | [IDB institutional practice](Internal) | Inter-American Development Bank | n/a · n/a | Needs a named internal document | 3 |
| `S37` | **D** | [IDB data protection framework](Internal) | Inter-American Development Bank | n/a · n/a | Needs pinning | 1 |
| `S38` | **D** | [IDB legal framework](Internal) | Inter-American Development Bank | n/a · n/a | Needs pinning | 1 |
| `S39` | **D** | [IDB internal audit standards](Internal) | Inter-American Development Bank | n/a · n/a | Needs pinning | 1 |

2 sources are in the register but cited by no capability: `S25`, `S31b`.

---

## Sources by capability

A locus in *italics* after a source is the clause, section or control the citation points into. A source with no locus informed the capability without saying where.

| ID | Capability | Sources (grade) *· locus* | Loci pinned |
|---|---|---|:-:|
| `1.1` | AI Vision & Strategy Definition | AWS CAF-AI (C) *· Business perspective*; ISO/IEC 38507 (C); MITRE AI Maturity Model (B) | 1 of 3 |
| `1.2` | AI Portfolio & Investment Management | AWS CAF-AI (C); Gartner (D); TOGAF G193 Capability-Based Planning (B) | 0 of 3 |
| `1.3` | Value Realization & Performance Reporting | WEF AI-First Operating System (B); MIT CISR (B); GAO AI Accountability Framework (A) | 0 of 3 |
| `1.4` | AI Sourcing & Partner Strategy | ISO/IEC 42001 (C) *· A.10 Third-party and customer relationships*; AWS CAF-AI (C) | 1 of 2 |
| `1.5` | AI Ecosystem & Alliance Management | ISO/IEC 42001 (C) *· Clause 4 Context of the organization*; Open Agile Architecture (B); IDB institutional practice (D) | 1 of 3 |
| `2.1` | Use Case Discovery & Intake | AWS CAF-AI (C); Google AI Adoption Framework (C) | 0 of 2 |
| `2.2` | AI Use-Case Feasibility & Qualification | IBM GenAI Capability Model (B); AWS CAF-AI (C) *· Business perspective*; TOGAF Standard (B) | 1 of 3 |
| `2.3` | AI Product Management | WEF AI-First Operating System (B); IT4IT Standard (B); Open Agile Architecture (B) | 0 of 3 |
| `2.4` | Business Process & Service Redesign | WEF AI-First Operating System (B); Consultancy transformation patterns (D); Open Agile Architecture (B) | 0 of 3 |
| `2.5` | Human-AI Interaction & Oversight Design | IMDA Model AI Governance Framework (A); ISO/IEC 42001 (C) | 0 of 2 |
| `2.6` | AI Innovation & Incubation | Google AI Adoption Framework (C); AWS CAF-AI (C); IDB institutional practice (D) | 0 of 3 |
| `3.1` | Data Governance & Stewardship for AI | EDM Council ADAC (D); ISO/IEC 42001 (C) | 0 of 2 |
| `3.2` | Data Sourcing, Licensing & Provenance | NIST AI RMF (A) *· MAP*; EDM Council ADAC (D) | 1 of 2 |
| `3.3` | Data Quality & Preparation for AI | ISO/IEC 5338 (C); EDM Council ADAC (D) | 0 of 2 |
| `3.4` | Metadata, Lineage & Cataloging for AI | EDM Council ADAC (D); ISO/IEC 5338 (C) | 0 of 2 |
| `3.5` | Knowledge Corpus & Content Management | IBM GenAI Capability Model (B) | 0 of 1 |
| `3.6` | Knowledge Access & Retrieval | IBM GenAI Capability Model (B); NIST AI 600-1 (A) | 0 of 2 |
| `3.7` | Derived Representation Management | IBM GenAI Capability Model (B); ISO/IEC 5338 (C) | 0 of 2 |
| `4.1` | AI Architecture Management & Solution Governance | TOGAF Standard (B); SAP AI-native North Star (B); NVIDIA Enterprise AI Factory (B) | 0 of 3 |
| `4.2` | Model Selection, Customization & Tuning | IBM GenAI Capability Model (B); ISO/IEC 5338 (C); NIST AI 600-1 (A) | 0 of 3 |
| `4.3` | Prompt & Context Engineering | IBM GenAI Capability Model (B); NIST AI 600-1 (A); OWASP GenAI Security Project (A) | 0 of 3 |
| `4.4` | Agent & Workflow Orchestration Design | Salesforce ADLC (C); SAP AI-native North Star (B); IBM GenAI Capability Model (B); IMDA Model AI Governance Framework (A) | 0 of 4 |
| `4.5` | Integration & Tool Enablement | IBM GenAI Capability Model (B); MCP specification (A); SAP AI-native North Star (B); IMDA Model AI Governance Framework (A) | 0 of 4 |
| `4.6` | AI Evaluation & Testing | NIST AI 600-1 (A); ISO/IEC 5338 (C) | 0 of 2 |
| `4.7` | AI Release & Change Management | ITIL 4 (C); IT4IT Standard (B); ISO/IEC 5338 (C) | 0 of 3 |
| `5.1` | AI Platform Service Provisioning | AWS CAF-AI (C) *· Platform perspective*; Microsoft CAF for AI (B); NVIDIA Enterprise AI Factory (B) | 1 of 3 |
| `5.2` | Model Access & Traffic Management | IBM GenAI Capability Model (B); Microsoft CAF for AI (B); ISO/IEC 42001 (C) | 0 of 3 |
| `5.3` | AI Environment & Workspace Management | Microsoft CAF for AI (B); ISO/IEC 27001 (C) | 0 of 2 |
| `5.4` | AI Compute & Capacity Management | NVIDIA Enterprise AI Factory (B); Microsoft CAF for AI (B); FinOps Framework (A) | 0 of 3 |
| `5.5` | Tool & Connector Catalog Management | SAP AI-native North Star (B); IMDA Model AI Governance Framework (A); MCP specification (A) | 0 of 3 |
| `5.6` | AI Developer Experience & Reuse Assets | IT4IT Standard (B); Open Agile Architecture (B); AWS CAF-AI (C) | 0 of 3 |
| `6.1` | AI Deployment & Serving Operations | IBM GenAI Capability Model (B); ITIL 4 (C); ISO/IEC 5338 (C) | 0 of 3 |
| `6.2` | AI Monitoring & Observability | IBM GenAI Capability Model (B); NVIDIA Enterprise AI Factory (B); NIST AI RMF (A) *· MEASURE* | 1 of 3 |
| `6.3` | Continuous Evaluation, Drift & Quality Management | NIST AI RMF (A) *· MEASURE*; ISO/IEC 5338 (C) | 1 of 2 |
| `6.4` | AI Incident & Problem Management | ISO/IEC 42001 (C); NIST AI RMF (A) *· MANAGE*; ITIL 4 (C) | 1 of 3 |
| `6.5` | AI Cost Management | FinOps Framework (A); Microsoft CAF for AI (B); Gartner (D) | 0 of 3 |
| `6.6` | AI Asset Retirement & Evidence Preservation | ISO/IEC 5338 (C) *· 6.4.17 Disposal*; ISO/IEC 42001 (C); GAO AI Accountability Framework (A) | 1 of 3 |
| `7.1` | AI Policy, Standards & Management System | ISO/IEC 42001 (C) *· Clauses 4-10 (the management system)*; ISO/IEC 38507 (C); GAO AI Accountability Framework (A) | 1 of 3 |
| `7.2` | Responsible & Trustworthy AI Practice | NIST AI RMF (A) *· GOVERN 1.2*; OECD AI Principles (A); ISO/IEC 42001 (C) | 1 of 3 |
| `7.3` | AI Risk Management | NIST AI RMF (A); ISO/IEC 23894 (C) *· 6.4.2 Risk identification*; ISO/IEC 42005 (C) | 1 of 3 |
| `7.4` | AI Security & Resilience | OWASP GenAI Security Project (A); ISO/IEC 27001 (C); IMDA Model AI Governance Framework (A); NIST AI RMF (A) | 0 of 4 |
| `7.5` | Privacy & Data Protection for AI | ISO/IEC 27701 (C); ISO/IEC 42001 (C); IDB data protection framework (D) | 0 of 3 |
| `7.6` | Legal, Regulatory & Contractual Compliance for AI | ISO/IEC 42001 (C); IDB legal framework (D) | 0 of 2 |
| `7.7` | AI System & Agent Inventory Management | ISO/IEC 42001 (C); GAO AI Accountability Framework (A) | 0 of 2 |
| `7.8` | AI Assurance & Evidence Management | GAO AI Accountability Framework (A); ISO/IEC 42001 (C); IDB internal audit standards (D) | 0 of 3 |
| `7.9` | AI Impact Assessment & Risk Classification | ISO/IEC 42005 (C); ISO/IEC 23894 (C); NIST AI RMF (A) *· MAP*; IIA Three Lines Model (A) | 1 of 4 |
| `8.1` | AI Operating Model & Decision Rights | WEF AI-First Operating System (B); MITRE AI Maturity Model (B); ISO/IEC 38507 (C) | 0 of 3 |
| `8.2` | AI Skills & Specialist Capability Building | AWS CAF-AI (C) *· People perspective*; WEF AI-First Operating System (B); Google AI Adoption Framework (C) | 1 of 3 |
| `8.3` | AI Literacy & Awareness | ISO/IEC 42001 (C); OECD AI Principles (A) | 0 of 2 |
| `8.4` | AI Adoption, Enablement & Support | Google AI Adoption Framework (C); AWS CAF-AI (C); WEF AI-First Operating System (B) | 0 of 3 |
| `8.5` | AI Change Management & Workforce Transition | WEF AI-First Operating System (B); Consultancy transformation patterns (D); OECD AI Principles (A) | 0 of 3 |
| `8.6` | AI Community & Reuse Culture | Open Agile Architecture (B); AWS CAF-AI (C); IDB institutional practice (D) | 0 of 3 |

---

## Statutory references (candidate, Legal-owned — ADR-0008)

18 references, all marked candidate until Legal determines applicability. `7.6.6 Regulatory Role Determination` is the prerequisite.

| Capability | Instrument | Subject | Status |
|---|---|---|---|
| `7.6` Legal, Regulatory & Contractual Compliance for AI | EU AI Act | Provider / deployer role determination (see 7.6.6) | candidate - applicability not determined (see 7.6.5) |
| `2.2` Feasibility & Impact Assessment | EU AI Act | Fundamental rights impact assessment | candidate - applicability not determined (see 7.6.5) |
| `2.5` Human-AI Interaction & Oversight Design | EU AI Act Art. 14 | Human oversight | candidate - applicability not determined (see 7.6.5) |
| `3.1` Data Governance & Stewardship for AI | EU AI Act Art. 10 | Data and data governance | candidate - applicability not determined (see 7.6.5) |
| `3.2` Data Sourcing, Licensing & Provenance | EU AI Act Art. 10 | Data and data governance | candidate - applicability not determined (see 7.6.5) |
| `3.3` Data Quality & Preparation | EU AI Act Art. 10 | Data and data governance | candidate - applicability not determined (see 7.6.5) |
| `4.6` Evaluation & Testing | EU AI Act Art. 15 | Accuracy, robustness, cybersecurity | candidate - applicability not determined (see 7.6.5) |
| `6.3` Continuous Evaluation, Drift & Quality Management | EU AI Act Art. 72 | Post-market monitoring - PROVIDER obligation | candidate - applicability not determined (see 7.6.5) |
| `6.4` AI Incident & Problem Management | EU AI Act Art. 73 | Serious incident reporting - PROVIDER obligation | candidate - applicability not determined (see 7.6.5) |
| `7.6` Legal, Regulatory & Contractual Compliance | EU AI Act | General | candidate - applicability not determined (see 7.6.5) |
| `7.7` AI System & Agent Inventory Management | EU AI Act Art. 49 | Registration - PROVIDER and public-authority deployer only | candidate - applicability not determined (see 7.6.5) |
| `8.3` AI Literacy & Awareness | EU AI Act Art. 4 | AI literacy | candidate - applicability not determined (see 7.6.5) |
| `7.9` AI Impact Assessment & Risk Classification | EU AI Act Annex III (biometric identification) | Biometric identification is an Annex III high-risk category, so any face-recognition use case must be classified before build (formerly catalog service S1.12 Face Detection & Recognition, which had no criterion link; classification is 7.9) | candidate - applicability not determined (see 7.6.5) |
| `2.5` Human-AI Interaction & Oversight Design | EU AI Act Art. 14 | Human-in-the-loop interrupt and approval before an action takes effect (2.5.2, 2.5.4, 7.2.3; formerly catalog service S5.10) | candidate - applicability not determined (see 7.6.5) |
| `7.2` Responsible & Trustworthy AI Practice | EU AI Act Art. 50 | Marking generated content so its origin can be established (7.2.2, 7.6.4; formerly catalog service S7.10 Output Provenance & Watermarking) | candidate - applicability not determined (see 7.6.5) |
| `6.2` AI Monitoring & Observability | EU AI Act Art. 12 (logging) | Retention-managed logging of prompts, context, outputs and decisions (6.2.2, 7.8.2; formerly catalog service S9.2 Interaction & Prompt Logging) | candidate - applicability not determined (see 7.6.5) |
| `6.3` Continuous Evaluation, Drift & Quality Management | EU AI Act Art. 72 (post-market monitoring) | Continuous evaluation of live output quality as the mechanism of post-market monitoring (6.3.1, 4.6.3; formerly catalog service S9.6) | candidate - applicability not determined (see 7.6.5) |
| `7.7` AI System & Agent Inventory Management | EU AI Act Art. 49 | Registration presupposes knowing which AI systems and agents are running (7.7.4, 7.7.5; formerly catalog service S9.11 Fleet & Agent Inventory Telemetry) | candidate - applicability not determined (see 7.6.5) |

