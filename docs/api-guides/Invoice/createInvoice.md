## POST /v1/workspaces/{workspaceId}/invoices
**Summary:** Add invoice

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
- `clientId` (string, required) Represents client identifier across the system.
- `currency` (string, required) Represents the currency used by the invoice.
- `dueDate` (string, required) Represents an invoice due date in yyyy-MM-ddThh:mm:ssZ format.
- `issuedDate` (string, required) Represents an invoice issued date in yyyy-MM-ddThh:mm:ssZ format.
- `number` (string, required) Represents an invoice number.
- **Minimal example:**
```json
{
  "clientId": "98h687e29ae1f428e7ebe707",
  "currency": "USD",
  "dueDate": "2020-06-01T08:00:00Z",
  "issuedDate": "2020-01-01T08:00:00Z",
  "number": "202306121129"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"clientId":"98h687e29ae1f428e7ebe707","currency":"USD","dueDate":"2020-06-01T08:00:00Z","issuedDate":"2020-01-01T08:00:00Z","number":"202306121129"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices'
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
- Artifact: `scripts/api-docs-runner/artifacts/createInvoice-201.json`
```json
{
  "billFrom": "Business X",
  "clientId": "34p687e29ae1f428e7ebe562",
  "currency": "USD",
  "dueDate": "2020-06-01T08:00:00Z",
  "id": "78a687e29ae1f428e7ebe303",
  "issuedDate": "2020-01-01T08:00:00Z",
  "number": "202306121129"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)