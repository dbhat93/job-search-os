## Date Handling Module (Always Active)

**Never infer a date from memory or context. Always compute via Bash before writing.**

Before writing ANY date-sensitive content into coaching_state.md or any output surface (prep brief, thank-you, calendar invite, cheat sheet, timeline, interview schedule):

1. If writing today's date or day-of-week: `date "+%A, %B %d, %Y"`
2. If writing a specific calendar date and you need the day-of-week: `date -j -f "%Y-%m-%d" "YYYY-MM-DD" "+%A, %B %d"`
3. If computing a future date (e.g., "3 business days from now"): compute via Bash, never via mental arithmetic.

**Why**: a wrong date in an interview schedule causes a missed interview. Date drift is the single highest-cost error class in this system. The rule applies mid-session (dates written hours into a long session can drift if computed from memory), not just at session start.

**Integration**: every command that writes a date into coaching_state.md or into user-facing output MUST invoke the relevant Bash check before writing. See references to this module in: `COACH.md` (Mandatory Rules), `round.md` (next round dates, round timestamps), `prep.md` (Date researched, interview schedule), `feedback.md` (outcome dates, rejection dates), `debrief.md` (interview date/time), `hype.md` (timeline calibration), `thankyou.md` (follow-up deadlines), `research.md` (Last updated), `sync.md` (stale-entry detection), `salary.md` (offer deadline computation), `map.md` (days-until calculations), `strategy.md` (2-week plan dates), `apply.md` (application deadline tracking). 

---
