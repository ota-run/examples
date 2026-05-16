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

# Rust toolchain flow

This is the dedicated public example for Rust toolchain ownership.

Use it when the repo needs Rust to behave as one provider-backed ecosystem instead of splitting the
same truth across `runtimes`, `tools`, and setup shell glue.

## What this teaches

- `toolchains.rust` is the owner for the managed Rust ecosystem
- the shipped Rust toolchain contract is the fixed pair `toolchains.rust` plus `provider: rustup`
- `provider: rustup` makes version, components, and targets explicit contract truth
- Ota validates and interprets this contract through the shipped Rustup provider contract rather
  than treating those fields as a generic ecosystem schema
- `requirements.toolchains` is the selected-path owner for Rust tasks
- `cargo`, `rustfmt`, and `clippy` should not be restated under `tools` when the Rust toolchain
  already owns them
- `runtimes.rust` should not be declared alongside `toolchains.rust`
- genuinely standalone tools can still stay under `tools`

## Why this exists

The generic tool acquisition examples teach unmanaged runtimes and standalone commands. They do not
show the managed-ecosystem boundary that shipped with `toolchains.rust`.

This example isolates that boundary so users can copy the Rust pattern directly:

- one Rustup-backed toolchain
- one selected-path `requirements.toolchains` lane
- one standalone tool (`git`) that stays outside the Rust toolchain

## Try this

Inspect the contract first:

```bash
ota validate .
ota doctor .
ota up --dry-run .
ota tasks --use .
```

Then compare the selected task paths:

```bash
ota run lint
ota run test
ota run release:tag
```

## Expected result

- `ota doctor` should diagnose Rust through `toolchains.rust`, not through `runtimes.rust`
- `ota up --dry-run` should talk about the Rust toolchain via `rustup` and say whether fulfillment
  is check-only or run-path provisioning
- `ota run lint` should require the Rust toolchain and its owned capabilities without separate
  `tools.cargo`, `tools.rustfmt`, or `tools.clippy` declarations
- `ota run release:tag` should still talk about `git` as a standalone tool, because the Rust
  toolchain does not own it

## When to copy this

- Rust repos that currently hide `rustup component add ...` in `setup`
- Rust repos that currently duplicate `runtimes.rust`, `tools.cargo`, or `tools.rustfmt`
- teams that need one copyable example for the shipped `toolchains` surface before wider provider
  support exists
