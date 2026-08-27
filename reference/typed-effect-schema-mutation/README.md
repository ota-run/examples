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

# Typed Schema-Mutation Effect

This reference shows the first V12 typed schema-mutation adapter, available from Ota v1.6.27. It
separates the real resource namespace, reusable consequence definition, exact task attachment, and
the typed `action.kind: database_schema_mutation` body.

The adapter captures the declared `migrations/` tree with bounded entry and byte limits on Unix by
opening every effective-cwd and migration-root component relative to a retained repository
descriptor without following symlinks; non-Unix execution refuses. It verifies the ordered manifest
against `migration_set.content_identity` and derives one exact selected-task-bound application plan
that also binds the contract invocation origin and repository-relative effective working directory.
Dry-run publishes the non-secret plan. Repo-level `ota run` and non-dry-run repo-level `ota up`
perform one closure-wide typed preflight
before command-scoped replay-input policy loading, agent/crossing/sandbox admission,
workflow-environment artifact rendering, durable-log preparation, task conditions, required
services, dependencies, PostgreSQL, or another provider is
started. Mode and OS-variant overlays may refine non-execution inputs, but cannot replace this typed
action with another executable body. Non-dry-run `ota up` preserves its generic blocked readiness
receipt with `execution_attempted: false`. This is local plan-to-executor continuity, not a
successful migration, agent-safe classification, positive effect or
execution receipt, archive, or positive assurance claim. The task therefore remains outside
`agent.safe_tasks`.

The accompanying `.ota/org-policy.yaml` demonstrates one exact typed denial. Dry-run exposes the
content-addressed decision and repository-controlled authority posture; real `run` or `up` returns
`OTA_EFFECT_POLICY_DENIED` before side effects. That refusal is operational enforcement, not proof
of PostgreSQL mutation, a canary result, receipt/archive evidence, or positive assurance.

Replace the example namespace and expected migration-set identity with non-secret canonical truth
owned by your repository and operator. Never place credentials or secret-derived identifiers in a
resource binding.
