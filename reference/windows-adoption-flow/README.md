<!--
                █████
               ░░███
       ██████  ███████    ██████
      ███░░███░░░███░    ░░░░░███
     ░███ ░███  ░███      ███████
     ░███ ░███  ░███ ███ ███░░███
     ░░██████   ░░█████ ░░████████
      ░░░░░░     ░░░░░   ░░░░░░░░

   Copyright (C) 2026 — 2026, Ota. All Rights Reserved.

   DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.

   Licensed under the Apache License, Version 2.0. See LICENSE for the full license text.
   You may not use this file except in compliance with that License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.

   If you need additional information or have any questions, please email: os@ota.run
-->

# Windows-first adoption flow example

This is the Windows-oriented flagship starter. Use it when the repo is `.NET`-based, Windows and PowerShell are part of the real operating model, and you still want one explicit Ota contract that humans and agents can trust across platforms.

## Example type

- Windows-first flagship adoption starter
- Copyable `.NET` service example
- Cross-platform repo shape with explicit PowerShell release flow

## Why this exists

- gives Ota a believable Windows-first adoption story instead of a Unix-only one
- keeps `.NET`, PowerShell, docs checks, and release flow explicit in one contract
- shows how one task name can stay stable while the platform-specific command changes
- gives mixed Windows and Unix teams a copyable repo shape instead of ad hoc shell glue

## Use when

- the repo already exists and the team is Windows-heavy
- setup and release behavior are real, but buried in PowerShell scripts or team memory
- you want `.NET` readiness, test flow, and release steps to be visible before people run them
- you want one contract that works for both humans and agents

## What this teaches

- how `ota doctor` gives exact `.NET` remediation when the SDK is missing or wrong
- how `ota detect --dry-run` reviews `global.json` and project signals before you write changes
- how cross-platform task variants keep task meaning stable while the launcher changes
- how `ota agents --write` turns the contract into agent-facing repo guidance

## What is included

- `ota.yaml` - Windows-first adoption contract
- `global.json` - explicit `.NET` SDK signal for exact remediation
- `Directory.Build.props` - repo-wide compiler settings
- `src/` and `tests/` - a minimal app and test project users can fork
- `docs/windows-first.md` and `docs/release-checklist.md` - repo guidance the contract keeps honest
- `scripts/release.ps1` and `scripts/release.sh` - explicit release edges for Windows and Unix-like environments

## Copy these files

- Always copy: `ota.yaml`
- Copy for exact `.NET` detection and remediation: `global.json`, `Directory.Build.props`
- Copy for a fuller starter: `src/`, `tests/`, `docs/`, `scripts/`

## Try this

```bash
ota doctor .
ota explain .
ota detect --dry-run .
ota validate .
ota run test .
ota agents --write .
```

## Expected result

- `ota doctor` should make the `.NET` SDK requirement and next step obvious
- `ota detect --dry-run` should review the contract against `global.json` and the project files
- `ota run test` should stay one task name even though docs/release helpers differ by OS
- `ota agents --write` should give the repo explicit derived guidance for agents

## What Ota will tell you

Exact `.NET` remediation:

```text
Primary Blocker
Version mismatch for runtime: dotnet
Why: dotnet resolved to `9.0.x` but the contract requires `8.0.203`
Next: run `dotnet --list-sdks` and install SDK `8.0.203`, then rerun `ota doctor ./reference/windows-adoption-flow/ota.yaml`
```

Cross-platform review:

```text
WARN  Review contract drift
Why: repo signals no longer match the declared contract
» `tasks.docs:check` differs from repo signals
```

## Important note about detect

- `ota detect` should infer the `.NET` SDK, starter setup/build/test tasks, and the shell-side release edge from repo-local signals
- the remaining drift here is intentional: `docs:check` stays human-authored because the contract carries a cross-platform documentation guardrail, not just raw repo inference
- keep the Windows PowerShell variant in the contract even when the preview mainly proves the repo shape and Unix-compatible default task

## Edit first

- `project.name` and `project.description`
- `runtimes.dotnet`
- `tasks.setup`, `tasks.build`, `tasks.test`, `tasks.docs:check`, and `tasks.release`
- `global.json` SDK version
- `scripts/release.ps1` and `scripts/release.sh`
- `agent.safe_tasks`, `agent.verify_after_changes`, `agent.writable_paths`, and `agent.protected_paths`
