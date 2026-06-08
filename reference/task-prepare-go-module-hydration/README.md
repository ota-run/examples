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

# Task prepare: Go module hydration

Use this when one setup task is really Go module hydration, not generic shell glue and not a long-running service.

This example shows the shipped Go module `tasks.<name>.prepare` slice:

- `prepare.kind: dependency_hydration`
- `medium: package_dependencies`
- `source.kind: go_modules`
- explicit `requirements.toolchains: [go]`
- explicit `effects.network_kind: dependency_hydration`

Why this exists:

- the repo truth is "hydrate modules before build or test"
- that is finite setup work
- it should not be modeled as a service
- it should not be hidden in `run: go mod download`

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
