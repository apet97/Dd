## PATCH /v1/workspaces/{workspaceId}/user/{userId}/time-entries
**Summary:** Stop currently running timer on workspace for user

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
- `end` (string, required) Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
- **Minimal example:**
```json
{
  "end": "2021-01-01T00:00:00Z"
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"end":"2021-01-01T00:00:00Z"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries'
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
- Artifact: `scripts/api-docs-runner/artifacts/stopRunningTimeEntry-200.json`
```json
{
  "billable": false,
  "customFieldValues": [
    {
      "$ref": "#/components/schemas/CustomFieldValueDtoV1"
    }
  ],
  "description": "This is a sample time entry description.",
  "id": "64c777ddd3fcab07cfbb210c",
  "isLocked": false,
  "kioskId": "94c777ddd3fcab07cfbb210d",
  "projectId": "25b687e29ae1f428e7ebe123",
  "tagIds": [
    "321r77ddd3fcab07cfbb567y",
    "44x777ddd3fcab07cfbb88f"
  ],
  "taskId": "54m377ddd3fcab07cfbb432w",
  "timeInterval": {
    "$ref": "#/components/schemas/TimeIntervalDtoV1"
  },
  "type": "BREAK",
  "userId": "5a0ab5acb07987125438b60f",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)