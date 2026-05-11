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

# Python service template

A copyable starting point for a Python service repo that needs explicit runtime expectations and a clean setup loop.

## Why this exists

- keeps interpreter and tool expectations explicit
- gives `ota doctor` enough signal to guide setup
- shows one honest acquisition lane for uv instead of assuming every machine already has it
- makes test and lint entrypoints predictable
- helps a Python team avoid “works on my machine” setup drift
- makes the environment explain itself before the first command runs

## Use when

- your repo uses Python and uv
- you want a clear setup/test loop
- you want agents to know what is safe to change and verify
- you want the repo to say exactly how uv becomes available on a clean machine
- you want the repo to explain its own environment instead of relying on a README paragraph somewhere else

## Try this

```bash
ota doctor
ota validate .
ota up --dry-run
ota up
ota run test
```

## What this teaches

- `tools.uv.acquisition.provider: command` keeps the uv install lane explicit and selectable
- `tasks.<name>.requirements.tools` scopes uv to the setup, lint, and test paths that actually need it
- `workflows.default` gives `ota up` one clear setup lane instead of making users infer which task is the front door
