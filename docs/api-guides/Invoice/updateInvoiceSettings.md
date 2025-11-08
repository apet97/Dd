## PUT /v1/workspaces/{workspaceId}/invoices/settings
**Summary:** Change invoice language

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `defaults` (ref: #/components/schemas/InvoiceDefaultSettingsRequestV1, optional) 
- `exportFields` (ref: #/components/schemas/InvoiceExportFieldsRequest, optional) 
- `labels` (ref: #/components/schemas/LabelsCustomizationRequest, required) 
- **Minimal example:**
```json
{
  "defaults": {
    "$ref": "#/components/schemas/InvoiceDefaultSettingsRequestV1"
  },
  "exportFields": {
    "$ref": "#/components/schemas/InvoiceExportFieldsRequest"
  },
  "labels": {
    "$ref": "#/components/schemas/LabelsCustomizationRequest"
  }
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"defaults":{"$ref":"#/components/schemas/InvoiceDefaultSettingsRequestV1"},"exportFields":{"$ref":"#/components/schemas/InvoiceExportFieldsRequest"},"labels":{"$ref":"#/components/schemas/LabelsCustomizationRequest"}}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/settings'
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
- Media type: `-`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateInvoiceSettings-200.json`
(No example available in spec; not executed in sandbox.)

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)