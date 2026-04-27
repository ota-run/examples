/*
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
*/

import { createServer } from "node:http";

const bindAddress = process.env.HOSTNAME ?? "0.0.0.0";
const bindPort = Number.parseInt(process.env.PORT ?? "3000", 10);
const metricsPort = Number.parseInt(process.env.METRICS_PORT ?? "9090", 10);
const projectedUrl = process.env.OTA_PUBLIC_URL ?? `http://${bindAddress}:${bindPort}/`;
const metricsUrl =
  process.env.OTA_PUBLIC_URL_METRICS ?? `http://${bindAddress}:${metricsPort}/metrics`;

const server = createServer((request, response) => {
  if (request.url === "/health") {
    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ ok: true }));
    return;
  }

  response.writeHead(200, { "content-type": "text/plain; charset=utf-8" });
  response.end([
    "Ota workload endpoint projection example",
    `Bind: ${bindAddress}:${bindPort}`,
    `OTA_PUBLIC_URL: ${projectedUrl}`,
    `OTA_PUBLIC_URL_METRICS: ${metricsUrl}`,
    "",
    "Use ota run dev and open the URL Ota prints.",
  ].join("\n"));
});

const metricsServer = createServer((request, response) => {
  if (request.url !== "/metrics") {
    response.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
    response.end("not found");
    return;
  }
  response.writeHead(200, { "content-type": "text/plain; charset=utf-8" });
  response.end("example_requests_total 1\n");
});

server.listen(bindPort, bindAddress, () => {
  console.log(`Listening on ${bindAddress}:${bindPort}`);
  console.log(`Open ${projectedUrl}`);
  console.log(`Metrics ${metricsUrl}`);
});

metricsServer.listen(metricsPort, bindAddress, () => {
  console.log(`Listening metrics on ${bindAddress}:${metricsPort}`);
});
