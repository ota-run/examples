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
ota authority inspect --json
ota run verify
ota run publish --dry-run
ota run publish --grant approved-publish
```

- `authority inspect` checks the fixed prebound-file hardening profile without selecting a grant,
  creating a crossing transaction, or writing authority state. Its strongest claim remains
  `current_process_filesystem_guarded`; informational unknowns are not provider attestation.
- `verify` is routine and rejects an inapplicable grant.
- `publish` refuses before execution when the exact grant is missing, stale, revoked, or out of
  scope.
- a matching grant binds the semantic contract identity, selected closure, platform, execution
  overrides, `non_agent` actor posture, and short validity window.
- real execution creates a runner-owned crossing transaction under `.ota/state/crossings` before
  the selected lane mutates state, then binds its terminal outcome to the fresh receipt and archive;
  refusal and dry-run perform admission only and create no transaction or crossing record.
- governed `ota proof runtime` and `ota proof lifecycle` retain one proof-owned transaction
  across their complete invocation set and cleanup. Their archives embed and re-derive the exact
  terminal carrier admission; nested task environments do not receive the runner-private authority
  capability.
- refused dry-run and admission-produced execution receipts carry typed `prebound_file` authority
  source, selected authority/grant when present, stable refusal reason, and
  `execution_started: false`; that refusal evidence is not crossing authority.
- the first local transaction carrier reports
  `authentication_posture: runner_local_content_addressed`: it is locked and internally
  reconciled, but it is not independently authenticated against same-user writes to `.ota/state`.
- free-form task inputs remain unsupported for this carrier because Ota will not hash or expose
  potentially secret values to manufacture a scope identity.
- `--grant` never bypasses `ota run --agent` safety refusal.

This example intentionally does not ship usable authority material. A repository-controlled key,
bundle, broker binding, launcher credential, or lease would be self-issued authority and would
defeat the boundary. The same repository contract works with either protected carrier; the fixed
system store, not `ota.yaml`, selects which carrier supplies authority.

## Operator layout

The repository is only the consumer. A system administrator installs the fixed trust store at
`/etc/ota/crossing-authorities.json` on Linux; the binding then points to separately protected,
root-owned bundle and sequence-state files, commonly under `/var/lib/ota/`. Run Ota as an
unprivileged user and keep the signing key outside the runner.

Read [Prebound Crossing Authority](https://ota.run/docs/reference/prebound-crossing-authority)
before provisioning this carrier. It defines the operator flow, fixed file roles, record shapes,
and the important limitation: root-owned files protect only against Ota's current process, not a
CI job with administrative escalation. Do not self-provision the authority in a GitHub-hosted
workflow.

## Broker carrier

On Linux, an administrator may instead install the protected broker binding at
`/etc/ota/crossing-brokers.json` and start Ota through a hardened launcher that supplies the fixed
connected Unix descriptor. The repository does not change:

```sh
ota run publish --dry-run --json
ota run publish
```

The preview reports `authority_carrier: authority_broker` and
`decision: requires_live_authorization` without contacting the launcher. Real `run`/`up` freezes
the exact semantic work unit, verifies challenge-bound launcher attestation and signed broker
authorization, durably creates the pending crossing transaction, and atomically consumes one lease
after deterministic admission succeeds and before provisioning or work. Ordinary workflow
readiness timeout is authority-significant. Receipts carry runner-derived closure/effect/resource
breadth using counts and hashed resource identities, not raw resource values. Optional
`--grant platform-release-authority` only checks the non-secret authority
label; it is not a lease ID.

If consumption acknowledgement is lost, Ota never starts or resumes the abandoned work. A later
invocation first obtains fresh launcher attestation, re-queries the exact durable consume intent,
and closes the old transaction as incomplete whether the broker reports consumed, not consumed,
or unknown. Any new work requires fresh authorization and a new lease.

Existing broker attestation v1 evidence remains bounded to
`launcher_attested_one_use`: it proves the challenge-bound launcher protocol and atomic one-use
consumption, not a complete runtime-separation profile. A v2 protected-launcher binding selects one
exact protocol-published profile and requires every ordered observation, including non-root
principal, protected authority/attestor state, credential and session isolation, host-control and
privilege posture, plus content-addressed launcher and configuration identities. Only complete v2
evidence emits `protected_launcher_attested_one_use`. The two branches are mutually exclusive and
neither implies provider-attested separation. The v2 marker is explicit on the protected binding
as `schema_version: 2`; an unversioned binding remains v1 and cannot be upgraded from nested fields.

Read [Broker Crossing Authority](https://ota.run/docs/reference/broker-crossing-authority)
for the protected binding, launcher protocol, receipt evidence, and current proof/pressure limits.
