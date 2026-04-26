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

# Shared local backend example

An advanced execution example where two long-running container tasks intentionally share one ota-managed local backend boundary:

- `dev` runs the primary API profile
- `dev:debug` runs the same service shape with a different operator-facing command profile
- both tasks bind to the same declared shared local backend identity

## Why this exists

- shows the actual slice-2 surface without pretending `depends_on` or matching contexts are enough
- keeps same-backend locality explicit instead of implied by shell glue
- demonstrates `execution.local_backends.<name>` plus `runtime.backend_binding`
- makes the current shape rule visible: bound tasks must resolve one deterministic container shape

## Use when

- multiple long-running task entrypoints should intentionally reuse one persistent local container backend
- those entrypoints resolve the same container image, publications, isolation paths, and memory shape
- you want ota to own reuse/recreate semantics for that backend boundary
- you want a contract-level example of `runtime.backend_binding` that validates today

## Contract shape

This example uses:

- `execution.local_backends.workbench` as the shared container boundary
- `tasks.dev.runtime.backend_binding: workbench`
- `tasks.dev:debug.runtime.backend_binding: workbench`
- identical listener/publication shape across both bound tasks so the shared backend stays deterministic

## Try this

```bash
ota doctor
ota validate .
ota run dev
ota run dev:debug
```

## What to notice

- ota can reuse one persistent backend identity across both long-running tasks instead of treating each task as its own unrelated container
- the shared backend is declared explicitly under `execution.local_backends`, not inferred from matching contexts
- current slice-2 validation is strict: if bound tasks resolve different image/publication/isolation/memory shape, ota rejects the contract instead of pretending the tasks are truly co-located
- pair this with `../task-target-binding/` when you want the slice-1 target-binding surface as well
- pair this with `../shared-local-backend-fulfillment/` when you also want ota to prepare the effective backend requirement union on the `ota run` path
