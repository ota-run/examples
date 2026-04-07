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

# Contributing

This repository is a curated collection of copyable Ota examples.

## What to submit

- real examples that can be copied and adapted
- templates that reflect a real repo shape
- workspace, CI, and release patterns that match shipped Ota behavior
- docs updates when the example changes the recommended flow

## What to avoid

- toy examples that do not map to a real workflow
- duplicate patterns that do not add new value
- examples that drift from the current CLI contract

## Pull requests

- Keep changes narrow and example-focused.
- Update the example README and contract together.
- Add a short note explaining why the example matters.
- Prefer one example per pull request unless the change is purely editorial.
- Run `ota run validate` before opening the pull request.
- Run `ota run dogfood` when the change touches Ota UX, flagship examples, or adoption-facing copy.

## Issues

- Use the issue templates under [`.github/ISSUE_TEMPLATE`](.github/ISSUE_TEMPLATE) for bugs and example requests.
- Include the repo or workflow you want documented if the request is specific.

## Review bar

- The example should be real enough to copy.
- The example should be explicit enough to modify safely.
- The example should stay aligned with current `ota` behavior.
- Flagship examples should still demonstrate obvious value on the current CLI, not only stay schema-valid.
