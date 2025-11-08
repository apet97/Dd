## DELETE /v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}
**Summary:** Delete request
This endpoint is deprecated. It will be available until 1st of July 2025. Use [Time Off](#tag/Time-Off/operation/deleteTimeOffRequest) instead.

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `policyId` | path | string | Yes |  | Represents policy identifier across the system. |
| `requestId` | path | string | Yes |  | Represents time off request identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X DELETE "https://developer.clockify.me/v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}', {
  method: 'DELETE',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json',
  },
});
const data = await response.json();
console.log(data);
```

```python
import os
import requests

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/policies/{policyId}/requests/{requestId}'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
}
response = requests.delete(url, headers=headers)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/deletePtoTimeOffRequest-200.json`
```json
{
  "balanceDiff": 1,
  "createdAt": "2022-08-26T08:32:01.640708Z",
  "id": "5b715612b079875110791111",
  "note": "Time Off Request Note",
  "policyId": "5b715612b079875110792333",
  "status": {
    "$ref": "#/components/schemas/PtoTimeOffRequestStatus"
  },
  "timeOffPeriod": {
    "$ref": "#/components/schemas/TimeOffRequestPeriod"
  },
  "userId": "5b715612b079875110794444",
  "workspaceId": "5b715612b079875110792222"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)