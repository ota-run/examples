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

import subprocess
import sys
from pathlib import Path


def run_plain(root: Path, args: list[str], allowed_exit_codes: set[int]) -> str:
    process = subprocess.run(
        ["ota", "--plain", *args],
        cwd=root,
        capture_output=True,
        text=True,
    )
    payload = process.stdout.strip() or process.stderr.strip()
    if process.returncode not in allowed_exit_codes:
        print(f"FAILED: ota --plain {' '.join(args)}")
        if payload:
            print(payload)
        raise SystemExit(process.returncode)
    return payload


def assert_contains(label: str, payload: str, needles: list[str]) -> None:
    missing = [needle for needle in needles if needle not in payload]
    if missing:
        print(f"FAILED: {label} is missing expected output")
        for needle in missing:
            print(f"- missing: {needle}")
        print(payload)
        raise SystemExit(1)


def main() -> None:
    root = Path(sys.argv[1]).resolve()
    examples = [
        ("reference/adoption-flow", "repo-with-services"),
        ("reference/windows-adoption-flow", "windows-first"),
        ("reference/canonical-team-repo", "canonical-advanced"),
    ]

    for rel_path, label in examples:
        validate = run_plain(root, ["validate", rel_path], {0})
        assert_contains(f"{label} validate", validate, ["VALIDATE", "VALID", "Next:"])

        doctor = run_plain(root, ["doctor", rel_path], {0, 1})
        assert_contains(f"{label} doctor", doctor, ["DOCTOR", "Verdict"])

        if rel_path == "reference/canonical-team-repo":
            env_report = run_plain(root, ["env", rel_path], {0, 1})
            assert_contains(
                f"{label} env",
                env_report,
                ["ENV", "Declared env sources", "DOCS_SITE_BASE_URL", "dotenv:.env.ota-example"],
            )

        detect = run_plain(root, ["detect", "--dry-run", rel_path], {0})
        assert_contains(
            f"{label} detect",
            detect,
            ["DETECT PREVIEW", "Existing contract comparison:", "Contract:", "Next:"],
        )

        agents = run_plain(root, ["agents", rel_path], {0})
        assert_contains(f"{label} agents", agents, ["AGENTS", "Target:", "Managed block:"])

        print(f"Dogfooded {rel_path}: validate, doctor, detect, and agents look healthy")


if __name__ == "__main__":
    main()
