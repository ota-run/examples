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

# Release-only CI example

A CI pattern where the workflow is only responsible for release dispatch, while Ota owns the repo truth and release steps.

## Why this exists

- separates validation CI from release dispatch
- keeps manual or scheduled release paths explicit
- makes release intent easy to audit

## Use when

- you want a release workflow without a full CI matrix
- you want the release step to stay narrow and intentional

## Copy these files

- [ota.yaml](ota.yaml)
- [.github/workflows/release.yml](.github/workflows/release.yml)

## Try this

```bash
ota validate .
ota run setup
ota run ci
ota run version:bump --version minor
ota run release
```
