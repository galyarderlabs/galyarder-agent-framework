---
name: "deploy"
description: "Infrastructure and CI/CD specialist. Automates deployments to Vercel, Docker, or AWS."
risk: low
source: internal
date_added: '2026-04-18'
---

# Deploy Command

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

**Note**: This command is powered by the `galyarder-framework:devops-deployment` skill.
