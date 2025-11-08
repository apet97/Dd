## PUT /v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/hourly-rate
**Summary:** Update task billable rate

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `id` | path | string | Yes |  | Represents task identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `amount` (integer, required) Represents an hourly rate amount as integer.
- `since` (string, optional) Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.
- **Minimal example:**
```json
{
  "amount": 20000,
  "since": "2020-01-01T00:00:00Z"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/hourly-rate" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"amount":20000,"since":"2020-01-01T00:00:00Z"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/hourly-rate', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/tasks/{id}/hourly-rate'
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
- Artifact: `scripts/api-docs-runner/artifacts/setTaskHourlyRate-200.json`
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