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

# Ota execution mode examples

Use this theme when Ota should run repo tasks through a backend boundary instead of only on the local host.

## Why this exists

- shows when execution boundaries matter more than local convenience
- keeps task intent stable while the runner changes
- gives humans and agents one place to learn backend-backed execution patterns

## What this teaches

- how to keep container execution explicit
- how to keep remote execution explicit
- how to preserve one repo contract across multiple execution locations

## Folders

- `container/` - container execution mode examples
- `remote/` - remote execution mode examples

## Read first

1. `container/README.md`
2. `container/template/README.md`
3. `container/node-service/README.md`
4. `remote/README.md`

## Rule

Keep the backend thin and put repo truth in `ota.yaml`.
