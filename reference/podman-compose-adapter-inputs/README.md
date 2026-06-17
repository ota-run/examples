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

# Podman compose adapter inputs

Use this when the real contract truth is `podman compose`, not `docker compose`, and the adapter
root, env-file interpolation, file stack, profiles, and project naming should stay first-class in
the contract.

This example shows the Podman compose ownership surface directly:

- `services.<name>.manager.engine: podman`
- `tasks.<name>.adapter_inputs.compose.cwd`
- `tasks.<name>.adapter_inputs.compose.env_files`
- `tasks.<name>.adapter_inputs.compose.files`
- `tasks.<name>.adapter_inputs.compose.profiles`
- `workflows.<name>.adapter_inputs.compose.cwd`
- `workflows.<name>.adapter_inputs.compose.files`
- `workflows.<name>.adapter_inputs.compose.profiles`
- `workflows.<name>.adapter_inputs.compose.project_name`

Why this exists:

- Podman compose is a real repo truth, not a Docker-only special case
- the truthful compose root may still be a repo subdirectory
- env interpolation files, compose file stacks, profile selection, and project naming still matter
- those inputs should not be hidden in `cd compose && ...`, `--env-file`, `-f`, or `-p` shell glue

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
