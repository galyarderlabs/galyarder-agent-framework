#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"

DEPARTMENTS = {
    "Executive": {"icon": "material/account-tie", "desc": "C-Suite Strategic Hegemony"},
    "Engineering": {"icon": "material/hammer-wrench", "desc": "Deterministic Implementation"},
    "Growth": {"icon": "material/trending-up", "desc": "Behavioral Arbitrage & Marketing"},
    "Security": {"icon": "material/shield-lock", "desc": "Offensive & Defensive Audits"},
    "Product": {"icon": "material/package-variant-closed", "desc": "Discovery & Roadmap Integrity"},
    "Infrastructure": {"icon": "material/server", "desc": "Reliability & Deployment Physics"},
    "Legal-Finance": {"icon": "material/scale-balance", "desc": "Regulatory & Token FinOps"},
    "Knowledge": {"icon": "material/brain", "desc": "Durable Memory & Visual Mapping"}
}

def extract_metadata(file_path):
    name, desc = "", ""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                name_m = re.search(r"^name:\s*(.*)", fm, re.MULTILINE)
                desc_m = re.search(r"^description:\s*(.*)", fm, re.MULTILINE)
                if name_m: name = name_m.group(1).strip().strip('"').strip("'")
                if desc_m: desc = desc_m.group(1).strip().strip('"').strip("'")
            if not name:
                h1_match = re.search(r"^# (.*)", content, re.MULTILINE)
                if h1_match: name = h1_match.group(1).strip()
    except: pass
    return name, desc

def generate_card(title, link, desc, icon=""):
    return f"""
[:octicons-terminal-24: **{title}**]({link})
: .card

{desc}
"""

def generate():
    print("Generating Apex Documentation Portal...")
    
    for d in ["agents", "skills", "commands", "design"]:
        target = DOCS_DIR / d
        if target.exists(): shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)

    dept_assets = {d: {"agents": [], "skills": [], "commands": []} for d in DEPARTMENTS}

    for dept, info in DEPARTMENTS.items():
        dept_path = REPO_ROOT / dept
        if not dept_path.exists(): continue
        
        # 1. Process Agents
        agent_src = dept_path / "agents"
        if agent_src.exists():
            for f in agent_src.glob("*.md"):
                if f.name == "README.md": continue
                name, desc = extract_metadata(f)
                shutil.copy(f, DOCS_DIR / "agents" / f.name)
                dept_assets[dept]["agents"].append((name or f.stem, f"../agents/{f.name}", desc))

        # 2. Process Commands
        cmd_src = dept_path / "commands"
        if cmd_src.exists():
            for f in cmd_src.glob("*.md"):
                shutil.copy(f, DOCS_DIR / "commands" / f.name)
                dept_assets[dept]["commands"].append((f"/{f.stem}", f"../commands/{f.name}", ""))

        # 3. Process Skills
        skill_src = dept_path / "skills"
        if skill_src.exists():
            for skill_folder in skill_src.iterdir():
                if not skill_folder.is_dir(): continue
                skill_md = skill_folder / "SKILL.md"
                if skill_md.exists():
                    name, desc = extract_metadata(skill_md)
                    dest_folder = DOCS_DIR / "skills" / skill_folder.name
                    dest_folder.mkdir(exist_ok=True)
                    shutil.copy(skill_md, dest_folder / "index.md")
                    for sub in ["references", "assets", "templates"]:
                        if (skill_folder / sub).exists():
                            shutil.copytree(skill_folder / sub, dest_folder / sub, dirs_exist_ok=True)
                    dept_assets[dept]["skills"].append((name or skill_folder.name, f"../skills/{skill_folder.name}/index.md", desc))

    # Build High-Fidelity Landing Pages with Material Grids
    for category in ["agents", "skills", "commands"]:
        idx_content = f"# Galyarder Framework {category.title()}\n\n"
        idx_content += '<div class="grid cards" markdown>\n'
        
        for dept, assets in dept_assets.items():
            if assets[category]:
                idx_content += f"\n## {DEPARTMENTS[dept]['icon']} {dept} Department\n\n"
                for title, link, desc in sorted(assets[category]):
                    idx_content += f"-   **[{title}]({link})**\n\n    ---\n\n    {desc}\n"
        
        idx_content += "\n</div>"
        with open(DOCS_DIR / f"{category}/index.md", "w") as f:
            f.write(idx_content)

    # Special: Design Systems
    design_idx = "# Design System Specifications\n\n"
    design_idx += '<div class="grid cards" markdown>\n'
    design_src = REPO_ROOT / "Growth" / "design"
    if design_src.exists():
        for f in sorted(design_src.glob("*.md")):
            shutil.copy(f, DOCS_DIR / "design" / f.name)
            design_idx += f"-   **[{f.stem}]({f.name})**\n\n    ---\n\n    High-fidelity design spec.\n"
    design_idx += "\n</div>"
    with open(DOCS_DIR / "design/index.md", "w") as f: f.write(design_idx)

    print("Portal generated with Material Card system.")

if __name__ == "__main__":
    generate()
