#!/usr/bin/env python3
import pathlib
ORDER = ["M14","M17","M18","M19","M48","M36","M30","M32","M64","M09"]
root = pathlib.Path(__file__).parent
def n(p): return len(list((root/p).glob("*.md"))) if (root/p).is_dir() else 0
def mk(m,x): return (root/m/x).exists()
done_all=True
for m in ORDER:
    exp=n(f"{m}/proposals"); c1=mk(m,"critique_c1.md")
    i2=n(f"{m}/improved_c2"); c2=mk(m,"critique_c2.md")
    i3=n(f"{m}/improved_c3"); c3=mk(m,"critique_c3.md")
    def L(x): return mk(m,x)
    if c3: st="DONE"
    elif exp<4: st=("cycle1 expanders RUNNING (WAIT)" if L(".exp_launched") else "cycle1: LAUNCH 4 expanders"); done_all=False
    elif not c1: st=("c1 critique RUNNING (WAIT)" if L(".c1_launched") else "cycle1: LAUNCH critique (pick 2)"); done_all=False
    elif i2<2: st=("cycle2 improvers RUNNING (WAIT)" if L(".imp2_launched") else "cycle2: LAUNCH 2 improvers"); done_all=False
    elif not c2: st=("c2 critique RUNNING (WAIT)" if L(".c2_launched") else "cycle2: LAUNCH critique"); done_all=False
    elif i3<2: st=("cycle3 improvers RUNNING (WAIT)" if L(".imp3_launched") else "cycle3: LAUNCH 2 improvers"); done_all=False
    elif not c3: st=("c3 critique RUNNING (WAIT)" if L(".c3_launched") else "cycle3: LAUNCH critique (pick 1 + qualify)"); done_all=False
    else: st="?"
    print(f"{m:5s} exp={exp}/4 c1={'Y' if c1 else '-'} i2={i2}/2 c2={'Y' if c2 else '-'} i3={i3}/2 c3={'Y' if c3 else '-'}  -> {st}")
print("\nTOP10 DONE:", done_all, "| SUMMARY:", (root/"TOURNAMENT2_SUMMARY.md").exists())
