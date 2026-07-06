#!/usr/bin/env bash
set -euo pipefail

mkdir -p openapi
curl -fsSL "https://apizero.cn/openapi.json" -o openapi/apizero-openapi.json
echo "Saved openapi/apizero-openapi.json"

