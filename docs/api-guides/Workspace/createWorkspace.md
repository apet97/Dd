## POST /v1/workspaces
**Summary:** Add workspace

### Path parameters
No parameters.

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `name` (string, optional) Represents a workspace name.
- `organizationId` (string, optional) Represents the Cake organization identifier across the system.
- **Minimal example:**
```json
{
  "name": "Cool Company",
  "organizationId": "67d471fb56aa9668b7bfa295"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"name":"Cool Company","organizationId":"67d471fb56aa9668b7bfa295"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces', {
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

url = 'https://developer.clockify.me/v1/workspaces'
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
- Media type: `application/json`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/createWorkspace-201.json`
```json
{
  "cakeOrganizationId": "67d471fb56aa9668b7bfa295",
  "costRate": {
    "$ref": "#/components/schemas/RateDtoV1"
  },
  "currencies": [
    {
      "$ref": "#/components/schemas/CurrencyWithDefaultInfoDtoV1"
    }
  ],
  "featureSubscriptionType": {
    "$ref": "#/components/schemas/FeatureSubscriptionType"
  },
  "features": {
    "$ref": "#/components/schemas/Feature"
  },
  "hourlyRate": {
    "$ref": "#/components/schemas/HourlyRateDtoV1"
  },
  "id": "64a687e29ae1f428e7ebe303",
  "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
  "memberships": [
    {
      "$ref": "#/components/schemas/MembershipDtoV1"
    }
  ],
  "name": "Cool Company",
  "subdomain": {
    "$ref": "#/components/schemas/WorkspaceSubdomainDtoV1"
  },
  "workspaceSettings": {
    "$ref": "#/components/schemas/WorkspaceSettingsDtoV1"
  }
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)