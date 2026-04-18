---
title: "/release  Slash Command for AI Coding Agents"
description: "Orchestrate the launch process, bump versions, and generate changelogs.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /release

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/release.md">Source</a></span>
</div>


This command invokes the **release-manager** to finalize a production-ready version.

## What This Command Does

1. **Version Management** - Executes `bump-version.sh` using SemVer.
2. **Changelog Generation** - Compiles git logs and Linear tickets into release notes.
3. **Launch Sync** - Coordinates with marketing agents for the release announcement.

---
**Note**: Powered by the `finishing-a-development-branch` and `writing-skills` skills.
