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

# Container execution mode examples

Use this theme when you want ota to run repo tasks inside a dedicated container execution context.

## Why this exists

- keeps setup and verification repeatable across machines
- shows when container execution is the boundary, not the repo truth
- gives humans and agents the same container-backed path

## What this teaches

- how to keep container execution explicit through `execution.contexts`
- how to make host drift less relevant
- how to keep `ota.yaml` as the repo contract even when ota runs tasks in a container context

## Folders

- `template/` - shared container contract pattern
- `node-service/` - real Node service example using a container execution context

## Read first

1. `template/README.md`
2. `template/ota.yaml`
3. `node-service/README.md`
4. `node-service/ota.yaml`

## Rule

Keep the container runner thin and put repo truth in `ota.yaml`.
