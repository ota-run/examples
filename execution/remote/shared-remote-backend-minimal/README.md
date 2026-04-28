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

# Minimal shared remote backend example

The smallest useful shared-remote example:

- `dev` runs the primary API service
- `sandbox` runs a helper service
- both intentionally reuse one ota-managed persistent remote backend boundary

## Why this exists

- gives a clean first example of `execution.shared_backends.<name>` on the remote plane
- shows `runtime.backend_binding` without layering in target activation first
- keeps the shared-remote-boundary idea explicit before moving into remote producer activation

## Use when

- two long-running tasks should intentionally share one remote execution boundary
- ota should own that shared boundary as the reusable unit instead of treating each task as unrelated remote execution
- you want the smallest copyable contract before adding remote target binding and activation

## Choose a provider

- `ssh` for a normal machine you already reach with SSH
- `tsh` for a Teleport-managed SSH target
- `kubectl` for a pod boundary you already operate through Kubernetes
- `daytona` for a Daytona-managed workspace

This minimal example uses `ssh`, but the same shared-backend model applies to the other shipped built-in providers.

## Do not use when

- tasks only need to point at an existing staging URL
- the shared remote boundary itself is not the story

## Try this

```bash
ota doctor
ota validate .
ota run dev
ota run sandbox
```

## What to notice

- the shared backend is declared once under `execution.shared_backends`
- each participating task opts in with `runtime.backend_binding: workbench`
- the remote boundary is explicit in contract instead of hidden in shell glue
- pair this with `../shared-remote-backend-activation/` when the helper should also ask ota to start or reuse the remote producer through `activation.mode: ensure_ready`
