## POST /v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals
**Summary:** Get all scheduled assignments per project

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
- `page` (integer, optional) Page number.
- `pageSize` (integer, optional) Page size.
- `search` (string, optional) Represents term for searching projects and clients by name.
- `start` (string, required) Represents start date in yyyy-MM-ddThh:mm:ssZ format.
- `statusFilter` (string, optional) Filters assignments by status.
- **Minimal example:**
```json
{
  "end": "2021-01-01T00:00:00Z",
  "page": 1,
  "pageSize": 50,
  "search": "Project name",
  "start": "2020-01-01T00:00:00Z",
  "statusFilter": "PUBLISHED"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"end":"2021-01-01T00:00:00Z","page":1,"pageSize":50,"search":"Project name","start":"2020-01-01T00:00:00Z","statusFilter":"PUBLISHED"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/projects/totals'
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
- Artifact: `scripts/api-docs-runner/artifacts/getFilteredProjectTotals-200.json`
```json
[
  {
    "$ref": "#/components/schemas/SchedulingProjectsTotalsDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)