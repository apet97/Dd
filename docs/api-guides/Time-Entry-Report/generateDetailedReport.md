## POST /v1/workspaces/{workspaceId}/reports/detailed
**Summary:** Detailed report
Detailed report data on FREE subscription plan is limited to a maximum interval length of one year (366 days).

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
- `amountShown` (string, optional) If provided, you'll get filtered result including reports with provided amount shown.
- `amounts` (array, optional) 
- `approvalState` (string, optional) If provided, you'll get filtered result including reports with provided approval state.
- `archived` (boolean, optional) Indicates whether the report is archived
- `attendanceFilter` (ref: #/components/schemas/AttendanceFilterV1, optional) 
- `billable` (boolean, optional) Indicates whether the report is billable
- `clients` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `currency` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `customFields` (array, optional) 
- `dateFormat` (string, optional) Provide date in format YYYY-MM-DD
- `dateRangeEnd` (string, required) Provide date in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `dateRangeStart` (string, required) Provide date in format YYYY-MM-DDTHH:MM:SS.ssssssZ
- `dateRangeType` (string, optional) Provide date range type
- `description` (string, optional) Represents search term for filtering report entries by description
- `detailedFilter` (ref: #/components/schemas/DetailedFilterV1, required) 
- `exportType` (string, optional) If provided, you'll get filtered result including reports with provided export type.
- `invoicingState` (string, optional) If provided, you'll get filtered result including reports with provided invoicing state.
- `projects` (ref: #/components/schemas/ContainsArchivedFilterV1, optional) 
- `rounding` (boolean, optional) Indicates whether the report filter is rounding
- `sortOrder` (string, optional) If provided, you'll get sorted result by provided sort order.
- `summaryFilter` (ref: #/components/schemas/SummaryFilterV1, optional) 
- `tags` (ref: #/components/schemas/ContainsTagFilterV1, optional) 
- `tasks` (ref: #/components/schemas/ContainsTaskFilterV1, optional) 
- `timeFormat` (string, optional) Provide time in format THH:MM:SS.ssssss
- `timeZone` (string, optional) If provided, you'll get filtered result including reports with provided time zone.
- `userGroups` (ref: #/components/schemas/ContainsUsersFilterV1, optional) 
- `userLocale` (string, optional) If provided, you'll get filtered result including reports with provided user locale.
- `users` (ref: #/components/schemas/ContainsUsersFilterV1, optional) 
- `weekStart` (string, optional) If provided, you'll get filtered result including reports with provided week start.
- `weeklyFilter` (ref: #/components/schemas/WeeklyFilterV1, optional) 
- `withoutDescription` (boolean, optional) If set to 'true', report will only include entries with empty description
- `zoomLevel` (string, optional) If provided, you'll get filtered result including reports with provided zoom level.
- **Minimal example:**
```json
{
  "amountShown": "COST",
  "amounts": [
    "[EARNED, COST]"
  ],
  "approvalState": "APPROVED",
  "archived": false,
  "attendanceFilter": {
    "$ref": "#/components/schemas/AttendanceFilterV1"
  },
  "billable": true,
  "clients": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "currency": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "customFields": [
    {
      "$ref": "#/components/schemas/CustomFieldFilterV1"
    }
  ],
  "dateFormat": "2018-11-01",
  "dateRangeEnd": "2018-11-30T23:59:59.999Z",
  "dateRangeStart": "2018-11-01T00:00:00Z",
  "dateRangeType": "LAST_MONTH",
  "description": "some description keyword",
  "detailedFilter": {
    "$ref": "#/components/schemas/DetailedFilterV1"
  },
  "exportType": "JSON",
  "invoicingState": "INVOICED",
  "projects": {
    "$ref": "#/components/schemas/ContainsArchivedFilterV1"
  },
  "rounding": false,
  "sortOrder": "ASCENDING",
  "summaryFilter": {
    "$ref": "#/components/schemas/SummaryFilterV1"
  },
  "tags": {
    "$ref": "#/components/schemas/ContainsTagFilterV1"
  },
  "tasks": {
    "$ref": "#/components/schemas/ContainsTaskFilterV1"
  },
  "timeFormat": "T00:00:00",
  "timeZone": "Europe/Belgrade",
  "userGroups": {
    "$ref": "#/components/schemas/ContainsUsersFilterV1"
  },
  "userLocale": "en",
  "users": {
    "$ref": "#/components/schemas/ContainsUsersFilterV1"
  },
  "weekStart": "MONDAY",
  "weeklyFilter": {
    "$ref": "#/components/schemas/WeeklyFilterV1"
  },
  "withoutDescription": false,
  "zoomLevel": "WEEK"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/detailed" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"amountShown":"COST","amounts":["[EARNED, COST]"],"approvalState":"APPROVED","archived":false,"attendanceFilter":{"$ref":"#/components/schemas/AttendanceFilterV1"},"billable":true,"clients":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"currency":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"customFields":[{"$ref":"#/components/schemas/CustomFieldFilterV1"}],"dateFormat":"2018-11-01","dateRangeEnd":"2018-11-30T23:59:59.999Z","dateRangeStart":"2018-11-01T00:00:00Z","dateRangeType":"LAST_MONTH","description":"some description keyword","detailedFilter":{"$ref":"#/components/schemas/DetailedFilterV1"},"exportType":"JSON","invoicingState":"INVOICED","projects":{"$ref":"#/components/schemas/ContainsArchivedFilterV1"},"rounding":false,"sortOrder":"ASCENDING","summaryFilter":{"$ref":"#/components/schemas/SummaryFilterV1"},"tags":{"$ref":"#/components/schemas/ContainsTagFilterV1"},"tasks":{"$ref":"#/components/schemas/ContainsTaskFilterV1"},"timeFormat":"T00:00:00","timeZone":"Europe/Belgrade","userGroups":{"$ref":"#/components/schemas/ContainsUsersFilterV1"},"userLocale":"en","users":{"$ref":"#/components/schemas/ContainsUsersFilterV1"},"weekStart":"MONDAY","weeklyFilter":{"$ref":"#/components/schemas/WeeklyFilterV1"},"withoutDescription":false,"zoomLevel":"WEEK"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/detailed', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/reports/detailed'
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
- Artifact: `scripts/api-docs-runner/artifacts/generateDetailedReport-200.json`
```json
{
  "timeEntries": [
    {
      "$ref": "#/components/schemas/TimeEntryDto"
    }
  ],
  "totals": [
    {
      "$ref": "#/components/schemas/TimeEntryReportTotals"
    }
  ]
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)