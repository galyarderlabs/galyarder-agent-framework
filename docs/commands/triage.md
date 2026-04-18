---
title: "/triage  Slash Command for AI Coding Agents"
description: "Triage a bug or issue. Explore the codebase to find root cause, then create a fix plan.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /triage

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/triage.md">Source</a></span>
</div>


This command invokes the **triage-issue** agent to diagnose and plan a fix for a reported bug.

## What This Command Does

1. **Root Cause Analysis** - Traces the error to the source.
2. **Reproduction** - Attempts to create a minimal reproduction script.
3. **Fix Planning** - Drafts a TDD-based implementation plan to resolve the issue.

---
**Note**: This command is powered by the `galyarder-framework:triage-issue` skill.
