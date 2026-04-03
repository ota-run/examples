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

# Workspace monorepo example

A real workspace blueprint for multi-repo bootstrap and dependency ordering when several repos need to become ready together. Use it when you want ota to remove the guessing around which repo comes first and which repos are safe to prepare together.

## Why this exists

- makes repo acquisition explicit
- keeps dependent repos from bootstrapping out of order
- gives you one contract for a multi-repo workspace
- helps teams stop guessing which repo should be cloned first
- keeps workspace setup repeatable for humans and agents
- makes workspace bootstrap feel like a planned system instead of a manual checklist

## What this teaches

- `source.repo` and `source.git` are both valid acquisition styles
- `depends_on` keeps workspace bootstrap order explicit
- `ota workspace up` acquires and prepares repos
- `ota workspace tasks` shows workspace tasks and dependency order
- after bootstrap, `ota workspace status`, `ota workspace diff`, and `ota workspace receipt` help inspect readiness and drift without changing anything

## Use when

- multiple repos need to be cloned into a workspace
- one repo depends on another being acquired first
- you want `ota workspace up` to be the canonical bootstrap path
- you want workspace bootstrap to be explicit enough that new contributors do not need tribal knowledge

## Try this

```bash
ota workspace validate .
ota workspace doctor .
ota workspace tasks .
ota workspace up
ota workspace status
ota workspace diff
ota workspace receipt
```
