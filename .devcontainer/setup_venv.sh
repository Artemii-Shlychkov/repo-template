#!/bin/bash
set -euxo pipefail

python3 -m venv .venv

# Fix possible execute permission issues for macOS/Docker Desktop
chmod +x .venv/bin/*

.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -e .
