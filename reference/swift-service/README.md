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

# Swift service reference

This is the advanced Swift example you fork when you want ota to shape a serious repo operating model, not just a starter contract. It shows how to make setup, verification, docs, and handoff explicit for a real Swift codebase.

## Why this exists

- gives a Swift repo one explicit readiness contract
- keeps package setup, build, and test behavior visible
- makes agent-safe paths and verification easy to review
- helps a team standardize the first serious repo experience instead of rediscovering it in every project
- makes the repo explain its own operating model

## Use when

- your service uses Swift Package Manager
- you want ota to explain missing toolchain or package issues clearly
- you want a repo shape that humans and agents can both trust
- you want setup, verification, and handoff to live close to the code

## What this teaches

- how a Swift repo makes its readiness contract explicit
- how `checks` make `ota doctor` fail fast when the Swift toolchain is missing
- how a team keeps `setup`, `build`, `test`, and `run` honest
- how to keep agent guidance close to the contract
- how to make the repo understandable without a separate ops wiki

## Read this first

1. [`ota.yaml`](ota.yaml)
2. [`docs/architecture.md`](docs/architecture.md)
3. [`docs/workflows.md`](docs/workflows.md)
4. [`docs/handoff.md`](docs/handoff.md)

## Structure

- `ota.yaml` - canonical repo contract and agent boundaries
- `Package.swift` - Swift package manifest
- `Sources/` - application code
- `Tests/` - verification code
- `docs/` - operational knowledge that should stay close to the repo

## Try this

```bash
ota validate .
ota doctor
ota run test
```

## Use this repo when

- you want a serious starting point, not a toy example
- you need a shared language for humans and AI agents
- you want to teach good ota usage through the repo shape itself
- you want a repo that feels production-adjacent from the first read
