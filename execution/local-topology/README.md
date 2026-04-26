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
- how `OTA_TARGET_<TARGET>` works when no override input is needed
- when `address_view: host` is the honest choice for helper apps that may run in another execution plane
- when `execution.local_backends.<name>` plus `runtime.backend_binding` make `address_view: topology` truthful for co-located long-running container tasks

## Folders

- `task-target-binding/` - advanced example showing one app service plus two consumers: one with `override_input`, one with `OTA_TARGET_*`
- `shared-local-backend/` - advanced example showing two long-running container tasks intentionally sharing one backend so a helper app can target the producer through `address_view: topology`
- `shared-local-backend-fulfillment/` - advanced example showing the same shared backend boundary with `fulfillment: run` so ota can prepare the effective runtime/tool union before bound tasks execute

## Read first

1. `task-target-binding/README.md`
2. `task-target-binding/ota.yaml`
3. `shared-local-backend/README.md`
4. `shared-local-backend/ota.yaml`
5. `shared-local-backend-fulfillment/README.md`
6. `shared-local-backend-fulfillment/ota.yaml`

## Rule

Declare the target relationship structurally first. Only use operator input as the override channel.
