#!/usr/bin/env python3
"""Disk-driven tournament state machine. Prints, per artifact, the NEXT action to take.
Resumable: reads only the filesystem, no memory needed."""
import pathlib
ART = ["01_paper_manifest","02_claims","03_concepts","04_problem","05_experiments",
       "06_related_work","07_solution","08_exploration_tree","09_evidence","10_implementation","11_dataset"]
root = pathlib.Path(__file__).parent
def n(p): return len(list((root/p).glob("*.md"))) if (root/p).is_dir() else 0
done_total = True
for a in ART:
    props = n(f"{a}/proposals")
    s1 = (root/a/"critique_stage1.md").exists()
    imp = n(f"{a}/improved")
    s2 = (root/a/"critique_stage2.md").exists()
    launched=(root/a/".proposers_launched").exists()
    if s2:
        state="DONE"
    elif props < 4:
        state=(f"STAGE1 proposers running: {props}/4 (WAIT)" if launched
               else f"STAGE1 proposers: LAUNCH 4 (not started)"); done_total=False
    elif not s1:
        cl=(root/a/".stage1_launched").exists()
        state=("STAGE1 critique running (WAIT)" if cl else "STAGE1 critique: LAUNCH (4 proposals ready)"); done_total=False
    elif imp < 2:
        il=(root/a/".improvers_launched").exists()
        state=(f"STAGE2 improvers running: {imp}/2 (WAIT)" if il
               else "STAGE2 improvers: LAUNCH 2 (from stage1 winners)"); done_total=False
    elif not (root/a/".stage2_launched").exists():
        state="STAGE2 critique: LAUNCH (2 improved ready)"; done_total=False
    else:
        state="STAGE2 critique running (WAIT)"; done_total=False
    print(f"{a:22s} props={props}/4 s1={'Y' if s1 else '-'} imp={imp}/2 s2={'Y' if s2 else '-'}  -> {state}")
print("\nTOTAL DONE:", done_total, "| SUMMARY exists:", (root/"TOURNAMENT_SUMMARY.md").exists())
