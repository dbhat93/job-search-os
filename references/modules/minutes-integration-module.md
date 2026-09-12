## Minutes Integration Module

**Active when minutes is installed** (`~/meetings/` exists and contains files). Minutes is open-source local conversation memory that records meetings and voice memos to `~/meetings/` as plain markdown with structured YAML frontmatter. This module defines the shared querying patterns used by `round`, `outreach`, `progress`, and `hype`.

### Detecting minutes availability

Before any minutes query, silently check:

```bash
ls ~/meetings/*.md 2>/dev/null | head -1
```

If this returns nothing, skip the integration entirely. Do not prompt the candidate to install minutes.

### File naming and frontmatter

Minutes files are named: `YYYY-MM-DD-[title-slug].md`

Key YAML frontmatter fields:
- `title`: meeting or voice memo topic
- `date`: ISO datetime of recording (ISO 8601 with timezone offset)
- `duration`: human-readable duration (e.g. `92m 9s`)
- `status`: `complete`, `degraded`, or `processing`
- `processing_warnings`: array of failed steps (present when `status: degraded`)
- `type`: `meeting` or `voice_memo`
- `entities.projects`: extracted project/entity references

**Speaker identity (Minutes 0.15.0+):** Speaker names confirmed in the desktop, CLI, or MCP now propagate to all surfaces. If speakers have been confirmed, the transcript uses real names instead of `SPEAKER_0` / `SPEAKER_1`. Do not assume speaker labels are generic.

**Degraded transcript check (Minutes 0.18.0+):** Before using any transcript for analysis, read the `status` field. If `status: degraded`, surface to the candidate:
"This transcript has processing warnings: [list from `processing_warnings`]. Analysis may be incomplete or unreliable. Do you want to proceed anyway?"
Do not silently analyze a degraded transcript. Common causes: misrouted mic, silent recording, long idle tail. The `status: complete` check replaces the old pattern of inferring quality from transcript content alone.

**Sensitivity consent gate (Minutes 0.19.0+):** Minutes enforces `sensitivity: restricted` on its own agent surfaces (MCP tools and knowledge graph drop restricted meetings by default). This skill reads `~/meetings/` directly via `ls`/`grep`, which BYPASSES that enforcement, so the gate must be honored here manually:
- Before using any meeting file, check the frontmatter for a `sensitivity` field.
- If `sensitivity: restricted`: exclude the file from auto-detection lists, keyword searches, cross-loop pattern mining, and any output. Do not quote, summarize, or index its contents.
- The ONLY exception: the candidate explicitly names that specific file or meeting in the current session ("use the transcript from my restricted 1:1 yesterday"). Explicit naming is the logged override. Confirm once before proceeding: "That meeting is marked restricted in Minutes. Confirm you want me to read it for this analysis?"
- When a keyword search would have matched a restricted file, do not reveal its title or contents. At most: "[N] restricted meeting(s) matched and were excluded."
This mirrors Minutes' own consent contract: the human-readable markdown stays on disk, but agents do not read it without an explicit, per-use override.

### Querying by date

```bash
ls ~/meetings/2026-06-04*.md 2>/dev/null     # All files on a given date
```

Replace the hardcoded date with the computed date from the Date Handling Module.

### Querying by keyword (company name, person name)

Prefer the CLI search (FTS5-backed, fast on large archives):

```bash
minutes search "company name" 2>/dev/null
```

Fallback to grep only if minutes is not on PATH:

```bash
grep -irl "company name" ~/meetings/ 2>/dev/null
```

For recent files only, filter by the date prefix in the filename before grepping.

### Distinguishing meeting transcripts from voice memos

- **Meeting transcripts**: contain a `## Transcript` section with speaker-attributed dialogue
- **Voice memos**: shorter, narrative content, no `## Transcript` section

To identify voice memos: `grep -rL "## Transcript" ~/meetings/ 2>/dev/null`

### Integration points in this skill

| Command | Integration | What it does |
|---|---|---|
| `round` Phase 3 | Transcript auto-detect | Finds today's meeting transcript for the identified company and auto-loads into Mode A |
| `round` Phase 4 | Voice memo context | Finds voice memos recorded in the last 4 hours mentioning the company and pre-loads as debrief memory aids |
| `outreach` Step 1 | Networking call intelligence | Finds past meetings with the target person or company and uses them as personalization fuel |
| `progress` Step 5.6 | Cross-loop pattern mining | Finds meetings aligned with Interview Loop date ranges and surfaces patterns not yet in the Question Bank |
| `hype` Phase 0 | Calendar awareness | Finds recent notes mentioning upcoming interviews and surfaces missing prep briefs |
