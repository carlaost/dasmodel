# Figure 6: The Live Research Manager session-boundary pipeline

- **Source**: Figure 6, §3 (The Live Research Manager)
- **Caption**: "The Live Research Manager operates at session boundaries: a three-stage pipeline (Context Harvester → Event Router → Maturity Tracker) distills each researcher–agent conversation into typed events that accumulate across ARA layers over time."
- **Screenshot**: ara_figure6.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: Top "Active Research Session" shows Researcher ↔ AI Agent loop over a long time horizon. A "Session-Boundary Pipeline" band contains three stages: Context Harvester → Event Router → Maturity Tracker. Bottom shows the "ARA Artifact" with its layers being written/updated, and a "Session briefing" surfaced back at the start of the next session.
- **Connections**: Session conversation feeds the Context Harvester; Event Router writes typed, provenance-tagged events into the appropriate ARA layers; Maturity Tracker promotes staged observations; artifact is read back to brief the next session (closing the loop).
- **Annotations**: Pipeline runs retrospectively at session close (silent during active research); provenance tags (user / ai-suggested / ai-executed / user-revised).
- **What it conveys**: The manager is a stateless, background, three-stage retrospective system; the artifact carries memory across sessions.
