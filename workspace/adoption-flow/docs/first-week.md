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

# First week

Use this sequence when ota is being introduced to an existing multi-repo workspace.

## Per-repo adoption

For each repo, start with the repo-level adoption flow:

1. `ota doctor`
2. `ota explain`
3. `ota init --dry-run` or `ota detect --dry-run`
4. `ota init` or `ota detect`
5. `ota validate`
6. `ota up`

## Workspace bootstrap

After the member repos are ready:

1. `ota workspace validate .`
2. `ota workspace tasks .`
3. `ota workspace up`

## What this gives the team

- a repeatable way to onboard each repo before the workspace depends on it
- fewer surprises when the workspace grows
- clearer signals for humans and agents about what is already ready and what still needs adoption
