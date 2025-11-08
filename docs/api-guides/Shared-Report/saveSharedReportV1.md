## POST /v1/workspaces/{workspaceId}/shared-reports
**Summary:** Create shared report
Saves shared report with name, options and report filter. 

Shared report data on FREE subscription plan is limited to a maximum interval length of one year (366 days).

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | - |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `filter` (ref: #/components/schemas/ReportFilterV1, optional) 
- `fixedDate` (boolean, optional) Indicates whether the shared report has a fixed date range.
- `isPublic` (boolean, optional) Indicates whether the shared report is public or not
- `name` (string, optional) Represents shared report's name
- `type` (string, optional) Represent the type of shared report.
- `visibleToUserGroups` (array, optional) Represents user group ids.
- `visibleToUsers` (array, optional) Represents user ids.
- **Minimal example:**
```json
{
  "filter": {
    "$ref": "#/components/schemas/ReportFilterV1"
  },
  "fixedDate": false,
  "isPublic": false,
  "name": "Weekly 1",
  "type": "WEEKLY",
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
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"filter":{"$ref":"#/components/schemas/ReportFilterV1"},"fixedDate":false,"isPublic":false,"name":"Weekly 1","type":"WEEKLY","visibleToUserGroups":"\"[5b715448b079875110792222\", \"5b715448b079875110791111\"]","visibleToUsers":["5b715448b079875110791234","5b715448b079875110791432","5b715448b079875110791324"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/shared-reports'
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
- Artifact: `scripts/api-docs-runner/artifacts/saveSharedReportV1-200.json`
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