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

# Systemd host service

Use this when the real service owner is `systemd` on the host and Ota should derive lifecycle from
the declared unit instead of hiding `systemctl start`, `systemctl stop`, and `systemctl is-active`
inside shell glue.

This example shows the thin typed host-manager surface directly:

- `services.<name>.manager.kind: host`
- `services.<name>.manager.host.kind: systemd`
- `services.<name>.manager.host.unit`
- `services.<name>.manager.host.scope`
- `services.<name>.readiness.kind: systemd_active`

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
