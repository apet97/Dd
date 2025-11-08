## POST /v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests
**Summary:** Create time off request

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `policyId` | path | string | Yes |  | Represents policy identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `note` (string, optional) Provide the note you would like to use for creating the time off request.
- `timeOffPeriod` (ref: #/components/schemas/TimeOffRequestPeriodV1Request, required) 
- **Minimal example:**
```json
{
  "note": "Create Time Off Note",
  "timeOffPeriod": {
    "$ref": "#/components/schemas/TimeOffRequestPeriodV1Request"
  }
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"note":"Create Time Off Note","timeOffPeriod":{"$ref":"#/components/schemas/TimeOffRequestPeriodV1Request"}}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/policies/{policyId}/requests'
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
- Artifact: `scripts/api-docs-runner/artifacts/createTimeOffRequest-200.json`
```json
{
  "balance": 10,
  "balanceDiff": 1,
  "createdAt": "2022-08-26T08:32:01.640708Z",
  "id": "5b715612b079875110791111",
  "note": "Time Off Request Note",
  "policyId": "5b715612b079875110792333",
  "policyName": "Days",
  "requesterUserId": "5b715612b0798751107925555",
  "requesterUserName": "John",
  "status": {
    "$ref": "#/components/schemas/TimeOffRequestStatus"
  },
  "timeOffPeriod": {
    "$ref": "#/components/schemas/TimeOffRequestPeriodDto"
  },
  "timeUnit": "DAYS",
  "userEmail": "nicholas@clockify.com",
  "userId": "5b715612b079875110794444",
  "userName": "Nicholas",
  "userTimeZone": "Europe/Budapest",
  "workspaceId": "5b715612b079875110792222"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)