## POST /v1/workspaces/{workspaceId}/expenses/categories
**Summary:** Add expense category

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `hasUnitPrice` (boolean, optional) Flag whether expense category has unit price or none.
- `name` (string, required) Represents a valid expense category name.
- `priceInCents` (integer, optional) Represents price in cents as integer.
- `unit` (string, optional) Represents a valid expense category unit.
- **Minimal example:**
```json
{
  "hasUnitPrice": false,
  "name": "Procurement",
  "priceInCents": 1000,
  "unit": "piece"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/categories" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"hasUnitPrice":false,"name":"Procurement","priceInCents":1000,"unit":"piece"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/categories', {
  method: 'POST',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(/* TODO: provide payload */),
});
const data = await response.json();
console.log(data);
```

```python
import os
import requests

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/categories'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 201
- Media type: `application/json`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/createExpenseCategory-201.json`
```json
{
  "archived": false,
  "hasUnitPrice": false,
  "id": "89a687e29ae1f428e7ebe303",
  "name": "Procurement",
  "priceInCents": 1000,
  "unit": "piece",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)