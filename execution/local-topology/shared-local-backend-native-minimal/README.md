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

# Minimal native shared local backend

Use this when multiple long-running native tasks should intentionally reuse one shared local host
boundary.

## Why this exists

- keeps the shared-boundary truth explicit instead of inferring it from matching native contexts
- lets ota attach one backend binding to more than one native workload intentionally
- keeps lifecycle and backend-family truth on the shared boundary itself

## What this teaches

- how to declare `execution.shared_backends.<name>` with `backend: native`
- how to bind more than one native service task with `runtime.backend_binding`
- how to keep the native shared boundary persistent without pretending it has container image or environment semantics

## Rule

Use a native shared backend when the shared boundary is the host environment itself. Do not use it
when tasks are just separate consumers of a published service and do not need one intentional
backend boundary.
