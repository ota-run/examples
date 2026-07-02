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

# Action ensure_git_template

Use this when one setup step really owns deterministic factory or scaffold materialization from a
Git-backed template and should not fall back to shell `git clone`, `rm -rf .git`, and `git init`
glue.

This example shows:

- `action.kind: ensure_git_template`
- bundled `ensure_directory`
- explicit host `requirements.tools.git`
- one finite native setup lane
- `workflows.<name>.prepare.task`

Why this exists:

- some repos are factories, starters, or scaffolds rather than vendored dependency checkouts
- that ownership should stay declarative and inspectable instead of being hidden in shell bootstrap
- the materialization lane should stay idempotent while producing a fresh child repository instead
  of leaving an inherited upstream clone behind

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
