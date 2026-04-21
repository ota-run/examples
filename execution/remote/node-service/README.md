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

# Node service in a remote execution context

Use this example when a Node service should run in a remote execution context, but the repo still needs a clear, local contract.

## Why this exists

- keeps the service workflow explicit when the execution location is not local
- shows how a remote dev box or sandbox can stay under the same ota contract
- gives teams a realistic pattern for remote setup and verification

## When to use it

- the service runs better on a shared host or sandbox
- the local machine should not own the execution environment
- you want remote execution to stay reviewable and predictable

## What this teaches

- how to keep `execution.contexts` visible in the contract
- how to keep setup, dev, and test tasks readable
- how to keep the remote backend thin while the repo contract stays authoritative
