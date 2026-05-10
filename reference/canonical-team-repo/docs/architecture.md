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

# Architecture

## Boundary rules

- `ota.yaml` defines readiness and execution.
- `docs/` defines durable operating knowledge.
- `tests/` proves behavior.
- `README.md` explains the shortest path to understanding.

## Design intent

- keep repo knowledge close to execution
- make the current operating model easy to audit
- avoid hidden conventions that only a few people remember
- let one reusable `docs` runtime surface carry the preview endpoint truth instead of repeating
  host URLs and readiness paths across tasks, checks, and workflows
- teach the surface model in a stable order:
  - simple task attachment first
  - workflow consumption second
  - external URL escape hatch only when the endpoint is outside Ota topology

## Decision rule

If a rule changes behavior, document it here before it becomes tribal knowledge.
