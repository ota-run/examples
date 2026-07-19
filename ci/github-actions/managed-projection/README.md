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

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

# Managed GitHub Projection

Use this shape when `ota.yaml` owns bootstrap and verification truth while GitHub retains triggers,
permissions, secrets, runner choice, and deployment jobs.

Generate the Ota-owned reusable workflow, then copy its emitted identity into the caller:

```bash
ota ci github render --workflow verify --target-os linux --output .github/workflows/ota-governance.yml --json
ota ci github sync --workflow verify \
  --target-os linux \
  --output .github/workflows/ota-governance.yml \
  --caller .github/workflows/ci.yml
ota ci github check --workflow verify \
  --target-os linux \
  --output .github/workflows/ota-governance.yml \
  --caller .github/workflows/ci.yml
```

`ota-governance.yml` is generated and Ota-owned. `ci.yml` is human-owned and carries only
provider scheduling and the immutable projection reference. The caller binds the exact
`ota_projection_identity` and `ota_target_os`. Runner labels remain
provider-owned; Ota performs the projection identity check without relying on a provider shell.

This example's `verify` task is finite. Its generated workflow prepares the selected workflow with
`ota up`, then executes `verify` through `ota run --agent`; it does not treat readiness-only
preparation as verification proof. Service-runtime and proof lanes retain their own authoritative
runtime execution path.
