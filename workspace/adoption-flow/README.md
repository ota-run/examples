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

# Workspace adoption flow

Use this example when you are introducing ota to several existing repos and want the workspace to feel like a deliberate operating model instead of a pile of clones. It shows how to get each repo ready first, then wire those repos into one explicit workspace contract.

## Why this matters

- keeps repo adoption and workspace bootstrap in the right order
- gives humans a clear first-week path instead of scattered tribal knowledge
- helps agents understand which repo to inspect first and which repos depend on each other
- turns multi-repo onboarding into a repeatable system instead of a checklist

## When to use it

- several repos need to become ready together
- each repo should be adopted with `ota doctor`, `ota explain`, `ota init` or `ota detect`, and `ota up` before the workspace is wired
- you want a workspace contract that stays readable when the repo count grows
- you want new contributors to know where the work starts and how readiness is supposed to land

## What is included

- `ota.workspace.yaml` with explicit repo paths and dependency ordering
- `docs/first-week.md` with the first repo-adoption sequence before workspace bootstrap

## Start here

1. Read `docs/first-week.md`.
2. Run `ota workspace validate .`.
3. Run `ota workspace tasks .`.
4. Run `ota workspace up` once the member repos are already adopted.

## What to expect

- each repo has its own readiness contract first
- the workspace contract explains ordering and shared bootstrap, not repo truth
- humans and agents can see the first week before the workspace becomes the default
