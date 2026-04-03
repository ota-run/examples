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

# Custom remote backend example

Use this example when a repo needs a backend provider that is not one of the built-in remote providers.

## Why this exists

- keeps the remote execution seam explicit in the contract
- shows how a custom backend can stay discoverable without hiding in shell glue
- gives teams a reference for remote execution under an extension contract

## Use when

- the built-in remote providers are not enough
- you want the repo to name its own remote backend
- you need remote execution behavior to stay visible to humans and agents

## Try this

```bash
ota doctor
ota validate .
ota run setup
ota run test
```

