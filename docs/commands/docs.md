---
title: "/docs  Slash Command for AI Coding Agents"
description: "Documentation and codemap specialist. Generates codemaps, updates READMEs, and syncs documentation with the source code.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /docs

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/docs.md">Source</a></span>
</div>


This command invokes the **doc-updater** agent to keep your documentation in sync with your implementation.

## What This Command Does

1. **Codemap Generation** - Updates `docs/CODEMAPS/*` to reflect current file structure and exports.
2. **README Sync** - Updates project READMEs based on new features or API changes.
3. **Guide Maintenance** - Ensures setup and contribution guides are up to date.

---
**Note**: This command is powered by the `galyarder-framework:doc-updater` skill.
