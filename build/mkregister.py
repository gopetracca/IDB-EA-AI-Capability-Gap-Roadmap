# -*- coding: utf-8 -*-
import io, json
_n={}; exec(io.open('catalog4.py',encoding='utf-8').read(),_n); S=_n['S']
M=json.load(open('model3.json'))
L2NAME={c[0]:c[1] for d in M for c in d[3]}
L3TOL2={x[0]:c[0] for d in M for c in d[3] for x in c[4]}

STATES=[
 {"n":0,"k":"Nothing","d":"No approved technology, no reusable asset, no service.",
  "ev":"—","who":"—"},
 {"n":1,"k":"Project-proven","d":"One team built it and it works. Not separable from their application, not reusable.",
  "ev":"The application itself","who":"That team"},
 {"n":2,"k":"Approved technology","d":"A technology is cleared for use. Each team assembles the solution itself.",
  "ev":"The approval record","who":"Consumer"},
 {"n":3,"k":"Paved road","d":"Published pattern plus a reusable, developed solution building block. Teams self-serve a compliant instance and operate it.",
  "ev":"The standard, the module or template repository, and a team that used it","who":"Consumer, on the platform's rails"},
 {"n":4,"k":"Managed service","d":"An exposed endpoint with a contract. Consumers call it; the platform operates it.",
  "ev":"The endpoint, its service levels, its operational owner, its consumers","who":"Platform"},
]

# The inheritance checklist for a paved road: which building blocks come IN THE BOX,
# inherited by every instance, versus left to each consuming team.
BOX=[
 ["identity","Distinct workload identity per instance, not a shared service principal","S6.9","7.4.4"],
 ["registry","Automatic registration in the AI system / agent inventory","S6.6","7.7.2"],
 ["tracing","Tracing and tool-call logging enabled by default","S9.1","6.2.2"],
 ["guardrails","Content filtering and safety controls on by default","S7.1","7.4.6"],
 ["injection","Prompt-injection defence configured","S7.4","7.4.3"],
 ["eval","Evaluation harness scaffolded in the template","S8.15","4.6.3"],
 ["cost","Cost attribution tags applied automatically","S9.4","6.5.1"],
 ["stop","A tested way to stop it and revoke its access","S7.13","6.4.2"],
 ["secrets","Credential issuance and rotation handled by the platform","S6.9","5.2.4"],
 ["network","Network isolation and private connectivity baseline","S8.20","5.3.3"],
 ["hitl","A hook for human approval of consequential actions","S5.10","2.5.2"],
 ["retention","Interaction log retention configured to policy","S9.2","3.1.4"],
]

services=[{
 "id":"SVC-001",
 "name":"Agent Runtime Provisioning",
 "catalog_ref":"S5.1",
 "state":3,
 "provides":"A compliant agent runtime environment, provisioned on demand to the published institutional standard.",
 "not_provided":"The agent itself: business rules, grounding data, evaluation criteria, human oversight design. Those remain with the delivery team.",
 "realizes":["5.1.2","5.6.1","4.1.2"],
 "pattern":"Internal standard for Foundry deployment; internal standard for building agents",
 "sbb":"Terraform modules and template repositories — developed in-house, not procured",
 "offerings":["Microsoft Foundry"],
 "operated_by":"Consumer — each team deploys and runs its own instance",
 "consumers":"",
 "evidence":["The published deployment standard","The published agent build standard",
             "The Terraform module repository","The template repositories"],
 "box":{k[0]:None for k in BOX},
 "owner":"AI Platform Owner",
 "asof":"",
 "note":"State 3 is arguably the correct TARGET for agent provisioning, not a way-station — agents are per-use-case by nature. The improvement path is enriching what comes in the box, not moving to state 4."
}]

seq=2
for g in S:
    for s in g[4]:
        if s[6]!="SVC": continue
        caps=sorted({L3TOL2.get(r,r) for r,_ in s[4]})
        services.append({
         "id":"SVC-%03d"%seq,"name":s[1],"catalog_ref":s[0],"state":None,
         "provides":s[2],"not_provided":"","realizes":caps,"pattern":"","sbb":"",
         "offerings":[],"operated_by":"","consumers":"","evidence":[],
         "box":{},"owner":"","asof":"","note":"Candidate — confirm whether this exists at IDB and at what state.",
         "candidate":True,"group":g[0],"ambiguous":bool(s[11])})
        seq+=1

json.dump({"scale":STATES,"box_checklist":BOX,"services":services},
          open('register.json','w'), ensure_ascii=False, indent=1)
pop=[s for s in services if s["state"] is not None]
print("register rows:",len(services),"| populated:",len(pop),"| candidates:",len(services)-len(pop))
# capability delivery state = max state of services realizing it
st={}
for s in services:
    if s["state"] is None: continue
    for c in s["realizes"]:
        c2=L3TOL2.get(c,c)
        st[c2]=max(st.get(c2,-1),s["state"])
print("capabilities with a known delivery state:",{k:v for k,v in sorted(st.items())})
print("box items awaiting confirmation:",len(BOX))
