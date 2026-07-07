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

# launch-runtime-projection

Use this when one long-running service task already declares canonical listener bind truth under
`runtime.listeners`, and the process launcher should consume that bind truth instead of duplicating
host/port flags in `launch.args`.

This reference shows the first shipped projection adapter:

- `launch.runtime_projection.adapter: uvicorn`

The launch body keeps only process identity:

- executable: `.venv/bin/uvicorn`
- app target: `web.app:app`

The listener keeps bind truth:

- `runtime.listeners.web:http.bind.address`
- `runtime.listeners.web:http.bind.port`

Ota then projects:

- `--host <bind.address>`
- `--port <bind.port>`

Use this only when the adapter is explicitly supported. Do not remove bind flags from arbitrary
servers unless the contract uses a shipped `launch.runtime_projection.adapter`.
