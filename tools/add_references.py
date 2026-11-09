"""One-time patch: adds the Legal basis panel, report annex and Nov 2026 legal updates
to index.html. Safe to run once; it asserts each anchor exists exactly once.
Data itself is injected by tools/build.py from refs/references.json."""
import sys
p = sys.argv[1]; h = open(p, encoding="utf-8").read()

def rep(old, new):
    global h
    n = h.count(old); assert n == 1, (old[:70], n); h = h.replace(old, new)

# --- legal content updates (verified 2026-11-09) ---
rep("Data entered here is held only in this browser session and is not saved; it will be lost if the page is closed or refreshed. Print the Report before closing.",
    "Answers autosave in this browser. Use Save to file to keep a record or to move between computers; the file may contain personal data. Each stage has a Legal basis panel, and the Report ends with an annex of the references your answers rely on.")
rep("sensitive biometric categorization, real-time remote biometric ID for law enforcement.",
    "sensitive biometric categorization, real-time remote biometric ID for law enforcement. From 2 Dec 2026 also systems generating non-consensual intimate imagery or CSAM (Art. 5(1)(ba)–(bb), added by Reg. (EU) 2026/1744).")
rep("High-risk AI system: apply AI Act high-risk obligations (Stage 5).",
    "High-risk AI system: apply AI Act high-risk obligations (Stage 5). Annex III obligations apply from 2 December 2027 (Art. 113 as amended by Reg. (EU) 2026/1744).")
rep("FRIA REQUIRED (Art. 27 AI Act): complete the FRIA section in Stage 4 and notify the market surveillance authority of the results.",
    "FRIA REQUIRED (Art. 27 AI Act): complete the FRIA section in Stage 4 and notify the market surveillance authority of the results. Applies to Annex III systems from 2 December 2027; doing it now is good practice.")
rep('"Bias testing methodology (Art. 10 AI Act)"', '"Bias testing methodology (Arts. 10, 4a AI Act)"')
rep('"AI literacy and training (Art. 4 AI Act)"', '"AI literacy measures (Art. 4 AI Act, as amended)"')

# --- references component ---
comp = r'''function __Refs({N:n,t}){const L=(window.__REFS&&window.__REFS.references)||[],A=r=>r.triggers.some(x=>t[x]),K={law:"Legislation",case:"Case law",guidance:"Guidance",authority:"Supervisory decisions"},
It=r=>s.jsxs("li",{className:"ref-item",children:[s.jsx("span",{className:"ref-kind ref-"+r.kind,children:K[r.kind]}),s.jsx("a",{href:r.url,target:"_blank",rel:"noopener noreferrer",className:"ref-cite",children:r.cite}),s.jsx("div",{className:"ref-note",children:r.note}),r.check&&s.jsx("div",{className:"ref-check",children:"Check: "+r.check})]},r.id),
F=s.jsx("p",{className:"ref-foot",children:"Curated references, last verified "+((window.__REFS&&window.__REFS.version)||"—")+". Links go to EUR-Lex, CURIA, the AI Act Service Desk, EDPB, IMY and Riksdagen. Always read the source before relying on it."});
if(n===0)return null;
if(n===8){const a=L.filter(A);return s.jsxs("div",{className:"ref-annex border rounded-lg bg-white p-4 mb-4",children:[s.jsx("h3",{className:"font-semibold mb-1",children:"Annex: legal references relied on"}),s.jsx("p",{className:"text-xs text-gray-500 mb-2",children:a.length?"Provisions, case law and guidance linked to the answers, risks and measures in this assessment.":"Complete the stages to build the annex."}),Object.keys(K).map(k=>{const g=a.filter(r=>r.kind===k);return g.length?s.jsxs("div",{children:[s.jsx("h4",{className:"ref-h",children:K[k]}),s.jsx("ul",{className:"ref-list",children:g.map(It)})]},k):null}),F]})}
const st=L.filter(r=>r.stages.includes(n)),tr=st.filter(A),o=st.filter(r=>!A(r));
return s.jsxs("details",{className:"ref-panel no-print",open:tr.length>0,children:[s.jsxs("summary",{children:["Legal basis for this stage (",st.length,")",tr.length?" · "+tr.length+" linked to your answers":""]}),
tr.length>0&&s.jsxs("div",{children:[s.jsx("h4",{className:"ref-h",children:"Linked to your answers"}),s.jsx("ul",{className:"ref-list",children:tr.map(It)})]}),
o.length>0&&s.jsxs("div",{children:[s.jsx("h4",{className:"ref-h",children:tr.length?"Other references for this stage":"References for this stage"}),s.jsx("ul",{className:"ref-list",children:o.map(It)})]}),F]},n)}'''
rep("function __P(", comp + "function __P(")

ctx = ('s.jsx(__Refs,{N:N,t:(()=>{const t={prohibited:me==="yes",dpia:ie.code==="MAND"||ie.code==="REQ",imy:X==="yes",high:vt,fria:Ge,art36:Bt,'
       'limited:ke.startsWith("Limited"),tier:ke!=="",provider:K.includes("Provider"),auto:h.decisionRole==="Fully automated decision",'
       'c353a:Y[0]==="yes",c353b:Y[1]==="yes",c353c:Y[2]==="yes"};xe.forEach((v,i)=>t["crit"+(i+1)]=v);'
       'Ye.forEach(r=>t[r.id]=r.inh>0||r.res>0);we.forEach((v,i)=>t["m"+i]=v);return t})()}),Ur]})}tf.createRoot')
rep("Ur]})}tf.createRoot", ctx)

# --- data slot + styles ---
rep('<script type="module"', '<script>window.__REFS=/*REFS_START*/null/*REFS_END*/;</script>\n<script type="module"')
css = '''<style>
.ref-panel{border:1px solid var(--mist);border-left:3px solid var(--fjord);background:#fff;border-radius:4px;padding:10px 14px;margin:0 0 16px}
.ref-panel summary{cursor:pointer;font-weight:700;color:var(--fjord);font-size:14px}
.ref-h{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--sage);margin:12px 0 6px}
.ref-list{list-style:none;padding:0;margin:0}
.ref-item{padding:8px 0;border-top:1px solid var(--mist);font-size:13px}
.ref-kind{display:inline-block;font-size:10px;padding:1px 6px;border-radius:3px;margin-right:8px;background:var(--mist);color:var(--fjord);vertical-align:1px}
.ref-case{background:#F3E3D6;color:#A85A28}.ref-authority{background:#E6ECEA;color:#4F7A75}
.ref-cite{font-weight:700;color:var(--fjord);text-decoration:underline;text-decoration-color:var(--copper);text-underline-offset:2px}
.ref-note{color:var(--ink);margin-top:2px;line-height:1.4}
.ref-check{color:#A85A28;font-size:12px;margin-top:3px}
.ref-annex .ref-kind{display:none}
.ref-foot{font-size:11px;color:var(--sage);margin-top:10px}
@media print{.ref-annex a{color:inherit;text-decoration:none}.ref-annex a::after{content:" — " attr(href);font-size:9px;color:#4F7A75;word-break:break-all}}
</style>'''
rep('</head>', css + '\n</head>')
open(p, 'w', encoding="utf-8").write(h)
print("ok")
