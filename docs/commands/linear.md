---
title: "/linear  Slash Command for AI Coding Agents"
description: "Project Management specialist. Converts PRDs into actionable Linear Epics and Issues.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /linear

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/linear.md">Source</a></span>
</div>


This command invokes the **product-manager** agent to manage the project roadmap and ticket lifecycle.

## What This Command Does

1. **Issue Mapping** - Deconstructs a PRD into atomic Linear tickets.
2. **Prioritization** - Sets P0/P1/P2 priorities based on business ROI.
3. **Sync** - (If Linear MCP active) Creates the tickets directly in your workspace.

## Example Usage

```
User: /linear Break down this authentication PRD into tickets.
```

---
**Note**: This command is powered by the `galyarder-framework:linear-ticket-management` skill.
