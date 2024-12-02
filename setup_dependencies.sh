#!/bin/bash
# Ensure submodules are updated
git submodule update --init --recursive

# Navigate to the submodule directory
cd llm-reasoning-api/api/algorithms/llm-reasoners
# Install the submodule as editable
pip install -e .
