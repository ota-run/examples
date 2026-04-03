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

# Repo check extension example

Use this example when a repo has a repeatable validation step that should be named, reviewed, and run through Ota instead of hiding in shell scripts.

## Why this exists

- keeps repo-specific validation explicit and reviewable
- gives teams one adapter name to inspect and run
- lets humans and agents see that extra checks are part of the repo contract
- makes the check easy to trust because the adapter is named and the purpose is clear

## Use when

- the repo has a repeatable check that is not just a shell script
- you want the check to be discoverable through `ota extensions`
- you want the adapter boundary to be obvious to contributors
- you want a validation step that feels part of the contract, not a hidden convention

## Try this

```bash
ota doctor
ota validate .
ota extensions --run repo-check
```
