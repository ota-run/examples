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

# ota adoption flow example

This is the flagship public adoption starter. Use it when you are introducing ota to an existing Java repo that already has scripts, habits, hidden setup, and too many places where setup knowledge can drift. It is intentionally richer than the thin templates so users can see Ota’s value on something that looks like a believable repo, then copy the parts that fit.

## Example type

- Flagship adoption starter
- Copyable Java/Maven service example
- Real repo shape with contract, docs, service wiring, source files, and release-script companions

## Why this exists

- shows how ota turns scattered repo knowledge into one contract
- gives humans a short path from diagnosis to a written contract
- gives agents explicit setup, validation, and execution boundaries
- makes the first week of adoption obvious instead of improvised
- gives a team a believable path from messy repo to repeatable operating model

## Use when

- the repo already exists and needs a cleaner operating model
- setup, validation, or release steps live in scripts or tribal knowledge
- you want to adopt ota without rewriting the application
- you want a concrete path from “messy repo” to “explicit contract”
- you want a starter that includes more than `ota.yaml`

## What this teaches

- how `ota doctor` surfaces readiness gaps first
- how `checks` make `ota doctor` fail fast when the Java toolchain is missing
- how typed `services` make local dependencies explicit instead of hidden in README prose
- how explicit host and app execution contexts keep repo work and containerized app work separate
- how typed service managers make Postgres ownership and readiness honest instead of implied
- how `ota explain` turns findings into concrete next steps
- how `ota detect --dry-run` reviews the contract against repo signals before you write or merge anything
- how `ota validate` and `ota up` become the repeatable path after adoption
- how `ota agents --write` turns the contract into agent-facing repo guidance
- how ota reduces repeated setup explanations for both humans and agents
- how `tasks.<name>.requires_services` lets `db:integration` wait for `postgres` before it runs
- how `tasks.<name>.runtime.listeners` lets a containerized Spring Boot API publish a deterministic host URL without pretending app ingress belongs in `services`

## What is included

- `ota.yaml` - adoption-ready repo contract
- `pom.xml` - a minimal Maven app signal that users can actually fork
- `.sdkmanrc` - repo-local Java version signal for exact remediation and setup
- `docker-compose.yml` - a local dependency pattern that ota can make explicit
- `scripts/release.sh` - release-script companion that keeps the repo’s release edge visible
- `src/` - minimal source and test files so the repo shape looks real
- `docs/first-week.md` - first-week adoption path and expected outcome
- `docs/release-checklist.md` - a small companion doc that the contract keeps honest

## Copy these files

- Always copy: `ota.yaml`
- Copy for repo signals and better `ota detect`: `pom.xml`, `.sdkmanrc`, `docker-compose.yml`
- Copy for a fuller starter: `src/`, `scripts/release.sh`, `docs/`

## Try this

```bash
ota doctor .
ota explain .
ota detect --dry-run .
ota validate .
ota run db:integration
ota run dev:api
ota up .
ota agents --write .
```

## Expected result

- `ota doctor` should tell you exactly what is missing or confirm the repo is ready
- `ota explain` should turn those findings into an ordered fix plan
- `ota detect --dry-run` should review the current contract against the repo signals instead of making you guess what ota saw
- `ota run db:integration` should start and verify `postgres` before the integration task runs
- `ota run dev:api` should print the resolved host endpoint for the API workload after it starts inside the container
- `ota up` should make setup, local service readiness, and published workload endpoint planning feel like one repeatable flow
- `ota agents --write` should give the repo an explicit agent-facing contract derived from `ota.yaml`

## What Ota will tell you

Exact Java remediation:

```text
Primary Blocker
Version mismatch for runtime: java
Why: java resolved to `23.0.2` but the contract requires `21-tem`
Next: run `sdk install java 21-tem` and rerun `ota doctor ./reference/adoption-flow/ota.yaml`
```

Local service readiness:

```text
ERROR  Service healthcheck failed: postgres
Why: service `postgres` did not pass its configured healthcheck
Next: run `ota up` and re-run `ota doctor ./reference/adoption-flow/ota.yaml`
```

Derived agent guidance:

```text
AGENTS ./reference/adoption-flow/ota.yaml
Target:
./reference/adoption-flow/AGENTS.md
Next:
▸  run `ota agents --write ./reference/adoption-flow/ota.yaml` to write `./reference/adoption-flow/AGENTS.md`
```

## Important note about detect

- `ota detect` should infer the base repo shape from files like `pom.xml`, `.sdkmanrc`, and `docker-compose.yml`
- `ota detect` should also recover the starter `setup` and `release` edges from repo-local signals instead of leaving them hidden
- the remaining drift here is intentional: `docs:check` is a higher-order repo guardrail that stays authored in the contract
- use this example to teach that Ota detection is deterministic repo inference, while the contract can still carry repo-specific operating knowledge like documentation guardrails

## Edit first

- `project.name` and `project.description`
- `execution.contexts.host` and `execution.contexts.app`
- `services.postgres.manager`, `services.postgres.endpoints`, and `services.postgres.readiness`
- `tasks.db:integration.requires_services`
- `tasks.dev:api.runtime.listeners`
- `tasks.setup`, `tasks.build`, `tasks.test`, `tasks.docs:check`, and `tasks.release`
- `agent.safe_tasks`, `agent.verify_after_changes`, `agent.writable_paths`, and `agent.protected_paths`
- `pom.xml` coordinates, dependencies, and Java release target
- `scripts/release.sh` to match the repo’s actual release gate

## Why this sells ota

- it gives users a believable “before this was tribal, now it is explicit” repo shape
- it shows diagnosis, contract review, task execution, services, and agent guidance in one place
- it shows a task prerequisite example where `db:integration` asks for Postgres readiness directly
- it shows workload ingress explicitly, so the app can stay containerized while ota still tells the host browser where to connect
- it can be forked as a starter instead of only read as a concept
