## POST /v1/workspaces/{workspaceId}/time-off/policies
**Summary:** Create time off policy

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
- `allowHalfDay` (boolean, optional) Indicates whether policy allows half days.
- `allowNegativeBalance` (boolean, optional) Indicates whether policy allows negative balances.
- `approve` (ref: #/components/schemas/ApproveDto, required) 
- `archived` (boolean, optional) Indicates whether policy is archived.
- `automaticAccrual` (ref: #/components/schemas/AutomaticAccrualRequest, optional) 
- `automaticTimeEntryCreation` (ref: #/components/schemas/AutomaticTimeEntryCreationRequest, optional) 
- `color` (string, optional) Provide color in format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
- `everyoneIncludingNew` (boolean, optional) Indicates whether the policy is to be applied to future new users.
- `icon` (string, optional) Provide icon.
- `name` (string, required) Represents name of new policy.
- `negativeBalance` (ref: #/components/schemas/NegativeBalanceRequest, optional) 
- `timeUnit` (string, optional) Indicates time unit of the policy. 
- `userGroups` (ref: #/components/schemas/UserGroupIdsSchema, optional) 
- `users` (ref: #/components/schemas/UserIdsSchema, optional) 
- **Minimal example:**
```json
{
  "allowHalfDay": false,
  "allowNegativeBalance": true,
  "approve": {
    "$ref": "#/components/schemas/ApproveDto"
  },
  "archived": true,
  "automaticAccrual": {
    "$ref": "#/components/schemas/AutomaticAccrualRequest"
  },
  "automaticTimeEntryCreation": {
    "$ref": "#/components/schemas/AutomaticTimeEntryCreationRequest"
  },
  "color": "#8BC34A",
  "everyoneIncludingNew": false,
  "icon": "UMBRELLA",
  "name": "Mental health days",
  "negativeBalance": {
    "$ref": "#/components/schemas/NegativeBalanceRequest"
  },
  "timeUnit": "DAYS",
  "userGroups": {
    "$ref": "#/components/schemas/UserGroupIdsSchema"
  },
  "users": {
    "$ref": "#/components/schemas/UserIdsSchema"
  }
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"allowHalfDay":false,"allowNegativeBalance":true,"approve":{"$ref":"#/components/schemas/ApproveDto"},"archived":true,"automaticAccrual":{"$ref":"#/components/schemas/AutomaticAccrualRequest"},"automaticTimeEntryCreation":{"$ref":"#/components/schemas/AutomaticTimeEntryCreationRequest"},"color":"#8BC34A","everyoneIncludingNew":false,"icon":"UMBRELLA","name":"Mental health days","negativeBalance":{"$ref":"#/components/schemas/NegativeBalanceRequest"},"timeUnit":"DAYS","userGroups":{"$ref":"#/components/schemas/UserGroupIdsSchema"},"users":{"$ref":"#/components/schemas/UserIdsSchema"}}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies'
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
- Artifact: `scripts/api-docs-runner/artifacts/createPolicy-201.json`
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