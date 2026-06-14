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

# Action ensure_container_network

Use this when one setup step really owns shared external Docker network readiness and should not
fall back to shell `docker network inspect ... || docker network create ...` glue.

This example shows:

- `action.kind: ensure_container_network`
- explicit host `requirements.tools.docker`
- one finite native setup lane
- `workflows.<name>.prepare.action`

Why this exists:

- some real repos need one shared Docker network before Compose-managed projects can attach
- that ownership should stay declarative and inspectable instead of being hidden in shell
- workflow-owned host preparation can stay inline through `prepare.action` instead of forcing a helper task

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
