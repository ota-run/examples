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

# Compose adapter inputs

Use this when a task or workflow really owns Docker Compose adapter truth and that truth should stay in the contract instead of shell flags.

This example shows the newer Compose surfaces together:

- `tasks.<name>.adapter_inputs.compose.cwd`
- `tasks.<name>.adapter_inputs.compose.env_files`
- `tasks.<name>.adapter_inputs.compose.files`
- `tasks.<name>.adapter_inputs.compose.profiles`
- `tasks.<name>.adapter_inputs.compose.project_name`
- `workflows.<name>.adapter_inputs.compose.cwd`
- `workflows.<name>.adapter_inputs.compose.files`
- `workflows.<name>.adapter_inputs.compose.profiles`
- `workflows.<name>.adapter_inputs.compose.project_name`
- `workflows.<name>.env.compose_env_file_services`
- `env.profiles.<name>.render.dotenv`
- `prepare.source.compose`

Why this exists:

- the repo truth is not only `docker compose up`
- the truthful Compose root may be a repo subdirectory
- the env interpolation file, compose file stack, profile selection, and project naming all matter
- those inputs should not be hidden in `cd docker && ...`, `--project-directory`, `--env-file`,
  `-f`, `--profile`, or `-p` shell glue
- when a native compose lane also needs the real host repo path or host uid, prefer ota-owned
  env templates such as `${OTA_HOST_WORKSPACE}` and `${OTA_HOST_UID}` over shell `pwd` or
  `id -u` glue
- workflow-owned overlays and task-owned compose additions should stay separate and inspectable
- when dependency hydration truthfully runs inside a Compose service, keep the typed package lane
  under `prepare.source.kind: ...` and use `prepare.source.compose` only as the service wrapper
- in that shape the host prerequisite is still the Compose engine, so keep
  `requirements.tools.docker` explicit and do not add fake host `requirements.toolchains.node`
  just because the in-service command is `npm ci`
- if the lane also owns destructive service-data reset, keep that as
  `action.kind: reset_compose_service_volume` instead of burying `docker compose stop/rm` plus
  `docker volume rm` in the task body

Host-derived env example:

```yaml
tasks:
  compose:up:
    env:
      SOURCE_ROOT: ${OTA_HOST_WORKSPACE}
      HOST_UID: ${OTA_HOST_UID}
    launch:
      kind: command
      exe: docker
      args:
        - compose
        - up
```

Open [`ota.yaml`](ota.yaml) for the exact contract shape.

The companion files:

- [`docker/docker-compose.yml`](docker/docker-compose.yml) are the task-owned base Compose services
- [`docker/docker-compose.override.yml`](docker/docker-compose.override.yml) is the workflow-owned overlay
- [`docker/.env.example`](docker/.env.example) is the immutable template rendered into `.env.compose`
