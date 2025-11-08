## PUT /v1/workspaces/{workspaceId}/projects/{projectId}
**Summary:** Update project on workspace

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
- `archived` (boolean, optional) Indicates whether project is archived or not.
- `billable` (boolean, optional) Indicates whether project is billable or not.
- `clientId` (string, optional) Represents client identifier across the system.
- `color` (string, optional) Color format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
- `costRate` (ref: #/components/schemas/CostRateRequestV1, optional) 
- `hourlyRate` (ref: #/components/schemas/HourlyRateRequestV1, optional) 
- `isPublic` (boolean, optional) Indicates whether project is public or not.
- `name` (string, optional) Represents a project name.
- `note` (string, optional) Represents project note.
- **Minimal example:**
```json
{
  "archived": false,
  "billable": false,
  "clientId": "9t641568b07987035750704",
  "color": "#000000",
  "costRate": {
    "$ref": "#/components/schemas/CostRateRequestV1"
  },
  "hourlyRate": {
    "$ref": "#/components/schemas/HourlyRateRequestV1"
  },
  "isPublic": false,
  "name": "Software Development",
  "note": "This is a sample note for the project."
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"archived":false,"billable":false,"clientId":"9t641568b07987035750704","color":"#000000","costRate":{"$ref":"#/components/schemas/CostRateRequestV1"},"hourlyRate":{"$ref":"#/components/schemas/HourlyRateRequestV1"},"isPublic":false,"name":"Software Development","note":"This is a sample note for the project."}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects/{projectId}'
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
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateProject-200.json`
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