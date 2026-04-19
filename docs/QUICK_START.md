# Quick Start: The Galyarder Ecosystem

Get the Galyarder Framework (Intelligence) and Galyarder HQ (Control Plane) working together in under 5 minutes.

## Prerequisites

- Node.js 20+
- Git installed
- A project where you want to deploy (e.g., `~/projects/my-startup`)

---

## Phase 1: Initialize the Intelligence (Framework)

First, bootstrap your system with the global Galyarder commands.

```bash
# 1. Clone the logic library
git clone https://github.com/galyarderlabs/galyarder-framework.git ~/galyarder-framework

# 2. Setup global CLI
cd ~/galyarder-framework
./scripts/setup-cli.sh
```

---

## Phase 2: Initialize Your Project HQ

Navigate to your target project and establish its digital headquarters.

```bash
cd ~/projects/my-startup

# 1. Build the Digital HQ structure
galyarder-scaffold

# 2. Deploy agents to your preferred tool (e.g., Cursor)
galyarder-deploy --tool cursor
```

---

## Phase 3: Launch the Control Plane (Galyarder HQ)

If you want a visual dashboard to monitor your agents, deploy **Galyarder HQ**.

```bash
# 1. Clone the Control Plane
git clone https://github.com/galyarderlabs/galyarder-hq.git ~/galyarder-hq

# 2. Start the Dashboard
cd ~/galyarder-hq
npm install
npm run dev
```

The dashboard will be available at: **http://localhost:3100**

---

## How to Link Them

Galyarder HQ automatically discovers any project that has been initialized via `galyarder-scaffold`.

1.  Open the HQ Dashboard.
2.  Click **"Connect Project"**.
3.  Point it to your project directory (`~/projects/my-startup`).
4.  The dashboard will immediately index your active agents, tasks, and Obsidian reports.

---

## Troubleshooting

### Commands not found
Ensure `~/.local/bin` is in your PATH. Run `source ~/.zshrc` (or `.bashrc`) after running the setup script.

### No agents detected
Ensure you have run `galyarder-scaffold` inside your project directory. Galyarder HQ relies on the `docs/departments/` structure to track progress.

---
© 2026 Galyarder Labs. Galyarder Framework. Engineering. Marketing. Distribution.
