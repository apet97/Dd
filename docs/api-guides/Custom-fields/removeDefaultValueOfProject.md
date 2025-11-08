## DELETE /v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}
**Summary:** Remove custom field from project

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |
| `customFieldId` | path | string | Yes |  | Represents custom field identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X DELETE "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/custom-fields/{customFieldId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/removeDefaultValueOfProject-200.json`
```json
{
  "allowedValues": [
    "New York",
    "London",
    "Manila",
    "Sydney",
    "Belgrade"
  ],
  "description": "This field contains a location.",
  "entityType": "USER",
  "id": "44a687e29ae1f428e7ebe305",
  "name": "location",
  "onlyAdminCanEdit": false,
  "placeholder": "Location",
  "projectDefaultValues": [
    {
      "$ref": "#/components/schemas/CustomFieldDefaultValuesDtoV1"
    }
  ],
  "required": false,
  "status": "VISIBLE",
  "type": "DROPDOWN_MULTIPLE",
  "workspaceDefaultValue": "Manila",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)