## GET /v1/workspaces/{workspaceId}/invoices/settings
**Summary:** Get invoice in another language

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings'
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
- Artifact: `scripts/api-docs-runner/artifacts/getInvoiceSettings-200.json`
```json
{
  "defaults": {
    "$ref": "#/components/schemas/InvoiceDefaultSettingsDto"
  },
  "exportFields": {
    "$ref": "#/components/schemas/InvoiceExportFields"
  },
  "labels": {
    "$ref": "#/components/schemas/LabelsCustomization"
  }
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)