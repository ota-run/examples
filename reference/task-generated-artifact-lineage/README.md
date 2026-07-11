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

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   Unless required by applicable law or agreed to in writing, software distributed under the
   License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions
   and limitations under the License.
-->

# Task generated artifact lineage

Use this when a generator creates source files consumed by another task. `artifacts` owns the
named producer, output paths, and source inputs. Consumers must directly depend on the producer
and list the artifact under `requires_artifacts`.

Ota checks output presence after the producer closure and records lineage in task JSON and
receipts. Existing files are not treated as fresh without later derivation evidence.

Open [`ota.yaml`](ota.yaml) for the copy-ready shape.
