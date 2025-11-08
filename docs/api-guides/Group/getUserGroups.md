## GET /v1/workspaces/{workspaceId}/user-groups
**Summary:** Find all groups on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `project-id` | query | string | No |  | If provided, you'll get a filtered list of groups that matches the string provided in their project id. |
| `name` | query | string | No |  | If provided, you'll get a filtered list of groups that matches the string provided in their name. |
| `sort-column` | query | string | No |  | Column to be used as the sorting criteria. |
| `sort-order` | query | string | No |  | Sorting mode. |
| `page` | query | integer | No | `1` | Page number. |
| `page-size` | query | integer | No | `50` | Page size. |
| `includeTeamManagers` | query | boolean | No | `False` | If provided, you'll get a list of team managers assigned to this user group. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/user-groups" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/user-groups', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/user-groups'
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
- Artifact: `scripts/api-docs-runner/artifacts/getUserGroups-200.json`
```json
[
  {
    "$ref": "#/components/schemas/UserGroupDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)