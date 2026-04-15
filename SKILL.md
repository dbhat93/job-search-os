---
name: coach
description: >
  Interview coaching system. Activates for any coaching command: kickoff, map, prep, mock, round, analyze, stories, practice, progress, debrief, feedback, reflect, research, decode, salary, negotiate, hype, pitch, resume, linkedin, outreach, present, concerns, questions, thankyou, sync, strategy, help.
metadata:
  author: dbhat93
  version: "4.1"
  license: MIT
---

The interview coaching system is now active.

**Base directory**: ${CLAUDE_SKILL_DIR}
**Coaching state**: ${CLAUDE_SKILL_DIR}/coaching_state.md

When loading any reference file (e.g. `references/commands/map.md`), resolve it as an absolute path under `${CLAUDE_SKILL_DIR}/`.

!`cat ${CLAUDE_SKILL_DIR}/COACH.md`
