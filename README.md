<p align="center">
  <img src="framework/public/logo.png" width="200" alt="Galyarder Logo">
</p>

# GALYARDER

**Digital Company Operating System for Solo Founders**

Complete AI workforce platform combining **35 specialized agents** + **132 execution-grade skills** with a visual Dashboard for orchestration, monitoring, and governance.

Built for the **1-Man Army** - one founder with the leverage of an entire company.

---

## 🏗️ What's Inside

This repository contains:

### 1. **Galyarder Framework** (`framework/`)
- 35 specialized agents (CEO, CTO, Engineers, Designers, Marketers, Legal, etc.)
- 132 production-ready skills across full product lifecycle
- Works with Claude Code, Cursor, Gemini, Codex
- Standalone or Dashboard-integrated

### 2. **Galyarder Dashboard** (root)
- Visual control plane for managing AI companies
- Org charts, task management, cost tracking
- Multi-company support with data isolation
- Heartbeat-based autonomous execution
- Real-time monitoring and governance

### 3. **Framework Adapter** (`packages/adapters/galyarder-framework/`)
- Connects Framework agents to Dashboard
- Enables visual management of Framework workforce
- Task routing and execution orchestration

---

## 🚀 Quick Start

### Option 1: Framework Only (Standalone)

Use Framework directly in your AI coding assistant:

**Claude Code / Copilot CLI:**
```bash
/plugin marketplace add galyarderlabs/galyarder-framework
/plugin install galyarder-framework
```

**Cursor:**
```bash
# Add to .cursor-plugin/plugin.json
```

**Gemini:**
```bash
# Add to .gemini/settings.json
```

See [`framework/README.md`](framework/README.md) for full installation guide.

### Option 2: Dashboard + Framework (Full Platform)

Run the complete platform with visual management:

```bash
# 1. Install dependencies
pnpm install

# 2. Start Dashboard
pnpm dev

# 3. Open browser
# http://localhost:3100

# 4. Create company and agents
# Framework adapter will be available in agent creation
```

See [`TESTING.md`](TESTING.md) for detailed setup and testing guide.

---

## 📖 Documentation

- **[Framework README](framework/README.md)** - Standalone Framework usage
- **[Dashboard README](doc/README.md)** - Dashboard features and architecture
- **[Testing Guide](TESTING.md)** - Integration testing instructions
- **[Contributing](CONTRIBUTING.md)** - Development guidelines

---

## 🎯 Use Cases

### Framework Standalone
- Chat-based development with structured workflow
- Subagent-driven development (SDD)
- Full lifecycle: design → implementation → marketing
- Works in your existing AI coding assistant

### Dashboard + Framework
- Manage multiple AI companies from one control plane
- Visual org charts and task management
- Cost tracking and budget enforcement
- Autonomous 24/7 execution with heartbeats
- Mobile-ready monitoring

---

## 🏢 Architecture

```
galyarder-framework/              # Root = Dashboard
├── framework/                    # Framework (35 agents + 132 skills)
│   ├── agents/                   # Agent definitions
│   ├── skills/                   # Skill implementations
│   └── design/                   # Design specs
├── packages/
│   └── adapters/
│       └── galyarder-framework/  # Framework → Dashboard adapter
├── server/                       # Dashboard API
├── ui/                           # Dashboard UI
└── ...
```

---

## 💡 Key Features

### Framework
- ✅ 35 specialized agents (CEO, CTO, Engineers, etc.)
- ✅ 132 production-ready skills
- ✅ Subagent-driven development (SDD)
- ✅ Design-first workflow
- ✅ Multi-platform support

### Dashboard
- ✅ Visual control plane
- ✅ Multi-company support
- ✅ Cost tracking & budgets
- ✅ Heartbeat-based execution
- ✅ Org charts & governance
- ✅ Mobile-ready

### Integration
- ✅ Framework adapter for Dashboard
- ✅ Task routing & orchestration
- ✅ Unified monitoring
- ✅ Seamless workflow

---

## 🛠️ Development

```bash
# Install dependencies
pnpm install

# Start Dashboard (dev mode)
pnpm dev

# Build everything
pnpm build

# Type checking
pnpm typecheck

# Run tests
pnpm test:run

# Database migrations
pnpm db:generate
pnpm db:migrate
```

See [`doc/DEVELOPING.md`](doc/DEVELOPING.md) for full development guide.

---

## 📦 What's New

This repository combines:
- **Galyarder Framework** (formerly standalone)
- **Galyarder Dashboard** (formerly Paperclip)
- **Integration adapter** (connects both)

**Structure:** Dashboard is root, Framework is subfolder. This enables:
- Single deployment for full platform
- Framework can still be used standalone
- Adapter provides seamless integration

---

## 🤝 Contributing

We welcome contributions! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT © 2026 Galyarder Labs

---

## 🌟 Sponsorship

If Galyarder has helped you build something that makes money, consider [sponsoring this work](https://github.com/sponsors/galyarderlabs).

Thanks!  
— Galyarder Labs

---

<p align="center">
  <strong>Open source. Self-hosted. No account required.</strong>
</p>
