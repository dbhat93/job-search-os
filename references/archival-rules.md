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
