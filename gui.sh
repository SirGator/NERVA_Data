#!/usr/bin/env bash
set -euo pipefail
measurement_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$measurement_dir/GUI/server.py" --root "$measurement_dir" "$@"
