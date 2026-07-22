<!--
Copyright (C) 2026 — 2026, Ota. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
-->

# Managed lifecycle proof

Use this shape when a workflow must prove a bounded manager-owned start/readiness/assertion/stop
transaction without copying Compose commands into shell. Run:

```sh
ota proof lifecycle --workflow smoke --json --archive .
```

Ota leases only services observed inactive by the declared manager and finalizes them in reverse
order after failure or interruption. The archive is local, scope-bound lifecycle evidence; read
its `not_proved[]` boundaries and do not treat it as application, CI, or repo-global proof.
