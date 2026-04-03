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

# Python service with OS-specific task variants

This example shows how Ota keeps one repo contract stable while selecting the right launcher for each operating system. Use it when the task meaning is the same everywhere, but the command you must run is not.

## Why this matters

- avoids hiding platform choices inside shell scripts
- keeps Windows and Unix behavior explicit and reviewable
- gives agents one task name to run without guessing the launcher
- reduces drift when contributors work from different operating systems

## When to use it

- your Python repo supports Windows and Unix-like systems
- the workflow is identical, but `python3` is not always the right launcher
- you want OS differences visible in the contract instead of implied by the shell

## What is included

- `ota.yaml` with OS-specific task variants
- `requirements.txt` with the test dependency set
- `tests/test_smoke.py` as a minimal verification example

## Start here

1. Open `ota.yaml`
2. Read the `setup` and `test` task notes
3. Run `ota doctor`
4. Run `ota validate`
5. Run `ota tasks --use`
6. Run `ota run setup`
7. Run `ota run test`

## What to expect

- Ota keeps the task names stable
- Windows uses `py -3`
- Unix-like systems use `python3`
- the contract stays readable even when the launcher changes
