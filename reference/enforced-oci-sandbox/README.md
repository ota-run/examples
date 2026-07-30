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

# Enforced OCI sandbox

Use this when a selected agent-safe task already declares an ephemeral container lane and Ota
should enforce the compatible runtime-boundary subset through the local OCI provider.

Run:

```sh
ota run verify --agent --sandbox-target oci_local
```

Omitting `--sandbox-target` in agent mode also selects `oci_local` when it is the one compatible
enforcing target. Human execution must request the enforcing target explicitly.

`container.platform` is ordinary container execution truth, not a sandbox-only hint. The current
backend accepts Linux OCI targets only. Ota applies the pin to task variants, inputs, environment,
service bindings, requirements, and every execution-backend container it creates for that lane;
`oci_local` additionally requires it so the runner host platform cannot silently replace the
declared target.

Dry-run resolves admission and declared requirement truth without starting a provider-backed probe
container. Real execution performs any required OCI runtime/tool probe only after the sandbox
application transaction and cleanup authority exist. Receipt JSON labels that boundary
`purpose: precondition_probe`, binds it to the exact admitted segment that owns the requirement,
and retains terminal cleanup evidence on a blocking refusal. It cannot substitute for the selected
task's `task_execution` evidence.

The example proves only the selected lane:

- the repository root is read-only;
- `reports/` is the only writable host-backed carve-out;
- declared protected paths cannot be written;
- external IP networking is denied within the isolated container namespace;
- every engine-reported mount is limited to the repository root and declared carve-outs;
- Ota inspects the applied controls through completion and confirms removal of its exact boundary;
- the runner-authored receipt is archived with the contract snapshot and any identified
  policy-authority snapshot needed to re-derive effective policy.

Image-declared volumes, undeclared mounts, and runtime-control sockets refuse rather than becoming
ambient provider state. It does not prove host-wide isolation, loopback absence, targeted egress,
application output correctness, or execution outside Ota.

The first provider admits finite `run`, `script`, and `command` task bodies only. It refuses typed
prepare/action/Compose/launch/attach bodies, requirements, required services, and conditional
checks because those paths would otherwise perform work before the evidenced OCI segment exists.
It also refuses `attachments.isolated_paths` until their durable files or named volumes have
transaction-bound creation, retention, and failure-cleanup evidence.
