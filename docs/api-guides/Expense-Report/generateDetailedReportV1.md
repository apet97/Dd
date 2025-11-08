## POST /v1/workspaces/{workspaceId}/reports/expenses/detailed
**Summary:** Generate expense report
Expense report data on FREE subscription plan is limited to a maximum interval length of one year (366 days).

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
- **Required:** No
- **Schema summary:**
- `approvalState` (string, optional) Represents approval state
- `billable` (boolean, optional) Indicates whether report is billable
- `categories` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `clients` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `currency` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `dateRangeEnd` (string, required) Provide date in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `dateRangeStart` (string, required) Provide date in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `dateRangeType` (string, optional) Represents date range type of expense report
- `exportType` (string, optional) Represents export type
- `invoicingState` (string, optional) Represents invoicing state
- `note` (string, optional) Represents search term for filtering report entries by note
- `page` (integer, optional) Page number.
- `pageSize` (integer, optional) Page size.
- `projects` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `sortColumn` (string, optional) Represents expenses sort column
- `sortOrder` (string, optional) Represents sort order
- `tasks` (ref: #/components/schemas/ContainsTaskFilterV1, optional) 
- `timeZone` (string, optional) Represents time zone
- `userGroups` (ref: #/components/schemas/ContainsUsersFilterV1, optional) 
- `userLocale` (string, optional) Represents user locale
- `users` (ref: #/components/schemas/ContainsUsersFilterV1, optional) 
- `weekStart` (string, optional) Represents week start
- `withoutNote` (boolean, optional) If set to 'true', report will only include entries with empty note
- `zoomLevel` (string, optional) Represents zoom level
- **Minimal example:**
```json
{
  "approvalState": "APPROVED",
  "billable": true,
  "categories": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "clients": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "currency": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "dateRangeEnd": "2021-10-27T23:59:59.999Z",
  "dateRangeStart": "2021-10-27T00:00:00Z",
  "dateRangeType": "TODAY",
  "exportType": "JSON",
  "invoicingState": "INVOICED",
  "note": "some note keyword",
  "page": 1,
  "pageSize": 50,
  "projects": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "sortColumn": "ID",
  "sortOrder": "ASCENDING",
  "tasks": {
    "$ref": "#/components/schemas/ContainsTaskFilterV1"
  },
  "timeZone": "Europe/Budapest",
  "userGroups": {
    "$ref": "#/components/schemas/ContainsUsersFilterV1"
  },
  "userLocale": "en",
  "users": {
    "$ref": "#/components/schemas/ContainsUsersFilterV1"
  },
  "weekStart": "MONDAY",
  "withoutNote": false,
  "zoomLevel": "WEEK"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/expenses/detailed" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"approvalState":"APPROVED","billable":true,"categories":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"clients":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"currency":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"dateRangeEnd":"2021-10-27T23:59:59.999Z","dateRangeStart":"2021-10-27T00:00:00Z","dateRangeType":"TODAY","exportType":"JSON","invoicingState":"INVOICED","note":"some note keyword","page":1,"pageSize":50,"projects":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"sortColumn":"ID","sortOrder":"ASCENDING","tasks":{"$ref":"#/components/schemas/ContainsTaskFilterV1"},"timeZone":"Europe/Budapest","userGroups":{"$ref":"#/components/schemas/ContainsUsersFilterV1"},"userLocale":"en","users":{"$ref":"#/components/schemas/ContainsUsersFilterV1"},"weekStart":"MONDAY","withoutNote":false,"zoomLevel":"WEEK"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/expenses/detailed', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/expenses/detailed'
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
- Artifact: `scripts/api-docs-runner/artifacts/generateDetailedReportV1-200.json`
```json
{
  "expenses": [
    {
      "$ref": "#/components/schemas/ExpenseReportDtoV1"
    }
  ],
  "totals": {
    "$ref": "#/components/schemas/ExpenseTotalsDtoV1"
  }
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)