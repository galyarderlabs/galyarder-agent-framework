---
name: "cybersecurity"
description: "Perform an advanced offensive security audit and attack simulation on the current features."
risk: low
source: internal
date_added: '2026-04-18'
---

# Cybersecurity Command

This command invokes the **perseus** agent to conduct red teaming, penetration testing, and identify bypasses in the security model.

## What This Command Does

1. **Attack Simulation** - Tests for BOLA, JWT bypass, and OAuth2 flaws.
2. **Payload Injection** - Probes for XSS, SQLi, and Command Injection.
3. **Bypass Discovery** - Identifies weaknesses in sanitization and authorization layers.
4. **PoC Generation** - Creates reproducible exploit scripts to demonstrate impact.

**Note**: This command leverages the `gemini-cli-security` suite of specialized testing skills.
