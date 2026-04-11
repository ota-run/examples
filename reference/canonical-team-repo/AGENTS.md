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

# AGENTS.md

## Purpose

This repo is the advanced example for a serious Ota operating model. Keep agent work explicit,
safe, and aligned with the contract and the shared org policy.

## Working rules

- Use `ota doctor` first when the repo feels out of sync.
- Use `ota validate` after contract edits.
- Keep agent work inside the declared writable paths.
- Treat `setup`, `test`, and `docs:check` as the safe task surface.
- Use `release` only after the contract, docs, and validation steps are green.

## Repo boundaries

- Writable paths: `docs`, `src`, `tests`, `scripts`
- Protected paths: `ota.yaml`, `docs/decision-log.md`

## Review loop

- After changes, run the repo's declared verification tasks before handing work back.
- Keep repo knowledge in `docs/` instead of in ad hoc shell scripts or chat history.
