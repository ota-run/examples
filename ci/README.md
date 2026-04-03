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

Use this theme when you want CI to stay thin while ota owns repo truth, setup, and release logic. It is the clean choice when workflows keep drifting, release steps are getting copied between providers, or you want one contract that survives runner changes.

This matters when pipeline steps drift across providers, release behavior gets copied into shell scripts, or different runners need the same repo contract without extra explanation.

## What this teaches

- the CI system decides when to run
- ota decides what the repo needs
- the contract stays close to execution
- provider-specific YAML stays thin and explicit
- release intent stays reviewable instead of hiding in ad hoc glue
- teams can keep the same release shape across GitHub Actions, Jenkins, and CircleCI

## Folders

- `template/` - shared CI contract pattern
- `github-actions/` - GitHub Actions workflow example
- `github-actions/matrix-tests/` - GitHub Actions matrix example
- `github-actions/scheduled-validation/` - GitHub Actions schedule example
- `jenkins/` - Jenkins pipeline example
- `circleci/` - CircleCI pipeline example

## Read first

1. `template/README.md`
2. `template/ota.yaml`
3. one provider-specific folder

## Rule

Keep CI orchestration in the provider file and repo truth in `ota.yaml`.
Install ota explicitly in each workflow run; do not conditionally skip the install step based on a preinstalled binary.
