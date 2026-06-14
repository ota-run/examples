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

# Action ensure_env_file

Use this when one setup step really is deterministic env-file bootstrap and normalization, not
shell copy plus `sed`.

This example shows:

- `action.kind: ensure_env_file`
- `action.template`
- `action.vars.<KEY>.value`
- `action.vars.<KEY>.from_env`
- `action.vars.<KEY>.random`
- `action.vars.<KEY>.mode: replace`
- `action.vars.<KEY>.mode: remove`
- `workflows.<name>.prepare.action`

Why this exists:

- `.env` bootstrap is one of the most common places repos hide shell glue
- env key replacement, deletion, and secret generation should be governed and inspectable
- workflow-owned host preparation can stay inline through `prepare.action` instead of forcing a helper task

Open [`ota.yaml`](ota.yaml) for the exact contract shape.

The companion files:

- [`.env.example`](.env.example) is the immutable seed template
