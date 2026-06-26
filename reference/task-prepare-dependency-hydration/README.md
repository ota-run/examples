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

# Task prepare: dependency hydration

Use this when one setup task is really dependency or image hydration, not generic shell glue and not a long-running service.

This example shows the docker image-hydration `tasks.<name>.prepare` slice:

- `prepare.kind: dependency_hydration`
- `medium: container_images`
- `source.kind: docker_compose`
- `prepare.source.files`
- `prepare.source.env_files`
- explicit `targets`
- `adapter_inputs.compose.cwd`
- `adapter_inputs.compose.files`
- explicit `requirements.tools.docker`
- explicit `effects.network_kind: dependency_hydration`

Why this exists:

- the repo truth is "hydrate these external images before startup"
- that is finite setup work
- it should not be modeled as a service
- it should not be hidden in `run: cd ... && docker compose pull ...`
- the follow-on setup task should keep compose root and file selection in `adapter_inputs.compose.*`

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
