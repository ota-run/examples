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
   You may not use this file except in compliance with the License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.

   If you need additional information or have any questions, please email: os@ota.run
-->

# Action build_container_image

Use this when a direct task owns Dockerfile-backed local image materialization for a declared
container or Compose lane and should not fall back to opaque `docker build` shell glue.

This example shows:

- `action.kind: build_container_image`
- explicit Dockerfile, context, and local tag ownership
- explicit host Docker and network-effect posture
- a finite image-build task that remains outside routine agent-safe execution

The action executes `docker build --file <file> --tag <tag> <context>` from the repository root.
It is deliberately a direct task action rather than an `ensure_bundle` or `prepare.steps` entry:
local image materialization is execution with Docker side effects, not idempotent host bootstrap.

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
