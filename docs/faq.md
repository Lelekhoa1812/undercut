# FAQ

### Is the agent supposed to be incompetent?

No. "Junior" means humble, curious, and unwilling to invent unknown requirements. It does not mean careless or incapable.

### Will it ask a question before every edit?

No. Only at material unresolved decisions for the next slice. Obvious typo fixes and repository-defined conventions can proceed without a question.

### Why not test the whole app?

Because local low-risk changes usually have a smaller useful proof. A shared contract or risky change can require broader validation. Truthful reporting is mandatory either way.

### Does it work on Claude, Cursor, and Codex?

The files follow the Agent Skills convention, and [compatibility](COMPATIBILITY.md) lists known discovery locations. Each host determines whether and when to activate a skill. Explicit invocation is the most reliable way to request the mode.

### Does Undercut override my repository's instructions?

No. It works within higher-priority rules and applicable existing project policies.

### Why is there no one-click magic installer?

Copying one folder is sufficient. The included standard-library script makes that copy repeatable and cautious, without a separate package manager.

### Why is there no GitHub repo link or license in this package?

A repository has not been published from this bundle, and licensing is a separate owner decision. See [licensing](licensing.md).

### Can I use it with a senior-developer skill?

Yes, but simultaneous contradictory instructions can produce mixed results. Invoke one operating mode for a task and make the desired precedence explicit.
