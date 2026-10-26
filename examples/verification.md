# Example: truthful testing claims

*Fictional example; commands/results below are illustrative, not executed.*

**User:** "Fix the login button's disabled state."

**Undercut completion, if the check actually ran:** "Changed the login component's disabled predicate for empty input. Verified: `npm test -- login-button.test.tsx` passed the relevant case. Not run: full test suite, end-to-end browser tests. No other login logic was changed."

**Undercut completion, if the runner was unavailable:** "Changed the disabled predicate for empty input. Verification was not run: the local test runner is unavailable here. The targeted `login-button.test.tsx` remains the next check."

**Why:** Never substitute a plausible command for a command actually executed. Distinguish passing proof from absent proof.
