# One slice at a time

Even when the request describes a whole feature, implement the smallest independently meaningful, accepted vertical slice first.

1. State the slice and a concrete acceptance example.
2. Identify what is **out** of scope in this slice.
3. Ask only the questions needed for it.
4. Implement, verify locally, and report.
5. Continue to the next already-authorised, unambiguous slice; otherwise ask before expanding.

A vertical slice traverses the minimum end-to-end paths needed for one observable behavior. Do not build every layer upfront. Do not demand a large design document or test plan before simple code.

When sequencing work across many slices, maintain a tiny checklist with `todo / doing / done / blocked` and evidence only if actually useful; do not build a project-management bureaucracy.

Do not conflate "one at a time" with refusing a clear multi-step request. Complete authorised low-risk slices sequentially without redundant permission prompts; only stop at a genuine decision boundary.
