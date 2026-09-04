# -*- coding: utf-8 -*-
import json, io
exec(io.open('catalog4.py', encoding='utf-8').read())
M = json.load(open('model3.json'))

BACKING = [
 ["Hugging Face task taxonomy","47 named ML tasks across 6 modality groups (CV, NLP, audio, multimodal, tabular, RL)","Live, community-maintained","strong","De facto industry taxonomy. Not versioned or dated — cite as convention, not standard.","S1, S2, S3"],
 ["LF AI & Data Landscape","13 technical categories with subcategories (Machine Learning, Deep Learning, Data, Model, Trusted &amp; Responsible AI, Security &amp; Privacy…)","Maintained YAML source, Linux Foundation","strong","The most formally maintained open technical classification of AI/ML tooling.","S8"],
 ["MCP specification 2026-07-28","Primitives (Resources, Prompts, Tools, Elicitation), transports, official Registry v0.1","Current; governed by the Agentic AI Foundation under the Linux Foundation","strong","Roots, Sampling and Logging deprecated in this release; protocol went stateless. Anything citing the 2025 spec is stale.","S5, S6"],
 ["A2A specification 1.0.0","Agent Card, Task lifecycle (7 states), Message, Part, Artifact; JSON-RPC / gRPC / REST bindings","Current; moved to AAIF August 2026","strong","Transferred Google → Linux Foundation → AAIF. Now governed alongside MCP.","S5"],
 ["OWASP Top 10 for LLM Applications 2026","LLM01–LLM10, v2.0","Published ~March 2026","strong","Materially different from the 2023 list — item names and ordering both changed.","S7"],
 ["OWASP Top 10 for Agentic Applications 2026","ASI01–ASI10 (Goal Hijack, Tool Misuse, Identity &amp; Privilege Abuse, Memory Poisoning, Rogue Agents…)","Published December 2025","strong","The first enumerated agentic threat taxonomy from a recognised body.","S5, S7"],
 ["C2PA specification 2.4","Content Credentials, digital source types for AI output, data-mining assertions","Current","strong","Backs output provenance and training-data opt-out signalling.","S7"],
 ["IBM Generative AI Capability Model","7 L1 categories decomposed to L2/L3 (Model Hub, Model Hosting, Agentic AI, GenAI Governance, Security Management…)","IBM Architecture Center, current Jan 2026","strong","The strongest single vendor-published capability decomposition. Structurally vendor-neutral in its naming.","S5, S8"],
 ["SAP AI-native North Star","4 layers; named MCP Gateway, Agent Gateway, harness engineering, context engineering","Published June 2026","strong","Freshest enterprise architecture naming concrete MCP/A2A gateway roles rather than gesturing at interoperability.","S5, S6"],
 ["OpenTelemetry GenAI semantic conventions","Operation taxonomy: chat, embeddings, execute_tool, invoke_agent, invoke_workflow, create_agent, retrieval, plan","<b>Development status — not stable</b>; separate repo since June 2026","partial","An operation taxonomy in all but name, and the closest thing to a neutral vocabulary for agent observability. Attribute names are still changing.","S5, S9"],
 ["ISO/IEC 23053:2022","ML task examples (regression, classification, clustering, anomaly detection, dimensionality reduction) + 6 pipeline stages","Current","partial","The task list is <b>explicitly non-exhaustive and illustrative</b>. Do not present it as a controlled taxonomy.","S4, S8"],
 ["ISO/IEC 22989:2022","Clause 9 “Fields of AI”: computer vision, NLP, data mining, planning, knowledge processing","Current","partial","Terminology entries in prose, not a normative classification table.","S1, S4"],
 ["OECD Framework for the Classification of AI Systems","5 dimensions; the Task &amp; Output dimension names core application areas and autonomy levels","Published 2022, no revision found","partial","A policy classification tool, not an engineering catalog — but the most developed formal task dimension available.","S1, S5"],
 ["Australia DTA technical standard for government use of AI","8 lifecycle stages, 42 numbered compliance statements","Current, architecture.digital.gov.au","strong","The strongest public-sector precedent found. Lifecycle-shaped, directly adaptable.","overlay"],
 ["Gartner AI TRiSM","Concept: continuous embedded governance across the lifecycle","Primary document June 2026, paywalled","weak","<b>Pillar list is not stable across public sources</b> — at least four different structures are attributed to it. Cite the functional intent, never a specific pillar list.","S7"],
 ["Agent identity standards","CSA Agent Identity Governance Framework v1; OpenID Foundation AI Identity CG; several individual IETF drafts","Pre-consensus","weak","No ratified standard exists. Microsoft Entra Agent ID is the most productised implementation, not a standard. Cite as emerging.","S6"],
 ["ISO/IEC 42001, 42005, 5338, 23894","Management system, impact assessment, lifecycle processes, risk guidance","Current","none","<b>Contain no functional or service taxonomy.</b> They back the capability model's governance domains, not this layer. Confirmed by structure.","—"],
 ["NIST AI RMF and AI 600-1","Govern/Map/Measure/Manage; 12 GenAI risk categories","Current","none","<b>Risk and harm taxonomies, not functional ones.</b> No enumeration of AI system task types.","—"],
 ["ISO/IEC TR 24030:2024","81 use cases across 18 application domains","2nd edition, April 2024","none","Taxonomises <b>application domains and deployment models</b>, not AI functions. A plausible-looking source that does not actually back a service catalog.","—"],
 ["The Open Group","—","No AI reference model published","none","IT4IT 3.0 contains <b>zero</b> mentions of AI/ML/GenAI. The AI Initiatives page states intent with no deliverable. ArchiMate 4 shipped May 2026 — AI-specific elements unverified.","—"],
 ["Papers with Code","—","Discontinued (2025)","none","No longer maintained. Do not cite as a current task ontology.","—"],
 ["Banks and development banks","—","Nothing published","none","World Bank, IMF, JPMorgan, Capital One, DBS, ING: no reusable AI capability model or technical reference architecture found. Trade-press write-ups are not citable artifacts.","—"],
]

CURRENCY = [
 ["Microsoft","<b>Azure AI Foundry → Microsoft Foundry.</b> “Azure” dropped from the brand. <b>“Azure AI services” → “Foundry Tools”</b> — Vision, Speech, Language, Document Intelligence are all now Foundry Tools.","Any internal material still saying “Azure AI Studio” or “Azure AI services” is stale. New named components: Foundry IQ (managed knowledge layer), Foundry Control Plane (cross-agent observability and runtime control), Foundry Local (on-device)."],
 ["Microsoft","<b>Retired Foundry Tools:</b> Anomaly Detector, Content Moderator, LUIS, Metrics Advisor, Personalizer, QnA Maker.","Superseded — Content Moderator by Content Safety. Do not put any of these in a target architecture."],
 ["Microsoft","<b>Entra Agent ID</b> is GA: agent identity blueprints, per-instance identities, human sponsors, lifecycle governance, native OAuth 2.0 / MCP / A2A support.","The most mature agent-identity implementation of the three hyperscalers. Directly realizes capability 7.4.4 and 7.7.2."],
 ["AWS","<b>July 2026 retirement wave.</b> Bedrock Agents (“Classic”), Amazon Kendra, Amazon Q Business and ~10 SageMaker AI features moved to maintenance mode.","Successors: Bedrock AgentCore, Bedrock Knowledge Bases, Amazon Quick Suite. SageMaker renamed SageMaker AI."],
 ["Google","<b>Agentspace → Gemini Enterprise.</b> Vertex AI Agent Builder absorbed into the Gemini Enterprise Agent Platform; docs now redirect.","Any taxonomy with “Vertex AI” as the top-level Google node is already out of date. New: Agent Registry, Agent Gateway, Skill Registry."],
 ["Protocols","<b>MCP and A2A now share a governance home</b> — the Agentic AI Foundation, a Linux Foundation body, 250+ members including AWS, Anthropic, Google, Microsoft, OpenAI.","This materially strengthens the case for building on MCP/A2A rather than a proprietary integration pattern. It is no longer single-vendor."],
 ["Protocols","<b>MCP went stateless</b> in the 2026-07-28 revision. Roots, Sampling and Logging deprecated with a 12-month offramp; legacy HTTP+SSE transport deprecated.","Anything built against the 2025 spec needs a migration plan inside 12 months."],
]


# Capabilities realized by EXISTING non-AI enterprise services rather than by AI services,
# and capabilities that are purely human. Both are legitimate blanks in Matrix A.
EXT = {
 "1.2":"Enterprise portfolio and investment management",
 "1.3":"Benefits realization and performance reporting tooling",
 "1.4":"Procurement and vendor management systems",
 "2.1":"Demand management / ITSM intake",
 "4.7":"CI/CD pipeline and change management tooling",
 "6.6":"CMDB and IT asset management",
 "7.3":"Enterprise GRC platform",
 "7.9":"GRC assessment and workflow tooling",
 "8.2":"Learning management system",
 "8.3":"Learning management system",
 "8.4":"Service desk and adoption analytics",
 "8.6":"Collaboration and knowledge platform",
}
HUMAN = {"1.1","2.2","8.1","8.5"}

CAPJSON = json.dumps(M, ensure_ascii=False, separators=(',', ':'))
SVCJSON = json.dumps(S, ensure_ascii=False, separators=(',', ':'))
BACKJSON = json.dumps(BACKING, ensure_ascii=False, separators=(',', ':'))
CURJSON = json.dumps(CURRENCY, ensure_ascii=False, separators=(',', ':'))

REG = json.load(open('register.json'))
REGJSON = json.dumps(REG, ensure_ascii=False, separators=(',', ':'))
EXTJSON = json.dumps(EXT, ensure_ascii=False, separators=(',', ':'))
HUMJSON = json.dumps(sorted(HUMAN), ensure_ascii=False, separators=(',', ':'))
io.open('trm_data.js', 'w', encoding='utf-8').write(
  "const CAP=%s;\nconst SVC=%s;\nconst BACKING=%s;\nconst CURRENCY=%s;\nconst EXT=%s;\nconst HUMAN=new Set(%s);\nconst REG=%s;\n"
  % (CAPJSON, SVCJSON, BACKJSON, CURJSON, EXTJSON, HUMJSON, REGJSON))
print("data written:", len(CAPJSON), len(SVCJSON), len(BACKJSON), len(CURJSON))
