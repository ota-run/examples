#
#                █████
#               ░░███
#       ██████  ███████    ██████
#      ███░░███░░░███░    ░░░░░███
#     ░███ ░███  ░███      ███████
#     ░███ ░███  ░███ ███ ███░░███
#     ░░██████   ░░█████ ░░████████
#      ░░░░░░     ░░░░░   ░░░░░░░░
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

# Integration-test network effect

This is the compact public example for `effects.network_kind: integration_test`.

Use it when the real verification lane is not generic "the network is on", but specifically:

- live integration tests
- staging-backed smoke checks
- remote verification that depends on non-local credentials or seeded external state

What it demonstrates:

- explicit `requirements.env` for the credential gate
- explicit `effects.network_kind: integration_test`
- explicit `effects.external_state` for the remote system the lane touches
- keeping that path out of routine `agent.safe_tasks`

Try:

```bash
ota validate ota.yaml
ota run test:live --dry-run --json
```

You should see:

- the task stays blocked without the declared env value
- the contract keeps the lane distinct from `dependency_hydration`
- the path is machine-readable without hiding the remote dependency in prose or shell glue
