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

# Scheduled validation example

A GitHub Actions example where a scheduled job checks contract health and repo readiness with Ota.

## Why this exists

- shows how to keep scheduled checks thin
- makes drift and readiness visible on a timer
- teaches that Ota can be the same contract path in scheduled CI

## Use when

- you want nightly contract validation
- you want a lightweight recurring health check

## Copy these files

- [ota.yaml](ota.yaml)
- [.github/workflows/scheduled.yml](.github/workflows/scheduled.yml)

## Try this

```bash
ota validate .
ota doctor
ota run setup
ota run ci
```
