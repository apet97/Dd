# POST /api/v1/workspaces/{workspaceId}/clients

**Summary:** Add a new client to the workspace.

## Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspaceId` | string | Yes | Clockify workspace identifier. |

## Query parameters
_None._

## Request body
- **Content type:** `application/json`
- **Schema highlights:**
  - `name` (string, required) – Client display name.
  - `email` (string, optional) – Primary contact email.
  - `note` (string, optional) – Internal note.

**Example used in sandbox:**
```json
{
  "email": "docs_test_20251108t154112z@example.com",
  "name": "DOCS_TEST_20251108T154112Z_CLIENT",
  "note": "Sandbox documentation seed client"
}
```

## Examples
### curl
```bash
curl -X POST "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"email":"docs_test_20251108t154112z@example.com","name":"DOCS_TEST_20251108T154112Z_CLIENT","note":"Sandbox documentation seed client"}'
```

### Node.js (fetch)
```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients', {
  method: 'POST',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'docs_test_20251108t154112z@example.com',
    name: 'DOCS_TEST_20251108T154112Z_CLIENT',
    note: 'Sandbox documentation seed client'
  })
});

const data = await response.json();
console.log(data);
```

### Python (requests)
```python
import os
import requests

url = "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients"
payload = {
    "email": "docs_test_20251108t154112z@example.com",
    "name": "DOCS_TEST_20251108T154112Z_CLIENT",
    "note": "Sandbox documentation seed client",
}
response = requests.post(
    url,
    headers={
        "X-Api-Key": os.environ["CLOCKIFY_API_KEY"],
        "Accept": "application/json",
        "Content-Type": "application/json",
    },
    json=payload,
)
response.raise_for_status()
print(response.json())
```

## Successful response
**Status 201 – Created**

````json
{
  "address": null,
  "archived": false,
  "ccEmails": null,
  "currencyCode": "USD",
  "currencyId": "672f9cf4ad6f45299c3e3de3",
  "email": "docs_test_20251108t154112z@example.com",
  "id": "690f6498c0ee2a5143bd3dab",
  "name": "DOCS_TEST_20251108T154112Z_CLIENT",
  "note": "Sandbox documentation seed client",
  "workspaceId": "672f9cf4ad6f45299c3e3de2"
}
````

Full artifact: `scripts/api-docs-runner/artifacts/createClient/response-201.json`

## Error examples
- `409 Conflict` when a client with the same name already exists in the workspace.

## Notes
- The API automatically populates currency fields based on the workspace settings.
- Use unique `DOCS_TEST_*` names when scripting documentation runs to avoid conflicts.

[Back to section](README.md) · [Back to index](../index.md)
