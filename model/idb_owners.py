# -*- coding: utf-8 -*-
"""Mapping of the AI capability model onto IDB's real product and enabler catalogue.

Source: sources/Product and Applications_ENTERPRISE.xlsx, sheet "Reviewed Product Fact Sheet",
read 4 September 2026. That file is the Bank's own accountability register; this module records
which product or enabler would own each AI capability, and where nothing in it fits.

MATCH is my classification, for the reviewer to confirm or correct:
  Direct    the product/enabler's own capability text names this, or something that plainly contains it
  Inferred  no capability line names it, but it falls inside that owner's stated remit
  Partial   the owner covers part of it; the AI-specific part is not covered by anything they claim
  NO MATCH  nothing in the catalogue covers it. The nearest adjacent owner is named in the basis.
"""

SOURCE_FILE = "sources/Product and Applications_ENTERPRISE.xlsx"
SOURCE_SHEET = "Reviewed Product Fact Sheet"
READ_ON = "4 September 2026"

# name, function, family, lead, technical lead, the capability text relied on (abridged)
IDB_OWNERS = [
 ("Artificial Intelligence","Enabler","Technology and Data Solutions","JAIRORI@IADB.ORG","",
  "Strategy & Roadmap · Platform Development (Unstructured Data Application, MCP Denodo, MCP Convergencia, MCP sgDelta) · Ops & Lifecycle Management · Agent Skill Admin · AI Gateway"),
 ("Enterprise Architecture","Enabler","Technology and Data Assurance","KARLAVI@IADB.ORG","RauldaSilva",
  "Technology Strategy (buy vs build, target architecture) · Software Architecture (co-design, institutional-reach projects)"),
 ("Cybersecurity","Enabler","Technology and Data Assurance","harleyj@IADB.ORG","",
  "Security Assurance (governance, awareness, ISMS, risk register, internal controls) · Security engineering and architecture"),
 ("Data Management","Enabler","Technology and Data Solutions","carlosd@iadb.org","",
  "Data Management · Database administration · Data Analytics Products · Data Marketplace · Data Architecture · Data services · Consultancy · Data Governance & Quality"),
 ("Cloud and Infrastructure","Enabler","Technology and Data Solutions","EGDARESF@IADB.ORG","",
  "Cloud Strategy and Cost Management · Cloud Operations, Engineering and Security · Identity and Access Management · Enterprise communications and networking (incl. observability)"),
 ("Core Platforms","Enabler","Technology and Data Solutions","JUANAA@iadb.org","",
  "Business process management · Integrations (Biztalk, API management, Service Bus) · Development platform (Terraform, CICD) · Content management (ezShare, OneDrive, SharePoint, search, e-disposition of records) · Collaboration and productivity"),
 ("Service Delivery","Enabler","Technology and Data Solutions","PAULOV@iadb.org","",
  "Service Desk · Desktop Support · Country Office Support · Contracts Management · Assets Management"),
 ("Strategic Portfolio Management","Enabler","Technology and Data Assurance","SUSANAP@IADB.ORG","Cesar Garces",
  "Governance Framework · Strategic Portfolio Management · Rationalization · Prioritization (WSJF) · Capacity & Budget Dashboard · Portfolio Health Monitoring · Ways of working · Dependency Mapping"),
 ("Strategic Resource Management","Enabler","CIO","BrunoFe@iadb.org","",
  "Resource Management · Budget Management · Vendor Management · People Management, Development, Engagement · Strategic Alignment / Prioritization of Resources"),
 ("IT Risk (Compliance)","Enabler","Technology and Data Assurance","","julissac@iadb.org",
  "Self-Assessment of Internal Controls for TTD · Oversight and follow-up of internal and external audits · PRAC reviews (design & implementation of controls) · Advisory services"),
 ("Digital Transformation","Enabler","Innovation and Business Transformation","gperla@IADB.ORG","",
  "Process transformation · Change management · Digitalization"),
 ("People Experience - IBT","Enabler","Innovation and Business Transformation","ANASP@IADB.ORG","",
  "Innovation · Open innovation · Communication · UX/UI (to be added) · Process redesign (to be added) · Digital transformation expertise"),
 ("Emerging Tech","Product","Technology and Transformation in the Region","rcerrato@IADB.ORG","",
  "Technological vigilance · Experimentation · Sandbox · Technological awareness (events, workshops) · Research"),
 ("Knowledge Management","Product","Operations","RBENITEZ@IADB.ORG","JAVIERFE@IADB.ORG",
  "Systematization · Analysis · Capture and dissemination of operational and analytical knowledge"),
 ("Risk, Audit & Compliance","Product","Enterprise and Finance","CARLOSEN@iadb.org","",
  "Operational Risk management (Metric Stream) · Control management · Audit and Assurance (CARP, TeamMate) · AML & CTM Operations · Grievances"),
 ("People Management","Product","Enterprise and Finance","ERICKMA@IADB.ORG","",
  "HR CORE · Performance Management · Learning · Recruitment & Onboarding · Compensation"),
]
OWNER_BY_NAME = {o[0]: o for o in IDB_OWNERS}

# capability id -> (owner name or '', match, basis / what to do about it)
MAP = {
 # ---- D1 Strategy & Value
 "1.1": ("Artificial Intelligence","Direct",
   "AI enabler claims 'Strategy & Roadmap: co-define and own the corporate AI capability strategy and execution roadmap with the Tech Office (TDA, TDS) and DT'."),
 "1.2": ("Strategic Portfolio Management","Direct",
   "SPM claims Strategic Portfolio Management, Prioritization (WSJF, strategic alignment, value, risk) and the Capacity & Budget Dashboard."),
 "1.3": ("Strategic Portfolio Management","Inferred",
   "SPM claims Portfolio Health Monitoring (progress, risk, impact). It does not claim value attribution for AI specifically — confirm whether AI benefit tracking sits here or with the AI enabler."),
 "1.4": ("Strategic Resource Management","Partial",
   "SRM claims Vendor Management. Nothing claims AI-specific contractual safeguards, model-provider evaluation, or concentration and exit risk. Second owner likely needed (Legal / Procurement)."),
 "1.5": ("","NO MATCH",
   "No product or enabler covers external AI partnerships, academic collaboration or multilateral cooperation. Nearest is Emerging Tech (research, publications, work with central banks), but its remit is technology watch, not alliance management."),
 # ---- D2 Demand & Solution Shaping
 "2.1": ("Artificial Intelligence","Inferred",
   "AI enabler maintains the enterprise AI capability catalogue, which implies an intake route, but no capability line names demand intake. Strategic Portfolio Management owns prioritisation. Boundary needs settling."),
 "2.2": ("Enterprise Architecture","Inferred",
   "EA claims co-design sessions and target/transition architecture work with product teams. Feasibility of AI use cases is not named by anyone."),
 "2.3": ("","NO MATCH",
   "Product management is exercised per product family, not centrally for AI. No enabler claims AI product management. Decide whether this is an AI-enabler responsibility or is delegated to consuming products."),
 "2.4": ("Digital Transformation","Direct",
   "Digital Transformation claims Process transformation and Digitalization. People Experience - IBT lists Process redesign as a capability to be formalised next year."),
 "2.5": ("People Experience - IBT","Partial",
   "IBT lists UX/UI as 'a formal capability to be added next year based on the bank's business plan'. Human-AI oversight design has no owner today."),
 "2.6": ("Emerging Tech","Direct",
   "Emerging Tech claims Experimentation, Sandbox, Technological vigilance and Research. People Experience - IBT also claims Innovation and Open innovation — two candidates, boundary needs settling."),
 # ---- D3 Data & Knowledge
 "3.1": ("Data Management","Direct","Data Management claims Data Governance & Quality."),
 "3.2": ("Data Management","Partial",
   "Data Management claims data integration, certification and publication. Licensing and provenance of data used for AI training or grounding is not covered by anyone."),
 "3.3": ("Data Management","Direct","Data Management claims Data Governance & Quality, and data integration and certification."),
 "3.4": ("Data Management","Direct",
   "Data Management claims the Data Marketplace — catalog and publication of certified data assets — and Data Architecture."),
 "3.5": ("Core Platforms","Partial",
   "Core Platforms claims Content management (ezShare, OneDrive, SharePoint, search). Knowledge Management claims capture and dissemination of operational knowledge. Two candidates and neither claims curation of a corpus for AI grounding."),
 "3.6": ("Artificial Intelligence","Direct",
   "AI enabler claims Platform Development including the Unstructured Data Application and the MCP servers, which is where retrieval is delivered."),
 "3.7": ("Artificial Intelligence","Inferred",
   "Embeddings and derived representations are named nowhere in the catalogue. They fall inside the AI enabler's platform remit by elimination."),
 # ---- D4 Solution Engineering
 "4.1": ("Enterprise Architecture","Direct",
   "EA claims Technology Strategy (guidelines, target architecture) and Software Architecture (co-design, review with tech leads)."),
 "4.2": ("Artificial Intelligence","Direct",
   "AI enabler claims Platform Development from MVP through production."),
 "4.3": ("Artificial Intelligence","Inferred",
   "Prompt and context engineering is named nowhere. Falls inside the AI enabler's platform remit by elimination."),
 "4.4": ("Artificial Intelligence","Partial",
   "AI enabler claims 'Agent Skill Admin'. Administering agent skills is not the same as designing agent goals, guardrails and termination. The design half has no owner."),
 "4.5": ("Core Platforms","Partial",
   "Core Platforms claims Integrations (Biztalk, API management, Service Bus). The AI enabler separately owns the MCP servers. Split ownership — settle who owns tool exposure to AI clients."),
 "4.6": ("","NO MATCH",
   "No product or enabler claims evaluation or testing of AI systems. This is the capability that decides whether anything the Bank ships actually works."),
 "4.7": ("Core Platforms","Inferred",
   "Core Platforms claims the Development platform (Terraform, CICD). AI-specific release gating is not named."),
 # ---- D5 Platform & Infrastructure
 "5.1": ("Artificial Intelligence","Direct",
   "AI enabler claims Ops & Lifecycle Management: operate and continuously improve AI platform capabilities in production."),
 "5.2": ("Artificial Intelligence","Direct",
   "The AI enabler's fact sheet names the AI Gateway (shared and dedicated model access) among its systems."),
 "5.3": ("Cloud and Infrastructure","Direct",
   "Cloud and Infrastructure claims Cloud Operations, Engineering and Security, and Identity and Access Management."),
 "5.4": ("Cloud and Infrastructure","Direct",
   "Cloud and Infrastructure claims Cloud Strategy and Cost Management."),
 "5.5": ("Artificial Intelligence","Partial",
   "AI enabler maintains the enterprise AI capability catalogue and owns the MCP servers. A catalogue of capabilities is not a governed inventory of callable tools with scopes and vetting."),
 "5.6": ("Core Platforms","Partial",
   "Core Platforms claims the Development platform (Terraform, CICD). Curation of AI reference implementations and templates is not named — today the AI enabler and EA produce them."),
 # ---- D6 Operations & Reliability
 "6.1": ("Artificial Intelligence","Direct","AI enabler claims Ops & Lifecycle Management in production."),
 "6.2": ("Cloud and Infrastructure","Partial",
   "Cloud and Infrastructure claims observability within networking and cloud service delivery. AI-specific telemetry — traces, tool calls, agent actions — is not named."),
 "6.3": ("","NO MATCH",
   "Nobody claims drift detection or continuous quality management. Related to 4.6: the Bank has no named owner for whether an AI system still works after release."),
 "6.4": ("Service Delivery","Partial",
   "Service Delivery claims the Service Desk as first point of contact. AI-specific incident handling, and the question of who triages a model or agent failure, is not covered."),
 "6.5": ("Cloud and Infrastructure","Direct",
   "Cloud and Infrastructure claims Cloud Strategy and Cost Management, including financial operations integration with SaaS and cloud."),
 "6.6": ("Service Delivery","Partial",
   "Service Delivery claims Assets Management; Core Platforms claims e-disposition of records. Retirement of an AI system with its evidence preserved is not named by either."),
 # ---- D7 Governance, Risk, Security & Assurance
 "7.1": ("Artificial Intelligence","Partial",
   "AI enabler owns the AI strategy; Cybersecurity owns Security Governance (policies, standards, baselines); EA owns technology guidelines. No one owns an AI management system as such."),
 "7.2": ("","NO MATCH",
   "No product or enabler names responsible, ethical or trustworthy AI. This is the single most visible absence in the catalogue for an institution of this kind."),
 "7.3": ("Risk, Audit & Compliance","Partial",
   "Risk, Audit & Compliance claims Operational Risk management (Metric Stream) and Control management. AI risk is not named, and it is unclear whether AI risk enters the operational risk register at all."),
 "7.4": ("Cybersecurity","Direct",
   "Cybersecurity claims Security engineering and architecture (design and review of applications) and Security Assurance including the risk register and exception management."),
 "7.5": ("","NO MATCH",
   "No privacy or data protection function appears anywhere in the catalogue. Confirm whether privacy sits outside TTD entirely."),
 "7.6": ("","NO MATCH",
   "Legal does not appear as a product or enabler. The obligations register (18 candidate statutory references) has no owner in this catalogue."),
 "7.7": ("Artificial Intelligence","Partial",
   "AI enabler maintains the enterprise AI capability catalogue. That is a catalogue of what the platform offers, not an inventory of every AI system and agent in operation with a named accountable owner."),
 "7.8": ("IT Risk (Compliance)","Partial",
   "IT Risk claims oversight of internal and external audits and PRAC reviews of control design and implementation. Producing and preserving AI assurance evidence is not named."),
 "7.9": ("","NO MATCH",
   "Nobody claims impact assessment or risk classification of AI systems. This is the prerequisite for almost every obligation in the register."),
 # ---- D8 People, Skills & Adoption
 "8.1": ("Strategic Portfolio Management","Inferred",
   "SPM claims the Governance Framework (reviews, approvals, tracking of decisions) and Ways of working. AI decision rights specifically are not named."),
 "8.2": ("Strategic Resource Management","Partial",
   "SRM claims People Management and Development; People Management (product) claims Learning. Neither names AI skills or specialist capability building."),
 "8.3": ("Emerging Tech","Partial",
   "Emerging Tech claims Technological awareness — events, workshops and sessions to disseminate knowledge. Bank-wide AI literacy is broader than that and is not named by anyone."),
 "8.4": ("Artificial Intelligence","Direct",
   "The AI enabler's stated value proposition is to 'enable every product and enabler team' — adoption and enablement is its reason for existing."),
 "8.5": ("Digital Transformation","Direct","Digital Transformation claims Change management."),
 "8.6": ("Emerging Tech","Partial",
   "Emerging Tech claims awareness and dissemination; People Experience - IBT claims Open innovation. Neither claims a practitioner community or reuse culture for AI."),
}
