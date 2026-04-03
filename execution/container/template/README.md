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
   You may not use this file except compliance with that License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.

   If you need additional information or have any questions, please email: os@ota.run
-->

# ota container template

Use this when the repo should run setup and verification through ota container mode.

## Why this exists

- avoids host-specific drift
- keeps dependency install and test behavior reproducible
- gives agents one explicit execution path
- makes the environment part of the contract so contributors do not have to guess what “ready” means

## Use when

- local and CI environments should match
- the toolchain is easier to standardize inside a container
- you want the container to be the execution boundary, not the source of truth
- you want every new contributor to start from the same runtime instead of recreating one

## Try this

```bash
ota doctor
ota validate .
ota run setup
ota run test
```
