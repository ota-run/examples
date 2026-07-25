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

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.
-->

# Trusted Replay Baseline Regeneration

Use this shape when a generated fixture, local store, or recorded evaluation baseline must be
reviewed as a produced artifact instead of pinned with a hand-edited digest.

```text
baseline:record -> recorded attestation -> explicit promotion -> read-only replay
```

This example uses `consumption: read_only`, so its replay task requires an ephemeral container
boundary. If a repo must retain native replay, use `consumption: verify_unchanged`: Ota rechecks
the promoted output manifest after the task and reports `replay_artifact_mutation_detected` if it
changed. An ephemeral container upgrades that posture to the stronger read-only overlay.

Run `ota baseline record --artifact recorded-baseline --json` only for an intentional baseline
change from a clean Git source tree. Ota captures that source identity before the producer changes
the outputs. Review the generated files and the attestation, then run:

```bash
ota baseline promote --artifact recorded-baseline \
  --attestation .ota/replay-baselines/recorded-baseline/attestation-<sha>.json --json
```

Commit the reviewed baseline files and `replay/recorded-baseline.ota.json`. The manifest embeds the
selected recorded attestation, so the portable authority retains reviewable producer provenance. The
replay task does not depend on the producer; Ota verifies promoted identities and mounts a runner-owned
read-only snapshot in an ephemeral container. Symlinked baseline outputs must stay inside declared
artifact paths; Ota refuses targets that escape into the mutable worktree.
