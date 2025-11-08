## PUT /v1/workspaces/{workspaceId}/scheduling/assignments/publish
**Summary:** Publish assignments

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
- `end` (string, required) Represents end date in yyyy-MM-ddThh:mm:ssZ format.
- `notifyUsers` (boolean, optional) Indicates whether to notify users when assignment is published.
- `search` (string, optional) Represents a search string.
- `start` (string, required) Represents start date in yyyy-MM-ddThh:mm:ssZ format.
- `userFilter` (ref: #/components/schemas/ContainsUsersFilterRequestV1, optional) 
- `userGroupFilter` (ref: #/components/schemas/ContainsUserGroupFilterRequestV1, optional) 
- `viewType` (string, optional) Represents view type.
- **Minimal example:**
```json
{
  "end": "2021-01-01T00:00:00Z",
  "notifyUsers": false,
  "search": "search keyword",
  "start": "2020-01-01T00:00:00Z",
  "userFilter": {
    "$ref": "#/components/schemas/ContainsUsersFilterRequestV1"
  },
  "userGroupFilter": {
    "$ref": "#/components/schemas/ContainsUserGroupFilterRequestV1"
  },
  "viewType": "PROJECTS"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/publish" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"end":"2021-01-01T00:00:00Z","notifyUsers":false,"search":"search keyword","start":"2020-01-01T00:00:00Z","userFilter":{"$ref":"#/components/schemas/ContainsUsersFilterRequestV1"},"userGroupFilter":{"$ref":"#/components/schemas/ContainsUserGroupFilterRequestV1"},"viewType":"PROJECTS"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/publish', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/publish'
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
- Media type: `-`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/publishAssignments-200.json`
(No example available in spec; not executed in sandbox.)

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)