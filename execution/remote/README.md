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

# ota remote execution examples

Use this theme when ota should run repo tasks off-host, or when multiple remote workloads should intentionally share one declared remote backend boundary.

## Why this exists

- keeps the contract stable while execution moves elsewhere
- makes remote execution explicit and reviewable
- helps teams use a shared host, sandbox, or cluster without losing repo truth

## Use when

- the work should run on a team dev box, sandbox, or remote host
- the local machine is not the right execution location
- you want the remote boundary to be part of the ota contract
- you want to choose intentionally between plain remote execution and a shared remote backend

## What this teaches

- how to keep execution intent explicit through `execution.contexts`
- how to keep remote targets understandable to humans and agents
- how to preserve one repo contract across multiple execution locations
- how to decide when a plain remote context is enough and when the remote boundary itself should be shared
- how the shipped built-in providers map to real operator targets

## Choose a provider

- `ssh`: normal SSH-reachable machine such as `user@host`
- `tsh`: Teleport-managed SSH target such as `user@host`
- `kubectl`: pod boundary such as `pod/ota-dev`
- `daytona`: Daytona workspace target such as `sandbox-dev`

Use a plain remote execution context when the task just needs to run off-host.
Use a shared remote backend when multiple long-running tasks intentionally reuse one remote execution boundary and ota should own reuse, targeting, and readiness there.

## Folders

- `template/` - remote execution template
- `shared-remote-backend-minimal/` - minimal example showing two long-running tasks intentionally reusing one persistent remote backend boundary
- `shared-remote-backend-activation/` - advanced example showing a helper task targeting a remote producer through one shared backend with `activation.mode: ensure_ready`
- `ssh-node-service/` - SSH-backed Node service remote execution example
