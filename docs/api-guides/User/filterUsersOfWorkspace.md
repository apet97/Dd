## POST /v1/workspaces/{workspaceId}/users/info
**Summary:**  Filter workspace users

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `accountStatuses` (array, optional) If provided, you'll get a filtered list of users with the corresponding account status filter. If not, this will only filter ACTIVE, PENDING_EMAIL_VERIFICATION, and NOT_REGISTERED Users.
- `email` (string, optional) If provided, you'll get a filtered list of users that contain the provided string in their email address.
- `includeRoles` (boolean, optional) If you pass along includeRoles=true, you'll get each user's detailed manager role (including projects and members for whom they're managers)
- `memberships` (string, optional) If provided, you'll get all users along with workspaces, groups, or projects they have access to.
- `name` (string, optional) If provided, you'll get a filtered list of users that contain the provided string in their name.
- `page` (integer, optional) Page number.
- `pageSize` (integer, optional) Page size.
- `projectId` (string, optional) If provided, you'll get a list of users that have access to the project.
- `roles` (array, optional) If provided, you'll get a filtered list of users that have any of the specified roles. Owners are counted as admins when filtering.
- `sortColumn` (string, optional) Sorting criteria
- `sortOrder` (string, optional) Sorting mode
- `status` (string, optional) If provided, you'll get a filtered list of users with the corresponding status.
- `userGroups` (array, optional) If provided, you'll get a list of users that belong to the specified user group IDs.
- **Minimal example:**
```json
{
  "accountStatuses": [
    "LIMITED",
    "ACTIVE"
  ],
  "email": "mail@example.com",
  "includeRoles": false,
  "memberships": "NONE",
  "name": "John",
  "page": 1,
  "pageSize": 50,
  "projectId": "21a687e29ae1f428e7ebe606",
  "roles": [
    "WORKSPACE_ADMIN",
    "OWNER"
  ],
  "sortColumn": "ID",
  "sortOrder": "ASCENDING",
  "status": "ACTIVE",
  "userGroups": [
    "5a0ab5acb07987125438b60f",
    "72wab5acb07987125438b564"
  ]
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/users/info" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"accountStatuses":["LIMITED","ACTIVE"],"email":"mail@example.com","includeRoles":false,"memberships":"NONE","name":"John","page":1,"pageSize":50,"projectId":"21a687e29ae1f428e7ebe606","roles":["WORKSPACE_ADMIN","OWNER"],"sortColumn":"ID","sortOrder":"ASCENDING","status":"ACTIVE","userGroups":["5a0ab5acb07987125438b60f","72wab5acb07987125438b564"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/users/info', {
  method: 'POST',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/users/info'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/filterUsersOfWorkspace-200.json`
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