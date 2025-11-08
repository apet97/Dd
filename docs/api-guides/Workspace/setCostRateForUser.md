## PUT /v1/workspaces/{workspaceId}/users/{userId}/cost-rate
**Summary:** Update user's cost rate

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `userId` | path | string | Yes |  | Represents user identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `amount` (integer, required) Represents an amount as integer.
- `since` (string, optional) Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.
- **Minimal example:**
```json
{
  "amount": 20000,
  "since": "2020-01-01T00:00:00Z"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/cost-rate" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"amount":20000,"since":"2020-01-01T00:00:00Z"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/cost-rate', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/users/{userId}/cost-rate'
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
- Artifact: `scripts/api-docs-runner/artifacts/setCostRateForUser-200.json`
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