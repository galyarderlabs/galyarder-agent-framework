#!/bin/bash
# Galyarder Framework: Audit-Grade Smoke Test
# Verifies system integrity, version parity, and structural health.

set -e

echo "🚀 Starting Galyarder v1.8.0 Smoke Test..."

# 1. Structural Verification
echo "[1/4] Verifying Departmental Silo Integrity..."
DEPARTMENTS=("Executive" "Engineering" "Growth" "Security" "Product" "Infrastructure" "Legal-Finance" "Knowledge")
for dept in "${DEPARTMENTS[@]}"; do
    if [ ! -d "$dept" ]; then
        echo "❌ Error: Department '$dept' is missing."
        exit 1
    fi
done
echo "✅ All 8 Departments accounted for."

# 2. Version Parity Check
echo "[2/4] Verifying Version Parity across Manifests..."
ROOT_VERSION=$(grep '"version":' gemini-extension.json | head -1 | awk -F'"' '{print $4}')
MARKETPLACE_VERSION=$(grep '"version":' .claude-plugin/marketplace.json | head -1 | awk -F'"' '{print $4}')

if [ "$ROOT_VERSION" != "1.8.0" ]; then
    echo "❌ Error: Root version mismatch ($ROOT_VERSION != 1.8.0)"
    exit 1
fi

if [ "$MARKETPLACE_VERSION" != "1.8.0" ]; then
    echo "❌ Error: Marketplace version mismatch ($MARKETPLACE_VERSION != 1.8.0)"
    exit 1
fi
echo "✅ Global Versioning synchronized at v1.8.0."

# 3. Asset Inventory Check
echo "[3/4] Checking minimum asset counts..."
AGENT_COUNT=$(find . -path "*/agents/*.md" | wc -l)
SKILL_COUNT=$(find . -name "SKILL.md" | wc -l)

if [ "$AGENT_COUNT" -lt 40 ]; then
    echo "⚠️ Warning: Detected only $AGENT_COUNT agents (Expected ~40)."
fi
echo "✅ Inventory check complete ($AGENT_COUNT Agents, $SKILL_COUNT Skills)."

# 4. Documentation Readiness
echo "[4/4] Verifying Documentation build paths..."
if [ ! -f "docs/index.md" ] || [ ! -f "docs/WORKFLOW.md" ]; then
    echo "❌ Error: Documentation portal source incomplete."
    exit 1
fi
echo "✅ Documentation paths verified."

echo "---"
echo "✅ SMOKE TEST PASSED: Galyarder Framework v1.8.0 is operational."
