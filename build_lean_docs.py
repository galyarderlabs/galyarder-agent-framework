import os

def read_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f: return f.read()

def build_agents_lean():
    content = ["# Galyarder Agents (Lean Index)\n"]
    content.append("## 🗺️ DEPARTMENTS\n")
    # Take only the department map summary
    content.append(read_file("obsidian-templates/Galyarder.Framework/Galyarder Department Map.md"))
    content.append("\n## 👥 AGENT DIRECTORY\n")
    
    for f in sorted(os.listdir("agents")):
        if f.endswith(".md"):
            raw = read_file(f"agents/{f}")
            lines = raw.split("\n")
            desc = ""
            for line in lines:
                if line.startswith("description:"): 
                    desc = line.replace("description:", "").strip()
                    break
            content.append(f"- **{f.replace('.md', '')}**: {desc}")
            
    with open("AGENTS.md", "w") as out: out.write("\n".join(content))

def build_claude_lean():
    content = ["# Galyarder Workforce (Lean Index)\n"]
    content.append("## ⚖️ WORKFLOW: Phase 1 (Discovery), 2 (Plan), 3 (TDD), 4 (QA), 5 (Growth).\n")
    content.append("## 🛠️ SKILLS DIRECTORY\n")
    
    skills_dir = "skills"
    for root, dirs, files in sorted(os.walk(skills_dir)):
        for f in sorted(files):
            if f == "SKILL.md":
                path = os.path.join(root, f)
                rel_path = os.path.relpath(root, skills_dir)
                raw = read_file(path)
                desc = ""
                # Find name and description in header or metadata
                lines = raw.split("\n")
                for line in lines:
                    if "description:" in line:
                        desc = line.split("description:", 1)[1].strip().strip('"')
                        break
                if not desc and len(lines) > 5: # Fallback to first line of body
                    desc = lines[5].strip() if len(lines) > 5 else "No description."
                
                content.append(f"- **{rel_path}**: {desc}")
                
    with open("CLAUDE.md", "w") as out: out.write("\n".join(content))

def build_gemini_lean():
    content = ["# Galyarder OS (Lean Index)\n"]
    content.append("## ⚙️ ADAPTERS: @./skills/using-galyarder-framework/SKILL.md\n")
    content.append("## ⌨️ COMMANDS\n")
    for f in sorted(os.listdir("commands")):
        if f.endswith(".md"):
            raw = read_file(f"commands/{f}")
            lines = raw.split("\n")
            desc = ""
            for line in lines:
                if "description:" in line:
                    desc = line.split("description:", 1)[1].strip()
                    break
            content.append(f"- **/{f.replace('.md', '')}**: {desc}")
            
    with open("GEMINI.md", "w") as out: out.write("\n".join(content))

if __name__ == "__main__":
    build_agents_lean()
    build_claude_lean()
    build_gemini_lean()
