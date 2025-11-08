## POST /v1/workspaces/{workspaceId}/projects/{projectId}/memberships
**Summary:** Assign/remove users to/from the project

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `projectId` | path | string | Yes |  | Represents project identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `remove` (boolean, optional) Setting this flag to 'true' will remove the given users from the project.
- `userGroups` (ref: #/components/schemas/UserGroupIdsSchema, optional) 
- `userIds` (array, optional) Represents array of user ids which should be added/removed.
- **Minimal example:**
```json
{
  "remove": false,
  "userGroups": {
    "$ref": "#/components/schemas/UserGroupIdsSchema"
  },
  "userIds": [
    "45b687e29ae1f428e7ebe123",
    "67s687e29ae1f428e7ebe678"
  ]
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/memberships" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"remove":false,"userGroups":{"$ref":"#/components/schemas/UserGroupIdsSchema"},"userIds":["45b687e29ae1f428e7ebe123","67s687e29ae1f428e7ebe678"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/memberships', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}/memberships'
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
- Media type: `*/*`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/addUsersToProject-200.json`
```json
{
  "archived": false,
  "billable": false,
  "budgetEstimate": {
    "$ref": "#/components/schemas/EstimateWithOptionsDto"
  },
  "clientId": "9t641568b07987035750704",
  "clientName": "Client X",
  "color": "#000000",
  "costRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "duration": "60000",
  "estimate": {
    "$ref": "#/components/schemas/EstimateDtoV1"
  },
  "estimateReset": {
    "$ref": "#/components/schemas/EstimateResetDto"
  },
  "hourlyRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "id": "5b641568b07987035750505e",
  "isPublic": false,
  "isTemplate": false,
  "memberships": [
    {
      "$ref": "#/components/schemas/MembershipDtoV1"
    }
  ],
  "name": "Software Development",
  "note": "This is a sample note for the project.",
  "public": false,
  "template": false,
  "timeEstimate": {
    "$ref": "#/components/schemas/TimeEstimateDto"
  },
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)