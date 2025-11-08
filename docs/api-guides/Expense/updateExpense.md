## PUT /v1/workspaces/{workspaceId}/expenses/{expenseId}
**Summary:** Update expense

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
- **Media type:** `multipart/form-data`
- **Required:** No
- **Schema summary:**
- `amount` (number, required) Represents expense amount as double data type.
- `billable` (boolean, optional) Indicates whether expense is billable or not.
- `categoryId` (string, required) Represents category identifier across the system.
- `changeFields` (array, required) Represents a list of expense change fields.
- `date` (string, required) Provides a valid yyyy-MM-ddThh:mm:ssZ format date.
- `file` (string, required) 
- `notes` (string, optional) Represents notes for an expense.
- `projectId` (string, optional) Represents project identifier across the system.
- `taskId` (string, optional) Represents task identifier across the system.
- `userId` (string, required) Represents user identifier across the system.
- **Minimal example:**
```json
{
  "amount": 99.5,
  "billable": false,
  "categoryId": "45y687e29ae1f428e7ebe890",
  "changeFields": [
    "USER",
    "DATE",
    "PROJECT"
  ],
  "date": "2020-01-01T00:00:00Z",
  "file": "string",
  "notes": "This is a sample note for this expense.",
  "projectId": "25b687e29ae1f428e7ebe123",
  "taskId": "25b687e29ae1f428e7ebe123",
  "userId": "89b687e29ae1f428e7ebe912"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"amount":99.5,"billable":false,"categoryId":"45y687e29ae1f428e7ebe890","changeFields":["USER","DATE","PROJECT"],"date":"2020-01-01T00:00:00Z","file":"string","notes":"This is a sample note for this expense.","projectId":"25b687e29ae1f428e7ebe123","taskId":"25b687e29ae1f428e7ebe123","userId":"89b687e29ae1f428e7ebe912"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/expenses/{expenseId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/updateExpense-200.json`
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