# GET /api/v1/workspaces/{workspaceId}/clients

**Summary:** Find clients on a workspace with pagination support.

## Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workspaceId` | string | Yes | Clockify workspace identifier. |

## Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `page` | integer | No (defaults to `1`) | Page index (1-based). |
| `page-size` | integer | No (defaults to `50`) | Number of records per page (max 500). |

## Examples
### curl
```bash
curl "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients?page=1&page-size=50" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

### Node.js (fetch)
```javascript
import fetch from 'node-fetch';

const url = new URL('https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients');
url.searchParams.set('page', '1');
url.searchParams.set('page-size', '50');

const response = await fetch(url, {
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

url = "https://developer.clockify.me/api/v1/workspaces/672f9cf4ad6f45299c3e3de2/clients"
params = {"page": 1, "page-size": 50}
response = requests.get(
    url,
    headers={
        "X-Api-Key": os.environ["CLOCKIFY_API_KEY"],
        "Accept": "application/json",
    },
    params=params,
)
response.raise_for_status()
print(response.json())
```

## Successful response
**Status 200 – OK**

````json
[
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
]
````

- `total-count` response header reflects the total number of clients. In this run it was `1`.
- Full artifact: `scripts/api-docs-runner/artifacts/getClients/response-200.json`

## Notes
- Filtering by name is not available in this endpoint; fetch all and filter client-side if needed.

[Back to section](README.md) · [Back to index](../index.md)
