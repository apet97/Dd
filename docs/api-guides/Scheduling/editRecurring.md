## PATCH /v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}
**Summary:** Update recurring assignment

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
- `billable` (boolean, optional) Indicates whether assignment is billable or not.
- `end` (string, required) Represents end date in yyyy-MM-ddThh:mm:ssZ format.
- `hoursPerDay` (number, optional) Represents assignment total hours per day.
- `includeNonWorkingDays` (boolean, optional) Indicates whether to include non-working days or not.
- `note` (string, optional) Represents assignment note.
- `seriesUpdateOption` (string, optional) Valid series option
- `start` (string, required) Represents start date in yyyy-MM-ddThh:mm:ssZ format.
- `startTime` (string, optional) Represents start time in hh:mm:ss format.
- `taskId` (string, optional) Represents task identifier across the system.
- **Minimal example:**
```json
{
  "billable": false,
  "end": "2021-01-01T00:00:00Z",
  "hoursPerDay": 7.5,
  "includeNonWorkingDays": false,
  "note": "This is a sample note for an assignment.",
  "seriesUpdateOption": "THIS_ONE",
  "start": "2020-01-01T00:00:00Z",
  "startTime": "10:00:00",
  "taskId": "56b687e29ae1f428e7ebe505"
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"billable":false,"end":"2021-01-01T00:00:00Z","hoursPerDay":7.5,"includeNonWorkingDays":false,"note":"This is a sample note for an assignment.","seriesUpdateOption":"THIS_ONE","start":"2020-01-01T00:00:00Z","startTime":"10:00:00","taskId":"56b687e29ae1f428e7ebe505"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/scheduling/assignments/recurring/{assignmentId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/editRecurring-200.json`
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