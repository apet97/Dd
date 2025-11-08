## POST /v1/workspaces/{workspaceId}/time-off/requests
**Summary:** Get all time off requests on workspace

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
- `end` (string, optional) Return time off requests created before the specified time in requester's time zone. Provide end in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `page` (integer, optional) Page number.
- `pageSize` (integer, optional) Page size.
- `start` (string, optional) Return time off requests created after the specified time in requester's time zone. Provide start in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `statuses` (array, optional) Filters time off requests by status.
- `userGroups` (array, optional) Provide the user group ids of time off requests.
- `users` (array, optional) Provide the user ids of time off requests. If empty, will return time off requests of all users (with a maximum of 5000 users).
- **Minimal example:**
```json
{
  "end": "2022-08-26T23:55:06.281873Z",
  "page": 1,
  "pageSize": 50,
  "start": "2022-08-26T08:00:06.281873Z",
  "statuses": [
    "APPROVED",
    "PENDING"
  ],
  "userGroups": [
    "5b715612b079875110791342",
    "5b715612b079875110791324",
    "5b715612b079875110793142"
  ],
  "users": [
    "5b715612b079875110791432",
    "b715612b079875110791234"
  ]
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/requests" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"end":"2022-08-26T23:55:06.281873Z","page":1,"pageSize":50,"start":"2022-08-26T08:00:06.281873Z","statuses":["APPROVED","PENDING"],"userGroups":["5b715612b079875110791342","5b715612b079875110791324","5b715612b079875110793142"],"users":["5b715612b079875110791432","b715612b079875110791234"]}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/requests', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/time-off/requests'
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
- Artifact: `scripts/api-docs-runner/artifacts/getTimeOffRequest-200.json`
```json
{
  "count": 1,
  "requests": [
    {
      "$ref": "#/components/schemas/TimeOffRequestFullV1Dto"
    }
  ]
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)