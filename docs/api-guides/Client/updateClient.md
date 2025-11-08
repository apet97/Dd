# PUT /api/v1/workspaces/{workspaceId}/clients/{id}

**Summary:** Update an existing client's details.

## Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspaceId` | string | Yes | Clockify workspace identifier. |
| `id` | string | Yes | Client ID returned when the client was created. |

## Query parameters
_None._

## Request body
- **Content type:** `application/json`
- **Schema highlights:**
  - `name` (string, optional) – Updated display name.
  - `email` (string, optional) – Updated contact email.
  - `note` (string, optional) – Internal note.
  - `address` (string, optional) – Mailing address.

**Example used in sandbox:**
```json
{
  "address": "123 Documentation Street",
  "email": "docs_test_20251108t154112z+updated@example.com",
  "name": "DOCS_TEST_20251108T154112Z_CLIENT_UPDATED",
  "note": "Updated note for sandbox documentation seed client"
}
```

## Examples
### curl
```bash
curl -X PUT "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"address":"123 Documentation Street","email":"docs_test_20251108t154112z+updated@example.com","name":"DOCS_TEST_20251108T154112Z_CLIENT_UPDATED","note":"Updated note for sandbox documentation seed client"}'
```

### Node.js (fetch)
```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab', {
  method: 'PUT',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    address: '123 Documentation Street',
    email: 'docs_test_20251108t154112z+updated@example.com',
    name: 'DOCS_TEST_20251108T154112Z_CLIENT_UPDATED',
    note: 'Updated note for sandbox documentation seed client'
  })
});

const data = await response.json();
console.log(data);
```

### Python (requests)
```python
import os
import requests

url = "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab"
payload = {
    "address": "123 Documentation Street",
    "email": "docs_test_20251108t154112z+updated@example.com",
    "name": "DOCS_TEST_20251108T154112Z_CLIENT_UPDATED",
    "note": "Updated note for sandbox documentation seed client",
}
response = requests.put(
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
**Status 200 – OK**

````json
{
  "address": "123 Documentation Street",
  "archived": false,
  "ccEmails": null,
  "currencyId": "672f9cf4ad6f45299c3e3de3",
  "email": "docs_test_20251108t154112z+updated@example.com",
  "id": "690f6498c0ee2a5143bd3dab",
  "name": "DOCS_TEST_20251108T154112Z_CLIENT_UPDATED",
  "note": "Updated note for sandbox documentation seed client",
  "workspaceId": "672f9cf4ad6f45299c3e3de2"
}
````

Full artifact: `scripts/api-docs-runner/artifacts/updateClient/response-200.json`

## Notes
- Only supplied fields are updated; omit fields to leave them unchanged.

[Back to section](README.md) · [Back to index](../index.md)
