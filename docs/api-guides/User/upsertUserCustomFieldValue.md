## PUT /v1/workspaces/{workspaceId}/users/{userId}/custom-field/{customFieldId}/value
**Summary:** Update user's custom field

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `userId` | path | string | Yes |  | Represents user identifier across the system. |
| `customFieldId` | path | string | Yes |  | Represents custom field identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `value` (object, optional) Represents custom field value.
- **Minimal example:**
```json
{
  "value": "20231211-12345"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/custom-field/{customFieldId}/value" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"value":"20231211-12345"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/custom-field/{customFieldId}/value', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/custom-field/{customFieldId}/value'
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
#### Status 201
- Media type: `application/json`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/upsertUserCustomFieldValue-201.json`
```json
{
  "customFieldId": "5e4117fe8c625f38930d57b7",
  "customFieldName": "TIN",
  "customFieldType": {
    "$ref": "#/components/schemas/CustomFieldType"
  },
  "userId": "5a0ab5acb07987125438b60f",
  "value": "20231211-12345"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)