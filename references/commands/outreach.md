# outreach — Networking CRM

**Job:** *Make sure I'm not leaving referral leverage on the table.*

---

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `outreach view` | All contacts by company + status — who's been touched, who hasn't |
| `outreach add [contact]` | Add a contact to the networking CRM |
| `outreach prep [company]` | For an active pipeline opportunity, surface relevant contacts and draft outreach |
| `outreach followup` | Contacts with no activity in 7+ days — surface with recommended next action |

**Default (bare `outreach`):** Run `outreach view`.

---

## State File

Read from and write to `state/contacts.md`.

If `state/contacts.md` doesn't exist, offer to create it: "You don't have a contacts file yet. Want to add your first contact?"

---

## Contact Schema (`state/contacts.md`)

```markdown
# Contacts — Job Search Network
Last updated: [date]

## Active Contacts

| Name | Company | Role | Pronouns | Relationship | Status | Last Touch | Loop ID | Notes |
|------|---------|------|----------|-------------|--------|------------|---------|-------|
| [name] | [company] | [role] | unknown | [strength] | [status] | [date] | [COMPANY-00X or —] | [notes] |

## Closed Contacts (loop closed / search ended)
[Archive contacts when the related pipeline loop closes]
```

**Field definitions:**

- **Pronouns**: Default `unknown` until confirmed by explicit source (LinkedIn profile field, photo, or the person stating them). When unknown, `draft` uses first name only — no he/she/they.
- **Relationship**: `Direct` (know personally) / `2nd degree` (mutual connection) / `Warm intro available` (someone can introduce you) / `Cold` (no connection)
- **Status**: `Not contacted` / `Outreach sent` / `Response received` / `Meeting scheduled` / `Referred` / `No response`
- **Loop ID**: Cross-reference to `state/pipeline.md` — connects contacts to active interview loops

---

## `outreach view` — Full Contact Snapshot

### Logic

1. Read `state/contacts.md`.
2. Read `state/pipeline.md` — cross-reference active loops to surface which companies have contacts and which don't.
3. Sort by urgency: contacts tied to active Interviewing loops first, then Screening, then others.
4. Flag contacts with no activity in 7+ days (⚠️) who are tied to active pipeline loops.
5. Flag active pipeline loops with **no contact** at the company — these are referral gaps.

### Output Schema

```markdown
## Contacts Snapshot — [date]

### By Active Pipeline Loop

**[Company] — [Stage] | [Priority]**
- [Contact Name] ([Role]) — [Relationship] | Status: [status] | Last touch: [date]
- [Contact Name 2] — [Relationship] | Status: [status]
- ⚠️ [Contact Name] — No activity in [X] days. Recommended: [action]

[repeat for each active loop]

### Referral Gaps ⚠️
Companies in active pipeline with no contacts identified:
- [Company] — [Stage] | [Priority] → Action: search your network or run `outreach add`

### Contacts Without Active Loops
[Contacts in the CRM not tied to a current pipeline opportunity — may be warm connections to keep warm]

### This Week's Network Move
[One highest-leverage outreach action — specific and actionable]

**Next commands**: `outreach add [contact]`, `outreach prep [company]`, `draft [contact]`
```

---

## `outreach add [contact]` — Add a Contact

### Logic

Ask in sequence — one question at a time:

1. "What's their name?"
2. "What company are they at, and what's their role?"
3. "How do you know them? [Direct / 2nd degree / Warm intro available / Cold]"
4. "Is this tied to an active pipeline opportunity?" (optional — if yes, link Loop ID)
5. "Any notes — how you met, what they work on, anything that makes this outreach specific?"

**Pronouns:** Default to `unknown` in the record. Say: "I'm leaving pronouns as unknown — update this field when you confirm them, and `draft` will use first name only until then."

After collecting inputs, write the row to `state/contacts.md` and confirm:

```markdown
Added to contacts:
- Name: [name]
- Company: [company] | Role: [role]
- Relationship: [strength]
- Status: Not contacted
- Loop ID: [if linked]

**Next commands**: `draft [contact]` (draft outreach), `outreach prep [company]` (if in active loop)
```

---

## `outreach prep [company]` — Referral Prep for Active Loop

### Logic

1. Pull the pipeline entry for [company] from `state/pipeline.md` — stage, priority, next action.
2. Pull all contacts at [company] from `state/contacts.md`.
3. Pull the Interview Loop from `coaching_state.md` — what round, what format, what's coming.
4. Assess referral leverage:
   - **No contacts**: "You have no contacts at [Company]. Options: (1) search your LinkedIn network for 2nd-degree connections, (2) post in relevant Slack communities, (3) cold outreach to a PM at the company. I can draft any of these."
   - **Contact exists, not reached**: Surface contact + draft outreach.
   - **Contact exists, reached**: Surface relationship status + recommended next touch.
5. If drafting outreach, route to `draft [contact]` with company context pre-loaded.

### Output Schema

```markdown
## Referral Prep: [Company] — [Stage]

### Contacts at [Company]
| Name | Role | Relationship | Status | Recommended action |
|------|------|-------------|--------|--------------------|
| [name] | [role] | [strength] | [status] | [action] |

### Leverage Assessment
- Referral available: [Yes / No / Potential]
- Highest-leverage contact: [name + why]
- Recommended action: [specific next step]

### If no referral is available:
[Options: LinkedIn 2nd-degree search, cold PM outreach, Slack/community post — with a draft offered for each]

**Next commands**: `draft [contact]`, `pipeline update [company]`
```

---

## `outreach followup` — Stalled Contacts

### Logic

1. Read `state/contacts.md`.
2. Identify every contact where Last Touch is 7+ days ago and Status is not `Referred` or `No response`.
3. For each stalled contact, surface recommended next action based on status:

| Status | Default next action if stalled |
|--------|-------------------------------|
| Outreach sent | Follow up — brief, reference first outreach |
| Response received | Have you moved the conversation forward? Schedule or ask |
| Meeting scheduled | Have you prepped for it? Run `prep` or `stories` |

### Output Schema

```markdown
## Stalled Contacts ⚠️

**[Name] — [Company]** | Status: [status] | Last touch: [X] days ago
- Recommended: [specific action]
- `draft [contact]` to write the follow-up

[repeat for each stalled contact]

**No stalled contacts:** "Your network is moving."

**Next commands**: `draft [contact]`, `outreach view`
```

---

## Design Principles

**Referral-first.** Referrals don't happen by accident — they require a system. `outreach` is that system. The view surfaces gaps (active loops with no contacts) as loudly as it surfaces contacts.

**Don't manage relationships you don't have.** `outreach` tracks contacts you actually know or can reach. It doesn't generate cold leads or suggest people to contact based on keywords. The networking is human work; the tracking is the tool's job.

**Pronoun integrity.** Every contact starts as `unknown`. This is not a bug — it's a guardrail. Confirming pronouns is the candidate's job; the tool just enforces the discipline of not assuming.

**Cross-reference with pipeline.** A contact at a company you're not actively pursuing is low priority. A contact at a Dream company in Screening is urgent. The tool sorts accordingly.
