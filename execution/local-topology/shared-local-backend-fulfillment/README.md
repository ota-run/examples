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

# Shared local backend fulfillment example

An advanced execution example where multiple container tasks intentionally share one ota-managed backend and let ota prepare the effective backend requirement union on the actual run path.

## Why this exists

- shows the shipped slice-3 surface instead of repo-local bootstrap glue
- keeps backend preparation attached to the shared backend identity, not scattered across tasks
- demonstrates `execution.shared_backends.<name>.fulfillment: run`
- keeps the shared backend story honest by using two bound tasks that resolve the same container shape

## Use when

- one shared backend shape should satisfy multiple long-running tasks
- the backend needs a deterministic union of runtimes and tools before any bound task or dependency executes
- you want missing requirements to be classified as backend-preparation problems instead of generic task failures

## Contract shape

This example uses:

- root requirements for repo-wide Java plus Maven expectations
- context requirements for Node plus pnpm in the shared app container
- `execution.shared_backends.workbench.fulfillment: run`
- one primary service entrypoint bound to the shared backend

## Try this

```bash
ota doctor
ota validate .
ota run dev
```

## What to notice

- ota computes one effective requirement set for the shared backend before bound tasks run
- `fulfillment: none` would fail clearly on missing prerequisites; `fulfillment: run` lets ota attempt approved provisioning first
- dependency and hook tasks that share the backend benefit from the same preparation path because fulfillment runs before bound task execution proceeds
- this example is intentionally strict about shape equality; if you want the target-binding side of local topology, pair it with `../task-target-binding/` or `../shared-local-backend/`

## Contrast with slice 2

- use `../shared-local-backend/` when you only need explicit co-location and reuse semantics
- use this example when the backend itself also needs preparation on the `ota run` path
