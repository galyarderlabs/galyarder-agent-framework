import os
import re

agents_dir = "agents"
seed_file = "dashboard/packages/db/src/seed.ts"

def get_full_meta(filename):
    path = os.path.join(agents_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    desc = ""
    # Look for description in yaml-like frontmatter
    match = re.search(r"description:\s*([\s\S]*?)(?=\n\w+:|\n---)", content)
    if match:
        desc = match.group(1).strip().replace('"', '\\"').replace('\n', ' ')
    
    return desc

# Define the reporting structure (Who reports to whom)
hierarchy = {
    # Engineering Dept
    "elite-developer.md": "super-architect",
    "qa-automation-engineer.md": "super-architect",
    "build-error-resolver.md": "super-architect",
    "code-reviewer.md": "super-architect",
    "refactor-cleaner.md": "super-architect",
    "vercel-react-expert.md": "super-architect",
    "remotion-engineer.md": "super-architect",
    "e2e-runner.md": "super-architect",
    
    # Growth Dept
    "growth-engineer.md": "growth-strategist",
    "conversion-engineer.md": "growth-strategist",
    "retention-specialist.md": "growth-strategist",
    "social-strategist.md": "growth-strategist",
    "analytics-architect.md": "growth-strategist",
    
    # Product Dept
    "planner.md": "product-manager",
    
    # Security Dept
    "security-reviewer.md": "security-guardian",
    "cyber-intel.md": "security-guardian",
    "perseus.md": "security-guardian",
    
    # All Leads report to the CEO (implicit in logic)
}

leads = ["super-architect", "growth-strategist", "product-manager", "security-guardian", "fundraising-operator", "legal-counsel", "finops-manager", "obsidian-architect"]

agent_files = sorted([f for f in os.listdir(agents_dir) if f.endswith(".md")])

ts_content = """import { createDb } from "./client.js";
import { companies, agents } from "./schema/index.js";

const url = process.env.DATABASE_URL;
if (!url) throw new Error("DATABASE_URL is required");

const db = createDb(url);

console.log("Seeding Galyarder Digital Company (Hierarchical Model)...");

const [company] = await db
  .insert(companies)
  .values({
    name: "Galyarder Digital Company",
    description: "1-Man Army Executive Control Plane.",
    status: "active",
    brandColor: "#06b6d4",
    issuePrefix: "GAL",
    budgetMonthlyCents: 1000000,
  })
  .returning();

const companyId = company!.id;

// 1. Create Department Leads first
const leadMap: Record<string, string> = {};
"""

# Part 1: Insert Leads
for lead in leads:
    filename = f"{lead}.md"
    desc = get_full_meta(filename)
    ts_content += f"""
const [{lead.replace("-", "_")}] = await db.insert(agents).values({{
  companyId,
  name: "{lead}",
  role: "manager",
  title: "Head of {lead.split("-")[0].title()}",
  status: "idle",
  capabilities: "{desc}",
  adapterType: "process",
  adapterConfig: {{ command: "rtk", args: ["gemini", "run", "--agent", "{filename}"] }},
  budgetMonthlyCents: 100000,
}}).returning();
leadMap["{lead}"] = {lead.replace("-", "_")}!.id;
"""

# Part 2: Insert Staff (Reporting to Leads)
ts_content += "\n// 2. Create Staff and map to Leads\nawait db.insert(agents).values([\n"
for f in agent_files:
    name = f.replace(".md", "")
    if name in leads: continue # Skip leads as they are already inserted
    
    desc = get_full_meta(f)
    reports_to = hierarchy.get(f, "null")
    reports_to_val = f"leadMap['{reports_to}']" if reports_to != "null" else "null"
    
    ts_content += f"""  {{
    companyId,
    name: "{name}",
    role: "staff",
    title: "{name.replace("-", " ").title()}",
    status: "idle",
    reportsTo: {reports_to_val},
    capabilities: "{desc}",
    adapterType: "process",
    adapterConfig: {{ command: "rtk", args: ["gemini", "run", "--agent", "{f}"] }},
    budgetMonthlyCents: 50000,
  }},
"""

ts_content += """]);

console.log("Galyarder Hierarchical Seed complete");
process.exit(0);
"""

with open(seed_file, "w") as f:
    f.write(ts_content)
