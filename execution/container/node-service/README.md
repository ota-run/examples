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

# Node service in Ota container mode

A copyable starting point for a Node service that runs setup and tests in Ota container mode.

## Why this exists

- keeps local and CI runtime behavior aligned
- makes the execution boundary obvious
- gives `ota doctor` and `ota run` a stable path
- helps a team standardize Node setup without turning the README into a shell-script graveyard

## Use when

- host setup drifts from CI
- you want everyone to run the same container image
- you want Ota to orchestrate container-backed setup and verification
- you want the first commands to work the same way on every machine

## Try this

```bash
ota doctor
ota validate .
ota run setup
ota run test
```
