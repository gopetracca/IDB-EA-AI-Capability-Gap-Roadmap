# -*- coding: utf-8 -*-
"""Scales and seed rows for the Realization & Readiness workbook."""

MATURITY = [
 (1,"Initial","Verified isolated execution that relies on individuals and is not repeatable.","Evidence of isolated execution; no common method."),
 (2,"Repeatable","Repeatable within named local scopes over a defined period.","Repeated execution, local ownership, specified coverage."),
 (3,"Defined","An approved common method and roles are applied across the required scope.","A published standard, a coverage rule, sampled conformance."),
 (4,"Managed","Thresholds, exceptions and corrective actions operate over a defined period.","Monitoring with thresholds, control tests, retained evidence."),
 (5,"Adaptive","At least one completed evidence-driven improvement cycle produced a verified outcome.","Trend, action, verified benefit, external comparison."),
]
MAT_STATES = [
 ("0","Absent","Applicability confirmed and a documented inquiry finds no operating instance.","A positive absence finding - not the lack of a search."),
 ("NE","Not evidenced","Applicable, but evidence is insufficient to rate.","Show in the completeness view; never treat as zero."),
 ("UC","Under clarification","Applicability or legal status unresolved.","Owner and due date required."),
 ("NA","Not applicable","Formally out of scope.","Approver, rationale and expiry required."),
]
READINESS = [
 (0,"Not available","No supported realization.","-"),
 (1,"Available or project-proven","The technology exists and can do it, or one team built it and it works. Not separable from their application, not reusable.","The application, or the vendor capability"),
 (2,"Approved","Cleared for enterprise use. Each team assembles the solution itself.","The approval record"),
 (3,"Standardized","A published standard and an architecture pattern or reference architecture exist.","The standard - the pattern document"),
 (4,"Industrialized","Reusable building blocks: IaC, security baseline, observability, CI/CD, implementation guidance, support model. Teams self-serve a compliant instance and operate it.","The module or template repository - a team that used it"),
 (5,"Productized","An exposed endpoint with a contract. Consumers call it; the platform operates it.","The endpoint - its service levels - its operational owner - its consumers"),
]
CONSUMPTION = [
 ("Guidance","EA tells you how to build it."),
 ("Building blocks","Reusable modules and components are provided."),
 ("Reference implementation","A working implementation exists and can be adapted."),
 ("Managed platform","The platform provides the underlying infrastructure; the consumer configures on top."),
 ("Service / API","The consumer calls it and gets a result."),
]
GENERIC_ASSETS = [
 ("Published standard","The institutional standard for how this is built."),
 ("Architecture pattern document","Problem, context, forces, solution, resulting context - not just a name."),
 ("Reference architecture","The worked target design."),
 ("Infrastructure as code","Provisioning is repeatable and reviewable."),
 ("CI/CD pipeline","Change is built and released through a controlled path."),
 ("Security baseline","Identity, network and data controls applied by default."),
 ("Observability wired","Telemetry emitted without the team adding it."),
 ("Runbook","Operations know what to do when it misbehaves."),
 ("Support model","Someone answers when it breaks."),
]

# --- realizations -------------------------------------------------------
# conf=True means stated by the platform owner or evidenced by a named IDB asset.
# prefill seeds sheet 3 where the asset inventory settles the answer.
REAL = [
 dict(id="REAL-001", conf=True, cap="5.1", also="5.3, 5.4",
      pattern="Microsoft Foundry Reference Architecture (RA-02)",
      tech="Microsoft Foundry", support="IAC-04 Foundry Account; IAC-05 Foundry Project",
      readiness=4, consumption="Building blocks", status="Approved", preferred="Y",
      operated="Consumer - each team deploys and runs its own instance",
      note="Standard published, reference architecture published, both Terraform modules published in JFrog. This is the strongest realization in the estate.",
      notprov="",
      prefill={"Published standard":"Yes","Architecture pattern document":"Yes","Reference architecture":"Yes",
               "Infrastructure as code":"Yes"}),

 dict(id="REAL-002", conf=True, cap="5.1", also="5.6, 4.4",
      pattern="Foundry Agents Reference Architecture (RA-05, PRE-RELEASE)",
      tech="Microsoft Foundry", support="IAC-04; IAC-05; IAC-02 Container Apps; STD-06 AI Agent Decision Tree",
      readiness=3, consumption="Building blocks", status="Approved", preferred="Y",
      operated="Consumer - each team deploys and runs its own instance",
      note="READINESS 3, NOT 4 - and only because the documentation trails the engineering. The Terraform modules are published and in use; the Foundry Agents Standard (STD-07) and its Reference Architecture (RA-05) are both PRE-RELEASE. Releasing those two documents is the whole distance to 4. Confirm this reading.",
      notprov="The agent itself: business rules, grounding data, evaluation criteria, human oversight design. Those remain with the delivery team.",
      prefill={"Published standard":"Partial","Architecture pattern document":"Partial",
               "Reference architecture":"Partial","Infrastructure as code":"Yes"}),

 dict(id="REAL-003", conf=True, cap="4.5", also="5.5",
      pattern="Custom MCP Server Reference Architecture (RA-01)",
      tech="C# / .NET on Azure Container Apps",
      support="TPL-01 template v1 (in use); TPL-02 template v2 (built, not distributed); IAC-02 published; IAC-01 and IAC-03 in review",
      readiness=4, consumption="Reference implementation", status="Approved", preferred="Y",
      operated="Consumer - each team deploys and runs its own server",
      note="Standard, reference architecture and a working template that built every custom MCP server on the AI MVP project. TEMPLATE v1 IMPLEMENTS THE SUPERSEDED MCP SPECIFICATION - the July 2026 revision deprecated Roots, Sampling, Logging, RFC 7591 dynamic client registration and the legacy HTTP+SSE transport on defined timelines. Every server built from v1 needs a migration plan inside that window, and v2 is built but not yet distributed. That is a dated roadmap item, not a maturity opinion.",
      notprov="",
      prefill={"Published standard":"Yes","Architecture pattern document":"Yes","Reference architecture":"Yes",
               "Infrastructure as code":"Partial"}),

 dict(id="REAL-004", conf=True, cap="3.6", also="",
      pattern="Azure AI Search Reference Architecture (RA-03) - hybrid / semantic retrieval",
      tech="Azure AI Search", support="IAC-06 AI Search module (published)",
      readiness=4, consumption="Building blocks", status="Approved", preferred="Y",
      operated="Consumer",
      note="Standard, reference architecture and a published Terraform module. Supply is well packaged - which is exactly why the maturity of capability 3.6 must be argued separately. See REAL-005.",
      notprov="",
      prefill={"Published standard":"Yes","Architecture pattern document":"Yes","Reference architecture":"Yes",
               "Infrastructure as code":"Yes"}),

 dict(id="REAL-005", conf=False, cap="3.6", also="",
      pattern="S3.10 Access-Trimmed Retrieval", tech="", support="",
      readiness=None, consumption="", status="", preferred="",
      operated="",
      note="CONFIRM THIS ROW - it decides the headline finding for D3. Does the Azure AI Search Standard (STD-04) mandate that source ACL metadata is extracted, indexed and applied as a pre-ranking filter? If it does, readiness follows REAL-004. If it does not, this sits at 0 and it is the reason capability 3.6 can carry readiness 4 and a much lower maturity. Filtering a ranked list after the fact both leaks and distorts relevance.",
      notprov="", prefill={}),

 dict(id="REAL-006", conf=True, cap="3.5", also="",
      pattern="Azure Document Intelligence Reference Architecture (RA-04)",
      tech="Azure AI Document Intelligence", support="",
      readiness=3, consumption="Guidance", status="Approved", preferred="Y",
      operated="Consumer",
      note="Standard and reference architecture published; no Terraform module in the inventory. Publishing one is the step to 4.",
      notprov="",
      prefill={"Published standard":"Yes","Architecture pattern document":"Yes","Reference architecture":"Yes",
               "Infrastructure as code":"No"}),

 dict(id="REAL-007", conf=True, cap="4.1", also="5.2",
      pattern="Tech Stack - AI standard (STD-01)", tech="", support="",
      readiness=3, consumption="Guidance", status="Approved", preferred="Y",
      operated="-",
      note="The approved AI technology stack. This is the asset that answers 'what is already approved for general use' at the technology level - it is evidence toward capability maturity, not a substitute for it.",
      notprov="",
      prefill={"Published standard":"Yes"}),

 dict(id="REAL-008", conf=True, cap="2.5", also="2.2",
      pattern="AI Agent Decision Tree (STD-06)", tech="", support="",
      readiness=3, consumption="Guidance", status="Approved", preferred="Y",
      operated="-",
      note="A published decision aid for whether and what kind of agent is appropriate. This is the only realization currently touching domain D2, and it maps to the autonomy and interaction-pattern determination.",
      notprov="",
      prefill={"Published standard":"Yes"}),
]

# --- pattern-specific controls per realization --------------------------
AGENT_CONTROLS = [
 ("Distinct workload identity per instance, not a shared service principal","S6.9","7.4.4",
  "A shared service principal makes every agent's actions indistinguishable. Nothing downstream can attribute or revoke."),
 ("Automatic registration in the AI system / agent inventory","S6.6","7.7.2",
  "An inventory that depends on teams remembering to register is not an inventory."),
 ("Tracing and tool-call logging enabled by default","S9.1","6.2.2",
  "If it is not on by default it will not be there when you need to explain what an agent did."),
 ("Content filtering and safety controls on by default","S7.1","7.4.6",
  "Opt-in safety is the control that is missing exactly when it is needed."),
 ("Prompt-injection defence configured","S7.4","7.4.3",
  "Content the agent reads can instruct it. Prompt design alone does not stop this at run time."),
 ("Evaluation harness scaffolded in the template","S8.15","4.6.3",
  "Without a harness in the template, evaluation happens once at launch and never again."),
 ("Cost attribution tags applied automatically","S9.4","6.5.1",
  "Untagged consumption cannot be attributed, forecast or stopped."),
 ("A tested way to stop it and revoke its access","S7.13","6.4.2",
  "An untested kill switch is an assumption, not a control."),
 ("Credential issuance and rotation handled by the platform","S6.9","5.2.4",
  "Credentials created by hand are credentials nobody rotates."),
 ("Network isolation and private connectivity baseline","S8.20","5.3.3",
  "Isolation applied per team is isolation applied inconsistently."),
 ("A hook for human approval of consequential actions","S5.10","2.5.2",
  "Oversight designed into the platform is exercised; oversight written into policy is not."),
 ("Interaction log retention configured to policy","S9.2","3.1.4",
  "Interaction logs are evidence. Retention set per project is evidence you cannot rely on."),
]
RETRIEVAL_CONTROLS = [
 ("Entitlement enforced at query time, before ranking","S3.10","3.6.2",
  "Filtering a ranked list after the fact both leaks and distorts relevance. The filter must precede ranking."),
 ("Citations resolvable to source, version and location","S3.12","3.6.5",
  "A citation that cannot be opened is decoration. It also does not prove the statement is true."),
 ("Retrieval quality measured against a benchmark","S8.15","3.6.3",
  "Relevance that is never measured degrades silently as the corpus changes."),
 ("Re-embedding runbook for model change","S3.8","3.7.3",
  "Changing the embedding model invalidates the index. Without a runbook this is an outage."),
 ("Index residency and access controls enforced","S3.8","3.1.5",
  "A vector index is a copy of the source content, and inherits its residency obligations."),
]

MCP_CONTROLS = [
 ("Server registered in an approved-server registry before any client may call it","S6.6","5.5.2",
  "A public registry entry is not enterprise approval. Discovery and approval are different registers."),
 ("Acting user's identity propagated on-behalf-of to the system of record","S6.8","4.5.4",
  "Without it every action looks like the service account and the audit trail names the wrong actor."),
 ("Tool scopes issued at least privilege","S6.9","5.5.3",
  "A tool that can do more than its purpose is the confused-deputy path."),
 ("Traffic passes a gateway or policy enforcement point","S6.5","7.4.5",
  "Per-server enforcement is enforcement that varies by team."),
 ("Protocol revision pinned, with a migration plan for the July 2026 spec","S10.1","5.5.5",
  "Roots, Sampling, Logging, RFC 7591 dynamic client registration and legacy HTTP+SSE are deprecated on defined timelines. Template v1 predates this."),
 ("Tool calls audited with arguments and effect","S9.3","6.2.3",
  "You cannot explain what an agent did without the call record."),
]
DOCAI_CONTROLS = [
 ("Extraction confidence thresholds set and enforced","S8.15","4.6.1",
  "Extraction without a confidence floor silently promotes guesses to facts."),
 ("Human validation path for low-confidence output","S5.10","2.5.2",
  "The threshold is only useful if something happens when it is not met."),
 ("Page and bounding-box provenance retained","S3.12","3.6.5",
  "An extracted value that cannot be traced to a page is unverifiable downstream."),
 ("Output validated against a declared schema","S2.5","4.5.2",
  "Schema validation is what makes the output machine-consumable rather than plausible text."),
]

CONTROLS_BY_REAL = {"REAL-002": AGENT_CONTROLS, "REAL-003": MCP_CONTROLS,
                    "REAL-004": RETRIEVAL_CONTROLS, "REAL-005": RETRIEVAL_CONTROLS,
                    "REAL-006": DOCAI_CONTROLS}
