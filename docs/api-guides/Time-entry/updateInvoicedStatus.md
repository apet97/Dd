## PATCH /v1/workspaces/{workspaceId}/time-entries/invoiced
**Summary:** Mark time entries as invoiced

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
- `invoiced` (boolean, required) Indicates whether time entry is invoiced or not.
- `timeEntryIds` (array, required) Represents a list of invoiced time entry ids
- **Minimal example:**
```json
{
  "invoiced": false,
  "timeEntryIds": [
    "54m377ddd3fcab07cfbb432w",
    "25b687e29ae1f428e7ebe123"
  ]
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/invoiced" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"invoiced":false,"timeEntryIds":["54m377ddd3fcab07cfbb432w","25b687e29ae1f428e7ebe123"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/invoiced', {
  method: 'PATCH',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-entries/invoiced'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.patch(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `-`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateInvoicedStatus-200.json`
(No example available in spec; not executed in sandbox.)

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)