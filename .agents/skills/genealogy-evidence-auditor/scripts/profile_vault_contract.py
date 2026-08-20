#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,re,collections
GED={".ged",".gedcom"}
REQ=["00 System/ChatGPT Work Instructions.md","00 System/Vault Operating Manual.md","00 System/Tag Dictionary.md","10 Projects/Aetheling Evidence Project/Project Index.md","10 Projects/Aetheling Evidence Project/Vault-First Research Rules.md"]
def fm(t):
    if not t.startswith("---\n"): return {}
    p=t.split("---",2); d={}
    if len(p)<3:return d
    for line in p[1].splitlines():
        m=re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$",line)
        if m:d[m.group(1)]=m.group(2).strip().strip('"')
    return d
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root");ap.add_argument("--json",action="store_true");a=ap.parse_args();r=Path(a.root).resolve()
    out={"required":{},"policy_hashes":{},"frontmatter_keys":{},"confidence_values":[],"source_classes":[],"gedcom":{"count":0,"content_parsed":False}}
    keys=collections.defaultdict(set);conf=set();classes=set()
    for rel in REQ:
        p=r/rel;out["required"][rel]=p.exists()
        if p.exists():out["policy_hashes"][rel]=hashlib.sha256(p.read_bytes()).hexdigest()
    for p in r.rglob("*"):
        if not p.is_file():continue
        if p.suffix.lower() in GED:out["gedcom"]["count"]+=1;continue
        if p.suffix.lower()!=".md":continue
        try:m=fm(p.read_text(encoding="utf-8"))
        except:continue
        if m.get("type"):keys[m["type"]].update(m.keys())
        if m.get("confidence"):conf.add(m["confidence"])
        if m.get("source-class"):classes.add(m["source-class"])
    out["frontmatter_keys"]={k:sorted(v) for k,v in keys.items()};out["confidence_values"]=sorted(conf);out["source_classes"]=sorted(classes)
    material=json.dumps({k:out[k] for k in ("required","policy_hashes","frontmatter_keys","confidence_values","source_classes")},sort_keys=True).encode()
    out["schema_fingerprint"]=hashlib.sha256(material).hexdigest()
    print(json.dumps(out,indent=2) if a.json else out["schema_fingerprint"])
if __name__=="__main__":main()
