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

# Minimal shared local backend example

The smallest useful shared-backend example:

- `dev` runs the primary API service
- `sandbox` runs a helper service
- both intentionally reuse one ota-managed persistent container backend

## Why this exists

- gives a clean first example of `execution.shared_backends.<name>`
- shows `runtime.backend_binding` without layering in fulfillment or policy-backed backend environment
- keeps the shared-boundary idea explicit before moving into richer local-topology patterns

## Use when

- two long-running container tasks should intentionally share one backend boundary
- ota should own reuse of that boundary instead of creating unrelated per-task containers
- you want the smallest copyable contract that still shows the shared-backend model honestly

## Do not use when

- tasks are independent and only need a normal published URL
- target binding alone is enough and the backend boundary itself is not the story

## Try this

```bash
ota doctor
ota validate .
ota run dev
ota run sandbox
```

## What to notice

- the shared backend is declared once under `execution.shared_backends`
- each participating task opts in with `runtime.backend_binding: workbench`
- both tasks keep their own commands and listeners while ota treats the backend boundary as the reusable unit
- pair this with `../shared-local-backend/` when you want the next step that adds truthful co-located target binding through `address_view: internal`
- pair this with `../shared-local-backend-fulfillment/` when the shared backend also needs run-path preparation
