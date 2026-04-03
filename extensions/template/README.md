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

# ota extension template

Use this template when a repo needs adapter descriptors but should keep the explanation short, local, and easy to trust.

## Why this exists

- keeps extension intent explicit in the contract
- gives teams a copyable pattern for check, export, and backend adapters
- keeps the README focused on why the repo needs the extension surface
- makes adapter behavior reviewable without forcing readers through framework noise

## Use when

- you want to introduce adapter contracts without extra framework noise
- you need a clean starting point for repo-specific extension metadata
- you want humans and agents to see the adapter boundary quickly
- you want the repo to explain the adapter's job before the task runs

## What this teaches

- how to declare `extensions` with a clear kind
- how to keep task guidance on the task itself
- how to keep adapter names and commands obvious
