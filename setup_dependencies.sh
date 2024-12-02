#!/bin/bash
# Ensure submodules are updated
git submodule update --init --recursive

# Navigate to the submodule directory
cd llm-reasoners

# Install the submodule as editable
pip install -e .
