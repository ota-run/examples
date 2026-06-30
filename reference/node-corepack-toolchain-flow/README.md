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

# Node Corepack toolchain flow

This is the dedicated public example for the shipped Corepack-backed Node toolchain boundary.

Use it when the repo wants Node runtime, `node` executable, and declared Corepack package-manager
activation under one `toolchains.node` owner.

## What this teaches

- `toolchains.node` is the owner for the managed Node runtime, `node` executable, and declared
  Corepack package managers
- `toolchains.node.fulfillment` separates capability truth from fulfillment truth
- `fulfillment.source: corepack` is the canonical public way to say the selected path should use Corepack activation
- Corepack-backed Node toolchains support `package_managers` plus selected-path `fulfillment.mode: run`
- `requirements.toolchains` now selects the Node runtime and declared Corepack package-manager lane
- `runtimes.node` should not be declared alongside `toolchains.node`
- `tools.node` should not be declared alongside `toolchains.node`
- package-manager tools such as `pnpm` should not be redeclared under `tools` when
  `toolchains.node.package_managers` already owns them

## Why this exists

The Rust example proves managed-surface ownership such as components and targets. This Node example
proves the narrower Node shape: `toolchains.node` owns Node plus declared Corepack package-manager
activation, while structured `fulfillment` says how ota may activate that toolchain on the selected
path.

## Try this

Inspect the contract first:

```bash
ota validate .
ota doctor .
ota up --dry-run .
ota tasks --use .
```

`ota tasks --use .` is the quickest way to inspect the runnable lane itself before execution:
command preview, default versus alternate modes, safety posture, declared effects, and the matching
dry-run / receipt follow-up commands.

Then compare the task paths:

```bash
ota run setup
ota run test
```

## Expected result

- `ota doctor` should diagnose Node through `toolchains.node` and surface missing Corepack-managed
  package managers from that same owner
- `ota up --dry-run` should show `toolchains.node` through structured fulfillment and surface
  Corepack activation actions for declared package managers from the selected workflow path
- `ota run setup` and `ota run test` should require the Node toolchain only
- `ota` should reject duplicate `runtimes.node` or `tools.node` declarations, while also rejecting
  duplicate package-manager ownership such as `tools.pnpm` when `toolchains.node.package_managers`
  already owns it

## When to copy this

- Node repos that want one owner for the Node runtime, `node` executable, and declared Corepack
  package-manager activation
- repos that activate `pnpm` or `yarn` through Corepack instead of global installs
- teams that want the canonical public Node toolchain model
