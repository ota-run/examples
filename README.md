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

# `ota-run/examples`

Collections of solid, real-world examples you can copy, adapt, and read as workflow guides.

Use these as starting points when you want:
- a repo contract you can adapt quickly
- a workspace contract for multi-repo setup
- a CI or release pattern built around `ota`
- a container-backed execution boundary when host drift is the problem

## Layout

- `templates/` - starter contracts you can copy into a new repo
- `advanced/` - production-oriented patterns and workflows

## Example folders

- `advanced/canonical-team-repo`
- `advanced/ci`
- `advanced/container`
- `templates/node-service`
- `templates/python-service`
- `advanced/workspace-monorepo`

## How to use

1. Copy the folder that matches your stack or workflow.
2. Adjust the contract to your repo.
3. Run `ota validate .` or `ota doctor`.
4. Keep the contract and the repo in sync as the project evolves.

## What these examples are teaching

- the repo shape and use-case for each example
- when to use the example
- what problem the example solves
- where to open the example's `ota.yaml` for task-level instructions

## Contributing

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.
- Use the pull request and issue templates under [`.github/`](.github/).
- Follow [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- See [`SECURITY.md`](SECURITY.md) for security disclosures.
- See [`SUPPORT.md`](SUPPORT.md) for help and response expectations.
