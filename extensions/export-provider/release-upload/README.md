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

# Release upload extension example

Use this example when a repo needs a named export adapter for release artifacts.

## Why this exists

- keeps release publishing explicit and contract-backed
- gives teams one adapter name to review and run
- lets humans and agents see where release data leaves the repo

## Use when

- the repo publishes build artifacts through a standard adapter
- you want export behavior to stay discoverable through `ota extensions`
- you want release handoff to remain explicit

## Try this

```bash
ota doctor
ota validate .
ota extensions --publish release-upload
```

