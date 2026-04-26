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

# Advanced task target binding example

An advanced execution example where one repo-managed app (`dev`) is consumed by two different helper tasks:

- `sandbox` keeps an explicit operator override channel through `base_url`
- `probe:api` has no override input and consumes the resolved target directly through `OTA_TARGET_API`

## Why this exists

- shows the intended long-term shape for helper apps and probes
- keeps topology truth in `targets`, not in guessed literal defaults
- demonstrates `address_view: host` for a consumer that may run in a different execution plane from the producer
- makes the non-override path explicit with a real `OTA_TARGET_*` export

## Use when

- one app service should be the default target for another helper task
- operators still need an escape hatch to point at staging, preview, or another local app
- you want a contract review to show service identity instead of only input defaults
- a probe or support task should target the same app without carrying a user-facing input

## Contract shape

This example uses:

- `tasks.dev.runtime.listeners.http` as the producer service identity
- `tasks.sandbox.targets.api` with `override_input: base_url`
- `tasks.probe:api.targets.api` without `override_input`
- `address_view: host` so the helper always consumes the producer's published host URL rather than guessing a same-plane address

## Try this

```bash
ota doctor
ota validate .
ota run sandbox
ota run sandbox --base-url https://staging.example.com
ota run probe:api
ota run dev --container
ota run sandbox --container
```

## What to notice

- `sandbox` still gets `OTA_INPUT_BASE_URL`, but the default now comes from `targets.api`
- `probe:api` gets `OTA_TARGET_API` without needing a matching task input
- `address_view: host` keeps the helper task honest when it does not actually share the producer's internal network plane
- receipt JSON preserves the declared target, the source, and the effective resolved URL for each executed step
