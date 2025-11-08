## GET /v1/workspaces/{workspaceId}/projects/{projectId}
**Summary:** Find project by ID

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `hydrated` | query | boolean | No | `False` | If set to true, results will contain additional information about the project |
| `custom-field-entity-type` | query | string | No | `TIMEENTRY` | If provided, you'll get a filtered list of custom fields that matches the provided string with the custom field entity type. |
| `expense-limit` | query | integer | No | `20` | Represents maximum number of expenses to fetch. |
| `expense-date` | query | string | No |  | If provided, you will get expenses dated before the provided value in yyyy-MM-dd format. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/getProject-200.json`
```json
{
  "color": "#000000",
  "duration": "60000",
  "id": "5b641568b07987035750505e",
  "memberships": [
    {
      "$ref": "#/components/schemas/MembershipDtoV1"
    }
  ],
  "name": "Software Development",
  "note": "This is a sample note for the project.",
  "public": false,
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)