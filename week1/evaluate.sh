#!/usr/bin/env bash
set -euxo pipefail
ulimit -s unlimited
python3 evaluate.py
