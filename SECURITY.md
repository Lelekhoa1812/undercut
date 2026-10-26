# Security policy

Undercut has no remote service, model endpoint, or telemetry. Its optional installer and validators execute locally with the current user's filesystem privileges.

## Reporting

If this project is published, use GitHub's **private vulnerability reporting** feature if enabled for the repository. If it is not enabled, contact the owner through an established private channel rather than publishing exploit details or credentials. No response time or disclosure SLA is implied.

Include the affected file/version, steps to reproduce with **non-sensitive** sample data, and the impact. Never include real credentials, private customer data, or exploit payloads targeting third parties.

## Scope

Potential issues include unsafe installer path handling, unintended destructive writes, injection through packaged scripts, or instructions that encourage bypassing security and data safeguards. Avoid speculative blanket claims that a text skill enforces security on the host agent.
