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

# Ota extension examples

Use this theme when a repo needs explicit adapters for checks, exports, or custom remote execution and you want those boundaries to stay visible in the contract. This is the right fit when ad hoc scripts are no longer enough because the team needs a named, reviewable adapter with a clear job.

## Why this exists

- keeps adapter intent in the contract instead of hiding it in scripts
- gives humans a clear place to review repo-specific integration points
- gives agents structured context for the extra behavior around the core contract
- makes custom behavior part of the repo story instead of a side channel
- turns special-case behavior into something the whole team can inspect, run, and trust

## When to use it

- a repo needs a custom check or export adapter
- a repo wants a custom remote execution backend
- you want adapter boundaries to stay reviewable and explicit
- you want the repo to explain why the adapter exists, not just that it exists

## What this teaches

- how to keep `extensions` readable and stable
- how to separate repo contract, adapter contract, and task execution
- how to keep extension-powered behavior close to the repo it serves

## Folders

- `template/` - extension contract template
- `check-provider/repo-check/` - repo validation adapter example
- `export-provider/release-upload/` - release export adapter example
- `backend-provider/remote-shell-node-service/` - custom remote backend example

## Read first

1. `template/README.md`
2. `check-provider/repo-check/README.md`
3. `export-provider/release-upload/README.md`
4. `backend-provider/remote-shell-node-service/README.md`

## Rule

Keep adapter metadata in `ota.yaml` and keep the README at the use-case level.
