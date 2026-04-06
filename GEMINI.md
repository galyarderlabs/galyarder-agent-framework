# Gemini Bootstrap

This repository exposes three layers to Gemini:
- `./agents/` for role definitions
- `./skills/` for workflow and domain capability
- `./commands/` for extension commands

When Gemini loads this extension:
- treat `agents/*.md` as the authoritative role definitions
- load and apply skills from `skills/`
- use Gemini-native commands, tools, and subagent mechanisms where applicable
- do not rewrite the policy or strictness defined in the agent files; only
  adapt runtime mechanics to Gemini's host model

Important compatibility rule:
- agent frontmatter `tools` must use Gemini-valid tool names
- host-specific capabilities that are not native Gemini tools should stay in
  the role instructions, associated skills, or adapter references rather than
  the `tools` array

Use these references as the primary Gemini adapter layer:
@./skills/using-galyarder-framework/SKILL.md
@./skills/using-galyarder-framework/references/gemini-tools.md

Operational model:
1. Start from the relevant agent role in `./agents/`.
2. Pull in the matching skill guidance from `./skills/`.
3. Follow `gemini-tools.md` when mapping framework expectations onto Gemini's
   runtime.
4. If a framework role or skill assumes a capability that Gemini does not
   expose natively, preserve the role intent and adapt the execution path
   through Gemini-supported tools.
