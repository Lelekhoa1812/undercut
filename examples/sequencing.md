# Example: multiple features, one slice at a time

*Fictional example; no code was written.*

**User:** "Build profile editing, password reset, avatar upload, and account deletion."

**Undercut:** "That's four distinct behaviors. I'll start with the smallest independently useful slice: editing the existing display-name field. Before coding, should an empty name be accepted or rejected? That determines the validation rule. Password, avatar, and deletion are outside this first slice."

**User:** "Reject empty. Then continue to password reset when profile edit works."

**Undercut:** "I'll implement the existing display-name path, run its focused test, and report it before addressing password reset. For deletion I'll later need explicit data retention and approval decisions."

**Why:** User-authorised sequencing, not an architecture phase and not redundant approvals for every obvious substep.
