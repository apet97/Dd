## PUT /v1/workspaces/{workspaceId}/shared-reports/{id}
**Summary:** Update shared report
Updates shared report name and/or options

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | - |
| `id` | path | string | Yes |  | - |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `fixedDate` (boolean, optional) Indicates whether the shared report has a fixed date range.
- `isPublic` (boolean, optional) Indicates whether the shared report is public.
- `name` (string, required) Represents shared reports name.
- `visibleToUserGroups` (array, optional) Provide user groups ids to which the shared report is visible.
- `visibleToUsers` (array, optional) Provide user ids to which the shared report is visible.
- **Minimal example:**
```json
{
  "fixedDate": false,
  "isPublic": false,
  "name": "Weekly Updated Report",
  "visibleToUserGroups": "\"[5b715448b079875110792222\", \"5b715448b079875110791111\"]",
  "visibleToUsers": [
    "5b715448b079875110791234",
    "5b715448b079875110791432",
    "5b715448b079875110791324"
  ]
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"fixedDate":false,"isPublic":false,"name":"Weekly Updated Report","visibleToUserGroups":"\"[5b715448b079875110792222\", \"5b715448b079875110791111\"]","visibleToUsers":["5b715448b079875110791234","5b715448b079875110791432","5b715448b079875110791324"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports/{id}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports/{id}'
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
- Media type: `*/*`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateSharedReportV1-200.json`
```json
{
  "filter": {
    "$ref": "#/components/schemas/ReportFilterV1"
  },
  "fixedDate": false,
  "id": "5b715612b079875110791111",
  "isPublic": false,
  "name": "Weekly 1",
  "type": "WEEKLY",
  "userId": "5b715612b079875110791113",
  "visibleToUserGroups": [
    "5b715612b079875110791342",
    "5b715612b079875110791324",
    "5b715612b079875110793142"
  ],
  "visibleToUsers": [
    "5b715612b079875110791432",
    "5b715612b079875110791234"
  ],
  "workspaceId": "5b715612b079875110791112"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)