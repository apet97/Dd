## GET /v1/workspaces/{workspaceId}/time-entries/{id}
**Summary:** Get a specific time entry on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `id` | path | string | Yes |  | Represents time entry identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `hydrated` | query | boolean | No | `False` | Flag to set whether to include additional information of a time entry or not. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}'
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
- Artifact: `scripts/api-docs-runner/artifacts/getTimeEntry-200.json`
```json
{
  "billable": false,
  "costRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "customFieldValues": [
    {
      "$ref": "#/components/schemas/CustomFieldValueDtoV1"
    }
  ],
  "description": "This is a sample time entry description.",
  "hourlyRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
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