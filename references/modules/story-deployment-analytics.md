## Story Deployment Analytics

Correlates story deployments with interview outcomes to identify which stories predict advances and which stories are underutilized.

**Data source:** Storybank (Use Count, Last Used, field notes) + Outcome Log (Result per round) + Score History (per-story scores when available)

**Metrics to compute (surfaced in `progress`):**

| Metric | Calculation | Why it matters |
|--------|-------------|---------------|
| **Deployment rate** | Use Count / total scored interviews | Stories with 0 deployments after 5+ interviews are either not relevant or actively avoided |
| **Advance rate per story** | Interviews where story was deployed AND candidate advanced / total deployments | S004 deployed 4x, advanced 3x = 75% advance rate. That's signal. |
| **Deployment diversity** | Unique stories deployed / total story deployments across all interviews | Low diversity = over-reliance on 1-2 stories. High diversity = healthy rotation. |
| **Unused high-strength stories** | Stories with Strength 4+ and Use Count 0 | These are ready weapons that aren't being fired. |

**Output (in `progress` Storybank Health section):**
```
Story Deployment Analytics:
- S004 (Consortium Hash): Deployed 4x, advanced 3x (75%). Your strongest signal story.
- S003 (AI Agents): Deployed 3x, advanced 2x (67%). Consistent performer.
- S002 (Regulator's Question): Strength 4, never deployed live. Unused weapon.
- S010 (IDV Kill): Strength 4, never deployed live. Unused weapon.
- Deployment diversity: 5 unique stories / 12 total deployments = 42%. Could be higher.
```

**Integration:**
- `progress`: Add "Story Deployment Analytics" subsection to Storybank Health.
- `prep`: When mapping stories to predicted questions, note advance rate: "S004 has a 75% advance rate when deployed. Consider leading with it."
- `stories`: Surface unused high-strength stories as deployment candidates.

---
