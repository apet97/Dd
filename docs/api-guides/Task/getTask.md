## GET /v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}
**Summary:** Get task by id

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `taskId` | path | string | Yes |  | Represents task identifier across the system. |
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}', {
  method: 'GET',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/getTask-200.json`
```json
{
  "assigneeId": "string",
  "assigneeIds": [
    "45b687e29ae1f428e7ebe123",
    "67s687e29ae1f428e7ebe678"
  ],
  "billable": false,
  "budgetEstimate": 10000,
  "costRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "duration": "PT1H30M",
  "estimate": "PT1H30M",
  "hourlyRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "id": "57a687e29ae1f428e7ebe107",
  "name": "Bugfixing",
  "projectId": "25b687e29ae1f428e7ebe123",
  "status": {
    "$ref": "#/components/schemas/TaskStatus"
  },
  "userGroupIds": [
    "67b687e29ae1f428e7ebe123",
    "12s687e29ae1f428e7ebe678"
  ]
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)