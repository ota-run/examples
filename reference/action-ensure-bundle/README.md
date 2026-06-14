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

# Action ensure_bundle

Use this when one setup step needs more than one deterministic setup action and you do not want
to fall back to shell orchestration.

This example shows:

- `action.kind: ensure_bundle`
- bundled `ensure_container_network`
- bundled `copy_if_missing`
- bundled `ensure_env_file`
- bundled `ensure_directory`
- bundled `ensure_file`
- `workflows.<name>.prepare.task`

Why this exists:

- some repos need a small bundle of setup actions, not one isolated env mutation
- that should still be one governed, ordered, idempotent contract body
- workflow preparation should stay finite and inspectable

Open [`ota.yaml`](ota.yaml) for the exact contract shape.

The companion files:

- [`.env.example`](.env.example) is the seed template copied into `.env.local`
