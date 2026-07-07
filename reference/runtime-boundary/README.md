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

# runtime-boundary

Use this when runtime sandbox truth should be contract-owned instead of reconstructed from broad
effects or only from `agent.writable_paths`.

This example shows the three shipped ownership layers:

- `execution.runtime_boundary` for repo-level baseline posture
- `workflows.<name>.runtime_boundary` for selected workflow specialization
- `tasks.<name>.runtime_boundary` for the narrowest selected-lane truth

The current harness-facing export uses that truth in `ota tasks --json` and `ota workflows --json`
under `capability_profile.*[].sandbox_policy` for the first compiled target, `codex_local`.

The shipped slice is intentionally honest:

- filesystem posture can compile from canonical `runtime_boundary`
- network posture can compile either as broad effect-owned `allow`/`deny`, or as targeted
  `outbound_targets[]` when the contract declares them
- `enforcement` stays `advisory_only` until Ota ships a real sandbox compilation target
