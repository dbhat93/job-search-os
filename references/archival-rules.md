# Archival Rules

## Score History Archival

When Score History exceeds 15 rows, summarize the oldest entries into a Historical Summary narrative and keep only the most recent 10 rows as individual entries. The summary should preserve: trend direction per dimension, inflection points (what caused jumps or drops), and what coaching changes triggered shifts. Run this check during `progress` or at session start when the file is large. Apply the same archival pattern to Session Log when it exceeds 15 rows. Compress old sessions into a brief narrative, keep recent ones detailed. The goal is to keep the file readable and within reasonable context limits for months-long coaching engagements.

## Interview Intelligence Archival Thresholds

Check during `progress` or session start:

- **Question Bank**: 30 rows. Summarize questions older than 3 months into Historical Intelligence Summary, keep 20 recent.
- **Effective/Ineffective Patterns**: 10 entries. Consolidate to 3-5 summary patterns in Historical Intelligence Summary.
- **Recruiter/Interviewer Feedback**: 15 rows. Summarize older feedback into Company Patterns, keep 10 recent.
- **Company Patterns for closed loops** (Status: Archived or Closed). Compress to 2-3 lines.

## JD Analysis Archival Thresholds

Check during `progress` or session start:

- When JD Analysis sections exceed 10 entries, archive analyses for roles the candidate chose not to pursue (no corresponding Interview Loop entry, or Loop status is Closed/Archived). Compress archived analyses into a `Past JD Analyses` summary section preserving only: company, role, fit verdict, date. Keep full analyses only for active/recent decodes.
- Presentation Prep sections for completed interview rounds (corresponding Interview Loop round is past) can be compressed to 1-2 lines preserving: topic, framework used, key adjustment. Full sections only needed for upcoming or active presentations.

## Interview Loops Archival

Check during `progress`, `reflect`, or session start.

When an Interview Loop has `Status: Closed / Rejected / Withdrawn` AND the loop's last update timestamp is >30 days ago, compress the loop to a 3-5 line summary:
- Final round reached
- Outcome (rejected / withdrew / offer declined / offer accepted but took other role)
- One-line cause or learning (if captured in debrief or reflect)
- Date range of the loop (first touch to close)
- Link: "S### stories used" (story IDs only, full field notes already captured in Storybank)

Move compressed loops to a `## Past Interview Loops` section at the bottom of the file. Keep full-detail loops only for active and recently-closed (within 30 days).

Rationale: the Interview Loops section is unbounded as the search continues. One Loop entry averages 30 to 60 lines (rounds, stories used, concerns, interviewer intel, outreach log, fit verdict). Without archival, a 6-month search accumulates hundreds of lines of loop detail that's no longer actionable.

Also enforces the 30-day transcript retention rule in COACH.md Data Privacy section: when archiving a loop, strip any full interview transcript body from the loop entry before compression. Keep extracted question/score/pattern data only.
