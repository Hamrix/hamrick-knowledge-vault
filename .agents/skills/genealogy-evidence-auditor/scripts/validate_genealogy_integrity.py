#!/usr/bin/env python3
from pathlib import Path
import argparse,re,json
N={"confirmed","strong","moderate","weak","speculative","contradicted"}
def fm(t):
    if not t.startswith("---\n"):return {}
    p=t.split("---",2);d={}
    if len(p)<3:return d
    for l in p[1].splitlines():
        m=re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$",l)
        if m:d[m.group(1)]=m.group(2).strip().strip('"')
    return d
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root");ap.add_argument("--json",action="store_true");a=ap.parse_args();r=Path(a.root).resolve();f=[]
    for p in r.rglob("*.md"):
        rel=str(p.relative_to(r)).replace("\\","/")
        try:m=fm(p.read_text(encoding="utf-8"))
        except Exception as e:f.append({"severity":"error","path":rel,"issue":str(e)});continue
        if rel.startswith("20 Knowledge/Claims/") and "Template" not in p.name:
            if m.get("type")!="claim":f.append({"severity":"error","path":rel,"issue":"missing type: claim"})
            if m.get("confidence") and m["confidence"] not in N:f.append({"severity":"error","path":rel,"issue":"non-native confidence"})
            if m.get("last-reviewed") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}",m["last-reviewed"]):f.append({"severity":"warning","path":rel,"issue":"bad last-reviewed"})
        if rel.startswith("20 Knowledge/People/") and "Template" not in p.name and m.get("type")!="person":f.append({"severity":"error","path":rel,"issue":"missing type: person"})
        if rel.startswith("20 Knowledge/Sources/") and m.get("type")!="source":f.append({"severity":"error","path":rel,"issue":"missing type: source"})
    out={"errors":sum(x["severity"]=="error" for x in f),"warnings":sum(x["severity"]=="warning" for x in f),"findings":f}
    print(json.dumps(out,indent=2) if a.json else f"errors={out['errors']} warnings={out['warnings']}")
    raise SystemExit(1 if out["errors"] else 0)
if __name__=="__main__":main()
