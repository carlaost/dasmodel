#!/usr/bin/env bash
# Stop hook: at the end of each turn, ask Claude to run the research-manager skill
# to capture the turn into the ARA at research/ara/.
#
# Loop guard: when the hook itself caused the continuation (stop_hook_active=true),
# allow the stop so we don't loop forever.
input="$(cat)"
active="$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null)"

if [ "$active" = "true" ]; then
  exit 0
fi

if [ -f "$(dirname "$0")/.disabled" ]; then
  exit 0
fi

reason="Turn ending. Before you stop, invoke the research-manager skill to record this turn into the ARA located at research/ara/ . IMPORTANT: treat research/ara/ as the skill's 'ara/' root (substitute research/ara/ wherever the skill says ara/). The skill captures research-significant events only and skips empty/conversational turns — if there is nothing research-significant to record, say so in one line and stop. Do not start any new unrelated work."

jq -nc --arg r "$reason" '{decision:"block", reason:$r}'
exit 0
