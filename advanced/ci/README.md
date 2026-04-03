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

# CI examples

This theme shows how serious teams keep CI thin while Ota owns repo truth, setup, and release logic.

## What this teaches

- the CI system decides when to run
- Ota decides what the repo needs
- the contract stays close to execution
- provider-specific YAML stays thin and explicit

## Folders

- `template/` - shared CI contract pattern
- `github-actions/` - GitHub Actions workflow example
- `release-only/` - release-dispatch-only variant
- `jenkins/` - Jenkins pipeline example
- `circleci/` - CircleCI pipeline example

## Read first

1. `template/README.md`
2. `template/ota.yaml`
3. one provider-specific folder

## Rule

Keep CI orchestration in the provider file and repo truth in `ota.yaml`.
