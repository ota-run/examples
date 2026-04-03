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

# GitHub Actions matrix tests

A GitHub Actions example where Ota owns the repo contract and the workflow fans out the test targets.

## Why this exists

- shows a real matrix pattern without losing contract clarity
- keeps each job explicit and repeatable
- teaches how to split tests by target while keeping Ota in control

## Use when

- you have multiple test targets in one repo
- you want CI fan-out without duplicating the contract

## Copy these files

- [ota.yaml](ota.yaml)
- [.github/workflows/matrix.yml](.github/workflows/matrix.yml)

## Try this

```bash
ota validate .
ota run setup
ota run test:web
ota run test:api
```
