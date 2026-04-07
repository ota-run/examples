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

# First week with Ota

This example shows the adoption path for a Java repo that already exists but does not yet have a clean Ota contract. The companion files in this folder are intentionally realistic enough that users can fork the whole shape instead of only reading about the flow.

## Day 1

1. Run `ota doctor .` to see readiness gaps.
2. Run `ota explain .` to turn the findings into next steps.
3. Run `ota detect --dry-run .` to review the contract against the repo signals.

Expected result:
- Ota tells you whether Java, Maven, Docker, or the local service stack is missing.
- The repo contract is no longer a guess; it is reviewed against `pom.xml`, `.sdkmanrc`, and `docker-compose.yml`.
- Detect should infer the base repo shape, while the authored contract can still carry richer repo-specific tasks like docs checks and release flow.

## Day 2

1. Run `ota validate .` to confirm the contract is valid.
2. Run `ota up .` to prepare the repo and local service stack the same way every time.
3. Run `ota agents --write .` to generate explicit agent-facing repo guidance from the contract.

Expected result:
- Setup, docs, build, and test flows are now legible in one contract.
- Humans and agents can see the same execution path and safe-task boundaries.

## What success looks like

- setup steps live in `ota.yaml`
- the Java version, Maven shape, and service startup path are visible from repo files and the contract
- validation steps are explicit
- task execution is discoverable through `ota tasks`
- the repo can generate `AGENTS.md` from the contract instead of repeating the same rules in prose
- the repo no longer depends on tribal knowledge for first success
