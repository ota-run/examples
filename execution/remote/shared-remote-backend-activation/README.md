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

# Shared remote backend activation example

An advanced remote example where a consumer task asks ota to make the producer service ready before the consumer runs on one shared remote backend boundary.

## Why this exists

- shows the shipped remote `activation.mode: ensure_ready` slice directly
- keeps shared remote boundary truth, target identity, and producer activation separate in the contract
- demonstrates the narrow honest remote slice instead of a vague “ota starts anything remote” promise

## Use when

- one remote consumer should follow a repo-managed remote producer by service identity
- the producer and consumer truly share one declared remote backend boundary
- the provider is one of the shipped built-ins
- readiness can be expressed as TCP on a fixed listener bind port

## Current shipped remote activation constraints

- built-in providers only:
  - `ssh`
  - `tsh`
  - `kubectl`
  - `daytona`
- shared-remote `address_view: internal` or `address_view: topology` only
- TCP readiness only
- fixed `bind.port.value` required

## Try this

```bash
ota doctor
ota validate .
ota run sandbox
```

## What to notice

- `sandbox` follows `dev` through `targets.api` instead of a guessed literal URL
- `activation.mode: ensure_ready` is separate from target identity
- `runtime.readiness.kind: tcp` is the truthful shipped remote readiness slice
- explicit override input still wins if you add one later
- test the provider outside ota first, then use this contract
