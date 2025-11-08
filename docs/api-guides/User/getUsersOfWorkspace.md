## GET /v1/workspaces/{workspaceId}/users
**Summary:** Find all users on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `email` | query | string | No |  | If provided, you'll get a filtered list of users that contain the provided string in their email address. |
| `project-id` | query | string | No |  | If provided, you'll get a list of users that have access to the project. |
| `status` | query | string | No |  | If provided, you'll get a filtered list of users with the corresponding status. |
| `account-statuses` | query | string | No |  | If provided, you'll get a filtered list of users with the corresponding account status filter. If not, this will only filter ACTIVE, PENDING_EMAIL_VERIFICATION, and NOT_REGISTERED Users. |
| `name` | query | string | No |  | If provided, you'll get a filtered list of users that contain the provided string in their name |
| `sort-column` | query | string | No |  | Sorting column criteria. Default value: EMAIL |
| `sort-order` | query | string | No |  | Sorting mode. Default value: ASCENDING |
| `page` | query | integer | No | `1` | Page number. |
| `page-size` | query | integer | No | `50` | Page size. |
| `memberships` | query | string | No |  | If provided, you'll get all users along with workspaces, groups, or projects they have access to. Default value is NONE. |
| `include-roles` | query | string | Yes | `false` | If you pass along includeRoles=true, you'll get each user's detailed manager role (including projects and members which they manage) |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/users" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/users', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/users'
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
- Artifact: `scripts/api-docs-runner/artifacts/getUsersOfWorkspace-200.json`
```json
[
  {
    "$ref": "#/components/schemas/UserDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)