## Contact Network
| Name | Company | Role Type | Last Contact | Open Promises | Relationship Strength | Losing Touch |
|------|---------|-----------|-------------|---------------|----------------------|-------------|
| Rachael | DoorDash | Recruiter | 2026-03-31 | Send NDA | Strong | No |
| Sritulasi Edpuganti | Interface AI | HM | 2026-03-27 | -- | Medium | Watch (5 days) |
| Bruno Almeida | Plaid | Referral | 2026-03-20 | Follow up on referral status | Weak | Yes (11 days) |
```

**Role types:** Recruiter, HM, Interviewer, Referral, Networking, Mentor

**Relationship Strength calculation:**
- **Strong**: Contact within 7 days AND at least 2 prior interactions
- **Medium**: Contact within 14 days OR 1 prior interaction within 7 days
- **Weak**: Contact 14+ days ago OR only 1 interaction total
- **Losing Touch**: 3+ prior interactions AND last contact >14 days ago (for job search, the decay is faster than Minutes' 21-day threshold because search timelines are compressed)

**Promise Tracker (embedded in Contact Network):**
Open Promises column tracks commitments the candidate made TO contacts or contacts made TO the candidate. Examples:
- "Send thank-you note" (candidate to contact)
- "Provide feedback by Monday" (contact to candidate)
- "Follow up on referral status" (candidate to contact)
- "Schedule next round" (contact to candidate)

**Staleness rules (adapted from Minutes' 4-condition cascade):**
A promise is stale when ANY of these are true:
- Age > 7 days (compressed from Minutes' 21 days for job search urgency)
- 2+ new sessions since the promise was made and no update
- A stated deadline has passed
- No owner is assigned

**When to update:**
- `round` Phase 7: Add/update interviewer and recruiter entries
- `feedback`: Update contact entry with new interaction date + any promises
- `prep`: Add interviewer entries (from LinkedIn research)
- `sync`: Surface stale promises and losing-touch alerts
- `map`: Include top 3 stale promises in "This Week" if actionable
- `outreach`: Add networking contacts

**Integration with `map` priority check:**
Add to the priority check table:
| Stale promise exists (>7 days, actionable) | Surface in "This Week" as action item | Medium |

**Integration with `sync` drift check:**
Add to Step 3 (Temporal Drift Check):
- **Contact with open promise >7 days**: Surface: "You promised [Name] at [Company] you'd [action]. That was [N] days ago."
- **Losing-touch referral with active loop**: Surface: "You haven't been in touch with [Name] in [N] days. They referred you to [Company] which is still active."

---
