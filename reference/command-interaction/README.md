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

# Command interaction

Use this when a finite command genuinely needs a human terminal, such as browser-based OAuth.

The example declares `command.interaction: required` for `wrangler login`.

- `ota run cloudflare:login` passes through a real native terminal.
- Agent, CI, container, remote, and non-TTY invocations refuse before execution.
- The task is deliberately not agent-safe.

Omitting the field uses `auto`, which passes through a human native terminal when available. Use
`forbidden` for deterministic captured commands. Do not use this field on `launch`, `run`, or
`script` bodies.
