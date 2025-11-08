## GET /v1/shared-reports/{id}
**Summary:** Generate shared report by ID
Response depends on report type and export type. Given example is for SUMMARY report and JSON exportType. 

Shared report data on FREE subscription plan is limited to a maximum interval length of one year (366 days).

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `id` | path | string | Yes |  | - |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `dateRangeStart` | query | string | No |  | - |
| `dateRangeEnd` | query | string | No |  | - |
| `sortOrder` | query | string | No |  | - |
| `sortColumn` | query | string | No |  | - |
| `exportType` | query | string | No |  | - |
| `page` | query | integer | No |  | - |
| `pageSize` | query | integer | No |  | - |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/shared-reports/{id}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/shared-reports/{id}', {
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

url = 'https://developer.clockify.me/v1/shared-reports/{id}'
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
- Media type: `*/*`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/generateSharedReportV1-200.json`
```json
{
  "chart": [
    {
      "$ref": "#/components/schemas/SummaryReportChartDto"
    }
  ],
  "groupOne": [
    {
      "$ref": "#/components/schemas/GroupOneDto"
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