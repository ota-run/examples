#
#                █████
#               ░░███
#       ██████  ███████    ██████
#      ███░░███░░░███░    ░░░░░███
#     ░███ ░███  ░███      ███████
#     ░███ ░███  ░███ ███ ███░░███
#     ░░██████   ░░█████ ░░████████
#      ░░░░░░     ░░░░░   ░░░░░░░░
#
#   Copyright (C) 2026 — 2026, Ota. All Rights Reserved.
#
#   DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
#   Licensed under the Apache License, Version 2.0. See LICENSE for the full license text.
#   You may not use this file except in compliance with that License.
#   Unless required by applicable law or agreed to in writing, software distributed under the
#   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#   either express or implied. See the License for the specific language governing permissions
#   and limitations under the License.
#
#   If you need additional information or have any questions, please email: os@ota.run

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "file://")


def run_ota(root: Path, args: list[str]) -> str:
    process = subprocess.run(
        ["ota", *args],
        cwd=root,
        capture_output=True,
        text=True,
    )
    payload = process.stdout.strip() or process.stderr.strip()
    if process.returncode != 0:
        print(f"FAILED: ota {' '.join(args)}")
        if payload:
            print(payload)
        raise SystemExit(process.returncode)
    return payload


def require_ok_json(root: Path, args: list[str]) -> dict[str, object]:
    payload = run_ota(root, args)
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        print(f"FAILED: ota {' '.join(args)} returned non-JSON output")
        print(payload)
        raise SystemExit(1) from exc
    if not data.get("ok", False):
        print(f"FAILED: ota {' '.join(args)} reported ok=false")
        print(payload)
        raise SystemExit(1)
    return data


def require_loaded_policy(root: Path, repo_dir: Path) -> dict[str, object]:
    data = require_ok_json(root, ["policy", "--json", str(repo_dir)])
    if not data.get("loaded", False):
        print(f"FAILED: ota policy --json {repo_dir} reported loaded=false")
        print(json.dumps(data, indent=2))
        raise SystemExit(1)
    return data


def check_markdown_links(root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors: list[str] = []
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts or ".idea" in md.parts:
            continue
        checked += 1
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{md.relative_to(root)}: broken local link -> {target}")
    return checked, errors


def main() -> None:
    root = Path(sys.argv[1]).resolve()

    repo_contracts = sorted(root.rglob("ota.yaml"))
    workspace_contracts = sorted(root.rglob("ota.workspace.yaml"))
    policy_packs = sorted(root.rglob(".ota/org-policy.yaml"))

    require_ok_json(root, ["validate", "--json", "."])

    repo_contract_count = 0
    for contract in repo_contracts:
        if contract.resolve() == (root / "ota.yaml").resolve():
            continue
        require_ok_json(root, ["validate", "--json", str(contract.parent)])
        repo_contract_count += 1

    workspace_contract_count = 0
    for contract in workspace_contracts:
        require_ok_json(root, ["workspace", "validate", "--json", str(contract.parent)])
        workspace_contract_count += 1

    policy_pack_count = 0
    for policy_pack in policy_packs:
        repo_dir = policy_pack.parent.parent
        data = require_loaded_policy(root, repo_dir)
        policy_path = data.get("policy_path")
        if policy_path not in ("./.ota/org-policy.yaml", ".ota/org-policy.yaml"):
            print(f"FAILED: ota policy --json {repo_dir} reported unexpected policy_path")
            print(json.dumps(data, indent=2))
            raise SystemExit(1)
        policy_pack_count += 1

    markdown_count, link_errors = check_markdown_links(root)
    if link_errors:
        print("Broken local markdown links:")
        for error in link_errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Examples validation complete")
    print(f"Repo contracts: {repo_contract_count + 1} valid")
    print(f"Workspace contracts: {workspace_contract_count} valid")
    print(f"Policy packs: {policy_pack_count} valid")
    print(f"Markdown files: {markdown_count} checked")
    print("Flagship starters: reference/adoption-flow, reference/windows-adoption-flow")


if __name__ == "__main__":
    main()
