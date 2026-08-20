#!/usr/bin/env python3
from pathlib import Path
import re,yaml
R=Path(__file__).resolve().parents[1];s=(R/"SKILL.md").read_text(encoding="utf-8")
if not s.startswith("---\n"):raise SystemExit("FAIL: frontmatter")
fm=yaml.safe_load(s.split("---",2)[1])
if fm.get("name")!="genealogy-evidence-auditor":raise SystemExit("FAIL: name")
refs=set(re.findall(r"`((?:references|assets|scripts|evals)/[^`]+)`",s))
missing=[x for x in refs if not (R/x).exists()]
if missing:raise SystemExit("FAIL missing: "+",".join(sorted(missing)))
for q in ["20 Knowledge/Claims/","20 Knowledge/People/","20 Knowledge/Sources/","90 Inbox/","GEDCOM","Selby / Shelby","schema-drift-and-integrity.md"]:
    if q not in s:raise SystemExit("FAIL rule: "+q)
print("PASS: v5 skill structure")
print("Referenced resources:",len(refs))
