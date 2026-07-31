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

# `ota-run/examples`

Collections of solid, real-world examples you can copy, adapt, and use to see how ota removes hidden setup, repeated explanations, and brittle workflow glue.

If you are introducing ota to a team, start with the adoption flows first. They show how ota earns trust before you move into CI, execution boundaries, or adapter patterns.

The shortest public first-run lane is now:

1. `ota doctor`
2. `ota detect --dry-run .` or `ota init --dry-run .`
3. `ota validate`
4. `ota up --dry-run`
5. `ota up`
6. `ota run <task>` or `ota proof runtime --workflow <name>`

Use these as starting points when you want:
- a repo contract you can adapt quickly
- a first-week adoption flow for an existing repo
- a workspace contract for multi-repo setup
- a CI or release pattern built around `ota`
- an `execution` boundary when host drift or remote execution is the problem
- an `extensions` boundary when the repo needs custom check, export, or backend adapters

## Layout

- `templates/` - starter contracts you can copy into a new repo
- `ci/` - provider-specific CI patterns
- `execution/` - container and remote execution patterns
- `execution/local-topology/` - task target-binding patterns for helper apps and probes
- `execution/os-aware/` - OS-specific launcher examples
- `extensions/` - check, export, and backend adapter patterns
- `workspace/` - multi-repo workspace patterns
- `workspace/adoption-flow/` - workspace onboarding and first-week adoption pattern
- `reference/` - canonical, production-adjacent repo examples

## Choose by problem

Start with the smallest example that names your problem. Each example README explains the
underlying contract shape; this page is a map, not a second contract reference.

### Execution-governance capability map

Use the public reference for the governing model, then copy the nearest example:

| Capability | Public reference | Example or operator path |
| --- | --- | --- |
| Safe agent execution and refusal | [Safe Agent Execution and Refusal](https://ota.run/docs/reference/safe-agent-execution-and-refusal) | [`reference/safe-agent-execution`](reference/safe-agent-execution) |
| Contract-to-CI governance | [Contract-to-CI Governance](https://ota.run/docs/reference/contract-to-ci-governance) | [`ci/github-actions`](ci/github-actions) |
| Sandbox policy and runtime enforcement | [Sandbox Policy and Runtime Enforcement](https://ota.run/docs/reference/sandbox-policy-and-runtime-enforcement) | [`reference/enforced-oci-sandbox`](reference/enforced-oci-sandbox) |
| Proof evidence and honest boundaries | [Proof Evidence and Honest Boundaries](https://ota.run/docs/reference/proof-evidence-and-honest-boundaries) | [`reference/runtime-proof-evidence`](reference/runtime-proof-evidence) and [`reference/managed-lifecycle-proof`](reference/managed-lifecycle-proof) |
| Replay inputs and trusted baselines | [Replay Inputs and Trusted Baselines](https://ota.run/docs/reference/replay-inputs-and-trusted-baselines) | [`reference/policy-replay-input-identity`](reference/policy-replay-input-identity) and [`reference/replay-baseline-regeneration`](reference/replay-baseline-regeneration) |
| Contract-claim assurance | [Contract-Claim Assurance](https://ota.run/docs/reference/contract-claim-assurance) | Use the runtime-proof and receipt-history examples together; assurance is derived from selected contract and evidence truth, not a second author-authored verdict. |
| Audited execution boundary crossings | [Audited Execution Boundary Crossings](https://ota.run/docs/reference/audited-execution-boundary-crossings) | [`reference/audited-crossing-authority`](reference/audited-crossing-authority), an unreleased V11.7 preview that deliberately ships no usable authority material |
| Semantic snapshots and correlation | [Semantic Snapshots and Correlation](https://ota.run/docs/reference/semantic-snapshots-and-correlation) | [`reference/receipt-workflow-history`](reference/receipt-workflow-history) |

| If you need to... | Start here | Why |
| --- | --- | --- |
| Write a first contract | [`templates/node-service`](templates/node-service) or [`templates/python-service`](templates/python-service) | Copyable workflow-first setup, toolchain ownership, hydration, and finite tasks. |
| Prove a local service runtime | [`templates/node-service`](templates/node-service) | Adds `.env.local` bootstrap and a declared URL for `ota proof runtime`. |
| Adopt Ota in an existing repo | [`reference/adoption-flow`](reference/adoption-flow) | Flagship Java/Maven adoption with services, task prerequisites, docs, and release companions. |
| Model a production-shaped team repo | [`reference/canonical-team-repo`](reference/canonical-team-repo) | Env policy, reusable surfaces, probe-backed readiness, and release-only requirements. |
| Add CI, container, or remote execution | [`ci`](ci) or [`execution`](execution) | Provider patterns and execution-boundary examples. |
| Bootstrap several repositories together | [`workspace/adoption-flow`](workspace/adoption-flow) | First-week workspace adoption and multi-repo readiness. |

### Setup, toolchains, and hydration

| Problem | Example | Use it when |
| --- | --- | --- |
| Focused tool acquisition | [`reference/tool-acquisition-flow`](reference/tool-acquisition-flow) | You need workflow-scoped Corepack or command acquisition without a full repo shape. |
| Managed Rust | [`reference/rust-toolchain-flow`](reference/rust-toolchain-flow) | `toolchains.rust` should own Rust rather than setup shell glue. |
| Managed Node and Corepack | [`reference/node-corepack-toolchain-flow`](reference/node-corepack-toolchain-flow) | One declaration should own Node, `node`, and Corepack activation. |
| Managed Java and SDKMAN | [`reference/java-sdkman-toolchain-flow`](reference/java-sdkman-toolchain-flow) | Java is contract-owned while Maven remains an explicit standalone tool. |
| Generic dependency or image hydration | [`reference/task-prepare-dependency-hydration`](reference/task-prepare-dependency-hydration) | A finite setup phase belongs in `tasks.<name>.prepare`. |
| Lockfile-backed Node package hydration | [`reference/task-prepare-package-hydration`](reference/task-prepare-package-hydration) | Ota should own `pnpm`, Yarn, or npm installation rather than a shell body. |
| Python `.venv` plus uv requirements | [`reference/task-prepare-uv-requirements`](reference/task-prepare-uv-requirements) | Setup owns deterministic virtualenv creation and requirements hydration. |
| Editable local Python project with uv | [`reference/task-prepare-uv-local-project`](reference/task-prepare-uv-local-project) | One checked-out package needs explicit extras, groups, source identity, and lockfile-aware replay truth. |
| Mixed ordered setup | [`reference/task-prepare-sequence`](reference/task-prepare-sequence) | One setup lane needs several structural finite steps. |
| Orchestrator-owned hydration | [`reference/task-prepare-orchestrated-hydration`](reference/task-prepare-orchestrated-hydration) | Hydration is mediated by a declared orchestrator such as Devbox. |
| Compose-owned hydration | [`reference/task-prepare-compose-hydration`](reference/task-prepare-compose-hydration) | A declared Compose service owns typed package hydration. |
| Go module hydration | [`reference/task-prepare-go-module-hydration`](reference/task-prepare-go-module-hydration) | Setup is `go mod download`, not shell glue. |
| Bundler hydration | [`reference/task-prepare-bundler-hydration`](reference/task-prepare-bundler-hydration) | Repo-local gems and their Ruby toolchain need first-class ownership. |

### Runtime, environment, and proof

| Problem | Example | Use it when |
| --- | --- | --- |
| Runtime-owned bind projection | [`reference/launch-runtime-projection`](reference/launch-runtime-projection) | A supported launch adapter should project host and port from `runtime.listeners`. |
| Service-derived environment | [`reference/service-env-bindings`](reference/service-env-bindings) | Tasks need endpoint-derived values such as `DATABASE_URL` rather than handwritten DSNs. |
| Deterministic `.env` creation | [`reference/action-ensure-env-file`](reference/action-ensure-env-file) | Ota should own key replacement, generation, and stale-key removal. |
| Workflow-rendered dotenv artifact | [`reference/workflow-rendered-env`](reference/workflow-rendered-env) | A workflow renders an environment file and projects it into Compose startup. |
| Live or staging verification effects | [`reference/task-effect-integration-test`](reference/task-effect-integration-test) | Verification uses real services or credentials and needs `effects.network_kind: integration_test`. |
| Runtime seam evidence | [`reference/runtime-proof-evidence`](reference/runtime-proof-evidence) | Readiness is insufficient; distinguish reachable, exercised, and fault-controlled dependencies. |
| Enforced OCI sandbox | [`reference/enforced-oci-sandbox`](reference/enforced-oci-sandbox) | An explicit-platform ephemeral container lane needs provider-attested read-only filesystem and bounded network-denial enforcement. |
| Audited crossing authority | [`reference/audited-crossing-authority`](reference/audited-crossing-authority) | A heavier non-agent lane requires an exact signed grant from an independently managed system authority. |
| Human-only OAuth or terminal prompt | [`reference/command-interaction`](reference/command-interaction) | A finite structured command requires a real native terminal and refuses for agents or CI. |
| Workflow-scoped receipt history | [`reference/receipt-workflow-history`](reference/receipt-workflow-history) | Archive, baseline, and snapshot history must stay in the selected workflow lane. |
| Fixed public URL override | [`reference/adoption-flow`](reference/adoption-flow) | Operators need a one-run `--host-port` without changing the internal bind. |
| Internal graph plumbing | `internal: true` | Setup-only nodes should remain runnable through dependencies but stay out of normal `ota tasks` discovery. |

### Compose, containers, and adapters

| Problem | Example | Use it when |
| --- | --- | --- |
| Docker Compose inputs and publication | [`reference/compose-adapter-inputs`](reference/compose-adapter-inputs) | Compose owns adapter root, env/file/profile/project inputs, typed hydration, and a service publication remap. |
| Podman Compose inputs | [`reference/podman-compose-adapter-inputs`](reference/podman-compose-adapter-inputs) | The same adapter-owned truth belongs to `podman compose`. |
| Bake file-stack inputs | [`reference/bake-adapter-inputs`](reference/bake-adapter-inputs) | `docker buildx bake` owns its adapter root and file stack. |
| Build a Dockerfile image | [`reference/action-build-container-image`](reference/action-build-container-image) | A task owns a local image required by a declared container or Compose lane. |
| Reset a Compose service volume | [`reference/action-reset-compose-service-volume`](reference/action-reset-compose-service-volume) | A destructive local recovery lane owns stop, reset, and restart. |
| Ensure a shared container network | [`reference/action-ensure-container-network`](reference/action-ensure-container-network) | Setup owns external Docker network readiness. |
| Container URL projection | [`execution/container/node-service`](execution/container/node-service) | Native and container modes share an app contract while Ota resolves public URLs. |
| Typed systemd ownership | [`reference/systemd-host-service`](reference/systemd-host-service) | The real service owner is `systemd`, not a shell wrapper. |

### Generated artifacts and deterministic bootstrap

| Problem | Example | Use it when |
| --- | --- | --- |
| Generated artifact lineage | [`reference/task-generated-artifact-lineage`](reference/task-generated-artifact-lineage) | A generator produces named source files consumed by downstream tasks. |
| Policy-governed replay inputs | [`reference/policy-replay-input-identity`](reference/policy-replay-input-identity) | Selected replay-sensitive closures must declare and match immutable input identities. |
| Bundled deterministic setup | [`reference/action-ensure-bundle`](reference/action-ensure-bundle) | Setup owns several ordered deterministic actions. |
| Clone a required sibling checkout | [`reference/action-ensure-git-checkout`](reference/action-ensure-git-checkout) | A setup lane owns clone-if-missing checkout materialization. |
| Materialize a Git template | [`reference/action-ensure-git-template`](reference/action-ensure-git-template) | A scaffold or factory comes from a Git-backed template. |

### Local and remote topology

| Problem | Example | Use it when |
| --- | --- | --- |
| Run one task remotely | [`execution/remote/template`](execution/remote/template) | You need off-host execution without a shared backend boundary. |
| Share a remote backend | [`execution/remote/shared-remote-backend-minimal`](execution/remote/shared-remote-backend-minimal) | Two remote tasks intentionally reuse one managed backend. |
| Activate a remote producer | [`execution/remote/shared-remote-backend-activation`](execution/remote/shared-remote-backend-activation) | A helper targets a managed remote producer and asks Ota to prepare it. |
| Target a local producer | [`execution/local-topology/task-target-binding`](execution/local-topology/task-target-binding) | A helper app or probe should use service identity instead of hardcoded host addresses. |
| Share a local container backend | [`execution/local-topology/shared-local-backend-minimal`](execution/local-topology/shared-local-backend-minimal) | Two long-running container tasks intentionally reuse one backend. |
| Share a local native backend | [`execution/local-topology/shared-local-backend-native-minimal`](execution/local-topology/shared-local-backend-native-minimal) | Two long-running native tasks intentionally reuse one host backend. |
| Co-locate a helper and producer | [`execution/local-topology/shared-local-backend`](execution/local-topology/shared-local-backend) | Container workloads share one backend and topology address view. |
| Fulfil a shared backend | [`execution/local-topology/shared-local-backend-fulfillment`](execution/local-topology/shared-local-backend-fulfillment) | Ota must prepare the effective runtime/tool union before a bound task runs. |
| Policy-resolved backend image | [`execution/local-topology/shared-local-backend-environment`](execution/local-topology/shared-local-backend-environment) | Policy resolves an approved shared-backend image. |

### Platform and workspace patterns

| Problem | Example | Use it when |
| --- | --- | --- |
| Windows-first adoption | [`reference/windows-adoption-flow`](reference/windows-adoption-flow) | `.NET`, PowerShell, and Windows-native tools need explicit cross-platform variants. |
| Serious Swift service | [`reference/swift-service`](reference/swift-service) | You need a production-adjacent non-Java reference shape. |
| CI and release flow | [`ci`](ci) | You need provider-specific verification and release patterns. |
| OS-specific launchers | [`execution/os-aware`](execution/os-aware) | Launch commands branch by platform. |
| Custom adapters or providers | [`extensions`](extensions) | The repo needs staged check, export, or backend adapters. |
| Multi-repo bootstrap | [`workspace/monorepo`](workspace/monorepo) | One workspace contract provisions several repositories. |

## Example types

- Starter contract: minimal copyable `ota.yaml` with a short README
- Flagship adoption starter: contract plus repo signals, docs, and companion files that show obvious `doctor -> explain -> detect -> up -> agents` value
- Windows-first flagship starter: a reference example that keeps `.NET`, PowerShell, and cross-platform variants explicit
- Canonical advanced reference: production-adjacent repo shape that teaches a full operating model
- Workspace reference: multi-repo bootstrap and adoption ordering.

## How to use

1. Pick the folder that matches the problem you are solving.
2. Read that folder's `README.md` first to understand why the pattern exists.
3. Open its `ota.yaml` for the exact contract and task notes.
4. Copy only the files you need.
5. Run `ota validate .` or `ota workspace validate .` before you ship the pattern.

## Validate this repo

Run `ota run validate` before opening a pull request.

## Dogfood this repo

Run `ota run dogfood` when Ota UX changes and you want to re-check the flagship examples against the current local CLI behavior.

## What these examples are teaching

- the repo shape and use-case for each example
- when to use the example
- what problem the example solves
- where to open the example's `ota.yaml` for task-level instructions

## Contributing

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.
- Use the pull request and issue templates under [`.github/`](.github/).
- Follow [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- See [`SECURITY.md`](SECURITY.md) for security disclosures.
- See [`SUPPORT.md`](SUPPORT.md) for help and response expectations.
