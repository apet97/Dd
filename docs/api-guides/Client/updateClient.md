## PUT /v1/workspaces/{workspaceId}/clients/{id}
**Summary:** Update client

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `id` | path | string | Yes |  | Represents client identifier across the system. |
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `archive-projects` | query | boolean | No |  | - |
| `mark-tasks-as-done` | query | boolean | No |  | - |

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `address` (string, optional) Represents client's address.
- `archived` (boolean, optional) Indicates if client will be archived or not.
- `ccEmails` (array, optional) 
- `currencyId` (string, optional) Represents currency identifier across the system.
- `email` (string, optional) Represents client email.
- `name` (string, optional) Represents client name.
- `note` (string, optional) Represents additional notes for the client.
- **Minimal example:**
```json
{
  "address": "Ground Floor, ABC Bldg., Palo Alto, California, USA 94020",
  "archived": false,
  "ccEmails": [
    "string"
  ],
  "currencyId": "53a687e29ae1f428e7ebe888",
  "email": "clientx@example.com",
  "name": "Client X",
  "note": "This is a sample note for the client."
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/clients/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"address":"Ground Floor, ABC Bldg., Palo Alto, California, USA 94020","archived":false,"ccEmails":["string"],"currencyId":"53a687e29ae1f428e7ebe888","email":"clientx@example.com","name":"Client X","note":"This is a sample note for the client."}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/clients/{id}', {
  method: 'PUT',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/clients/{id}'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.put(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateClient-200.json`
```json
{
  "address": "Ground Floor, ABC Bldg., Palo Alto, California, USA 94020",
  "archived": false,
  "ccEmails": "clientx@example.com",
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