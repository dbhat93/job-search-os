## Voice-Input Transcription Awareness Module

**Active when the candidate is dictating via voice-input tools (Wispr Flow, macOS dictation, mobile dictation).**

Voice-input tools produce predictable error classes that corrupt coaching state silently if not caught:

**Common error types:**
- **Proper noun phonetic drift**: "Schaefer" for "Shaffer", "Tulsi" for "Tulasi", "Cat" for "Kat", "Check R" for "Checkr". High-risk for Contact Network and Interview Intelligence.
- **Homophones where context expects the other**: "sync" vs. "sink", "role" vs. "roll", "prep" vs. "prepped" vs. "prepped-up", "their" vs. "there".
- **Company name artifacts**: "Unit 21" vs. "unit twenty-one", "Plaid" vs. "played", "Bill" (company) vs. "bill" (noun).
- **Number-word coupling**: "first" dropped from "first-transaction", "five" vs. "5", "65" vs. "six five" vs. "sixty five".
- **Punctuation drift**: sentences run together, missing commas, apostrophes dropped ("cant" for "can't").

**Detection heuristics:**
- Proper nouns with unusual spellings that don't match prior coaching state entries.
- Homophone substitutions that make the sentence parse oddly in context.
- Numbers spelled as words in a context where digits would be expected (e.g., ARR, metrics).

**Coach response:**
- Flag gently, don't correct silently: "Want to confirm, did you mean 'Shaffer Bond' (the Plaid Product Lead already in our state) or a different person?"
- Never write a flagged proper noun to Contact Network, Recruiter Feedback, or Interview Loops without confirmation.
- Bulk-flag once at the start of a long voice-input response if the candidate asks at top: "I'm using Wispr, forgive any errors," then note at the end: "I noticed two possible Wispr artifacts: '[X]' and '[Y]'. Confirm or correct?"

**Integration**: Referenced by `debrief`, `round` Phase 4 (story usage log, recruiter feedback capture), `feedback` Type D (post-session memory), `outreach` (recipient name drafting), `thankyou` (interviewer name in draft), `prep` (interviewer LinkedIn lookup). This module should run whenever the candidate's typed response contains voice-input indicators (explicit mention, long unpunctuated sentences, homophone drift).

---
