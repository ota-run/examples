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

# Bake adapter inputs

Use this when a task or workflow really owns `docker buildx bake` file selection and that truth
should stay in the contract instead of shell `-f` flags.

This example shows the Bake surfaces together:

- `tasks.<name>.adapter_inputs.bake.cwd`
- `tasks.<name>.adapter_inputs.bake.files`
- `workflows.<name>.adapter_inputs.bake.cwd`
- `workflows.<name>.adapter_inputs.bake.files`

Why this exists:

- the repo truth is not only `docker buildx bake app`
- the truthful Bake root may be a repo subdirectory
- Bake file selection often has a base file plus workflow or task overlays
- those inputs should not be hidden in `cd docker && docker buildx bake ...` or
  `docker buildx bake -f ... -f ...` shell glue
- workflow-owned base Bake files and task-owned narrower overlays should stay separate

Open [`ota.yaml`](ota.yaml) for the exact contract shape.

The companion files:

- [`docker/docker-bake.hcl`](docker/docker-bake.hcl) is the base Bake file
- [`docker/docker-bake.ci.hcl`](docker/docker-bake.ci.hcl) is a task-owned CI overlay
- [`docker/docker-bake.platform.hcl`](docker/docker-bake.platform.hcl) is a workflow-owned platform overlay
- [`docker/docker-bake.release.hcl`](docker/docker-bake.release.hcl) is a workflow-owned release overlay
