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

# Task prepare: orchestrated hydration

Use this when the truthful setup lane is still first-class dependency hydration, but the selected
environment is mediated by a declared orchestrator such as `devbox`.

This example shows the shipped slice:

- `orchestrators.devbox`
- `tasks.<name>.prepare.kind: dependency_hydration`
- `tasks.<name>.execution.orchestrator.mode: exec`
- `toolchains.node.package_managers.pnpm`
- explicit `effects.network_kind: dependency_hydration`

Why this exists:

- the repo truth is not “run raw pnpm on the ambient host”
- the repo truth is “hydrate dependencies inside the declared devbox environment”
- setup should stay structural and machine-readable instead of falling back to `run: devbox run -- pnpm install`

Important boundary:

- command-backed `prepare.kind: dependency_hydration` and `prepare.kind: tool_bootstrap` can use
  orchestrator `mode: exec`
- mixed/native `prepare.kind: sequence` is still outside this slice until Ota has step-level
  prepare execution ownership

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
