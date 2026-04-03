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

# CI template

Use this when you want a shared ota contract pattern for a CI system that you can copy into GitHub Actions, Jenkins, or CircleCI without rewriting the contract.

## Why this exists

- keeps `ota.yaml` consistent across providers
- shows the same repo flow regardless of CI runner
- makes the contract easy to copy into a real repo
- gives teams one place to review validation, setup, and release intent

## Use when

- you want a provider-neutral baseline
- you want to teach the ota contract before the workflow wrapper
- you want the same release shape even if the CI runner changes later

## Try this

```bash
ota validate .
ota run ci
ota run release
```
