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

A real workspace blueprint for multi-repo bootstrap and dependency ordering.

## Why this exists

- makes repo acquisition explicit
- keeps dependent repos from bootstrapping out of order
- gives you one contract for a multi-repo workspace

## Use when

- multiple repos need to be cloned into a workspace
- one repo depends on another being acquired first
- you want `ota workspace up` to be the canonical bootstrap path

## Try this

```bash
ota workspace validate .
ota workspace up
ota workspace status
ota workspace diff
ota workspace receipt
```
