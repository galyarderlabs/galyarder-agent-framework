import os
import re

def read_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f: return f.read()

def extract_agent_essentials(content):
    # Extract description and key mandates
    desc = ""
    mandates = []
    lines = content.split("\n")
    for line in lines:
        if line.startswith("description:"):
            desc = line.replace("description:", "").strip()
        if line.strip().startswith("- ") and len(mandates) < 3:
            mandates.append(line.strip())
    return desc, mandates

def build_agents_moderate():
    content = ["# Galyarder Digital Company: Org Chart & Management Roles\n"]
    content.append("## 🏢 CORPORATE MISSION")
    content.append("Autonomous workforce orchestration for Solo Founders. Maximize leverage, minimize slop.\n")
    
    content.append("## 🗺️ DEPARTMENT MAP")
    content.append(read_file("obsidian-templates/Galyarder.Framework/Galyarder Department Map.md"))
    
    content.append("\n## 👥 DEPARTMENT HEADS & SPECIALISTS")
    for f in sorted(os.listdir("agents")):
        if f.endswith(".md"):
            raw = read_file(f"agents/{f}")
            desc, mandates = extract_agent_essentials(raw)
            agent_name = f.replace(".md", "")
            content.append(f"### @{agent_name}")
            content.append(f"**Mission:** {desc}")
            if mandates:
                content.append("**Core Responsibilities:**")
                content.extend(mandates)
            content.append("")
            
    with open("AGENTS.md", "w") as out: out.write("\n".join(content))

def build_claude_moderate():
    content = ["# Galyarder Workforce: SOPs & Skill Matrix\n"]
    content.append("## ⚖️ THE WORKFLOW CONSTITUTION (PHASE 1-5)")
    content.append("1. **Discovery**: PRD & Business Intent.")
    content.append("2. **Blueprint**: Architecture & Plan.md (Vertical Slices).")
    content.append("3. **Factory**: TDD Implementation.")
    content.append("4. **Gatekeeper**: QA (BrowserOS) & Security Audit.")
    content.append("5. **Distribution**: Marketing, SEO & Video.\n")
    
    content.append("## 🛠️ SKILL DIRECTORY")
    skills_dir = "skills"
    # Grouping by first letter or common prefixes for better moderate density
    current_cat = ""
    for root, dirs, files in sorted(os.walk(skills_dir)):
        for f in sorted(files):
            if f == "SKILL.md":
                rel_path = os.path.relpath(root, skills_dir)
                raw = read_file(os.path.join(root, f))
                desc = ""
                lines = raw.split("\n")
                for line in lines:
                    if "description:" in line:
                        desc = line.split("description:", 1)[1].strip().strip('"')
                        break
                
                # Moderate density: Name + One sentence core capability
                content.append(f"- **@{rel_path}**: {desc}")
                
    with open("CLAUDE.md", "w") as out: out.write("\n".join(content))

def build_gemini_moderate():
    content = ["# Galyarder OS: Executive Operating Loops\n"]
    content.append("## ⚙️ SYSTEM BOOTLOADER")
    content.append("- **Adapter**: @./skills/using-galyarder-framework/SKILL.md")
    content.append("- **Shield**: Mandatory `rtk` prefix for all shell/git operations.\n")
    
    content.append("## ⌨️ EXECUTIVE COMMANDS")
    for f in sorted(os.listdir("commands")):
        if f.endswith(".md"):
            raw = read_file(f"commands/{f}")
            desc = ""
            for line in raw.split("\n"):
                if "description:" in line:
                    desc = line.split("description:", 1)[1].strip()
                    break
            content.append(f"### /{f.replace('.md', '')}")
            content.append(f"**Action:** {desc}")
            
    content.append("\n## 📊 REPORTING STANDARDS")
    content.append("- **Linear**: Task status & issue tracking.")
    content.append("- **Obsidian**: Strategic memory & Department Reports (Templates in `obsidian-templates/`).")
    
    with open("GEMINI.md", "w") as out: out.write("\n".join(content))

if __name__ == "__main__":
    build_agents_moderate()
    build_claude_moderate()
    build_gemini_moderate()
