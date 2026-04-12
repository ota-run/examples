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

# Jenkins readiness-gate example

Use this when Jenkins is the runner and you want a blocking readiness stage that still archives
portable annotations and receipts before the pipeline stops.

## Why this exists

- shows the generic `doctor` plus plain annotations plus receipt pattern on Jenkins
- uses `post { always { ... } }` so artifacts survive blocked readiness runs
- keeps setup and CI stages behind an explicit readiness boundary

## Copy these files

- [ota.yaml](ota.yaml)
- [Jenkinsfile](Jenkinsfile)

## Try this

```bash
ota validate .
ota doctor
ota run setup
ota run ci
```
