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
   You may not use this file except in compliance with the License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.

   If you need additional information or have any questions, please email: os@ota.run
-->

# Audited crossing authority

Use this shape when routine verification should remain available, but a heavier non-agent lane
must be admitted by an independently managed signed authority.

The repository declares only the authority identity:

```yaml
governance:
  crossing_authority:
    authority_id: platform-release-authority
```

It must not contain the public key, signed bundle path, sequence state, or a caller-selectable trust
path. The first `prebound_file` carrier resolves those from a fixed root-owned system trust store.

Expected behavior:

```sh
ota run verify
ota run publish --dry-run
ota run publish --grant approved-publish
```

- `verify` is routine and rejects an inapplicable grant.
- `publish` refuses before execution when the exact grant is missing, stale, revoked, or out of
  scope.
- a matching grant binds the semantic contract identity, selected closure, platform, execution
  overrides, `non_agent` actor posture, and short validity window.
- real execution creates a runner-owned crossing transaction under `.ota/state/crossings` before
  the selected lane mutates state, then binds its terminal outcome to the fresh receipt and archive;
  refusal and dry-run perform admission only and create no transaction or crossing record.
- refused dry-run and admission-produced execution receipts carry typed `prebound_file` authority
  source, selected authority/grant when present, stable refusal reason, and
  `execution_started: false`; that refusal evidence is not crossing authority.
- the first local transaction carrier reports
  `authentication_posture: runner_local_content_addressed`: it is locked and internally
  reconciled, but it is not independently authenticated against same-user writes to `.ota/state`.
- free-form task inputs remain unsupported for this carrier because Ota will not hash or expose
  potentially secret values to manufacture a scope identity.
- `--grant` never bypasses `ota run --agent` safety refusal.

This example intentionally does not ship usable authority material. A repository-controlled key or
bundle would be self-issued authority and would defeat the boundary. The signed-file carrier is
bounded offline authority with a bounded local transaction carrier; broker-backed, independently
authenticated one-use work-unit grants remain a later V11.7 surface.
