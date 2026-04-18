# LLM Format Output Reference

## Overview

The `--format llm` output is a compact, token-optimized hybrid XML/text format designed specifically for AI agent consumption. It provides structured audit data in a format that balances machine readability with token efficiency.

## Key Characteristics

- **40-70% smaller** than verbose XML format
- **1-space indentation** for minimal token usage
- **Hybrid structure**: XML tags + text prefixes for metadata
- **Inline attributes**: Metadata stored as XML attributes, not nested elements
- **Comma-separated lists**: Pages and arrays formatted inline
- **Flattened hierarchy**: Reduced nesting depth compared to verbose XML

## Format Structure

### 1. Document Header

```xml
<?xml version="1.0" encoding="UTF-8"?>
<audit version="0.0.24">
```

### 2. Site Information

```xml
<site url="https://example.com" crawled="51" date="2025-01-18T10:30:00Z"/>
```

Attributes:
- `url` - Base URL audited
- `crawled` - Number of pages crawled
- `date` - ISO 8601 timestamp

### 3. Health Score

```xml
<score overall="85" grade="B">
 <cat name="Core SEO" score="92"/>
 <cat name="Technical SEO" score="88"/>
 <cat name="Content Quality" score="76"/>
</score>
```

Attributes:
- `overall` - 0-100 health score
- `grade` - Letter grade (A-F)
- Categories with individual scores

### 4. Summary

```xml
<summary passed="120" warnings="15" failed="8"/>
```

Attributes:
- `passed` - Number of passed checks
- `warnings` - Number of warnings
- `failed` - Number of failed checks

### 5. Issues Section

Issues are grouped by category with compact inline metadata:

```xml
<issues>
 <category name="Core SEO" errors="2" warnings="3">
  <rule id="core/meta-title" severity="error" status="fail">
   Missing or empty meta title tags
   Desc: Every page should have a unique meta title
   Fix: Add descriptive <title> tags to each page
   Pages (2): https://example.com/about, https://example.com/contact
   Items (2):
    - https://example.com/about
    - https://example.com/contact
  </rule>
  <rule id="core/meta-description" severity="warning" status="warn">
   Desc: Pages should have meta descriptions
   Fix: Add <meta name="description"> tags
   Pages (5): https://example.com/page1, https://example.com/page2, ...
  </rule>
 </category>
 <category name="Performance" errors="0" warnings="1">
  ...
 </category>
</issues>
```

#### Rule Structure

Each `<rule>` element contains:

**Attributes:**
- `id` - Rule identifier (e.g., `core/meta-title`)
- `severity` - `error`, `warning`, or `info`
- `status` - `pass`, `warn`, or `fail`

**Text Content (in order):**
1. **Message** (optional) - Human-readable issue summary
2. **Desc:** - Rule description (what's being checked)
3. **Fix:** - Recommended solution (how to fix)
4. **Pages (n):** - Comma-separated list of affected URLs
5. **Items (n):** - Dash-prefixed list of specific items with metadata

### 6. Items Format

### 7. Technical Integrity: The Karpathy Principles
Combat AI slop through rigid adherence to the four principles of Andrej Karpathy:

### 8. Corporate Reporting: The Obsidian Loop
Durable memory is mandatory. Every task must result in a persistent artifact:
- **Write Report**: Upon completion, save a summary/artifact to the relevant department in `docs/departments/` (e.g., `Engineering/`, `Growth/`).
- **Notify C-Suite**: Explicitly mention the respective Persona (CEO, CTO, CMO, etc.) that the report is ready for review.
- **Traceability**: Link the report to the corresponding Linear ticket.
1. **Think Before Coding**: Don't guess. **If uncertain, STOP and ASK.** State assumptions explicitly. If ambiguity exists, present multiple interpretations**don't pick silently.** Push back if a simpler approach exists.
2. **Simplicity First**: Implement the minimum code that solves the problem. **No speculative abstractions.** If 200 lines could be 50, **rewrite it.** No "configurability" unless requested.
3. **Surgical Changes**: Touch **ONLY** what you must. Every changed line must trace to the request. Don't "improve" adjacent code or refactor things that aren't broken. Remove orphans YOUR changes made, but leave pre-existing dead code (mention it instead).
4. **Goal-Driven Execution**: Define success criteria via tests-first. **Loop until verified.**
   - Multi-step tasks MUST use this syntax:
     1. [Step]  verify: [check]
     2. [Step]  verify: [check]

---
 2026 Galyarder Labs. Galyarder Framework.
