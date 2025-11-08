## GET /v1/workspaces/{workspaceId}/expenses/{expenseId}
**Summary:** Get expense by ID

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `expenseId` | path | string | Yes |  | Represents expense identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/getExpense-200.json`
```json
{
  "billable": false,
  "categoryId": "45y687e29ae1f428e7ebe890",
  "date": "2020-01-01",
  "fileId": "745687e29ae1f428e7ebe890",
  "id": "64c777ddd3fcab07cfbb210c",
  "isLocked": false,
  "locked": false,
  "notes": "This is a sample note for this expense.",
  "projectId": "25b687e29ae1f428e7ebe123",
  "quantity": 0,
  "taskId": "25b687e29ae1f428e7ebe123",
  "total": 10500.5,
  "userId": "89b687e29ae1f428e7ebe912",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)