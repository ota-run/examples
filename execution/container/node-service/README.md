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

# Node service in a container execution context

A copyable starting point for a Node service that runs in a container context, keeps `node_modules` isolated from the host tree, and uses workload endpoint projection so `ota run start` prints one real host URL plus one secondary listener URL.

## Why this exists

- keeps local and CI runtime behavior aligned
- makes the execution boundary obvious
- gives `ota doctor` and `ota run` a stable path
- keeps `run: pnpm dev` simple while ota owns host URL resolution
- keeps one canonical task intent (`start`) while still supporting `--mode native` and mode-specific lifecycle
- helps a team standardize Node setup without turning the README into a shell-script graveyard

## Use when

- host setup drifts from CI
- you want everyone to run the same container image
- you want ota to orchestrate container-backed setup and verification
- you want ota to reserve a free host port and inject `OTA_PUBLIC_URL` before startup
- you want the container to use its own `node_modules` tree instead of host-native binaries
- you need one primary app URL and one secondary listener URL from the same task
- you want the first commands to work the same way on every machine

## Try this

```bash
ota doctor
ota validate .
ota run setup
ota run start
# open the URL ota prints (same value as OTA_PUBLIC_URL)
ota run start --mode native
```

## Projection contract

`tasks.start` in this example shows:

- fixed internal binds on `0.0.0.0:3000` (`http`) and `0.0.0.0:9090` (`metrics`)
- `attachments.isolated_paths: [node_modules]` so the container uses an Ota-managed named volume for dependencies
- host projection with `project.host.port.mode: auto` on both listeners
- explicit `project.host.primary: true` on `http` so ota can pick one deterministic primary URL
- mode-aware execution branches so `ota run start` defaults to the container branch and `ota run start --mode native` uses host wiring without a duplicate task name
- pre-start env injection (`OTA_PUBLIC_URL`, `OTA_PUBLIC_HOST`, `OTA_PUBLIC_PORT`, `OTA_PUBLIC_URL_HTTP`, `OTA_PUBLIC_URL_METRICS`)
- one printed primary host URL that matches `OTA_PUBLIC_URL`, plus listener-specific URLs for secondary endpoints

Ota binds the repo source into the container as usual, but overlays `node_modules` with an engine-managed named volume under the execution context so platform-specific binaries stay compatible with the container image.

## Included app

This folder includes a minimal runnable app:

- `package.json` with `dev` and `test` scripts
- `src/server.mjs` that serves `http` and `metrics`, and prints `OTA_PUBLIC_URL` plus `OTA_PUBLIC_URL_METRICS`

Run `ota run test` if you want to verify the example task chain without starting the long-running dev server.
Run `ota run clean:start` if you want the same app intent with container `lifecycle: ephemeral`.

## Reset Ota-managed state

Use this when you want to clear the container execution residue and isolated dependency volume:

```bash
ota clean
```
