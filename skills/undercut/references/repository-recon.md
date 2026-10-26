# Repository reconnaissance: the tiny map

Explore **just enough** to know where to make the next edit.

1. Read root-level agent or contribution instructions that govern the work (`AGENTS.md`, `CLAUDE.md`, relevant rules). They do not override higher-priority user/system instructions.
2. Find the code path for the requested behavior with a filename search, symbol search, or the existing test name.
3. Read the caller, implementation, and closest test **only as needed** to determine the contract.
4. Find the appropriate package manager / test command from manifest or repo docs; never guess.
5. Explain what is verified and what remains unknown. Stop exploring when the next minimal edit is clear.

Avoid reading an entire monorepo, generating elaborate architecture diagrams, or conducting a wholesale audit for a local change. Expand search only when the relevant path is genuinely not locatable.

If the user supplied a specific source-of-truth document, follow it for the affected question unless it conflicts with higher-priority requirements or demonstrably newer approved decisions. Do not invent missing policy.
