## POST /v1/workspaces/{workspaceId}/clients
**Summary:** Add a new client

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
- `address` (string, optional) Represents client's address.
- `email` (string, optional) Represents client email.
- `name` (string, optional) Represents client name.
- `note` (string, optional) Represents additional notes for the client.
- **Minimal example:**
```json
{
  "address": "Ground Floor, ABC Bldg., Palo Alto, California, USA 94020",
  "email": "clientx@example.com",
  "name": "Client X",
  "note": "This is a sample note for the client."
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/clients" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"address":"Ground Floor, ABC Bldg., Palo Alto, California, USA 94020","email":"clientx@example.com","name":"Client X","note":"This is a sample note for the client."}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/clients', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/clients'
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
- Artifact: `scripts/api-docs-runner/artifacts/createClient-201.json`
```json
{
  "address": "Ground Floor, ABC Bldg., Palo Alto, California, USA 94020",
  "archived": false,
  "ccEmails": "clientx@example.com",
  "currencyCode": "USD",
  "currencyId": "33t687e29ae1f428e7ebe505",
  "email": "clientx@example.com",
  "id": "44a687e29ae1f428e7ebe305",
  "name": "Client X",
  "note": "This is a sample note for the client.",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)
