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

# Node service template

A copyable starting point for a real Node service repo that needs a clear contract, predictable setup, one explicit service front door, and a trustworthy `ota doctor` experience.

## Why this exists

- gives the repo a clear readiness contract
- keeps prepare, setup, dev, test, and aggregate verify behavior explicit
- shows one honest tool acquisition lane for pnpm instead of assuming a global install
- shows a real runtime surface and proof path instead of treating the service like a loose shell command
- makes agent-safe paths and verification visible up front
- helps a Node team standardize the first repo experience instead of rediscovering it in every project
- makes the first repo setup feel repeatable instead of tribal

## Use when

- your service uses Node and pnpm
- you want one contract for humans and agents
- you want `ota doctor` to explain missing runtime or tool issues clearly
- you want `ota up` to activate pnpm through Corepack only on the workflow paths that actually need it
- you want `ota up` to create `.env.local` from a committed template before normal setup begins
- you want `ota proof runtime --workflow app` to validate a real declared service surface
- you want setup and verification to feel repeatable across machines

## Try this

```bash
ota doctor
ota validate .
ota up --dry-run
ota up
ota run verify
ota proof runtime --workflow app
```

## What this teaches

- `tools.pnpm.acquisition` keeps the pnpm activation path attached to the tool instead of burying it in docs
- `workflows.default` makes the local app path explicit, so `ota up` and `ota proof runtime` target the same front door
- `workflows.app.prepare` keeps deterministic host file preparation separate from normal setup and runtime work
- `action.kind: copy_if_missing` lets the contract create `.env.local` without shell-specific glue
- `tasks.dev.launch.kind: command` keeps the long-running service start structured, so Ota can reason about launch separately from the declared runtime surface
- `tasks.verify.aggregate.tasks` gives the repo one named verification entrypoint without a fake `run: "true"` wrapper
- `surfaces.app` gives the local Node path one declared URL and readiness contract instead of repeating host URLs in prose
- `tasks.<name>.requirements.tools` scopes pnpm to the tasks that actually need it instead of turning every repo path into one flat prerequisite set
