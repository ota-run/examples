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

# Java SDKMAN toolchain flow

This is the dedicated public example for the shipped SDKMAN-backed Java toolchain boundary.

Use it when the repo wants `toolchains.java` to own `java` and `javac`, while Maven stays explicit
under `tools`.

## What this teaches

- `toolchains.java` is the owner for the managed Java runtime and `javac`
- `toolchains.java.fulfillment` separates Java capability truth from fulfillment truth
- `fulfillment.source: sdkman` is the canonical public way to say the selected path should use SDKMAN-backed fulfillment
- `requirements.toolchains` selects the Java runtime lane for the chosen task path
- Maven should stay under `tools.maven` because the Java toolchain does not own it in v1
- `runtimes.java`, `tools.java`, and `tools.javac` should not be declared alongside
  `toolchains.java`

## Why this exists

Rust proves the richer managed-surface shape and Node proves the narrower Corepack shape. This
example teaches the Java boundary directly:

- one Java toolchain owner
- one standalone Maven tool lane
- one selected-path contract that keeps those owners separate

## Try this

Inspect the contract first:

```bash
ota validate .
ota doctor .
ota up --dry-run .
ota tasks --use .
```

Use `ota tasks --use .` to inspect the runnable task surface before execution: command preview,
mode selection, safety posture, declared effects, and the matching dry-run / receipt follow-up
commands stay visible in one place.

Then compare the selected task paths:

```bash
ota run build
ota run test
```

## Expected result

- `ota doctor` should diagnose Java through `toolchains.java`
- `ota up --dry-run` should show `toolchains.java` through structured fulfillment and keep Maven
  separate as a standalone tool requirement
- `ota run build` and `ota run test` should require both the Java toolchain and Maven
- ota should reject duplicate `runtimes.java`, `tools.java`, or `tools.javac` declarations

## When to copy this

- Java repos that currently hide SDKMAN or JDK setup in shell scripts
- repos that want one clear Java owner without pretending Maven belongs to the toolchain
- teams that need one copyable example for the shipped Java toolchain surface
