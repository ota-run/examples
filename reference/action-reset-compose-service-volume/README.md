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

# Action reset_compose_service_volume

Use this when one destructive host-side recovery or local-reset lane really owns resetting a
Compose-managed service volume and should not hide that behavior in shell `docker compose stop/rm`
plus `docker volume rm` glue.

This example shows:

- `action.kind: reset_compose_service_volume`
- task-owned Compose file and project-name truth under `action.compose.*`
- explicit host `requirements.tools.docker`
- destructive state ownership kept outside routine agent-safe lanes

Why this exists:

- some repos need an explicit "fresh local Postgres" or similar data-reset lane
- that is not the same thing as generic `docker compose down`
- the stop/rm/volume-reset/restart sequence should stay declarative and reviewable instead of
  disappearing into shell glue
- adapter-owned Compose inputs still matter on this lane because Ota needs the right Compose root,
  file stack, and project name while it performs the reset

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
