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

# Policy-governed shared backend environment example

An advanced local-topology example where a shared container backend declares environment intent and policy resolves the effective backend image.

## Why this exists

- shows the shipped slice-4 surface instead of hardcoding raw backend images in every repo
- keeps one shared local backend boundary while policy chooses the approved effective image
- demonstrates declared-versus-effective backend environment evidence in `ota execution plan`, `ota run`, and run receipts
- stays compatible with the strict shared-backend shape rules because the shared shape is anchored to one declared profile

## Use when

- the repo should declare backend image intent, not the final approved image string
- one shared local backend should still stay explicit and deterministic
- operators need to inspect the effective approved image before they run tasks

## Contract shape

This example uses:

- one shared local backend bound to the `app` container context
- `execution.shared_backends.workbench.environment.profile: java-node-workbench`
- a repo policy pack under `.ota/org-policy.yaml`
- one bound service task whose effective backend image is policy-resolved

## Try this

```bash
ota validate .
ota execution plan
ota run dev
```

## What to notice

- the context image is intentionally different from the effective approved image so the policy-backed resolution is visible
- `ota execution plan` and `ota run` should agree on the effective backend image
- run receipts and summaries surface both the declared environment intent and the effective image/source/registry chosen by policy
- if you want policy `default_profile` instead of an explicit profile, replace the `profile:` selector with `environment: {}`

## Pair with other local-topology slices

- use `../shared-local-backend/` when the shared boundary itself is the story and raw image compatibility is enough
- use `../shared-local-backend-fulfillment/` when the backend also needs run-path preparation after the effective image is resolved
