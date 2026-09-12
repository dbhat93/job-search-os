## Channel Benchmark Module

Channel choice (cold application vs. warm intro vs. direct outreach) is currently reasoned about qualitatively across this skill. This module gives the coach a directional baseline so channel-prioritization advice has a number behind it, not just instinct. Borrowed from mukeshbasvekar/Job-Search-OS channel-data pattern.

**Directional benchmarks** (industry-general, not candidate-specific, tag per the "No Number Without A Source" rule above):

| Channel | Interview Conversion | Decision-Maker Reach | Source Tier |
|---|---|---|---|
| Direct outreach to founder/HM | ~5-8% | ~67% reach a decision-maker | `[estimated]`, general cold-outreach job-search data, not a named study |
| Warm intro / referral | Varies widely by relationship strength | ~50% reach a decision-maker | `[estimated]` |
| Cold application (ATS) | ~1% | ~44% reach a decision-maker (rest filtered by ATS/recruiter screen) | `[estimated]` |

**How to use these:**
- These are priors, not predictions for this specific candidate. Once 3+ real outcomes exist per channel in this candidate's own Outcome Log, prefer the candidate's own observed conversion rate over the generic benchmark (see Funnel Stats in `progress.md`).
- Use to justify channel-prioritization advice with a number: "Cold ATS applications convert at roughly 1% industry-wide, that's the case for prioritizing the Trisha intro over the careers-page application."
- Never present these as the candidate's personal rate until their own data supports it. Always label as a general/directional benchmark when used before the candidate has their own data: "Industry-general benchmark, not your personal rate yet."
- Do not silently swap these out for the candidate's own funnel stats once available. Present both: "Industry-general direct-outreach conversion is ~5-8%. Yours so far is [X]% across [N] attempts."

**Integration:**
- `outreach`: When recommending channel for a target company, cite the relevant benchmark if no candidate-specific data yet exists.
- `strategy`: Channel allocation recommendations cite these benchmarks as the starting prior, replaced by Funnel Stats once available.
- `progress`: Funnel Stats section (see `progress.md`) computes the candidate's own per-channel rates and compares against these benchmarks once 3+ data points per channel exist.

---
