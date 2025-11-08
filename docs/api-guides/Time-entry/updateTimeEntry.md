## PUT /v1/workspaces/{workspaceId}/time-entries/{id}
**Summary:** Update time entry on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `id` | path | string | Yes |  | Represents time entry identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `billable` (boolean, optional) Indicates whether a time entry is billable or not.
- `customFields` (array, optional) Represents a list of value objects for user’s custom fields.
- `description` (string, optional) Represents time entry description.
- `end` (string, optional) Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
- `projectId` (string, optional) Represents project identifier across the system.
- `start` (string, required) Represents a start date in yyyy-MM-ddThh:mm:ssZ format.
- `tagIds` (array, optional) Represents a list of tag ids.
- `taskId` (string, optional) Represents task identifier across the system.
- `type` (string, optional) 
- **Minimal example:**
```json
{
  "billable": false,
  "customFields": [
    {
      "$ref": "#/components/schemas/UpdateCustomFieldRequest"
    }
  ],
  "description": "This is a sample time entry description.",
  "end": "2021-01-01T00:00:00Z",
  "projectId": "25b687e29ae1f428e7ebe123",
  "start": "2020-01-01T00:00:00Z",
  "tagIds": [
    "321r77ddd3fcab07cfbb567y",
    "44x777ddd3fcab07cfbb88f"
  ],
  "taskId": "54m377ddd3fcab07cfbb432w",
  "type": "REGULAR"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"billable":false,"customFields":[{"$ref":"#/components/schemas/UpdateCustomFieldRequest"}],"description":"This is a sample time entry description.","end":"2021-01-01T00:00:00Z","projectId":"25b687e29ae1f428e7ebe123","start":"2020-01-01T00:00:00Z","tagIds":["321r77ddd3fcab07cfbb567y","44x777ddd3fcab07cfbb88f"],"taskId":"54m377ddd3fcab07cfbb432w","type":"REGULAR"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/{id}'
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
- Artifact: `scripts/api-docs-runner/artifacts/updateTimeEntry-200.json`
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