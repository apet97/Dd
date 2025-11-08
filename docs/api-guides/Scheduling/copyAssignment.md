## POST /v1/workspaces/{workspaceId}/scheduling/assignments/{assignmentId}/copy
**Summary:** Copy scheduled assignment

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `assignmentId` | path | string | Yes |  | Represents assignment identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `seriesUpdateOption` (string, optional) Represents series update option.
- `userId` (string, required) Represents user identifier across the system.
- **Minimal example:**
```json
{
  "seriesUpdateOption": "THIS_ONE",
  "userId": "72k687e29ae1f428e7ebe109"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/{assignmentId}/copy" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"seriesUpdateOption":"THIS_ONE","userId":"72k687e29ae1f428e7ebe109"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/{assignmentId}/copy', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/{assignmentId}/copy'
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
- Artifact: `scripts/api-docs-runner/artifacts/copyAssignment-200.json`
```json
[
  {
    "$ref": "#/components/schemas/AssignmentDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)