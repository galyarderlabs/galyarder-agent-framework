---
title: "/build-fix  Slash Command for AI Coding Agents"
description: "Systematically investigate and fix build errors, TypeScript errors, or test failures with minimal diffs.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /build-fix

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/build-fix.md">Source</a></span>
</div>


This command invokes the **build-error-resolver** agent to surgically fix compilation or runtime errors.

## What This Command Does

1. **Error Analysis** - Reads the full stack trace and identifies the origin of the failure.
2. **Minimal Correction** - Applies the smallest possible change to resolve the error.
3. **Verification** - Runs the build or tests again to ensure the fix works.

## When to Use

Use `/build-fix` when:
- `npm run build` fails.
- TypeScript compiler (`tsc`) reports errors.
- Tests are failing due to environment or type mismatches.

---
**Note**: This command is powered by the `galyarder-framework:systematic-debugging` skill.
