# undercut

**The junior developer who asks first, writes less, and tests what changed.**

*A portable Agent Skill for deliberately unassuming software work.*

```text
      UNDERCUT
      question → smallest slice → smallest edit → focused proof
      no mind-reading • no architecture theatre • no fake confidence
```

Undercut teaches a coding agent to approach work like an inquisitive junior developer: openly admit what is not known, clarify **material** choices, inspect only the relevant code, choose the smallest reasonable fix, and verify the exact behavior being changed. It deliberately resists speculative architecture, sprawling implementations, mandatory full-suite testing for every tiny change, and unrequested cleanup.

**Underconfident in assumptions. Disciplined in execution.** This is a work style—not permission to produce broken code, skip required security controls, or misrepresent test coverage.

## In 30 seconds

**Ask your agent:**

> Use undercut for this task. Assume you don't know the product. Ask precise questions for decisions that affect behavior. Find the smallest existing place to implement one slice. Test just that slice, expanding only when risk or coupling requires it. Never invent an answer.

**Install into your project:**

```bash
# Run from the downloaded/cloned undercut repository
python3 scripts/undercut.py install --agent codex --scope project --project /path/to/your-repo
```

This installs the skill at `/path/to/your-repo/.agents/skills/undercut/SKILL.md`. The installer does not change your codebase, alter existing agent instructions, or fetch dependencies. See [Installation](docs/INSTALLATION.md) for individual tools and user-global scopes.

## Philosophy in five moves

| Step | Undercut does | Undercut does not |
| --- | --- | --- |
| **1. Question** | Clarifies the first behavior-changing unknown | Guesses requirements or asks broad ritual questions |
| **2. Slice** | Defines one observable behavior and a boundary | Plans an entire platform to fix one issue |
| **3. Change** | Makes a minimal local edit consistent with the repository | Introduces frameworks, layers, or unrelated rewrites |
| **4. Check** | Runs a focused, relevant proof and records the result | Claims the full repo is verified or skips mandatory high-risk checks |
| **5. Report** | States facts, uncertainty, and the next step | Announces unearned certainty or invents completion |

### Example

**User:** "Fix the form; blank submissions are broken."

**Undercut:** "I found the submit handler, but I can't tell whether a blank submission should be blocked with an error or saved as a draft. Which behavior do you want? That changes the validation branch."

**User:** "Show 'Required field' and don't submit."

**Undercut:** "I'll change only the blank-value branch and run the form's closest validation test."

**Completion:** "Changed the blank-value branch in the submit handler. The targeted validation test passes. I did not run unrelated suites; other validation rules are untouched."

This sample illustrates expected *language*; it is not a claim about an actual application or a test that has been executed.

## Behaviors you can rely on

- **Curious, not clueless.** Asks what the specification actually means; still reads the code before asking questions the repository already answers.
- **Questions only at meaningful forks.** A high-value, contextual question should determine a real coding choice. Minor reversible details should follow existing project conventions.
- **Anti-overengineering.** Reuse code before adding new code; add minimal new code before adding structure; do not pre-build hypothetical future requirements.
- **Sequential work.** One accepted behavior at a time. Do not build all the layers or features simultaneously. Follow through on already-authorised slices without asking redundant approval.
- **Local evidence.** Exact command, exact relevant test or manual reproduction, honest result; expand checks for risk, shared coupling, or repository policy.
- **Clear stop conditions.** Material ambiguity or unsafe shortcuts are blockers, not invitations to make assumptions.

## Install and compatibility

The canonical skill lives at [`skills/undercut/SKILL.md`](skills/undercut/SKILL.md). It follows the [Agent Skills specification](https://agentskills.io/specification): YAML metadata, an instruction file, and optional on-demand references.

| Agent | Recommended project target | Notes |
| --- | --- | --- |
| **Codex** | `.agents/skills/undercut/` | Native repository skill discovery |
| **Cursor** | `.agents/skills/undercut/` | Also supports `.cursor/skills/undercut/` |
| **Claude Code** | `.claude/skills/undercut/` | Explicit Claude path is simplest to reason about |
| **GitHub Copilot** | `.github/skills/undercut/` | Also supports `.agents/skills/` in supported hosts |
| **Gemini CLI** | `.gemini/skills/undercut/` | Also supports `.agents/skills/` alias |
| **Other Agent Skills tools** | Tool-specific discovery path | Follow the host's documentation |

Run:

```bash
# Portable shared location: Codex (also discovered by other compatible hosts)
python3 scripts/undercut.py install --agent codex --scope project --project /path/to/repo

# Claude Code-specific
python3 scripts/undercut.py install --agent claude --scope project --project /path/to/repo

# Preview without writes
python3 scripts/undercut.py install --agent cursor --scope user --dry-run

# Replace an existing Undercut install, after inspecting local changes
python3 scripts/undercut.py install --agent codex --scope project --project /path/to/repo --force
```

Installing duplicate copies under multiple discovery paths can make the skill appear multiple times. Prefer **one canonical installed copy per project**; see [Compatibility](docs/COMPATIBILITY.md) and [Installation](docs/INSTALLATION.md).

## Safety rule, not an escape hatch

Undercut's testing discipline means **narrow verification proportionate to the change**. Authentication, authorization, payment, destructive operations, sensitive data, shared contracts, and required CI may need broader checks. Do not bypass tests or protection to keep the task "simple." See [Risk boundaries](skills/undercut/references/risk-boundaries.md).

## What's in this repository?

```text
skills/undercut/
  SKILL.md                Canonical skill: concise executable operating contract
  references/             Questioning, minimal-change, testing, debugging, risks
  assets/                 Optional communication patterns
docs/                     Installation, compatibility, design, maintenance
examples/                 Worked conversations covering everyday and risky tasks
evaluation/               Human review rubric and scenario catalog
scripts/                  Standard-library installer and offline validators
tests/                    Focused contract and installer tests
.github/                  CI and contribution workflow
```

Everything is static files or Python standard-library scripts. **No model API, telemetry, credentials, background services, or external dependencies.** The repository is a skill pack—not an autonomous runner or claim of behavioral guarantees across every model. Results still depend on the host agent's instruction hierarchy and tools.

## Documentation

- [Install / update / remove](docs/INSTALLATION.md) · [Agent compatibility](docs/COMPATIBILITY.md)
- [Design principles](docs/DESIGN.md) · [Question decision guide](docs/asking-questions.md)
- [Verification boundaries](docs/testing-strategy.md) · [Security posture](SECURITY.md)
- [Worked examples](examples/README.md) · [Evaluation](evaluation/README.md)
- [Maintainer guide](docs/MAINTENANCE.md) · [Roadmap / non-goals](docs/roadmap.md) · [FAQ](docs/faq.md)

## Validate the pack

```bash
python3 scripts/undercut.py check
python3 -m unittest discover -s tests -v
```

Validation checks actual paths, metadata, link targets, installer behavior, and scenario structure. It is **not** an automated guarantee that an LLM will behave as intended; the evaluation cases require a human or explicitly configured model harness.

## Contributing

Keep contributions small, factual, testable, and aligned with the purpose. See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md). When suggesting new behaviors, provide a before/after transcript that proves the benefit; avoid turning the pack into a larger process framework.

## License

No open-source license has been selected or granted in this initial package. The repository owner must choose and add a license before representing this as openly reusable software. See [Licensing decision](docs/licensing.md).
