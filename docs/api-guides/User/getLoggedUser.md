## GET /v1/user
**Summary:** Get currently logged-in user's info

### Path parameters
No parameters.

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `include-memberships` | query | boolean | No |  | If set to true, memberships will be included. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/user" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/user', {
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

url = 'https://developer.clockify.me/v1/user'
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
- Artifact: `scripts/api-docs-runner/artifacts/getLoggedUser-200.json`
```json
{
  "activeWorkspace": "64a687e29ae1f428e7ebe303",
  "customFields": [
    {
      "$ref": "#/components/schemas/UserCustomFieldValueDtoV1"
    }
  ],
  "defaultWorkspace": "64a687e29ae1f428e7ebe303",
  "email": "johndoe@example.com",
  "id": "5a0ab5acb07987125438b60f",
  "memberships": [
    {
      "$ref": "#/components/schemas/MembershipDtoV1"
    }
  ],
  "name": "John Doe",
  "profilePicture": "https://www.url.com/profile-picture1234567890.png",
  "settings": {
    "$ref": "#/components/schemas/UserSettingsDtoV1"
  },
  "status": {
    "$ref": "#/components/schemas/AccountStatus"
  }
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)