# Galyarder Agents

Galyarder Framework works by splitting responsibility across specialized agent
roles. This file is the human-readable roster and entrypoint for the agent
layer.

The runtime contract lives in the files under `./agents/`. Each agent file
defines the role, rules, workflow, and output expectations for that specialist.
Platform adapters such as Codex, Gemini, Claude, Cursor, or OpenCode may load
or dispatch those roles differently, but `agents/*.md` remains the canonical
source for the role itself.

The capability layer lives in `./skills/`. In practice:
- `agents/*.md` define who should think and operate in a given role
- `skills/*` define the workflows, guardrails, and specialized techniques
- platform adapter files such as `GEMINI.md` explain how a host should load and
  use the framework

## Executive Layer
- [galyarder-specialist](./agents/galyarder-specialist.md): master orchestrator
  and framework enforcer
- [product-manager](./agents/product-manager.md): ticket, ROI, and priority
  control
- [fundraising-operator](./agents/fundraising-operator.md): fundraising pipeline, investor operations, and capital readiness
- [planner](./agents/planner.md): planning, decomposition, and execution maps
- [perseus](./agents/perseus.md): high-level strategic execution role

## Architecture Layer
- [super-architect](./agents/super-architect.md): system and platform
  architecture
- [architect](./agents/architect.md): technical architecture and design review
- [interface-designer](./agents/interface-designer.md): interfaces, boundaries,
  and API surfaces
- [obsidian-architect](./agents/obsidian-architect.md): knowledge-base,
  canvas, and documentation architecture

## Engineering Layer
- [elite-developer](./agents/elite-developer.md): implementation, debugging,
  and TDD execution
- [build-error-resolver](./agents/build-error-resolver.md): build and toolchain
  failure recovery
- [code-reviewer](./agents/code-reviewer.md): review and defect detection
- [doc-updater](./agents/doc-updater.md): documentation maintenance
- [e2e-runner](./agents/e2e-runner.md): end-to-end execution and validation
- [qa-automation-engineer](./agents/qa-automation-engineer.md): QA automation
  and coverage
- [refactor-cleaner](./agents/refactor-cleaner.md): cleanup and safe refactors
- [tdd-guide](./agents/tdd-guide.md): TDD workflow enforcement
- [vercel-react-expert](./agents/vercel-react-expert.md): React, Next.js, and
  Vercel performance specialization
- [remotion-engineer](./agents/remotion-engineer.md): Remotion and React video
  systems

## Security And Ops Layer
- [security-guardian](./agents/security-guardian.md): defensive engineering and
  hardening
- [security-reviewer](./agents/security-reviewer.md): security review and risk
  surfacing
- [cyber-intel](./agents/cyber-intel.md): threat research and intelligence
- [devops-engineer](./agents/devops-engineer.md): CI/CD, infra, deployment, and
  operations
- [release-manager](./agents/release-manager.md): release execution and
  coordination
- [support-lead](./agents/support-lead.md): support response and issue triage
- [legal-counsel](./agents/legal-counsel.md): policy, risk, and legal review

## Growth And Revenue Layer
- [analytics-architect](./agents/analytics-architect.md): event design,
  tracking, and measurement architecture
- [conversion-engineer](./agents/conversion-engineer.md): CRO and funnel
  optimization
- [experimentation-engineer](./agents/experimentation-engineer.md): testing and
  experimentation systems
- [finops-manager](./agents/finops-manager.md): financial operations and cost
  control
- [growth-engineer](./agents/growth-engineer.md): product-led growth execution
- [growth-strategist](./agents/growth-strategist.md): SEO, positioning, and
  strategic growth planning
- [retention-specialist](./agents/retention-specialist.md): retention,
  lifecycle, and churn prevention
- [revenue-architect](./agents/revenue-architect.md): monetization and pricing
  architecture
- [social-strategist](./agents/social-strategist.md): social distribution and
  content amplification
- [ui-ux-designer](./agents/ui-ux-designer.md): product interface and visual UX

## Working Model
1. Pick the right role from `agents/*.md`.
2. Load the relevant skills and workflow guidance.
3. Execute through the host's native mechanism for commands, skills, and
   subagents.
4. Preserve the strict role instructions in the agent files; adapters translate
   runtime mechanics, not framework policy.
