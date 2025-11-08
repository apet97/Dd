#!/usr/bin/env python3
"""Execute Clockify API calls to capture live request/response artifacts."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import time
from pathlib import Path
from typing import Any, Dict, Optional

import requests

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"
ARTIFACT_ROOT = Path(__file__).resolve().parent / "artifacts"
RATE_LIMIT_SECONDS = 0.4


class ArtifactWriter:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def write(self, operation_id: str, request_payload: Dict[str, Any], response_payload: Dict[str, Any], status_code: int) -> None:
        base = self.root / operation_id
        base.mkdir(parents=True, exist_ok=True)
        (base / "request.json").write_text(json.dumps(request_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (base / f"response-{status_code}.json").write_text(
            json.dumps(response_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )


class ClockifyRunner:
    def __init__(self, config: Dict[str, Any], tags: Optional[list[str]] = None) -> None:
        self.config = config
        self.tags = {tag.lower() for tag in tags} if tags else None
        base_url = config.get("baseUrl")
        if not base_url:
            raise SystemExit("config.json must include baseUrl")
        self.base_url = base_url.rstrip("/")
        self.workspace_id = config.get("workspaceId")
        if not self.workspace_id:
            raise SystemExit("config.json must include workspaceId")
        headers = config.get("headers", {})
        self.session = requests.Session()
        self.session.headers.update(headers)
        if "Content-Type" not in self.session.headers and config.get("defaultContentType"):
            self.session.headers["Content-Type"] = config["defaultContentType"]
        self.writer = ArtifactWriter(ARTIFACT_ROOT)
        now_utc = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
        self.timestamp = now_utc.isoformat().replace("+00:00", "Z")
        self.prefix = f"DOCS_TEST_{self.timestamp.replace(':', '').replace('-', '')}"
        self.created_client_id: Optional[str] = None

    def request(
        self,
        operation_id: str,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        expected_status: Optional[int] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        headers = dict(self.session.headers)
        api_key_header = next((key for key in headers if key.lower() == "x-api-key"), None)
        if api_key_header:
            headers[api_key_header] = "REDACTED"
        request_payload = {
            "method": method,
            "url": url,
            "headers": headers,
            "params": params or {},
            "json": json_body,
        }
        response = self.session.request(method, url, params=params, json=json_body, timeout=60)
        time.sleep(RATE_LIMIT_SECONDS)
        try:
            body: Any = response.json()
        except ValueError:
            body = response.text
        response_payload = {
            "status": response.status_code,
            "headers": dict(response.headers),
            "body": body,
        }
        self.writer.write(operation_id, request_payload, response_payload, response.status_code)
        if expected_status and response.status_code != expected_status:
            raise RuntimeError(
                f"{operation_id} expected status {expected_status} but received {response.status_code}: {body}"
            )
        return response_payload

    # Client operations -------------------------------------------------
    def run_client_operations(self) -> None:
        client_name = f"{self.prefix}_CLIENT"
        create_payload = {
            "name": client_name,
            "email": f"{self.prefix.lower()}@example.com",
            "note": "Sandbox documentation seed client",
        }
        create_response = self.request(
            "createClient",
            "POST",
            f"/api/v1/workspaces/{self.workspace_id}/clients",
            json_body=create_payload,
            expected_status=201,
        )
        body = create_response["body"]
        if not isinstance(body, dict) or "id" not in body:
            raise RuntimeError("createClient did not return a JSON object with an id")
        client_id = body["id"]
        self.created_client_id = client_id

        self.request(
            "getClients",
            "GET",
            f"/api/v1/workspaces/{self.workspace_id}/clients",
            params={"page": 1, "page-size": 50},
            expected_status=200,
        )

        update_payload = {
            "name": f"{client_name}_UPDATED",
            "email": f"{self.prefix.lower()}+updated@example.com",
            "note": "Updated note for sandbox documentation seed client",
            "address": "123 Documentation Street",
        }
        self.request(
            "updateClient",
            "PUT",
            f"/api/v1/workspaces/{self.workspace_id}/clients/{client_id}",
            json_body=update_payload,
            expected_status=200,
        )

        self.request(
            "getClient",
            "GET",
            f"/api/v1/workspaces/{self.workspace_id}/clients/{client_id}",
            expected_status=200,
        )

        self.request(
            "deleteClient",
            "DELETE",
            f"/api/v1/workspaces/{self.workspace_id}/clients/{client_id}",
            expected_status=200,
        )
        self.created_client_id = None

        self.request(
            "getClientNotFound",
            "GET",
            f"/api/v1/workspaces/{self.workspace_id}/clients/{client_id}",
            expected_status=400,
        )

    def cleanup(self) -> None:
        if not self.created_client_id:
            return
        try:
            self.request(
                "deleteClient",
                "DELETE",
                f"/api/v1/workspaces/{self.workspace_id}/clients/{self.created_client_id}",
            )
        except Exception as exc:  # pragma: no cover - best effort cleanup
            print(f"Failed to cleanup client {self.created_client_id}: {exc}")

    def run(self) -> None:
        try:
            if self.tags is None or "client" in self.tags:
                self.run_client_operations()
        finally:
            self.cleanup()


def load_config() -> Dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise SystemExit("Missing config.json. See scripts/api-docs-runner/config.json.example for guidance.")
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Execute Clockify API documentation calls")
    parser.add_argument("--tags", nargs="*", help="Limit execution to specific tags (e.g. Client)")
    args = parser.parse_args()
    config = load_config()
    runner = ClockifyRunner(config, args.tags)
    runner.run()


if __name__ == "__main__":
    main()
