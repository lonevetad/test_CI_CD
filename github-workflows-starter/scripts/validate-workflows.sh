#!/bin/bash

# This script validates the YAML syntax of the workflow files in the .github/workflows directory.

set -e

WORKFLOW_DIR=".github/workflows"
YAML_FILES=("$WORKFLOW_DIR"/*.yml)

for file in "${YAML_FILES[@]}"; do
    if ! yamllint "$file"; then
        echo "YAML syntax error in $file"
        exit 1
    fi
done

echo "All workflow files have valid YAML syntax."