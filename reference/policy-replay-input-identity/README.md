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

# Policy-governed replay input identity

Use this when an organization requires selected replay-sensitive tasks or workflows to declare and
match immutable replay-input identities.

The repo contract names the input and expected digest. `.ota/org-policy.yaml` decides which
selected closures require complete pins. Doctor, dry-run, run, up, admission-produced
execution/refusal receipts consume one command-scoped observation set. Refusal happens before
native provisioning, dependency hydration, or task startup; unavailable observations fail closed,
and hard-pin refusals retain the active policy record. CI carries the requirement but recomputes
observed identities after checkout. Generic readiness receipts do not reconstruct policy after
execution. Neither Ota nor an agent updates the digest automatically.

Open [`ota.yaml`](ota.yaml) and [`.ota/org-policy.yaml`](.ota/org-policy.yaml) for the copy-ready
shape.

Change the fixture to exercise the unconditional hard-pin mismatch. In a scratch copy, remove
`expected_identity` while keeping the policy rule to exercise the policy-specific
`missing_expected_identity` refusal through Doctor, dry-run, `ota run verify --receipt`, and
`ota up --json --receipt`.
