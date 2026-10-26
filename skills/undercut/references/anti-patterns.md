# Anti-patterns and corrections

| Failure | Undercut correction |
| --- | --- |
| Guessing expected behavior | Ask about the observable fork and wait for the decision |
| Asking 20 broad questions before looking at code | Inspect the local path; ask every material question for the current slice, no more |
| Asking about facts the repo already documents | Quote verified source; proceed |
| "While I am here" refactor | Exclude unrelated improvements explicitly |
| Installing new dependencies for a tiny utility | Use existing dependencies or standard library if fit for purpose |
| Building an abstraction for one case | Keep simple local code until multiple real uses require generality |
| Full suite after a local typo | Run the relevant content/path check |
| No meaningful test after a logic change | Execute at least one focused check, or disclose inability |
| Broad rewrite for one broken input | Reproduce that input and fix its branch |
| Silently deciding risky product semantics | Ask approval before code or external side effects |
| Testing narrowly despite changed shared security contracts | Expand verification because evidence/risk demands it |
| Over-selling confidence | Name exact evidence and what was not checked |
| Treating "junior" as permission for bad code | Preserve reliability, safety, and real contracts |
| Constantly asking permission for every trivial edit | Continue on authorised, reversible, unambiguous steps |
