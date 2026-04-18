# Installing Galyarder Framework for Codex

Enable galyarder-framework skills in Codex via native skill discovery. Just clone and symlink.

## Prerequisites

- Git

## Installation

1. **Clone the galyarder-framework repository:**
   ```bash
   git clone https://github.com/galyarderlabs/galyarder-framework.git ~/.codex/galyarder-framework
   ```

2. **Create the skills symlink:**
   ```bash
   mkdir -p ~/.agents/skills
   ln -s ~/.codex/skills ~/.agents/skills/galyarder-framework
   ```

   **Windows (PowerShell):**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
   cmd /c mklink /J "$env:USERPROFILE\.agents\skills\galyarder-framework" "$env:USERPROFILE\.codex\galyarder-framework\skills"
   ```

3. **Restart Codex** (quit and relaunch the CLI) to discover the skills.

## Migrating from old bootstrap

If you installed galyarder-framework before native skill discovery, you need to:

1. **Update the repo:**
   ```bash
   cd ~/.codex/galyarder-framework && git pull
   ```

2. **Create the skills symlink** (step 2 above)  this is the new discovery mechanism.

3. **Remove the old bootstrap block** from `~/.codex/AGENTS.md`  any block referencing `galyarder-framework-codex bootstrap` is no longer needed.

4. **Restart Codex.**

## Verify

```bash
ls -la ~/.agents/skills/galyarder-framework
```

You should see a symlink (or junction on Windows) pointing to your galyarder-framework skills directory.

## Updating

```bash
cd ~/.codex/galyarder-framework && git pull
```

Skills update instantly through the symlink.

## Uninstalling

```bash
rm ~/.agents/skills/galyarder-framework
```

Optionally delete the clone: `rm -rf ~/.codex/galyarder-framework`.
