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

# Tool acquisition flow

This is the dedicated public example for tool acquisition.

Use it when the repo has more than one front door and each front door should carry its own honest
tool acquisition lane instead of one repo-global install story.

## What this teaches

- `tools.<name>.acquisition` belongs on the tool truth, not inside a setup script
- `tasks.<name>.requirements.runtimes` keeps runtime prerequisites scoped to the chosen front door
- `tasks.<name>.requirements.tools` selects when that tool truth actually applies
- `workflows` decide which prerequisite surface is active for `ota doctor` and `ota up`
- `provider: corepack` and `provider: command` can coexist in one repo without forcing both lanes
  onto every user

## Why this exists

The templates now use acquisition, but they still teach it as part of a broader starter. This
example isolates the behavior so users can see the product boundary directly:

- `web` selects only the Corepack-managed `pnpm` lane
- `python` selects only the command-backed `uv` lane
- both workflows scope their runtime requirements at the task path instead of declaring repo-global
  runtimes

That is the contract truth Ota should surface in diagnosis and preparation.

## Try this

Inspect the declared front doors first:

```bash
ota workflows .
```

Then compare the selected acquisition lanes:

```bash
ota doctor --workflow web .
ota up --dry-run --workflow web .
ota doctor --workflow python .
ota up --dry-run --workflow python .
```

## Expected result

- `ota doctor --workflow web` should talk about `node` and `pnpm` through Corepack, not `python`
  or `uv`
- `ota up --dry-run --workflow web` should show only the Corepack activation lane
- `ota doctor --workflow python` should talk about `python` and `uv` through the declared shell
  command, not `node` or `pnpm`
- `ota up --dry-run --workflow python` should show only the command-backed `uv` acquisition lane

## When to copy this

- one repo has multiple valid developer paths
- different paths need different tools
- you want first-run setup to stay honest without inventing repo-global prerequisites
- you want a compact example that explains acquisition better than prose alone
