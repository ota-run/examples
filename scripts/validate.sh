#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

validate_contracts() {
  while IFS= read -r file; do
    ota validate "$(dirname "$file")"
  done < <(find . -name ota.yaml -not -path './.git/*' | sort)

  while IFS= read -r file; do
    ota workspace validate "$(dirname "$file")"
  done < <(find . -name ota.workspace.yaml -not -path './.git/*' | sort)
}

validate_local_links() {
  python3 - "$root" <<'PY'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
link_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
skip_prefixes = ('http://', 'https://', 'mailto:', 'tel:', '#', 'file://')
errors = []

for md in sorted(root.rglob('*.md')):
    if '.git' in md.parts or '.idea' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1].strip()
        if not target or target.startswith(skip_prefixes):
            continue
        target = target.split('#', 1)[0].split('?', 1)[0]
        if not target:
            continue
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            errors.append(f'{md.relative_to(root)}: broken local link -> {target}')

if errors:
    print('Broken local markdown links:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
PY
}

validate_contracts
validate_local_links
