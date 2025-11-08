## GET /v1/workspaces/{workspaceId}/entities/created
**Summary:** Created entities (Experimental)
Retrieves records from the database collection that were created within a specified date range.  
The date range is determined by two parameters: start and end.  

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `type` | query | array | Yes |  | Specifies the type of document to be retrieved. Expected values are TIME_ENTRY, TIME_ENTRY_CUSTOM_FIELD_VALUE and TIME_ENTRY_RATE.This parameter can accept multiple values, and at least one option must be provided. Based on the input, the application will return results corresponding to the selected document types. |
| `start` | query | string | No |  | Represents the start date in yyyy-MM-ddThh:mm:ssZ format. This parameter is optional; if no start date is provided, the application will set a default start date that matches the end date to create a date range of 30 days. If the end date is not specified either, the default behavior will apply from the current date. |
| `end` | query | string | No |  | Represents the end date in yyyy-MM-ddThh:mm:ssZ format. This parameter is optional; if no end date is provided, the application will set a default end date that matches the start date to create a date range of 30 days. |
| `page` | query | string | No | `0` | - |
| `limit` | query | string | No | `50` | - |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/entities/created" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/entities/created', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/entities/created'
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
- Artifact: `scripts/api-docs-runner/artifacts/getCreatedEntityInfo-200.json`
```json
[
  "string"
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)