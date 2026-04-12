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

# GitLab CI readiness-gate example

Use this when GitLab CI is the runner and you want a read-only readiness gate that keeps portable
annotations and archived receipts before any mutating setup or CI work runs.

## Why this exists

- shows the provider-neutral `doctor` plus plain annotations plus receipt pattern on GitLab CI
- keeps the merge-request gate read-only and archive-friendly
- demonstrates that GitHub-specific wrappers are optional, not required for good CI integration

## Use when

- GitLab CI is the runner
- the job should keep `.ota/ci/` and `.ota/receipts/` even when readiness is blocked
- the later CI job should only run after the readiness gate is clear

## Copy these files

- [ota.yaml](ota.yaml)
- [.gitlab-ci.yml](.gitlab-ci.yml)

## Try this

```bash
ota validate .
ota doctor
ota run setup
ota run ci
```
