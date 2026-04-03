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

# First week with Ota

This example shows the adoption path for a Java repo that already exists but does not yet have a clean Ota contract.

## Day 1

1. Run `ota doctor .` to see readiness gaps.
2. Run `ota explain .` to turn the findings into next steps.
3. Run `ota init --dry-run .` or `ota detect --dry-run .` to preview the contract.

## Day 2

1. Write the contract with `ota init` or `ota detect --write .`.
2. Run `ota validate .` to confirm the contract is valid.
3. Run `ota up .` to prepare the repo the same way every time.

## What success looks like

- setup steps live in `ota.yaml`
- validation steps are explicit
- task execution is discoverable through `ota tasks`
- the repo no longer depends on tribal knowledge for first success
