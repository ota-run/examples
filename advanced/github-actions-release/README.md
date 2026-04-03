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

# GitHub Actions release example

A production-oriented release pattern that uses `ota` as the orchestration entrypoint.

## Why this exists

- keeps CI and release orchestration explicit
- makes the release path reproducible
- gives a real example of `ota` driving the workflow

## Use when

- you want release automation in GitHub Actions
- you want a single repo-level orchestration command
- you want the release path to be visible and auditable

## Try this

```bash
ota validate .
ota run ci
ota run version:bump --version patch
```
