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

# GitHub Action readiness example

Use this when you want GitHub Actions to show ota summaries, annotations, sticky PR comments, and
receipt artifacts, but you still want a separate execution job for real setup and CI work.

## Why this exists

- shows the clean split between read-only readiness gating and later execution
- demonstrates the official `ota-run/action@v1` wrapper instead of hand-written JSON glue
- keeps the PR surface compact while preserving direct ota control where the repo actually changes

## Use when

- pull requests need a read-only readiness receipt and human-friendly summary
- the repo wants annotations and an archived receipt artifact by default
- a later CI job still needs direct `ota validate`, `ota run setup`, or `ota run ci`

## Copy these files

- [ota.yaml](ota.yaml)
- [.github/workflows/readiness.yml](.github/workflows/readiness.yml)

## What this teaches

- `ota-run/action@v1` is the right surface for GitHub-native reporting
- direct `ota` commands still belong in the job that actually prepares or executes repo work
- job-local install state does not cross into a separate job

## Try this

```bash
ota validate .
ota doctor
ota run setup
ota run ci
```
