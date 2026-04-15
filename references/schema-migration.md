# Schema Migration Check

After reading `coaching_state.md`, check whether it contains all sections and columns defined in the current schema (`references/coaching-state-schema.md`).

Coaching state files created with earlier versions of the skill may be missing newer fields. If any are missing, migrate silently:

- **Missing `Secondary Skill` column in Storybank**: Add the column to the table header. Leave existing rows blank for Secondary Skill. Note in Coaching Notes: "[date]: Storybank upgraded to include Secondary Skill tracking. Existing stories need secondary skills added during next `stories improve` session."
- **Missing `Use Count` column in Storybank**: Add the column to the table header. Initialize all existing rows to 0. The count will begin tracking from this point forward.
- **Missing `Calibration State` section**: Add the full section using the schema defined in `references/coaching-state-schema.md` (after Active Coaching Strategy). Initialize Calibration Status to "uncalibrated", Last calibration check to "never", Data points available to the count of entries in the Outcome Log. All tables start empty.
- **Missing `LinkedIn Analysis` section**: Add the section header with empty fields. Note in Coaching Notes: "[date]: LinkedIn Analysis section added. Run `linkedin` to populate."
- **Missing `Resume Optimization` section**: Add the section header with empty fields. Note in Coaching Notes: "[date]: Resume Optimization section added. Run `resume` to populate."
- **Missing `Positioning Statement` section**: Add the section header with empty fields. Note in Coaching Notes: "[date]: Positioning Statement section added. Run `pitch` to populate."
- **Missing `Outreach Strategy` section**: Add the section header with empty fields. Note in Coaching Notes: "[date]: Outreach Strategy section added. Run `outreach` to populate."
- **Missing `JD Analysis` section(s)**: No migration needed. JD Analysis sections are created per-JD when `decode` is run. Absence is normal.
- **Missing `Presentation Prep` section**: No migration needed. Created when `present` is run. Absence is normal.
- **Missing `Comp Strategy` section**: Add the section header with empty fields. Note in Coaching Notes: "[date]: Comp Strategy section added. Run `salary` to populate."
- **Missing `Anxiety profile` in Profile**: Add the field with value "unknown". It will be set during the next `hype` session.
- **Missing `Career transition` in Profile**: Add the field with value "none". If the candidate's resume suggests a transition, update during the next session.
- **Missing `Transition narrative status` in Profile**: Add the field with value "not started". Only relevant when Career transition is not "none".
- **Missing `Known interview formats` in Profile**: Add the field with an empty value. It will be populated by the Format Discovery Protocol during `prep` or `mock`.
- **Missing `Search Strategy` section**: No migration needed. Created when `strategy` is first run. Absence is normal.
- **Missing `Interview Intelligence` section**: Add the full section with empty subsections: Question Bank (empty table with columns: Date, Company, Role, Round Type, Question, Competency, Score, Outcome), Effective Patterns (what works for this candidate) (empty), Ineffective Patterns (what keeps not working) (empty), Recruiter/Interviewer Feedback (empty table with columns: Date, Company, Source, Feedback, Linked Dimension), Company Patterns (learned from real experience) (empty), Historical Intelligence Summary (empty). Note in Coaching Notes: "[date]: Interview Intelligence section added. Will be populated by `analyze`, `debrief`, and `feedback`."
- **`Signal` column renamed to `Hire Signal` in Score History**: If the Score History table header contains a `Signal` column (without the `Hire` prefix), rename it to `Hire Signal`. Leave all existing row data unchanged.
- **Interview Loops entries missing newer fields**: When reading existing Interview Loop entries for a company, check for missing fields: `Status`, `Round formats`, `Fit verdict`, `Fit confidence`, `Fit signals`, `Structural gaps`, `Date researched`. Add any missing fields with empty values. Set `Status` to "Interviewing" if the entry has rounds completed, or "Researched" if it has research data but no rounds.
- **Outreach log in non-table format**: When reading an Interview Loop entry that contains outreach data in prose or bullet-point format (not the canonical table), silently normalize it to the table format defined in `references/commands/outreach.md` (columns: Date | Contact | Channel | Attempts | Status). Preserve all existing data. Just restructure the presentation. This ensures `outreach` cadence tracking works consistently regardless of how the data was originally entered.

Run this migration silently. Do not announce schema changes to the candidate unless they affect immediate coaching recommendations.
