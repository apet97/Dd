## GET /v1/workspaces/{workspaceId}/user/{userId}/time-entries
**Summary:** Get time entries for a user on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `userId` | path | string | Yes |  | Represents user identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `description` | query | string | No |  | Represents term for searching time entries by description. |
| `start` | query | string | No |  | Represents start date in yyyy-MM-ddThh:mm:ssZ format. |
| `end` | query | string | No |  | Represents end date in yyyy-MM-ddThh:mm:ssZ format. |
| `project` | query | string | No |  | If provided, you'll get a filtered list of time entries that matches the provided string in their project id. |
| `task` | query | string | No |  | If provided, you'll get a filtered list of time entries that matches the provided string in their task id. |
| `tags` | query | array | No |  | If provided, you'll get a filtered list of time entries that matches the provided string(s) in their tag id(s). |
| `project-required` | query | boolean | No |  | Flag to set whether to only get time entries which have a project. |
| `task-required` | query | boolean | No |  | Flag to set whether to only get time entries which have tasks. |
| `hydrated` | query | boolean | No | `False` | Flag to set whether to include additional information on time entries or not. |
| `page` | query | integer | No | `1` | Page number. |
| `page-size` | query | integer | No | `50` | Page size. |
| `in-progress` | query | boolean | No |  | Flag to set whether to filter only in progress time entries. |
| `get-week-before` | query | string | No |  | Valid yyyy-MM-ddThh:mm:ssZ format date. If provided, filters results within the week before the datetime provided and only those entries with assigned project or task. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries', {
  method: 'GET',
  headers: {
    'X-Api-Key': process.env.CLOCKIFY_API_KEY,
    'Accept': 'application/json',
  },
});
const data = await response.json();
console.log(data);
```

```python
import os
import requests

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/user/{userId}/time-entries'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/getTimeEntries-200.json`
```json
[
  {
    "$ref": "#/components/schemas/TimeEntryWithRatesDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)