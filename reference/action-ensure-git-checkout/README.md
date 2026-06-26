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

# Action ensure_git_checkout

Use this when one setup step really owns clone-if-missing materialization of a sibling or vendored
Git checkout and should not fall back to shell `git clone` glue.

This example shows:

- `action.kind: ensure_git_checkout`
- bundled `ensure_directory`
- explicit host `requirements.tools.git`
- one finite native setup lane
- `workflows.<name>.prepare.task`

Why this exists:

- some repos need one repo-local checkout before the main repo becomes ready
- that ownership should stay declarative and inspectable instead of being hidden in shell bootstrap
- the materialization lane should stay idempotent without silently turning into fetch/reset/update

Open [`ota.yaml`](ota.yaml) for the exact contract shape.
