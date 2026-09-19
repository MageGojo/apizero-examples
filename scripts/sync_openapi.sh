#!/usr/bin/env bash
# OpenAPI 已下线。现在用 sitemap + raw.md 重导接口清单。
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/export_interfaces.py
