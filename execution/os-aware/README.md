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

# Ota OS-aware execution examples

Use this theme when the repo means the same thing everywhere, but the launcher, shell, or platform-specific command syntax does not. It keeps OS decisions explicit in the contract instead of burying them in ad hoc scripts.

## Why this exists

- shows how Ota handles real cross-platform differences without changing task meaning
- keeps Windows and Unix launcher choices visible to humans and agents
- reduces the chance that platform-specific shell assumptions leak into repo logic
- makes the execution path more predictable when teams or CI run on different operating systems

## What this teaches

- how to express OS-specific task variants cleanly
- how to keep one task name while selecting the right launcher per platform
- how to make cross-platform repos easier for agents to execute safely

## Folders

- `python-service/` - Python repo with OS-specific launcher variants

## Read first

1. `python-service/README.md`
2. `python-service/ota.yaml`

## Rule

Keep OS differences in `ota.yaml` so the task intent stays stable and the launcher choice stays explicit.
