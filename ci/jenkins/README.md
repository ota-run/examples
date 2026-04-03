<!--
                █████
               ░░███
       ██████  ███████    ██████
      ███░░███░░░███░    ░░░░░███
     ░███ ░███  ░███      ███████
     ░███ ░███  ░███ ███ ███░░███
     ░░██████   ░░█████ ░░████████
      ░░░░░░     ░░░░░   ░░░░░░░░
#
#   Copyright (C) 2026 — 2026, Ota. All Rights Reserved.
#
#   DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
#   Licensed under the Apache License, Version 2.0. See LICENSE for the full license text.
#   You may not use this file except in compliance with that License.
#   Unless required by applicable law or agreed to in writing, software distributed under the
#   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#   either express or implied. See the License for the specific language governing permissions
#   and limitations under the License.
#
#   If you need additional information or have any questions, please email: os@ota.run
-->

# Jenkins CI example

Use this when Jenkins is already your execution layer, but the repo contract should still live in ota.

## Why this exists

- keeps the pipeline explicit
- shows how Jenkins can stay thin
- teaches a reusable release pattern with ota in the middle
- makes setup and release behavior visible instead of buried in Jenkinsfile logic

## Use when

- you run CI or release jobs in Jenkins
- you want the repo contract to remain the source of truth
- you want a pipeline that is easy to review and hard to misread

## Copy these files

- [ota.yaml](ota.yaml)
- [Jenkinsfile](Jenkinsfile)

## Try this

```bash
ota validate .
ota run setup
ota run ci
ota run release
```
