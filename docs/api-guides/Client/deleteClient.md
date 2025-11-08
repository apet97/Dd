# DELETE /api/v1/workspaces/{workspaceId}/clients/{id}

**Summary:** Delete a client from the workspace.

## Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspaceId` | string | Yes | Clockify workspace identifier. |
| `id` | string | Yes | Client ID to delete. |

## Query parameters
_None._

## Examples
### curl
```bash
curl -X DELETE "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

### Node.js (fetch)
```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab', {
  method: 'DELETE',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json'
  }
});

const data = await response.json();
console.log(data);
```

### Python (requests)
```python
import os
import requests

url = "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients/690f6498c0ee2a5143bd3dab"
response = requests.delete(
    url,
    headers={
        "X-Api-Key": os.environ["CLOCKIFY_API_KEY"],
        "Accept": "application/json",
    },
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

Full artifact: `scripts/api-docs-runner/artifacts/deleteClient/response-200.json`

## Notes
- Deletion is permanent; to restore a client you must recreate it.
- The API echoes the deleted entity payload for confirmation.

[Back to section](README.md) · [Back to index](../index.md)
