## PUT /v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}
**Summary:** Update task on project

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `taskId` | path | string | Yes |  | Represents task identifier across the system. |
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `contains-assignee` | query | boolean | No | `True` | Flag to set whether task will have assignee or none. |
| `membership-status` | query | string | No |  | Represents a membership status. |

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `assigneeId` (string, optional) 
- `assigneeIds` (array, optional) Represents list of assignee ids for the task.
- `billable` (boolean, optional) Indicates whether a task is billable or not.
- `budgetEstimate` (integer, optional) Represents a task budget estimate as integer.
- `estimate` (string, optional) Represents a task duration estimate.
- `name` (string, required) Represents task name.
- `status` (string, optional) Represents task status.
- `userGroupIds` (array, optional) Represents list of user group ids for the task.
- **Minimal example:**
```json
{
  "assigneeId": "string",
  "assigneeIds": [
    "45b687e29ae1f428e7ebe123",
    "67s687e29ae1f428e7ebe678"
  ],
  "billable": false,
  "budgetEstimate": 10000,
  "estimate": "PT1H30M",
  "name": "Bugfixing",
  "status": "DONE",
  "userGroupIds": [
    "67b687e29ae1f428e7ebe123",
    "12s687e29ae1f428e7ebe678"
  ]
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"assigneeId":"string","assigneeIds":["45b687e29ae1f428e7ebe123","67s687e29ae1f428e7ebe678"],"billable":false,"budgetEstimate":10000,"estimate":"PT1H30M","name":"Bugfixing","status":"DONE","userGroupIds":["67b687e29ae1f428e7ebe123","12s687e29ae1f428e7ebe678"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{taskId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/updateTask-200.json`
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