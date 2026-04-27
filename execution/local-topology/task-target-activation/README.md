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

# Advanced target activation example

An advanced execution example where a consumer task asks ota to make the producer service ready
before the consumer runs.

## Why this exists

- shows the first shipped `activation.mode: ensure_ready` surface directly
- keeps target identity and producer activation separate in the contract
- demonstrates the narrow honest first slice: persistent container producer service on the host-view
  path

## Use when

- one local consumer should follow a repo-managed producer service by identity
- target resolution alone is not enough because the producer should be started if needed
- the producer can truthfully run as a persistent container service

## Contract shape

This example uses:

- `tasks.dev.runtime.listeners.http` as the producer service identity
- `tasks.sandbox.targets.api.override_input: base_url` as the explicit operator override channel
- `tasks.sandbox.targets.api.activation.mode: ensure_ready` so ota may reuse or start the producer
  before running the consumer
- a persistent container producer backend because that is the first shipped auto-start slice

## Try this

```bash
ota doctor
ota validate .
ota run sandbox
ota run sandbox --base-url https://staging.example.com
ota run dev
```

## What to notice

- `sandbox` still gets `OTA_INPUT_BASE_URL`, but the default now comes from `targets.api`
- when `dev` is already reachable, ota reuses it instead of starting it again
- when the operator passes `--base-url`, ota preserves the explicit override and skips producer
  auto-start
- this example is intentionally `address_view: host` because that is the currently supported
  `ensure_ready` startup path
