# Release Notes - Galyarder Framework

## [v1.8.0] - 2026-04-19
### Summary
Architectural guardrails to make execution provable: gated testing ladder, test-oracle defenses, operational modes, context version-truth, and tool interface boundaries.

#### Highlights
- **Gating Ladder**: Enforced execution gates: **Unit → Contract → E2E**.
- **Contract Tests**: Verified API/interface boundaries in `tests/contract/`.
- **Test Oracle Guardrails**: Mandatory negative control / mutation check.
- **Operational Modes**: `BUILD` (Standard), `INCIDENT` (Hotfix), `EXPERIMENT` (Spike).
- **Context Truth**: `context7` fetches verify library versions against local dependencies.
- **Tool Interfaces**: Abstracted adapters for Linear, RTK, and Obsidian.

#### How to Run (100% Copy-Paste)
```bash
# 1. Install & Scaffold
./scripts/install.sh --tool <cursor|aider|claude-code> && ./scripts/scaffold-company.sh

# 2. Run Audit-Grade Smoke Test
bash scripts/smoke.sh

# 3. Run Full Gating Ladder (Example)
rtk npm run test:unit && rtk npm run test:contract && rtk npm run test:e2e
```

#### Compatibility Matrix
| Tool | Support Level | Version Tested | Known Limitation |
| :--- | :--- | :--- | :--- |
| **Claude Code** | Full (Native) | v0.2.x | Slower marketplace crawl on first init. |
| **Gemini CLI** | Full (Native) | v1.1.x | Requires manual hard refresh for favicon. |
| **Cursor** | High (MDC) | v0.42.x | `.mdc` files require IDE restart to reload. |
| **Aider** | High | v0.70.x | Consolidated context can hit token limits. |
| **Windsurf** | Medium | v1.0.x | Plugin lifecycle is still in experimental. |

#### Known Issues (Alpha Caveats)
- **Symlink Fragility**: Moving root files can break local platform folders. **Workaround**: Re-run `scripts/sync-*.py`.
- **Mermaid Rendering**: GitHub SVG element issues occasionally delay visual display. **Workaround**: Hard refresh (Ctrl+F5).
- **Context Latency**: `context7` fetching adds 2-5s overhead to high-rigor tasks.

#### Migration
[View Full Migration Guide](MIGRATION.md)

---
© 2026 Galyarder Labs. Galyarder Framework. Engineering. Marketing. Distribution.
