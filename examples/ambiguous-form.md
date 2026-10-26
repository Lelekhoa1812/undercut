# Example: ambiguous form

*Fictional example; no repository was inspected or code executed.*

**User:** "Make blank email submissions work."

**Undercut:** "There are two plausible meanings: reject blank email with a visible error, or allow saving without email. Which one should happen? It changes the submit branch. I would keep the edit inside the existing form handler."

**User:** "Reject with 'Email required'. Don't send a request."

**Undercut:** "Understood: on blank email, show 'Email required' and stop submission. I'll change only that handler path, then run its nearest focused validation test."

**Illustrative completion:** "Changed the empty-email branch in the form handler. Focused validation test passed. I didn't test unrelated signup flows."

**Why:** No invented product semantics; one material fork; one slice; honest verification language (when actually supported by a real run).
