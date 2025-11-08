## POST /v1/workspaces/{workspaceId}/custom-fields
**Summary:** Create custom fields on workspace

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
- `allowedValues` (array, optional) Represents a list of custom field's allowed values.
- `description` (string, optional) Represents custom field description.
- `entityType` (string, optional) Represents custom field entity type
- `name` (string, required) Represents custom field name.
- `onlyAdminCanEdit` (boolean, optional) Flag to set whether custom field is modifiable only by admin users.
- `placeholder` (string, optional) Represents custom field placeholder value.
- `status` (string, optional) Represents custom field status
- `type` (string, required) Represents custom field type.
- `workspaceDefaultValue` (object, optional) Represents a custom field's default value in the workspace.<li>if type = NUMBER, then value must be a number</li><li>if type = DROPDOWN_MULTIPLE, value must be a list</li><li>if type = CHECKBOX, value must be true/false</li><li>otherwise any string</li>
- **Minimal example:**
```json
{
  "allowedValues": [
    "New York",
    "London",
    "Manila",
    "Sydney",
    "Belgrade"
  ],
  "description": "This field contains a location.",
  "entityType": "TIMEENTRY",
  "name": "location",
  "onlyAdminCanEdit": false,
  "placeholder": "Location",
  "status": "VISIBLE",
  "type": "DROPDOWN_MULTIPLE",
  "workspaceDefaultValue": "Manila"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/custom-fields" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"allowedValues":["New York","London","Manila","Sydney","Belgrade"],"description":"This field contains a location.","entityType":"TIMEENTRY","name":"location","onlyAdminCanEdit":false,"placeholder":"Location","status":"VISIBLE","type":"DROPDOWN_MULTIPLE","workspaceDefaultValue":"Manila"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/custom-fields', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/custom-fields'
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
#### Status 201
- Media type: `*/*`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/create-201.json`
```json
{
  "allowedValues": [
    "New York",
    "London",
    "Manila",
    "Sydney",
    "Belgrade"
  ],
  "description": "This field contains a location.",
  "entityType": "USER",
  "id": "44a687e29ae1f428e7ebe305",
  "name": "location",
  "onlyAdminCanEdit": false,
  "placeholder": "Location",
  "projectDefaultValues": [
    {
      "$ref": "#/components/schemas/CustomFieldDefaultValuesDtoV1"
    }
  ],
  "required": false,
  "status": "VISIBLE",
  "type": "DROPDOWN_MULTIPLE",
  "workspaceDefaultValue": "Manila",
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)