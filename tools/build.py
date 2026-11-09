"""Inject refs/references.json into index.html and regenerate docs/LEGAL_REFERENCES.md.

Usage (from the repo root):  python3 tools/build.py
Edit refs/references.json, run this, commit both files.
"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "refs/references.json").read_text(encoding="utf-8"))

# 1. inject into the page
html = (root / "index.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
new, n = re.subn(r"/\*REFS_START\*/.*?/\*REFS_END\*/", lambda m: "/*REFS_START*/" + blob + "/*REFS_END*/", html, flags=re.S)
assert n == 1, "REFS markers not found exactly once"
(root / "index.html").write_text(new, encoding="utf-8")

# 2. human-readable review list
kinds = {"law": "Legislation", "case": "Case law", "guidance": "Guidance", "authority": "Supervisory decisions"}
stages = {1: "Screening", 2: "Scoping", 3: "Necessity", 4: "Risk", 5: "Mitigation", 6: "Residual/sign-off", 7: "Governance"}
md = [f"# Legal references\n\nLast verified: **{data['version']}**. Source of truth: `refs/references.json`.\n",
      "Items marked ⚠ need a follow-up check before you rely on the pinpoint or status.\n"]
for k, title in kinds.items():
    md.append(f"\n## {title}\n\n| Reference | What it covers | Stages | Check |\n|---|---|---|---|")
    for r in data["references"]:
        if r["kind"] != k: continue
        st = ", ".join(stages[s] for s in r["stages"])
        md.append(f"| [{r['cite']}]({r['url']}) | {r['note']} | {st} | {'⚠ ' + r['check'] if r['check'] else ''} |")
(root / "docs/LEGAL_REFERENCES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"Injected {len(data['references'])} references; wrote docs/LEGAL_REFERENCES.md")
