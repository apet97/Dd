#!/usr/bin/env python3
"""Clockify API documentation runner.

This script parses the bundled OpenAPI spec and produces:
- Markdown guides grouped per tag under docs/api-guides/
- Placeholder request/response artifacts under scripts/api-docs-runner/artifacts/
- A coverage report recording which operations were executed.

It is designed to be extended with real HTTP execution. For now, it focuses on
schema-driven documentation to provide a consistent baseline that can be
verified and enhanced with live calls later.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_CANDIDATES = [
    REPO_ROOT / "openapi.json",
    REPO_ROOT / "openapi.yaml",
    REPO_ROOT / "openapi.yml",
]
# Include oddly named exports such as "openapi (1).json".
SPEC_CANDIDATES.extend(REPO_ROOT.glob("**/openapi*.json"))
SPEC_CANDIDATES.extend(REPO_ROOT.glob("**/openapi*.yaml"))
SPEC_CANDIDATES.extend(REPO_ROOT.glob("**/openapi*.yml"))

DOCS_ROOT = REPO_ROOT / "docs" / "api-guides"
ARTIFACT_ROOT = REPO_ROOT / "scripts" / "api-docs-runner" / "artifacts"
FIXTURE_ROOT = REPO_ROOT / "scripts" / "api-docs-runner" / "fixtures"


def load_spec(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        if path.suffix in {".yaml", ".yml"}:
            import yaml  # type: ignore

            return yaml.safe_load(f)
        return json.load(f)


def find_spec() -> Path:
    for candidate in SPEC_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Unable to locate an OpenAPI document in the repository")


def slugify(value: str) -> str:
    value = value.strip().replace("&", "and")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "untitled"


@dataclasses.dataclass
class Parameter:
    name: str
    location: str
    required: bool
    schema: Dict[str, Any]
    description: str

    def to_row(self) -> str:
        schema_type = self.schema.get("type") or self.schema.get("$ref", "")
        default = self.schema.get("default", "")
        if default != "":
            default = f"`{default}`"
        return f"| `{self.name}` | {self.location} | {schema_type or 'object'} | {'Yes' if self.required else 'No'} | {default} | {self.description or '-'} |"


@dataclasses.dataclass
class RequestBody:
    description: str
    required: bool
    media_type: str
    schema: Dict[str, Any]


@dataclasses.dataclass
class ResponseExample:
    status: str
    media_type: str
    example: Any
    description: str
    executed: bool = False


@dataclasses.dataclass
class OperationDoc:
    tag: str
    operation_id: str
    summary: str
    description: str
    method: str
    path: str
    parameters: List[Parameter]
    request_body: Optional[RequestBody]
    responses: List[ResponseExample]
    executed: bool = False
    notes: List[str] = dataclasses.field(default_factory=list)


class SpecParser:
    def __init__(self, spec: Dict[str, Any]):
        self.spec = spec
        self.components = spec.get("components", {})

    def resolve_ref(self, ref: str) -> Dict[str, Any]:
        assert ref.startswith("#/"), f"Unsupported ref format: {ref}"
        parts = ref[2:].split("/")
        node: Any = self.spec
        for part in parts:
            node = node[part]
        return node

    def collect_parameters(self, path_item: Dict[str, Any], operation: Dict[str, Any]) -> List[Parameter]:
        params = []
        for level in (path_item.get("parameters", []), operation.get("parameters", [])):
            for raw in level:
                if "$ref" in raw:
                    raw = self.resolve_ref(raw["$ref"])
                schema = raw.get("schema", {})
                params.append(
                    Parameter(
                        name=raw["name"],
                        location=raw["in"],
                        required=raw.get("required", False),
                        schema=schema,
                        description=raw.get("description", ""),
                    )
                )
        return params

    def get_request_body(self, operation: Dict[str, Any]) -> Optional[RequestBody]:
        body = operation.get("requestBody")
        if not body:
            return None
        if "$ref" in body:
            body = self.resolve_ref(body["$ref"])
        content = body.get("content", {})
        if not content:
            return None
        # prefer JSON
        media_type, schema = next(iter(content.items()))
        if "application/json" in content:
            media_type = "application/json"
            schema = content[media_type]
        schema_def = schema.get("schema", {})
        if "$ref" in schema_def:
            schema_def = self.resolve_ref(schema_def["$ref"])
        return RequestBody(
            description=body.get("description", ""),
            required=body.get("required", False),
            media_type=media_type,
            schema=schema_def,
        )

    def build_response_examples(self, operation: Dict[str, Any]) -> List[ResponseExample]:
        responses = []
        for status, resp in operation.get("responses", {}).items():
            if "$ref" in resp:
                resp = self.resolve_ref(resp["$ref"])
            description = resp.get("description", "")
            content = resp.get("content", {})
            media_type = "application/json" if "application/json" in content else (next(iter(content.keys()), ""))
            example = None
            if media_type and media_type in content:
                media_info = content[media_type]
                if "example" in media_info:
                    example = media_info["example"]
                elif "examples" in media_info:
                    example = next(iter(media_info["examples"].values())).get("value")
                schema = media_info.get("schema")
                if example is None and schema:
                    if "$ref" in schema:
                        schema = self.resolve_ref(schema["$ref"])
                    example = synthesize_example(schema)
            responses.append(ResponseExample(status=status, media_type=media_type or "-", example=example, description=description))
        return responses

    def iter_operations(self) -> Iterable[OperationDoc]:
        for path, path_item in self.spec.get("paths", {}).items():
            for method, operation in path_item.items():
                if method.startswith("x-"):
                    continue
                if not isinstance(operation, dict):
                    continue
                tags = operation.get("tags") or ["General"]
                for tag in tags:
                    parameters = self.collect_parameters(path_item, operation)
                    request_body = self.get_request_body(operation)
                    responses = self.build_response_examples(operation)
                    op_id = operation.get("operationId") or slugify(f"{method}-{path}")
                    summary = operation.get("summary") or ""
                    description = operation.get("description") or summary
                    notes = []
                    servers = operation.get("servers") or self.spec.get("servers") or []
                    if servers:
                        server_urls = ", ".join(s.get("url", "") for s in servers)
                        notes.append(f"Servers declared in spec: {server_urls}")
                    yield OperationDoc(
                        tag=tag,
                        operation_id=op_id,
                        summary=summary,
                        description=description,
                        method=method.upper(),
                        path=path,
                        parameters=parameters,
                        request_body=request_body,
                        responses=responses,
                        notes=notes,
                    )


def synthesize_example(schema: Dict[str, Any], depth: int = 0) -> Any:
    if depth > 5:
        return "…"
    if not schema:
        return {}
    if "$ref" in schema:
        return {"$ref": schema["$ref"]}
    if "example" in schema:
        return schema["example"]
    if "default" in schema:
        return schema["default"]
    schema_type = schema.get("type")
    if schema_type == "object" or (not schema_type and "properties" in schema):
        properties = schema.get("properties", {})
        example = {}
        for name, prop in properties.items():
            if "$ref" in prop:
                example[name] = {"$ref": prop["$ref"]}
                continue
            example[name] = synthesize_example(prop, depth + 1)
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            example["additionalProperty"] = synthesize_example(additional, depth + 1)
        return example
    if schema_type == "array":
        item_schema = schema.get("items", {})
        if "$ref" in item_schema:
            return [{"$ref": item_schema["$ref"]}]
        return [synthesize_example(item_schema, depth + 1)]
    if schema_type == "string":
        fmt = schema.get("format")
        if fmt == "date-time":
            return dt.datetime.utcnow().isoformat() + "Z"
        if fmt == "date":
            return dt.date.today().isoformat()
        if "enum" in schema:
            return schema["enum"][0]
        return "string"
    if schema_type == "integer":
        return 0
    if schema_type == "number":
        return 0
    if schema_type == "boolean":
        return False
    return {}


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_params_table(params: List[Parameter]) -> str:
    if not params:
        return "No parameters."
    header = "| Name | In | Type | Required | Default | Description |\n|------|----|------|----------|---------|-------------|"
    rows = [p.to_row() for p in params]
    return "\n".join([header, *rows])


def render_request_body(body: Optional[RequestBody]) -> str:
    if not body:
        return "This operation does not accept a request body."
    summary_lines = [
        f"- **Media type:** `{body.media_type}`",
        f"- **Required:** {'Yes' if body.required else 'No'}",
    ]
    if body.description:
        summary_lines.append(f"- **Description:** {body.description}")
    schema_summary = summarize_schema(body.schema)
    example = json.dumps(synthesize_example(body.schema), indent=2, ensure_ascii=False)
    return "\n".join([
        *summary_lines,
        "- **Schema summary:**",
        schema_summary,
        "- **Minimal example:**",
        f"```json\n{example}\n```",
    ])


def summarize_schema(schema: Dict[str, Any], indent: int = 0) -> str:
    pad = "  " * indent
    if not schema:
        return pad + "(schema not provided)"
    if "properties" in schema:
        lines = []
        required = set(schema.get("required", []))
        for name, prop in schema["properties"].items():
            if "$ref" in prop:
                prop_type = f"ref: {prop['$ref']}"
                desc = prop.get("description", "")
                req = "required" if name in required else "optional"
                lines.append(f"{pad}- `{name}` ({prop_type}, {req}) {desc}")
                continue
            prop_type = prop.get("type", prop.get("$ref", "object"))
            desc = prop.get("description", "")
            req = "required" if name in required else "optional"
            lines.append(f"{pad}- `{name}` ({prop_type}, {req}) {desc}")
            if prop.get("properties"):
                lines.append(summarize_schema(prop, indent + 1))
        return "\n".join(lines) or pad + "(no properties described)"
    if "items" in schema:
        return pad + f"Array of: {summarize_schema(schema['items'], indent + 1)}"
    if "$ref" in schema:
        return pad + f"Reference to {schema['$ref']}"
    return pad + f"Type: {schema.get('type', 'object')}"


def render_responses(responses: List[ResponseExample], op: OperationDoc) -> str:
    if not responses:
        return "No response schema documented."
    blocks = []
    for resp in responses:
        title = f"#### Status {resp.status}"
        example = resp.example
        if example is None:
            example_text = "(No example available in spec; not executed in sandbox.)"
        else:
            example_text = json.dumps(example, indent=2, ensure_ascii=False)
        artifact_path = ARTIFACT_ROOT / f"{op.operation_id}-{resp.status}.json"
        if example is None:
            artifact_content = {
                "status": resp.status,
                "executed": False,
                "note": "No live example captured yet.",
            }
        else:
            artifact_content = {
                "status": resp.status,
                "executed": False,
                "example": example,
            }
        write_file(artifact_path, json.dumps(artifact_content, indent=2))
        blocks.append(
            "\n".join(
                [
                    title,
                    f"- Media type: `{resp.media_type}`" if resp.media_type else "- Media type: n/a",
                    f"- Description: {resp.description or '-'}",
                    f"- Captured example: {'Not executed in sandbox yet.' if not resp.executed else 'See below.'}",
                    f"- Artifact: `{artifact_path.relative_to(REPO_ROOT)}`",
                    "```json\n" + example_text + "\n```" if example is not None else example_text,
                ]
            )
        )
    return "\n\n".join(blocks)


def render_code_samples(op: OperationDoc, config: Dict[str, Any]) -> str:
    base_url = config.get("baseUrl", "https://developer.clockify.me")
    url = f"{base_url}{op.path}"
    curl_lines = [
        "```bash",
        f"curl -X {op.method} \"{url}\" \\",
        "  -H 'X-Api-Key: <YOUR_API_KEY>' \\",
        "  -H 'Accept: application/json'" + (" \\\n  -H 'Content-Type: application/json'" if op.request_body else ""),
    ]
    if op.request_body:
        body_example = json.dumps(synthesize_example(op.request_body.schema), separators=(",", ":"))
        curl_lines.append(f"  -d '{body_example}'")
    curl_lines.append("```")

    node_lines = [
        "```javascript",
        "import fetch from 'node-fetch';",
        "",
        "const response = await fetch('" + url + "', {",
        f"  method: '{op.method}',",
        "  headers: {",
        "    'X-Api-Key': process.env.CLOCKIFY_API_KEY,",
        "    'Accept': 'application/json',",
    ]
    if op.request_body:
        node_lines.append("    'Content-Type': 'application/json',")
    node_lines.append("  },")
    if op.request_body:
        node_lines.append("  body: JSON.stringify(/* TODO: provide payload */),")
    node_lines.append("});")
    node_lines.append("const data = await response.json();")
    node_lines.append("console.log(data);")
    node_lines.append("```")

    py_lines = [
        "```python",
        "import os",
        "import requests",
        "",
        "url = '" + url + "'",
        "headers = {",
        "    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],",
        "    'Accept': 'application/json',",
    ]
    if op.request_body:
        py_lines.append("    'Content-Type': 'application/json',")
    py_lines.append("}")
    if op.request_body:
        py_lines.append("payload = {/* TODO: provide payload */}")
        py_lines.append("response = requests." + ("post" if op.method == "POST" else op.method.lower()) + "(url, headers=headers, json=payload)")
    else:
        py_lines.append("response = requests." + op.method.lower() + "(url, headers=headers)")
    py_lines.append("response.raise_for_status()"); py_lines.append("print(response.json())")
    py_lines.append("```")

    return "\n".join(curl_lines + [""] + node_lines + [""] + py_lines)


def render_operation_markdown(op: OperationDoc, config: Dict[str, Any]) -> str:
    parts = [
        f"## {op.method} {op.path}",
    ]
    if op.summary:
        parts.append(f"**Summary:** {op.summary}")
    if op.description and op.description != op.summary:
        parts.append(op.description)
    parts.append("\n### Path parameters\n" + render_params_table([p for p in op.parameters if p.location == "path"]))
    query_params = [p for p in op.parameters if p.location == "query"]
    parts.append("\n### Query parameters\n" + render_params_table(query_params))
    parts.append("\n### Header parameters\n" + render_params_table([p for p in op.parameters if p.location == "header"]))
    parts.append("\n### Request body\n" + render_request_body(op.request_body))
    parts.append("\n### Code examples\n" + render_code_samples(op, config))
    parts.append("\n### Success responses\n" + render_responses([r for r in op.responses if r.status.startswith('2')], op))
    errors = [r for r in op.responses if not r.status.startswith('2')]
    if errors:
        parts.append("\n### Error responses\n" + render_responses(errors, op))
    else:
        parts.append("\n### Error responses\nNo error responses documented in the spec.")
    if op.notes:
        notes_md = "\n".join(f"- {note}" for note in op.notes)
    else:
        notes_md = "- Sandbox execution pending."
    parts.append("\n### Notes\n" + notes_md)
    parts.append("\n[Back to section](README.md) · [Back to index](../index.md)")
    return "\n".join(parts)


def render_tag_readme(tag: str, operations: List[OperationDoc], tag_descriptions: Dict[str, str]) -> str:
    summary = tag_descriptions.get(tag, "This guide summarises the endpoints available under this tag.")
    ops_table_lines = ["| Method | Path | Operation |", "|--------|------|-----------|"]
    for op in operations:
        ops_table_lines.append(f"| {op.method} | `{op.path}` | [{op.operation_id}.md]({op.operation_id}.md) |")
    common_params = sorted({p.name for op in operations for p in op.parameters if p.location == "query"})
    common_params_md = "- " + "\n- ".join(f"`{name}`" for name in common_params) if common_params else "- None documented."
    errors = sorted({(resp.status, resp.description) for op in operations for resp in op.responses if resp.status.startswith(('4', '5'))})
    error_lines = ["| Status | Notes |", "|--------|-------|"] if errors else ["No shared error patterns documented yet."]
    for status, desc in errors:
        error_lines.append(f"| {status} | {desc or '-'} |")
    entity_map = "- Workspace ID\n- Resource IDs as described per operation"
    cleanup = "The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented."
    prereq = "The automated runner has not yet provisioned fixtures. Future runs should create DOCS_TEST_* resources as needed."
    return f"""# {tag} API

**Summary:** {summary}

- **Base URL (sandbox):** https://developer.clockify.me
- **Authentication:**
  ```
  X-Api-Key: <YOUR_API_KEY>
  Accept: application/json
  Content-Type: application/json
  ```
- **Entity identifiers:**
{entity_map}
- **Prerequisites:** {prereq}

## Operations
{os.linesep.join(ops_table_lines)}

## Common query parameters
{common_params_md}

## Error reference
{os.linesep.join(error_lines)}

## Cleanup policy
{cleanup}
"""


def render_index(tags: List[str], tag_slugs: Dict[str, str], generated_at: str, gaps: List[str]) -> str:
    toc_lines = [f"- [{tag}](./{tag_slugs[tag]}/README.md)" for tag in tags]
    gaps_md = "\n".join(f"- {gap}" for gap in gaps) if gaps else "- None recorded."
    return f"""# Clockify API Guides Index

Welcome! These guides were generated from the repository OpenAPI specification to
make it easier to explore the Clockify API surface area. Each section mirrors a
Clockify API tag and contains individual operation walkthroughs.

## How to use these guides
1. Pick the API section relevant to your task from the table below.
2. Review the prerequisites and entity map to understand required IDs.
3. Follow the code samples and adapt them with your data and API key.
4. Execute against the sandbox first to verify the flow, then promote to production.

## Environments
| Purpose | Base URL |
|---------|----------|
| Sandbox | https://developer.clockify.me |
| Prod | https://api.clockify.me |

## Authentication quickstart
Add the `X-Api-Key` header with your Clockify API key on every request. For JSON
payloads, include `Content-Type: application/json`.

## Sections
{os.linesep.join(toc_lines)}

Generated from OpenAPI spec in repo on {generated_at} UTC.

## Known gaps
{gaps_md}
"""


def render_coverage(operations: List[OperationDoc]) -> str:
    lines = ["# API Coverage", "", "| OperationId | Method | Path | Executed | Artifact |", "|-------------|--------|------|----------|----------|"]
    for op in operations:
        artifact = f"scripts/api-docs-runner/artifacts/{op.operation_id}-*.json"
        lines.append(f"| {op.operation_id} | {op.method} | `{op.path}` | {'Yes' if op.executed else 'No'} | `{artifact}` |")
    return "\n".join(lines)


def load_config() -> Dict[str, Any]:
    config_path = REPO_ROOT / "scripts" / "api-docs-runner" / "config.json"
    if not config_path.exists():
        raise FileNotFoundError("Missing config.json; please create it before running the generator.")
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Clockify API documentation from OpenAPI spec")
    parser.add_argument("--execute", action="store_true", help="(Reserved) Execute live calls against the sandbox")
    args = parser.parse_args()

    spec_path = find_spec()
    spec = load_spec(spec_path)
    parser_obj = SpecParser(spec)

    config = load_config()

    tag_meta = {tag["name"]: tag.get("description", "") for tag in spec.get("tags", []) if isinstance(tag, dict) and tag.get("name")}

    operations = list(parser_obj.iter_operations())
    operations_by_tag: Dict[str, List[OperationDoc]] = {}
    for op in operations:
        operations_by_tag.setdefault(op.tag, []).append(op)

    # Sort operations for consistency
    for ops in operations_by_tag.values():
        ops.sort(key=lambda o: (o.path, o.method))

    tags_sorted = sorted(operations_by_tag.keys())
    tag_slugs = {tag: slugify(tag) for tag in tags_sorted}

    # Generate tag docs
    for tag in tags_sorted:
        ops = operations_by_tag[tag]
        tag_dir = DOCS_ROOT / tag_slugs[tag]
        ensure_directory(tag_dir)
        readme = render_tag_readme(tag, ops, tag_meta)
        write_file(tag_dir / "README.md", readme)
        for op in ops:
            op_md = render_operation_markdown(op, config)
            write_file(tag_dir / f"{op.operation_id}.md", op_md)

    # Index
    generated_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    gaps = ["Sandbox execution not yet automated; examples are schema-derived."]
    index_md = render_index(tags_sorted, tag_slugs, generated_at, gaps)
    write_file(DOCS_ROOT / "index.md", index_md)

    # Coverage
    coverage_md = render_coverage(operations)
    write_file(DOCS_ROOT / "COVERAGE.md", coverage_md)

    # Placeholder fixture README
    fixture_readme = """# Fixtures

This directory will hold JSON templates used to seed sandbox data for the API
documentation runner. It is currently a placeholder.
"""
    write_file(FIXTURE_ROOT / "README.md", fixture_readme)

    print(f"Generated documentation for {len(operations)} operations across {len(tags_sorted)} tags.")
    print(f"Spec source: {spec_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
