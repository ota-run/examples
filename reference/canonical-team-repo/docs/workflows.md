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

# Workflows

This repo uses explicit ota workflows instead of asking contributors to infer the front door from a
flat task list.

## Declared paths

- `docs`
  - canonical local authoring path
  - setup task: `setup`
  - run task: `docs:preview`
  - readiness surface: `docs`
  - expose surface: `docs`
- `release`
  - release preparation path
  - setup task: `setup`
  - run task: `release`

## Human workflow

1. `ota doctor`
2. `ota validate`
3. `ota workflows`
4. `ota up --workflow docs` or `ota run docs:preview`
5. update docs when the operating model changes

## Surface progression in this repo

Use this repo's workflow path to learn the surface model in the right order:

1. `docs:preview` attaches the `docs` surface in the simple native list form
2. `workflows.docs.readiness.surfaces` proves that surface on the selected run task
3. `workflows.docs.exposes` resolves `{ surface: docs }` into the host URL
4. `checks.docs-preview-ready` shows when a reusable probe is the better fit than another inline
   runtime or workflow readiness block
5. external endpoints should stay as literal URL probes, not surfaces

## Agent workflow

1. read `ota.yaml`
2. read `docs/workflows.md`
3. run only safe tasks
4. verify after changes

## Principle

Use the repo's declared workflow before inventing a new path or guessing from task names alone.
