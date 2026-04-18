---
name: "analytics"
description: "Design tracking schemas, audit event implementations, and define KPIs."
risk: low
source: internal
date_added: '2026-04-18'
---

# Analytics Command

This command invokes the **analytics-architect** to ensure the project has high-fidelity data tracking.

## What This Command Does

1. **Schema Design** - Defines event names and properties (PostHog/Segment).
2. **Implementation Audit** - Scans code for missing track calls.
3. **KPI Definition** - Aligns technical events with business goals.

**Note**: Powered by the `analytics-tracking` skill.
