# Release Notes - Galyarder Framework

## [v1.8.0] - 2026-04-19
### Summary
Architectural guardrails to make execution provable: gated testing ladder, test-oracle defenses, operational modes, context version-truth, and tool interface boundaries.

#### Highlights
- **Gating Ladder**: Enforced execution gates: **Unit → Contract → E2E**.
- **Test Oracle Guardrails**: Mandatory negative control / mutation check to prevent “fake green” tests.
- **Operational Modes**:
  - `BUILD` (default): PRD-driven, full ceremony, full TDD.
  - `INCIDENT`: hotfix bypass with mandatory post-mortem.
  - `EXPERIMENT`: timeboxed, quarantined throwaway work.
- **Context Truth**: `context7` fetch must verify **library version** against local dependencies before adoption.
- **Tool Interfaces**: Standard interfaces introduced for Linear, RTK, and Obsidian.
- **Obsidian Loop**: Mandatory durable reporting artifact output to `docs/departments/`.

#### Breaking Changes
- Removed `framework/` subdirectory; paths have changed accordingly.

#### Migration
1. Update local references from `framework/...` to repo root paths.
2. Re-run install/conversion scripts for your tool (`./scripts/install.sh --tool <...>`).
3. Regenerate docs via `generate-docs.py`.

---

## [v1.7.1] - 2026-04-18
### Path Integrity & Silo Hardening
A maintenance release focusing on the structural hardening of the Digital Department Silos.

#### Fixes & Improvements
- **Manifest Discovery**: Standardized Claude Code sub-plugin manifests.
- **Link Integrity**: Surgical fix for 404s and relative pathing in the portal.
- **Auto-Deployment**: Integrated GitHub Actions for portal updates.

---

## [v1.7.0] - 2026-04-17
### Humans 2.0 & Department Silos
The foundational transformation into a high-integrity Digital Company OS.

---

## [v1.6.0] - 2026-04-12
### Operational Expansion
Added 5 new specialized agents. Total: 40 agents, 132 skills.

---

## [v1.3.1] - 2026-04-06
### Identity Update
Official transition to the **Galyarder Framework** name.

---

## [v1.0.0] - 2026-04-04
### Initial Release
Full restoration of high-rigor engineering agents and the 1-Man Army C-Suite.

---
© 2026 Galyarder Labs. Galyarder Framework. Engineering. Marketing. Distribution.
