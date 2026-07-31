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

# Safe agent execution and refusal

Use this example when an agent should execute one routine verification lane while a heavier task
must remain unavailable.

The contract declares:

- `verify` as the complete agent-safe task closure;
- `publish` as outside the safe surface;
- a `publish` refusal canary that exercises the real agent admission boundary.

Both demonstration task bodies use the already-required, cross-platform `ota --version` command so
an unrelated shell or language runtime does not obscure the admission behavior. Replace those task
bodies with the repository's real verification and heavier execution lanes.

Run the positive and negative controls through agent mode:

```sh
ota run verify --agent
ota run publish --agent --expect-refusal
```

The canary succeeds only when Ota refuses `publish` before its task body starts. Ota derives the
current refusal reason from the selected closure; the contract does not self-attest why refusal
should happen.

This controls execution through Ota. It does not constrain an unrestricted developer or agent that
bypasses Ota with raw shell.
