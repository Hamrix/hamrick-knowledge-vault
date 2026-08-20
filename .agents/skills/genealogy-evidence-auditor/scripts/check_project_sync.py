#!/usr/bin/env python3
from pathlib import Path
import argparse,re,json
W=re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FILES=["10 Projects/Aetheling Evidence Project/Project Index.md","10 Projects/Aetheling Evidence Project/Modern Selby Stafford Evidence State.md","10 Projects/Aetheling Evidence Project/Colonial Selby Source Facts 1701-1790.md"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("root");ap.add_argument("--json",action="store_true");a=ap.parse_args();r=Path(a.root).resolve()
    stems={}
    for p in r.rglob("*.md"):stems.setdefault(p.stem,[]).append(p)
    f=[]
    for rel in FILES:
        p=r/rel
        if not p.exists():f.append({"severity":"warning","path":rel,"issue":"state file missing"});continue
        for target in W.findall(p.read_text(encoding="utf-8")):
            if "/" not in target and not stems.get(Path(target).stem):f.append({"severity":"warning","path":rel,"issue":f"unresolved state link: {target}"})
    out={"findings":f};print(json.dumps(out,indent=2) if a.json else f"findings={len(f)}")
if __name__=="__main__":main()
