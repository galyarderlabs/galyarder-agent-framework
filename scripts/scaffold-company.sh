#!/bin/bash

# Galyarder Framework: Company Scaffolder
# Purpose: Initialize the hierarchical directory structure for a Digital Enterprise.
# This script can be run from anywhere by pointing to its absolute path.

# Determine where the script lives to find templates
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/../docs/templates"

echo "🚀 Initializing Galyarder Framework Digital Enterprise headquarters in $(pwd)..."

# 1. Base Directories
mkdir -p docs/specs
mkdir -p docs/plans
mkdir -p docs/reports
mkdir -p docs/templates

# 2. Departmental Structure
DEPARTMENTS=("Executive" "Product" "Engineering" "Growth" "Security" "Legal-Finance" "Knowledge")

for DEPT in "${DEPARTMENTS[@]}"; do
    DEPT_PATH="docs/departments/$DEPT"
    mkdir -p "$DEPT_PATH"
    
    # Initialize Department README if missing
    if [ ! -f "$DEPT_PATH/README.md" ]; then
        echo "# Department: $DEPT" > "$DEPT_PATH/README.md"
        echo "This directory contains persistent reports and strategic memory for the $DEPT department." >> "$DEPT_PATH/README.md"
        echo "---" >> "$DEPT_PATH/README.md"
        echo "Copyright 2026 Galyarder Labs. Galyarder Framework." >> "$DEPT_PATH/README.md"
    fi
done

# 3. Seed Templates (Logic: Look for templates relative to the script)
if [ -d "$TEMPLATE_DIR" ]; then
    echo "[*] Seeding departmental templates from $TEMPLATE_DIR..."
    cp "$TEMPLATE_DIR"/*Founder* docs/departments/Executive/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Product* docs/departments/Product/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Engineering* docs/departments/Engineering/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Growth* docs/departments/Growth/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Security* docs/departments/Security/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Legal-Finance* docs/departments/Legal-Finance/ 2>/dev/null || true
    cp "$TEMPLATE_DIR"/*Knowledge* docs/departments/Knowledge/ 2>/dev/null || true
else
    echo "⚠️ Warning: Template source not found at $TEMPLATE_DIR. Skipping seed."
fi

echo "✅ Company structure initialized at docs/departments/"
echo "Your Digital Headquarters is ready for Obsidian."
