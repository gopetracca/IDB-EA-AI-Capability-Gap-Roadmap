# -*- coding: utf-8 -*-
"""IDB enterprise assets: standards, reference architectures, templates, IaC modules."""

# type, id, name, status, location, note
ASSETS = [
 # ---- standards -------------------------------------------------------
 ("Standard","STD-01","Tech Stack - AI","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-22",
  "Defines the approved AI technology stack."),
 ("Standard","STD-02","Custom MCP Server Standard","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-18",""),
 ("Standard","STD-03","Microsoft Foundry Standard","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-957",
  "Covers platform deployment."),
 ("Standard","STD-04","Azure AI Search Standard","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-726",""),
 ("Standard","STD-05","Azure Document Intelligence Standard","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-105",""),
 ("Standard","STD-06","AI Agent Decision Tree","Published",
  "https://ezws.iadb.org/getdocument.aspx?docnum=EZIDB0000557-1067528196-110",
  "Decision aid for whether and what kind of agent is appropriate."),
 ("Standard","STD-07","Foundry Agents Standard","Pre-release","",
  "PRE-RELEASE. Releasing this is one of two steps that move agent provisioning from readiness 3 to 4."),
 # ---- reference architectures ----------------------------------------
 ("Reference architecture","RA-01","Custom MCP Server Reference Architecture","Published",
  "https://iadb.leanix.net/IADBProduction/diagrams/dataflow/e1b8ef3c-f669-45ec-8f0e-aeee58780f8a",""),
 ("Reference architecture","RA-02","Microsoft Foundry Reference Architecture","Published",
  "https://iadb.leanix.net/IADBProduction/diagrams/freedraw/27c7c109-7da7-4c2f-b248-eeab47f07238",""),
 ("Reference architecture","RA-03","Azure AI Search Reference Architecture","Published",
  "https://iadb.leanix.net/IADBProduction/diagrams/freedraw/be67338a-33a5-49cb-95ed-13360102ff0e",""),
 ("Reference architecture","RA-04","Azure Document Intelligence Reference Architecture","Published",
  "https://iadb.leanix.net/IADBProduction/diagrams/dataflow/6379d8b3-20c7-421e-a555-8ba35e9e2b6e",""),
 ("Reference architecture","RA-05","Foundry Agents Reference Architecture","Pre-release","",
  "PRE-RELEASE. The second of the two steps to readiness 4 for agent provisioning."),
 # ---- templates -------------------------------------------------------
 ("Template","TPL-01","MCP Server Template v1 (C# / .NET)","In use","",
  "Built by EA, shared with the AI MVP team. Used to build all custom MCP servers on that project and "
  "serves as the blueprint for other teams. Implements the SUPERSEDED MCP specification."),
 ("Template","TPL-02","MCP Server Template v2 (C# / .NET)","Built, not yet distributed","",
  "Implements the MCP specification released July 2026. To be shared across the organization. "
  "Every server built from v1 needs a migration plan inside the deprecation window."),
 # ---- IaC modules -----------------------------------------------------
 ("IaC module","IAC-01","Container App Environment","In review by DX",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/16",
  "PR open. Not yet published by DX."),
 ("IaC module","IAC-02","Container Apps","Published (JFrog)",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/17",""),
 ("IaC module","IAC-03","Container Registry","In review by DX",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/15",
  "PR open. Not yet published by DX."),
 ("IaC module","IAC-04","Foundry Account","Published (JFrog)",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/18",""),
 ("IaC module","IAC-05","Foundry Project","Published (JFrog)",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/19",""),
 ("IaC module","IAC-06","AI Search (fix)","Published (JFrog)",
  "https://github.com/dx-developer-platform/terraform.az-iac-core-modules/pull/20",""),
]

# realization id -> asset ids
ASSET_LINK = {
 "REAL-001": ["STD-03","RA-02","IAC-04","IAC-05"],
 "REAL-002": ["STD-03","STD-07","RA-02","RA-05","IAC-04","IAC-05","IAC-02","STD-06"],
 "REAL-003": ["STD-02","RA-01","TPL-01","TPL-02","IAC-02","IAC-01","IAC-03"],
 "REAL-004": ["STD-04","RA-03","IAC-06"],
 "REAL-005": ["STD-04","RA-03"],
 "REAL-006": ["STD-05","RA-04"],
 "REAL-007": ["STD-01"],
 "REAL-008": ["STD-06"],
}
