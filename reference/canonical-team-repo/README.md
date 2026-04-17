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

# Canonical advanced repo

This is the advanced example you fork when you want ota to be part of the repo operating model, not a side note, and you want that operating model to be easy to hand to another team or an agent. It is the strongest “this is how a serious repo works” example in the set.

## What this teaches

- how to make repo knowledge explicit and durable
- how to give humans and agents the same operational context
- how to keep setup, validation, release, and handoff close to execution
- how to reduce repeated explanations with structured docs
- how to turn repo conventions into something people can trust and reuse
- how to make the repo itself explain the operating model
- how repo intent and org policy stay separate through explicit `version_policy`, provisioning, and adapter bootstrap rules
- how to declare env requirements explicitly through `env.vars` and ordered `env.sources` instead of relying on silent `.env` loading

## Read this first

1. [`ota.yaml`](ota.yaml)
2. [`.ota/org-policy.yaml`](.ota/org-policy.yaml)
3. [`AGENTS.md`](AGENTS.md)
4. [`docs/architecture.md`](docs/architecture.md)
5. [`docs/workflows.md`](docs/workflows.md)
6. [`docs/instruction-examples.md`](docs/instruction-examples.md)
7. [`docs/templates/agent-brief.md`](docs/templates/agent-brief.md)

## Structure

- `ota.yaml` - canonical repo contract and agent boundaries
- `.env.ota-example` - committed non-secret dotenv source used to demonstrate ordered `env.sources` and `must_exist`
- `.ota/org-policy.yaml` - shared org rules that sit above the repo contract, including explicit version approvals and provisioning sources
- `AGENTS.md` - repo-local guidance for safe and reviewable agent work
- `docs/` - operational knowledge that should stay close to the repo
- `docs/templates/` - reusable templates for recurring work

## Env model

This example intentionally dogfoods the current env contract:

- `env.vars` declares the repo-facing values
- `env.sources` declares where ota may read them from
- `.ota/org-policy.yaml` can supply shared env values through `policies.env.values`
- `.env.local` stays optional for local overrides
- `.env.ota-example` is required and committed so the example validates and doctors cleanly without manual setup
- org policy env values outrank process env and declared dotenv sources
- process env still outranks declared dotenv sources

## Use this repo when

- you want a serious starting point, not a toy example
- you need a shared language for humans and AI agents
- you want to teach good ota usage through the repo shape itself
- you want a repo that feels production-adjacent from the first read
