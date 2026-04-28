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

An advanced execution example where two container workloads intentionally share one ota-managed local backend boundary:

- `dev` runs the primary API producer
- `sandbox` runs a co-located helper app that targets `dev` through `address_view: internal`

## Why this exists

- shows the actual slice-2 surface without pretending `depends_on` or matching contexts are enough
- keeps same-backend locality explicit instead of implied by shell glue
- demonstrates `execution.shared_backends.<name>` plus `runtime.backend_binding`
- demonstrates the first shipped truthful `address_view: internal` slice for co-located shared-backend workloads
- makes the current shape rule visible: bound tasks must resolve one deterministic container shape

## Use when

- a producer service and a co-located helper app should intentionally reuse one persistent local container backend
- those workloads resolve one backend-shared image, isolation shape, and memory shape while keeping workload-local listeners and publications honest
- you want ota to own reuse/recreate semantics for that backend boundary
- you want a contract-level example of `runtime.backend_binding` plus `address_view: internal` that validates today

## Contract shape

This example uses:

- `execution.shared_backends.workbench` as the shared container boundary
- `tasks.dev.runtime.backend_binding: workbench`
- `tasks.sandbox.runtime.backend_binding: workbench`
- `tasks.sandbox.targets.api` with `address_view: internal`
- workload-local listeners and commands, while the backend-shared image/isolation/memory shape stays deterministic

## Try this

```bash
ota doctor
ota validate .
ota run dev
ota run sandbox
ota run sandbox --base-url https://staging.example.com
```

## What to notice

- ota can reuse one persistent backend identity across all bound workloads instead of treating each task as its own unrelated container
- the shared backend is declared explicitly under `execution.shared_backends`, not inferred from matching contexts
- `sandbox` can target `dev` through `address_view: internal` because both workloads share one declared container backend boundary
- `sandbox` still keeps `base_url` as an explicit operator override channel when it must point somewhere else
- current validation is strict: if bound tasks conflict on in-backend bind endpoints or fixed host publications, ota rejects the contract instead of pretending the workloads can coexist
- pair this with `../task-target-binding/` when you want the slice-1 target-binding surface as well
- pair this with `../shared-local-backend-fulfillment/` when you also want ota to prepare the effective backend requirement union on the `ota run` path
