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

# Local topology examples

Use this theme when one task or helper app should target another repo-managed app by service identity instead of by guessed URLs.

## Why this exists

- keeps topology truth in `ota.yaml` instead of README caveats
- lets helper tasks target the repo-managed app without hardcoding `localhost` or `host.docker.internal`
- keeps operator overrides available when the helper needs to point somewhere else
- shows how target bindings and execution planes fit together without repo-local glue

## What this teaches

- how to use `tasks.<name>.targets.<target>` as the primary topology declaration
- how to keep `override_input` as an explicit operator override instead of the primary wiring surface
- how to use `activation.mode: ensure_ready` when ota should make the producer ready before the consumer runs
- how `OTA_TARGET_<TARGET>` works when no override input is needed
- when `address_view: host` is the honest choice for helper apps that may run in another execution plane
- when `execution.shared_backends.<name>` plus `runtime.backend_binding` make `address_view: topology` truthful for co-located long-running container tasks

## Folders

- `task-target-binding/` - advanced example showing one app service plus two consumers: one with `override_input`, one with `OTA_TARGET_*`
- `task-target-activation/` - advanced example showing `activation.mode: ensure_ready` on a host-view consumer that asks ota to make a persistent container producer service ready first
- `shared-local-backend-minimal/` - minimal example showing two long-running services intentionally reusing one shared backend boundary without adding fulfillment or policy-backed backend environment
- `shared-local-backend-native-minimal/` - minimal example showing two long-running native services intentionally reusing one shared host backend boundary without container image or policy-backed environment layers
- `shared-local-backend/` - advanced example showing a producer and a co-located helper intentionally sharing one backend so the helper can target the producer through `address_view: internal`
- `shared-local-backend-fulfillment/` - advanced example showing the same shared backend boundary with `fulfillment: run` so ota can prepare the effective runtime/tool union before bound tasks execute
- `shared-local-backend-environment/` - advanced example showing a shared backend that declares `environment.profile` so policy resolves the effective backend image while shared-backend identity stays explicit

## Read first

1. `task-target-binding/README.md`
2. `task-target-binding/ota.yaml`
3. `task-target-activation/README.md`
4. `task-target-activation/ota.yaml`
5. `shared-local-backend-minimal/README.md`
6. `shared-local-backend-minimal/ota.yaml`
7. `shared-local-backend-native-minimal/README.md`
8. `shared-local-backend-native-minimal/ota.yaml`
9. `shared-local-backend/README.md`
10. `shared-local-backend/ota.yaml`
11. `shared-local-backend-fulfillment/README.md`
12. `shared-local-backend-fulfillment/ota.yaml`
13. `shared-local-backend-environment/README.md`
14. `shared-local-backend-environment/ota.yaml`

## Rule

Declare the target relationship structurally first. Only use operator input as the override channel.
