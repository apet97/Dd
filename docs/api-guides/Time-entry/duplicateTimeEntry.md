## POST /v1/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate
**Summary:** Duplicate time entry

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `userId` | path | string | Yes |  | Represents user identifier across the system. |
| `id` | path | string | Yes |  | Represents time entry identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate', {
  method: 'POST',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
}
response = requests.post(url, headers=headers)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 201
- Media type: `application/json`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/duplicateTimeEntry-201.json`
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