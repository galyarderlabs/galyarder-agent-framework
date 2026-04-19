#!/usr/bin/env python3
import os
import re
import json
import shutil
from pathlib import Path

# Galyarder Graphify Engine v1.0
# Purpose: Map structural and semantic relationships across the Framework.

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
OUTPUT_FILE = REPO_ROOT / "docs" / "graph.json"

class Graphify:
    def __init__(self):
        self.nodes = {}  # path -> metadata
        self.edges = []  # list of (source, target, type)

    def add_node(self, path, title, category):
        rel_path = str(Path(path).relative_to(REPO_ROOT))
        self.nodes[rel_path] = {
            "title": title,
            "category": category,
            "silo": rel_path.split('/')[0] if '/' in rel_path else "Root"
        }

    def add_edge(self, source, target, edge_type):
        self.edges.append({
            "source": str(source),
            "target": str(target),
            "type": edge_type
        })

    def scan_markdown(self):
        print(f"[*] Scanning Knowledge Base: {DOCS_DIR}")
        for root, _, files in os.walk(DOCS_DIR):
            for f in files:
                if f.endswith(".md"):
                    file_path = Path(root) / f
                    rel_src = str(file_path.relative_to(REPO_ROOT))
                    
                    # Extract Title
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    
                    title_match = re.search(r"^# (.*)", content, re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else f
                    
                    self.add_node(file_path, title, "documentation")
                    
                    # Find links: [text](link.md)
                    links = re.findall(r"\[.*?\]\((.*?\.md)\)", content)
                    for link in links:
                        # Resolve relative link
                        if link.startswith("http"): continue
                        
                        target_path = (file_path.parent / link).resolve()
                        if target_path.exists():
                            rel_target = str(target_path.relative_to(REPO_ROOT))
                            self.add_edge(rel_src, rel_target, "references")

    def scan_python(self):
        print(f"[*] Scanning Logic Engine (Python): {REPO_ROOT}/scripts")
        scripts_dir = REPO_ROOT / "scripts"
        for f in scripts_dir.glob("*.py"):
            rel_src = str(f.relative_to(REPO_ROOT))
            self.add_node(f, f.name, "script")
            
            with open(f, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Find open() calls or path references
            paths = re.findall(r"['\"](.*?\.(?:md|json|py))['\"]", content)
            for path in paths:
                # Try to resolve relative to root or script dir
                potential_targets = [
                    REPO_ROOT / path,
                    f.parent / path,
                    REPO_ROOT / "docs" / path
                ]
                for target in potential_targets:
                    if target.exists() and target.is_file():
                        rel_target = str(target.resolve().relative_to(REPO_ROOT))
                        self.add_edge(rel_src, rel_target, "executes")
                        break

    def generate_obsidian_map(self):
        map_dir = REPO_ROOT / "docs" / "departments" / "Knowledge" / "World-Map"
        if map_dir.exists(): shutil.rmtree(map_dir)
        map_dir.mkdir(parents=True, exist_ok=True)
        print(f"[*] Generating Obsidian World Map: {map_dir}")
        
        for rel_path, meta in self.nodes.items():
            # Create a slug for the filename
            node_name = meta["title"].replace("/", "-").replace(" ", "-")
            file_name = f"{node_name}.md"
            
            # Find related nodes
            outgoing = [e["target"] for e in self.edges if e["source"] == rel_path]
            incoming = [e["source"] for e in self.edges if e["target"] == rel_path]
            
            content = f"""---
node_type: {meta['category']}
silo: {meta['silo']}
source_path: {rel_path}
---

# {meta['title']}

## Links Out
"""
            for out in outgoing:
                if out in self.nodes:
                    target_title = self.nodes[out]["title"]
                    content += f"- [[{target_title.replace(' ', '-')}]]\n"
            
            content += "\n## Linked From\n"
            for inc in incoming:
                if inc in self.nodes:
                    source_title = self.nodes[inc]["title"]
                    content += f"- [[{source_title.replace(' ', '-')}]]\n"
            
            content += f"\n---\n[View Original Source](../../../../{rel_path})\n"
            
            with open(map_dir / file_name, "w", encoding="utf-8") as f:
                f.write(content)

    def export(self):
        data = {
            "nodes": self.nodes,
            "edges": self.edges,
            "metadata": {
                "version": "1.0.0",
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges)
            }
        }
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Graph exported to {OUTPUT_FILE}")
        print(f"   Nodes: {len(self.nodes)} | Edges: {len(self.edges)}")

if __name__ == "__main__":
    engine = Graphify()
    engine.scan_markdown()
    engine.scan_python()
    engine.generate_obsidian_map()
    engine.export()
