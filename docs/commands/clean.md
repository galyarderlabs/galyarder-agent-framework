---
title: "/clean  Slash Command for AI Coding Agents"
description: "Dead code cleanup and consolidation specialist. Removes unused code, duplicates, and refactors for maintainability.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /clean

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/clean.md">Source</a></span>
</div>


This command invokes the **refactor-cleaner** agent to reduce technical debt.

## What This Command Does

1. **Dead Code Detection** - Runs tools like `knip` or `ts-prune` to find unused exports.
2. **Consolidation** - Merges duplicated logic into shared utilities.
3. **Refactoring** - Simplifies complex functions and deepens shallow modules.

---
**Note**: This command is powered by the `galyarder-framework:improve-codebase-architecture` skill.
