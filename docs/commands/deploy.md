---
title: "/deploy  Slash Command for AI Coding Agents"
description: "Infrastructure and CI/CD specialist. Automates deployments to Vercel, Docker, or AWS.. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /deploy

<div class="page-meta" markdown>
<span class="meta-badge"> Slash Command</span>
<span class="meta-badge"> <a href="https://github.com/galyarderlabs/galyarder-framework/tree/main/commands/deploy.md">Source</a></span>
</div>


This command invokes the **devops-engineer** agent to productionize your application.

## What This Command Does

1. **CI/CD Setup** - Writes GitHub Actions or GitLab CI pipelines.
2. **Containerization** - Creates optimized multi-stage Dockerfiles.
3. **Cloud Config** - Sets up `vercel.json`, `wrangler.toml`, or Terraform files.

## When to Use

Use `/deploy` when:
- Moving from local development to a staging environment.
- Automating the release process.
- Scaling infrastructure to handle more users.

---
**Note**: This command is powered by the `galyarder-framework:devops-deployment` skill.
