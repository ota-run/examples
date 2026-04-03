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

# Ota remote execution mode examples

Use this theme when Ota should run repo tasks on a remote target instead of the local machine.

## Why this exists

- keeps the contract stable while execution moves elsewhere
- makes remote execution explicit and reviewable
- helps teams use a shared host, sandbox, or cluster without losing repo truth

## Use when

- the work should run on a team dev box, sandbox, or remote host
- the local machine is not the right execution location
- you want the remote boundary to be part of the Ota contract

## What this teaches

- how to keep execution intent explicit
- how to keep remote targets understandable to humans and agents
- how to preserve one repo contract across multiple execution locations

## Folders

- `template/` - remote execution template
- `node-service/` - Node service remote execution example
