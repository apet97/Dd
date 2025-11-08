## POST /v1/workspaces/{workspaceId}/holidays
**Summary:** Create holiday

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
- `automaticTimeEntryCreation` (ref: #/components/schemas/AutomaticTimeEntryCreationRequest, optional) 
- `color` (string, optional) Provide color in format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
- `datePeriod` (ref: #/components/schemas/DatePeriodRequest, required) 
- `everyoneIncludingNew` (boolean, optional) Indicates whether the holiday is shown to new users.
- `name` (string, required) Provide the name of the holiday.
- `occursAnnually` (boolean, optional) Indicates whether the holiday occurs annually.
- `userGroups` (ref: #/components/schemas/UserGroupIdsSchema, optional) 
- `users` (ref: #/components/schemas/UserIdsSchema, optional) 
- **Minimal example:**
```json
{
  "automaticTimeEntryCreation": {
    "$ref": "#/components/schemas/AutomaticTimeEntryCreationRequest"
  },
  "color": "#8BC34A",
  "datePeriod": {
    "$ref": "#/components/schemas/DatePeriodRequest"
  },
  "everyoneIncludingNew": true,
  "name": "Labour Day",
  "occursAnnually": true,
  "userGroups": {
    "$ref": "#/components/schemas/UserGroupIdsSchema"
  },
  "users": {
    "$ref": "#/components/schemas/UserIdsSchema"
  }
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/holidays" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"automaticTimeEntryCreation":{"$ref":"#/components/schemas/AutomaticTimeEntryCreationRequest"},"color":"#8BC34A","datePeriod":{"$ref":"#/components/schemas/DatePeriodRequest"},"everyoneIncludingNew":true,"name":"Labour Day","occursAnnually":true,"userGroups":{"$ref":"#/components/schemas/UserGroupIdsSchema"},"users":{"$ref":"#/components/schemas/UserIdsSchema"}}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/holidays', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/holidays'
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
- Artifact: `scripts/api-docs-runner/artifacts/createHoliday-200.json`
```json
{
  "automaticTimeEntryCreation": false,
  "datePeriod": {
    "$ref": "#/components/schemas/DatePeriod"
  },
  "everyoneIncludingNew": false,
  "id": "5b715612b079875110791111",
  "name": "New Year's Day",
  "occursAnnually": true,
  "projectId": "65b36d3c525e243c48f9150f",
  "taskId": "65b36d46fa3df8607e42d21a",
  "userGroupIds": [
    "5b715612b079875110791342",
    "5b715612b079875110791324",
    "5b715612b079875110793142"
  ],
  "userIds": [
    "5b715612b079875110791432",
    "5b715612b079875110791234"
  ],
  "workspaceId": "5b715612b079875110792222"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)