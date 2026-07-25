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

# Task prepare: uv local project hydration

Use this when one checked-out Python package is installed into the repository's virtualenv and its
extras or dependency groups are part of the real setup contract.

This example keeps the install on Ota's typed hydration surface:

- `mode: pip_local_project` owns the editable install instead of a shell body
- `local_project.path` is relative to `source.cwd`; it can use `..` only when it resolves inside
  the contract root
- ordered `extras[]` and `groups[]` are contract truth
- `lockfile` and clean source identity are separately witnessed before execution

For replay, a matching editable-project record is acquitting only when resolved hydration posture,
the declared lockfile identity, and clean source identity are all available. Without a lockfile or
clean source identity, Ota keeps the record as narrowing evidence rather than claiming the project
is replay-pinned.

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
