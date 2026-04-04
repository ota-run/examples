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

Use this example when you are introducing ota to an existing Java repo that already has scripts, habits, hidden setup, and too many places where setup knowledge can drift. It shows how ota makes the first week of adoption legible instead of forcing everyone to rediscover the repo by hand.

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

## What this teaches

- how `ota doctor` surfaces readiness gaps first
- how `checks` make `ota doctor` fail fast when the Java toolchain is missing
- how `ota explain` turns findings into concrete next steps
- how `ota init --dry-run` and `ota detect --dry-run` show the contract before writing
- how `ota detect --write` or `ota init` makes the contract explicit
- how `ota validate` and `ota up` become the repeatable path after adoption
- how ota reduces repeated setup explanations for both humans and agents

## What is included

- `ota.yaml` - adoption-ready repo contract
- `docs/first-week.md` - the first-week adoption path and expected outcome

## Try this

```bash
ota doctor .
ota explain .
ota init --dry-run .
ota detect --dry-run .
ota detect --write .
ota validate .
ota up .
```

## Edit first

- `project.description`
- `tasks.setup`, `tasks.build`, `tasks.test`, `tasks.docs:check`, and `tasks.release`
- `agent.safe_tasks`
- `agent.verify_after_changes`
- `agent.writable_paths`
- `agent.protected_paths`
