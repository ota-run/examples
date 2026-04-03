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

Use this example when a repo needs to move release artifacts to another system and you want the publish path to stay explicit, reviewable, and repeatable. It is the pattern for teams that want release uploads to feel deliberate instead of improvised.

## Why this exists

- keeps artifact publication explicit and contract-backed
- gives teams one adapter name to review, run, and gate
- lets humans and agents see exactly where release data leaves the repo
- keeps Ota in the release path so publish steps stay repeatable after `ota validate`
- makes release handoff visible instead of burying it in shell glue or one-off upload scripts
- gives teams one place to decide when artifacts are allowed to leave the repo
- makes it obvious what is being uploaded, where it goes, and which task is responsible

## Use when

- the repo publishes build artifacts to object storage, an internal API, or another release system
- you want export behavior to stay discoverable through `ota extensions`
- you want release handoff to remain explicit and reviewable
- you want Ota to control when release export is allowed
- you need a clean audit trail for what was published and why

## Try this

```bash
ota doctor
ota validate .
ota run test
ota extensions --publish release-upload
```
