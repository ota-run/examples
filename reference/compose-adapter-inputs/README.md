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
- `services.<name>.manager.files`
- `services.<name>.manager.env_files`
- `env.profiles.<name>.render.dotenv`
- `prepare.source.compose`
- `runtime.listeners.<name>.project.publication.compose.service`
- `tasks.<name>.variants.<i>.env`
- `tasks.<name>.variants.<i>.adapter_inputs.overlays.compose.*`

Why this exists:

- the repo truth is not only `docker compose up`
- the truthful Compose root may be a repo subdirectory
- the env interpolation file, compose file stack, profile selection, and project naming all matter
- those inputs should not be hidden in `cd docker && ...`, `--project-directory`, `--env-file`,
  `-f`, `--profile`, or `-p` shell glue
- when a native compose lane also needs the real host repo path or host uid/gid, prefer ota-owned
  env templates such as `${OTA_HOST_WORKSPACE}`, `${OTA_HOST_UID}`, and `${OTA_HOST_GID}` over
  shell `pwd`, `id -u`, or `id -g` glue
- workflow-owned overlays and task-owned compose additions should stay separate and inspectable
- when a managed Compose service itself depends on a stable Compose file or env-file stack, keep
  that ownership on `services.<name>.manager.files` / `.env_files` instead of pushing it back into
  shell or pretending every Compose input belongs to the runnable task path
- when one OS keeps the same task body but needs different host-derived env or a different Compose
  file, env-file, or profile set, use `tasks.<name>.variants.<i>.env` and/or
  `tasks.<name>.variants.<i>.adapter_inputs` instead of cloning the whole task body into
  shell-only OS variants
- when dependency hydration truthfully runs inside a Compose service, keep the typed package lane
  under `prepare.source.kind: ...` and use `prepare.source.compose` only as the service wrapper
- in that shape the host prerequisite is still the Compose engine, so keep
  `requirements.tools.docker` explicit and do not add fake host `requirements.toolchains.node`
  just because the in-service command is `npm ci`
- when the durable install state lives in a Compose volume instead of a repo path, declare it
  under `effects.adapter_state` with a token such as `compose_volume:node_modules` instead of
  faking repo writes under `effects.writes`
- if the lane also owns destructive service-data reset, keep that as
  `action.kind: reset_compose_service_volume` instead of burying `docker compose stop/rm` plus
  `docker volume rm` in the task body
- if a native structured Docker Compose lane owns the published host URL for one service, declare
  that mapping under `runtime.listeners.<name>.project.publication.compose.service` so one-run
  `ota run <task> --host-port <port>` can remap the published host port without changing the
  workload's internal bind port or editing compose YAML

Native publication example:

```yaml
tasks:
  compose:native:published:
    adapter_inputs:
      compose:
        cwd: docker
        files:
          - docker/docker-compose.yml
    compose:
      kind: up
      detach: true
      services:
        - published
    runtime:
      kind: service
      listeners:
        http:
          protocol: http
          bind:
            address: 0.0.0.0
            port:
              mode: fixed
              value: 3000
          project:
            host:
              address: 127.0.0.1
              primary: true
              port:
                mode: fixed
                value: 3000
              path: /
            publication:
              compose:
                service: published
```

That shape lets ota rewrite the published Docker Compose host port for one run:

```bash
ota run compose:native:published --host-port 4000
```

The service still binds internally to `3000`; ota only remaps the published host port for that
run.

Host-derived env example:

```yaml
tasks:
  compose:up:
    env:
      SOURCE_ROOT: ${OTA_HOST_WORKSPACE}
      HOST_UID: ${OTA_HOST_UID}
      HOST_GID: ${OTA_HOST_GID}
    launch:
      kind: command
      exe: docker
      args:
        - compose
        - up
```

OS-scoped adapter overlay example:

```yaml
tasks:
  compose:linux:up:
    adapter_inputs:
      overlays:
        compose:
          cwd: docker
          files:
            - docker/docker-compose.yml
    launch:
      kind: compose
      action: up
      services:
        - api
    variants:
      - when:
          os: linux
        env:
          CURRENT_UID: ${OTA_HOST_UID}:${OTA_HOST_GID}
        adapter_inputs:
          overlays:
            compose:
              env_files:
                - docker/.env.linux
              files:
                - docker/docker-compose.linux.yml
```

Open [`ota.yaml`](ota.yaml) for the exact contract shape.

The companion files:

- [`docker/docker-compose.yml`](docker/docker-compose.yml) are the task-owned base Compose services
- [`docker/docker-compose.override.yml`](docker/docker-compose.override.yml) is the workflow-owned overlay
- [`docker/.env.example`](docker/.env.example) is the immutable template rendered into `.env.compose`
