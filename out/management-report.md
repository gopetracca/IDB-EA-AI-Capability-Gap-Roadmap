# AI capability — management report

**Inter-American Development Bank** · 2026-09-10

---

## 1 · What this report can and cannot say

Read this section before the findings. It states the coverage of the assessment so that nothing below is read as more than it is.

| | |
|---|---|
| Capabilities in the map | 56 |
| **Rated** | **10** |
| Not yet rated | 46 |
| Platform offerings with evidence | 7 |
| Assets recorded, with status and location | 20 |

> 10 of 56 capabilities carry a rating. The remainder are not zero — they are unobserved, and are shown as such throughout.

---

## 2 · What the institution has built

Every row below is backed by a named asset with a location and a status. This is the part of the picture that is **not** an opinion.

| Offering | What a delivery team gets | Assets released | Capabilities it enables |
|---|---|:-:|---|
| **Foundry platform** | Building blocks | 4 of 4 | `5.1`, `5.3`, `5.4` |
| **Foundry agents** | Building blocks | 6 of 8 ⚠ | `4.4`, `5.1`, `5.6`, `5.8` |
| **Custom MCP servers** | Reference implementation | 4 of 7 ⚠ | `4.5`, `5.5` |
| **Retrieval on AI Search** | Building blocks | 3 of 3 | `3.6` |
| **Document extraction** | Guidance | 2 of 2 | `3.5` |
| **Approved AI tech stack** | Guidance | 1 of 1 | `4.1`, `5.2` |
| **Agent design guidance** | Guidance | 1 of 1 | `2.2`, `2.5` |

**5 of 7 offerings are complete.** The other 2 are each waiting on named documents or modules, listed in section 4.

---

## 3 · The finding

> **The institution has built its enablers ahead of its practice.**

The scale used here — *Capability level* — places *performance* at Level 1, *tooling and competent people* at Level 2, and *an approved standard, applied* at Level 3. Measured that way, the institution has assembled a large part of its Level 2 and Level 3 apparatus — platforms, standards, reference architectures, infrastructure modules — while Level 1, whether the work is actually done, has been examined for 10 of 56 capabilities.

That is not a criticism of the build. It is the explanation for a disagreement that recurs in this institution: one person says the capability exists, meaning the platform and the standard exist, and another says it does not, meaning nothing is running on it. **Both are right about different things**, and a model carrying a single number cannot show that. This one shows it as four columns.

| What we can evidence today | What we cannot |
|---|---|
| 7 offerings, 20 assets, with locations | Whether any of it is used in production |
| Which capabilities have platform tooling (9), partial tooling (5), or none needed (16) | Whether tooling exists for the 24 nobody has yet examined |
| Which capabilities have an approved standard (9) or one in pre-release (3) | Whether work is done against them |
| Where a standard exists in the platform register | Whether the people who need the skills have them: 56 of 56 unobserved |

---

## 4 · What needs a decision

### 4.1 · Capabilities nobody owns

9 of 56 capabilities are claimed by no product or enabler in the institution's own catalogue. This is a finding about the operating model, not a gap in the model. Several are governance capabilities that an institution of this kind is normally expected to hold.

| ID | Capability | Domain |
|---|---|---|
| `1.5` | **AI Ecosystem & Alliance Management** | AI Strategy & Value Management |
| `2.3` | **AI Product Management** | AI Demand & Solution Shaping |
| `5.5` | **Tool & Connector Catalog Management** | AI Platform & Infrastructure |
| `6.3` | **Continuous Evaluation, Drift & Quality Management** | AI Operations & Reliability |
| `6.7` | **Human Oversight Operations** | AI Operations & Reliability |
| `7.2` | **Responsible & Trustworthy AI Practice** | AI Governance, Risk, Security & Assurance |
| `7.5` | **Privacy & Data Protection for AI** | AI Governance, Risk, Security & Assurance |
| `7.6` | **Legal, Regulatory & Contractual Compliance for AI** | AI Governance, Risk, Security & Assurance |
| `7.9` | **AI Impact Assessment & Risk Classification** | AI Governance, Risk, Security & Assurance |

**Decision required:** assign an owner to each, or record a deliberate decision not to hold it.

### 4.2 · Work that is finished but not released

5 assets exist and are not yet available to delivery teams. Each is days of work from being usable, and each currently holds a capability below the level the underlying work would support.

| Asset | What it is | Status |
|---|---|---|
| `STD-07` | Foundry Agents Standard | **Pre-release** |
| `RA-05` | Foundry Agents Reference Architecture | **Pre-release** |
| `TPL-02` | MCP Server Template v2 (C# / .NET) | **Built, not yet distributed** |
| `IAC-01` | Container App Environment | **In review by DX** |
| `IAC-03` | Container Registry | **In review by DX** |

**Decision required:** a release date for each, with a named owner.

### 4.3 · Questions only the platform teams can answer

**0 of 27 answered.** These decide whether a delivery team inherits its controls or rebuilds them. Every unanswered row is both an unknown and, once answered with a *no*, a roadmap item — usually a cheap one, because it means extending a module rather than building a platform.

| Offering | Questions outstanding |
|---|:-:|
| Foundry agents | 12 of 12 |
| Custom MCP servers | 6 of 6 |
| Retrieval on AI Search | 5 of 5 |
| Document extraction | 4 of 4 |

---

## 5 · What would make the next report say more

| Who | What is being asked of them | What it unlocks |
|---|---|---|
| Capability owners | For each L3 criterion under a capability they own: is this done on real AI systems, and where? | Every rating in the model. Nothing can be rated without it |
| Platform teams | The 27 in-the-box questions | Whether controls are inherited or rebuilt per team |
| Cybersecurity · Data Management · Legal · HR | Does an approved standard exist in your domain? | 40 capabilities currently show *unknown* because the asset register covers platform assets only |
| Learning & Development | Who is trained, and in what? | Level 2 for every capability where practice exists |

None of this requires new tooling or new investment. It requires four questions put to the people who already know the answers.

---

*Generated from the capability model. Scale: Capability level. Adapted from ISO/IEC 33020:2019 (process measurement framework). Simplified: four observations rather than five process attributes, three values rather than the standard's four-point N-P-L-F scale.*
