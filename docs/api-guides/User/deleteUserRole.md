## DELETE /v1/workspaces/{workspaceId}/users/{userId}/roles
**Summary:** Remove user's manager role

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `userId` | path | string | Yes |  | Represents user identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `entityId` (string, required) Represents entity identifier across the system.
- `role` (string, required) Represents valid role.
- `sourceType` (string, required) Represents the source type of this request.
This helps the API to determine on where to select this 'entity', and applies a corresponding
action base on the endpoint.
The entityId should be relative to this source, and can be used whenever the endpoint needs to
access a certain resource. e.g. User group (USER_GROUP)
- **Minimal example:**
```json
{
  "entityId": "60f924bafdaf031696ec6218",
  "role": "WORKSPACE_ADMIN",
  "sourceType": "USER_GROUP"
}
```

### Code examples
```bash
curl -X DELETE "https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/roles" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"entityId":"60f924bafdaf031696ec6218","role":"WORKSPACE_ADMIN","sourceType":"USER_GROUP"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/roles', {
  method: 'DELETE',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/roles'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.delete(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 204
- Media type: `-`
- Description: No Content
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/deleteUserRole-204.json`
(No example available in spec; not executed in sandbox.)

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)