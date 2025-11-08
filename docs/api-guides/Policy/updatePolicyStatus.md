## PATCH /v1/workspaces/{workspaceId}/time-off/policies/{id}
**Summary:** Change policy status

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `id` | path | string | Yes |  | Represents policy identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `status` (string, required) Provide the status you would like to use for changing the policy.
- **Minimal example:**
```json
{
  "status": "ACTIVE"
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"status":"ACTIVE"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{id}', {
  method: 'PATCH',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{id}'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.patch(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updatePolicyStatus-200.json`
```json
{
  "allowHalfDay": false,
  "allowNegativeBalance": true,
  "approve": {
    "$ref": "#/components/schemas/ApproveDto"
  },
  "archived": true,
  "automaticAccrual": {
    "$ref": "#/components/schemas/AutomaticAccrualDto"
  },
  "automaticTimeEntryCreation": {
    "$ref": "#/components/schemas/AutomaticTimeEntryCreationDto"
  },
  "everyoneIncludingNew": false,
  "id": "5b715612b079875110791111",
  "name": "Days",
  "negativeBalance": {
    "$ref": "#/components/schemas/NegativeBalanceDto"
  },
  "projectId": "string",
  "timeUnit": "DAYS",
  "userGroupIds": [
    "5b715612b079875110791342",
    "5b715612b079875110791324",
    "5b715612b079875110793142"
  ],
  "userIds": [
    "5b715612b079875110791432",
    "5b715612b079875110791234"
  ],
  "workspaceId": "5b715612b079875110792222"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)