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

# Node service in Ota remote execution mode

A copyable starting point for a Node service that runs setup and tests on a remote host through Ota.

## Why this exists

- keeps the execution boundary explicit instead of hiding it in ad hoc scripts
- lets teams run the same repo contract on a remote host without changing task intent
- gives humans and agents a realistic remote pattern to copy

## Use when

- the repo should run on a team host or sandbox
- the local machine should not own the execution environment
- you want remote execution to stay reviewable and predictable

## Try this

```bash
ota doctor
ota validate .
ota run setup
ota run test
```

