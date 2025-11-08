## PATCH /v1/workspaces/{workspaceId}/approval-requests/{approvalRequestId}
**Summary:** Update approval request

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `approvalRequestId` | path | string | Yes |  | Represents approval request identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `note` (string, optional) Additional notes for the approval request.
- `state` (string, required) Specifies the approval state to set.
- **Minimal example:**
```json
{
  "note": "This is a sample note.",
  "state": "PENDING"
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/approval-requests/{approvalRequestId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"note":"This is a sample note.","state":"PENDING"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/approval-requests/{approvalRequestId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/approval-requests/{approvalRequestId}'
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
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateApprovalStatus-200.json`
```json
{
  "creator": {
    "$ref": "#/components/schemas/ApprovalRequestCreatorDtoV1"
  },
  "dateRange": {
    "$ref": "#/components/schemas/DateRangeDto"
  },
  "id": "567687e29ae1f428e7ebf564",
  "owner": {
    "$ref": "#/components/schemas/ApprovalRequestOwnerDtoV1"
  },
  "status": {
    "$ref": "#/components/schemas/ApprovalRequestStatusDtoV1"
  },
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)