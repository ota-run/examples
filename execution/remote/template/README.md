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

# ota remote execution template

Use this template when a repo should keep its contract local, but run setup and verification on a remote target. It is useful when the environment is shared, the local machine is not the right place to execute, or you want the remote boundary to stay visible in the repo itself.

## Why this exists

- keeps execution location explicit instead of hidden in shell scripts
- lets teams use a shared dev box, sandbox, or remote host without changing task intent
- keeps humans and agents on the same repo contract
- makes remote execution something ota can describe and validate, not just tolerate
- reduces “works on my machine” problems by making the execution site part of the contract
- gives teams a reusable pattern for predictable remote automation

## When to use it

- the local machine is not the right execution location
- you want remote execution to be part of the contract review
- the repo needs repeatable setup and verification on a remote target
- you need the environment to be shared but still want the repo to stay the source of truth
- you want agents to see the execution target before they act

## What this teaches

- how to keep `execution.preferred: remote` explicit
- how to keep the remote provider, target, and working directory in the contract
- how to keep task guidance close to the task itself
