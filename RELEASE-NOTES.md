# Release Notes - Galyarder Agent Framework v1.3.0

The **Visual Intelligence & Compatibility Update**. Version 1.3.0 marks a major milestone by integrating Obsidian as the framework's visual "War Room" and resolving critical compatibility issues across OpenCode and Codex.

## Highlights

### 1. Obsidian Visual Integration
We have introduced a deep integration with Obsidian to provide a visual layer for the 1-Man Army workflow:
- **New Agent**: `obsidian-architect` — Your specialist for Digital Gardens, Visual Mapping (Canvas), and Knowledge Base management.
- **Visual Mapping**: Automated creation of `Architecture.canvas` files to visualize complex logic and system flows.
- **Automated Journaling**: Real-time activity logging into `03 - Activity Log.md` to maintain a durable history of development decisions.
- **Knowledge Base**: Structured storage for design specs and plans directly in your vault.

### 2. OpenCode Professional Grade
Significant refactoring to ensure 100% compatibility with OpenCode:
- **Tool Mapping Fix**: Converted all agent `tools` definitions to the record format required by OpenCode's parser.
- **Validation Cleanup**: Removed non-standard `model` fields that were causing validation errors.
- **Plugin Integration**: Official registration of the `galyarder-agent-framework.js` plugin for a seamless UI experience.

### 3. Branding & Environment Purge
Unified the framework identity by removing legacy "Superpowers" artifacts:
- **Variable Cleanup**: Renamed all internal and test variables from `SUPERPOWERS_*` to `GALYARDER_*`.
- **Shadow Binary Protocol**: Established documentation for resolving npm global prefix conflicts and "shadow binary" issues.

### 4. Codex Discovery Optimization
Improved discovery for OpenAI Codex through project-level manifests:
- **Project AGENTS.md**: Native agent catalog in the project root for easier @mention discovery.
- **Local Config**: Added `.codex/config.toml` to map project-level slash commands directly to their markdown definitions.

---
© 2026 Galyarder Labs. Built for the 1-Man Army.
