#!/bin/bash
# Keeps the Obsidian vault copy of the good-science metrics doc in sync with the repo file.
# Triggered by a launchd WatchPaths agent (com.desciencemodel.metrics-obsidian-sync)
# whenever the source file changes. Also runnable by hand.
SRC="/Users/carlaostmann/code/desciencemodel/metrics-directions.md"
DEST="/Users/carlaostmann/Documents/Documents - Carla’s MacBook Pro/obsidian_local/knowledge representation/desciencemodel - good-science metrics.md"
[ -f "$SRC" ] || exit 0
cp "$SRC" "$DEST"
