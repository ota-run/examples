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

- First contract: [`templates/node-service`](templates/node-service) or [`templates/python-service`](templates/python-service)
  These are now the cleanest copyable examples for workflow-first setup plus tool acquisition truth.
  They also match the starter direction `ota init` now prefers when Ota can model the repo honestly:
  toolchain-owned ecosystems, `prepare.kind: dependency_hydration` for setup, and `command` for
  simple finite task bodies.
- Service starter with `prepare` plus runtime proof: [`templates/node-service`](templates/node-service)
  Use this when the repo needs one honest `.env.local` bootstrap step before setup and one declared service URL that `ota proof runtime` can verify.
- Existing messy repo: [`reference/adoption-flow`](reference/adoption-flow)
  This is the flagship adoption starter. It now includes a real Java/Maven repo shape with
  `toolchains.java` as the Java owner, a local service example, a task-prerequisite example with
  `requires_services`, docs, and release-script companions so users can copy more than just
  `ota.yaml`.
- Env policy plus task-scoped env requirements in a serious repo: [`reference/canonical-team-repo`](reference/canonical-team-repo)
  Use this when you want `env.vars`, ordered `env.sources`, reusable surfaces, probe-backed readiness, and one release-only env requirement in the same contract.
- Tool acquisition through the contract: [`templates/node-service`](templates/node-service) or [`templates/python-service`](templates/python-service)
  Use the Node template when `pnpm` should activate through Corepack only on selected workflow paths. Use the Python template when `toolchains.python` should own the `uv` lane directly through first-class hydration; `toolchains.python` can also own Poetry under `package_managers.poetry` when the repo is Poetry-first.
- Focused acquisition behavior: [`reference/tool-acquisition-flow`](reference/tool-acquisition-flow)
  Use this when you want one compact example that isolates workflow-scoped Corepack and command acquisition without the rest of a larger flagship repo.
- Focused live or staging verification effect truth: [`reference/task-effect-integration-test`](reference/task-effect-integration-test)
  Use this when the verification lane depends on real services or non-local credentials and should be classified as `effects.network_kind: integration_test` instead of a vague broad network task.
- Managed Rust toolchain ownership: [`reference/rust-toolchain-flow`](reference/rust-toolchain-flow)
  Use this when the repo needs Rust to behave as one managed ecosystem through `toolchains.rust`
  instead of duplicating the same truth under `runtimes`, `tools`, or setup shell glue.
- Managed Node runtime ownership with Corepack package-manager activation:
  [`reference/node-corepack-toolchain-flow`](reference/node-corepack-toolchain-flow)
  Use this when the repo wants `toolchains.node` to own the Node runtime, `node` executable, and
  declared Corepack package-manager activation in one place.
- Managed Java runtime ownership with SDKMAN:
  [`reference/java-sdkman-toolchain-flow`](reference/java-sdkman-toolchain-flow)
  Use this when the repo wants `toolchains.java` to own `java` and `javac`, while Maven stays
  explicitly standalone under `tools`.
- First-class dependency or image hydration:
  [`reference/task-prepare-dependency-hydration`](reference/task-prepare-dependency-hydration)
  Use this when one setup task is really finite dependency hydration and ota should model that
  phase structurally through `tasks.<name>.prepare` instead of hiding it in a shell command.
- First-class package hydration through a node package manager:
  [`reference/task-prepare-package-hydration`](reference/task-prepare-package-hydration)
  Use this when a repo's root install lane is really lockfile-backed package hydration and ota
  should own that setup phase structurally instead of teaching `pnpm install --frozen-lockfile`,
  `yarn install --immutable`, or `npm ci` as shell glue.
- First-class mixed setup sequencing:
  [`reference/task-prepare-sequence`](reference/task-prepare-sequence)
  Use this when one repo-level `setup` task honestly needs more than one structural finite step,
  such as Node package hydration plus Python `uv` hydration in one ordered lane.
- First-class orchestrated dependency hydration:
  [`reference/task-prepare-orchestrated-hydration`](reference/task-prepare-orchestrated-hydration)
  Use this when the truthful setup lane is still first-class dependency hydration, but the
  selected environment is mediated by a declared orchestrator such as `devbox`.
- First-class Go module hydration:
  [`reference/task-prepare-go-module-hydration`](reference/task-prepare-go-module-hydration)
  Use this when a repo's setup lane is really `go mod download` and ota should own that finite
  module-hydration phase structurally instead of hiding it in `run`.
- First-class Bundler hydration:
  [`reference/task-prepare-bundler-hydration`](reference/task-prepare-bundler-hydration)
  Use this when a repo's setup lane is really repo-local gem hydration and ota should own that
  finite Bundler phase structurally instead of teaching `bundle install` as shell glue, with
  Bundler version governance and selected-path fulfillment carried by `toolchains.ruby`.
- Compose adapter-owned env/file/profile/project truth:
  [`reference/compose-adapter-inputs`](reference/compose-adapter-inputs)
  Use this when the repo's real Docker Compose lane owns a repo-subdirectory adapter root,
  interpolation files, file-stack selection, profile selection, or project naming and those
  inputs should stay in `adapter_inputs.compose.*` plus workflow-owned overlays instead of shell
  `cd`, `--project-directory`, `--env-file`, `-f`, `--profile`, or `-p` glue. It also shows the
  right lane for host-derived compose interpolation such as `${OTA_HOST_WORKSPACE}` and
  `${OTA_HOST_UID}` when the runtime truth depends on the real host repo root or host uid. The
  same example also shows `prepare.source.compose` for typed dependency hydration inside a Compose
  service, where the host prerequisite stays `requirements.tools.docker` instead of duplicating a
  host Node toolchain just because the in-service command is `npm ci`.
- Podman compose adapter-owned env/file/profile/project truth:
  [`reference/podman-compose-adapter-inputs`](reference/podman-compose-adapter-inputs)
  Use this when the repo's real compose lane is `podman compose` and the adapter root,
  interpolation files, file-stack selection, profile selection, and project naming should stay on
  first-class compose surfaces instead of shell `cd`, `--env-file`, `-f`, or `-p` glue.
- Bake adapter-owned file-stack truth:
  [`reference/bake-adapter-inputs`](reference/bake-adapter-inputs)
  Use this when the repo's real `docker buildx bake` lane owns a repo-subdirectory adapter root,
  one base Bake file stack, plus task- or workflow-scoped overlays and that truth should stay in
  `adapter_inputs.bake.*` instead of shell `cd` or `-f` / `--file` flags.
- Deterministic env bootstrap without shell glue:
  [`reference/action-ensure-env-file`](reference/action-ensure-env-file)
  Use this when `.env` preparation is really governed host-file mutation and ota should own key
  replacement, secret generation, and stale-key removal through `action.kind: ensure_env_file`.
- Service-derived env values:
  [`reference/service-env-bindings`](reference/service-env-bindings)
  Use this when a task should receive `DB_HOST`, `DATABASE_URL`, or similar values from declared
  service endpoint truth instead of freezing `localhost`, `host.docker.internal`, or handwritten
  DSNs into task shells.
- Workflow-owned rendered env artifacts:
  [`reference/workflow-rendered-env`](reference/workflow-rendered-env)
  Use this when one workflow should render a dotenv artifact from repo template truth plus
  workflow-specific overlays and then project that file into Compose-managed service startup.
- Workflow-scoped receipt archive and baseline truth:
  [`reference/receipt-workflow-history`](reference/receipt-workflow-history)
  Use this when a repo has more than one workflow and receipt archive, baseline, or snapshot
  history must stay inside the selected workflow lane instead of drifting to whichever receipt ran
  last.
- Bundled deterministic setup bootstrap:
  [`reference/action-ensure-bundle`](reference/action-ensure-bundle)
  Use this when setup needs more than one ordered deterministic setup action and ota should own
  that finite bundle through `action.kind: ensure_bundle` instead of a shell script wrapper.
- Deterministic Git checkout bootstrap:
  [`reference/action-ensure-git-checkout`](reference/action-ensure-git-checkout)
  Use this when one setup lane owns clone-if-missing materialization of a sibling or vendored
  checkout and ota should own that truth through `action.kind: ensure_git_checkout` instead of
  shell `git clone` glue.
- Container network bootstrap:
  [`reference/action-ensure-container-network`](reference/action-ensure-container-network)
  Use this when one setup lane owns shared external Docker network readiness and ota should own
  that truth through `action.kind: ensure_container_network` instead of shell
  `docker network inspect/create` glue.
- Compose adapter-owned publication remap:
  [`reference/compose-adapter-inputs`](reference/compose-adapter-inputs)
  Use this when a native structured Docker Compose lane owns the published host URL for one
  Compose service and ota should map `--host-port` through
  `runtime.listeners.<name>.project.publication.compose.service` instead of asking operators to
  patch compose files or kill ports by hand.
- Compose-managed service volume reset:
  [`reference/action-reset-compose-service-volume`](reference/action-reset-compose-service-volume)
  Use this when one destructive local recovery lane truthfully owns resetting a Compose-managed
  service volume such as local Postgres data and ota should own the stop/rm/volume-reset/restart
  sequence through `action.kind: reset_compose_service_volume` instead of shell glue.
- Typed systemd host-service ownership:
  [`reference/systemd-host-service`](reference/systemd-host-service)
  Use this when the repo's real service owner is `systemd` and ota should derive start, stop, and
  active-state readiness from a declared unit instead of shell `systemctl` glue.
- Container app URL projection: [`execution/container/node-service`](execution/container/node-service)
  Use this when one canonical app task should support container and native execution modes, bind to fixed internal ports (`3000` app + `9090` metrics), let ota pick free host ports, inject `OTA_PUBLIC_URL` and listener-specific env values before startup, and print the same reachable primary URL for users.
- Fixed host URL + one-run override: [`reference/adoption-flow`](reference/adoption-flow)
  Use this when the task keeps a fixed projected host port in contract (`8080`) but operators sometimes need a predictable one-run public override like `ota run dev:api --host-port 4000` without changing the app’s internal bind.
- Internal task plumbing boundary: mark setup-only graph nodes with `internal: true`
  Use this when tasks like `setup` should still run through `depends_on`/hooks but should stay out of default operator discovery (`ota tasks`). Use `ota tasks --all` to inspect the full graph including internal nodes.
- Windows-first repo adoption: [`reference/windows-adoption-flow`](reference/windows-adoption-flow)
  This is the Windows-oriented flagship starter. It shows how ota keeps `.NET`, PowerShell release flow, Windows-native build-tool activation, and cross-platform task variants explicit without hiding the repo behind shell glue.
- Workspace adoption flow: [`workspace/adoption-flow`](workspace/adoption-flow)
- CI and release flow: [`ci`](ci)
- Container or remote execution: [`execution`](execution)
- Remote execution context only: [`execution/remote/template`](execution/remote/template)
  Use this when one task should simply run off-host and you do not need one intentional shared remote backend boundary.
- Minimal shared remote backend boundary: [`execution/remote/shared-remote-backend-minimal`](execution/remote/shared-remote-backend-minimal)
  Use this when two long-running remote tasks should intentionally reuse one ota-managed remote backend boundary and you want the smallest copyable example before adding remote target activation.
- Shared remote backend plus remote producer activation: [`execution/remote/shared-remote-backend-activation`](execution/remote/shared-remote-backend-activation)
  Use this when a helper task should target a repo-managed remote producer through one shared backend and ask ota to make that producer ready first.
- Local helper app or probe targeting a repo-managed service: [`execution/local-topology/task-target-binding`](execution/local-topology/task-target-binding)
  Use this when a helper workload like a sandbox, SDK harness, or smoke probe should target one repo-managed app by service identity, keep an open override when needed, and stop hardcoding `localhost` or `host.docker.internal` as the primary contract truth.
- Minimal shared local backend boundary: [`execution/local-topology/shared-local-backend-minimal`](execution/local-topology/shared-local-backend-minimal)
  Use this when two long-running container tasks should intentionally reuse one ota-managed backend boundary and you want the smallest copyable example before adding target binding, fulfillment, or policy-backed backend environment.
- Minimal native shared local backend boundary: [`execution/local-topology/shared-local-backend-native-minimal`](execution/local-topology/shared-local-backend-native-minimal)
  Use this when two long-running native tasks should intentionally reuse one ota-managed host backend boundary without adding container image or policy-backed backend environment semantics.
- Co-located long-running helper app plus producer in one shared container boundary: [`execution/local-topology/shared-local-backend`](execution/local-topology/shared-local-backend)
  Use this when both workloads are intentional long-running container tasks and ota should treat them as one shared local backend so `address_view: topology` resolves to the producer's in-boundary address without host bridge hacks.
- Shared local backend plus backend preparation on the actual run path: [`execution/local-topology/shared-local-backend-fulfillment`](execution/local-topology/shared-local-backend-fulfillment)
  Use this when one shared backend shape should stay explicit but ota also needs to prepare the effective runtime/tool union before any bound task or dependency executes.
- Shared local backend plus policy-governed backend image resolution: [`execution/local-topology/shared-local-backend-environment`](execution/local-topology/shared-local-backend-environment)
  Use this when the repo should declare backend image intent and let policy resolve the approved effective image for the shared backend instead of hardcoding the final image string in every contract.
- OS-specific launchers or platform branching: [`execution/os-aware`](execution/os-aware)
- Custom adapters and backend providers: [`extensions`](extensions)
- Multi-repo bootstrap: [`workspace/monorepo`](workspace/monorepo)
- Serious repo reference shape: [`reference/canonical-team-repo`](reference/canonical-team-repo) or [`reference/swift-service`](reference/swift-service)
  The canonical team repo is the advanced example that now shows the modern workflow surface:
  `workflows.default`, one reusable runtime `surface`, one reusable probe-backed readiness
  check, and one tool acquisition lane attached to `pnpm`.

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
