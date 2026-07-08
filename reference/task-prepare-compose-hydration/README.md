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

# Task prepare: Compose-wrapped hydration

Use this when the dependency lane is still a first-class typed hydration surface, but the truthful
execution owner is a declared Compose service instead of the ambient host.

This example shows the shipped shape:

- `toolchains.node.package_managers.npm`
- `prepare.kind: dependency_hydration`
- `prepare.source.kind: node_package_manager`
- `prepare.source.compose.kind: run`
- `prepare.source.compose.service`
- `requirements.tools.docker`
- durable service-side state in `effects.adapter_state`

Why this exists:

- the repo truth is not "run raw npm on the host"
- the repo truth is "hydrate dependencies inside the app service"
- that should stay structural package-manager truth instead of shell `docker compose run ... npm ci`

Important boundary:

- keep Node package-manager ownership under `toolchains.node.package_managers.npm`
- keep package-manager truth under `prepare.source.kind: ...`
- keep service/container truth under `prepare.source.compose`
- do not duplicate host language toolchain requirements just because the in-container command is
  `npm`, `bundle`, `poetry`, or `uv`
- when the durable install state lives in a Compose volume, publish that under `effects.adapter_state`
  instead of faking repo writes

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
