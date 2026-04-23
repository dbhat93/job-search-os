---
name: coach
description: >
  Interview coaching system. Activates for any coaching command: kickoff, map, prep, mock, round, analyze, stories, practice, progress, apply, feedback, reflect, research, decode, salary, negotiate, hype, pitch, resume, linkedin, outreach, present, concerns, questions, thankyou, sync, strategy, help. Note: debrief is now merged into round (run round for all post-interview captures); debrief still works as an alias for backward compatibility.
metadata:
  author: dbhat93
  version: "4.3"
  license: MIT
---

The interview coaching system is now active.

**Base directory**: ${CLAUDE_SKILL_DIR}
**Coaching state**: ${CLAUDE_SKILL_DIR}/coaching_state.md

When loading any reference file (e.g. `references/commands/map.md`), resolve it as an absolute path under `${CLAUDE_SKILL_DIR}/`.

!`cat ${CLAUDE_SKILL_DIR}/COACH.md`
