## PATCH /v1/workspaces/{workspaceId}/member-profile/{userId}
**Summary:** Update member's profile

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
- `imageUrl` (string, optional) Represents an image url. A field that can only be updated for limited users.
- `name` (string, optional) This body field is deprecated and can only be updated for limited users. Represents name of the user and can be changed on the CAKE.com Account profile page.
- `removeProfileImage` (boolean, optional) Indicates whether to remove profile image or not. A field that can only be updated for limited users.
- `userCustomFields` (array, optional) Represents a list of upsert user custom field objects.
- `weekStart` (string, optional) Represents a day of the week.
- `workCapacity` (string, optional) Represents work capacity as a time duration in the ISO-8601 format. For example, for a 7hr work day, input should be PT7H.
- `workingDays` (string, optional) Represents a list of days of the week.
- **Minimal example:**
```json
{
  "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
  "name": "John Doe",
  "removeProfileImage": false,
  "userCustomFields": [
    {
      "$ref": "#/components/schemas/UpsertUserCustomFieldRequest"
    }
  ],
  "weekStart": "MONDAY",
  "workCapacity": "PT7H",
  "workingDays": "[\"MONDAY\",\"TUESDAY\",\"WEDNESDAY\",\"THURSDAY\",\"FRIDAY\"]"
}
```

### Code examples
```bash
curl -X PATCH "https://developer.clockify.me/v1/workspaces/{workspaceId}/member-profile/{userId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"imageUrl":"https://www.url.com/imageurl-1234567890.jpg","name":"John Doe","removeProfileImage":false,"userCustomFields":[{"$ref":"#/components/schemas/UpsertUserCustomFieldRequest"}],"weekStart":"MONDAY","workCapacity":"PT7H","workingDays":"[\"MONDAY\",\"TUESDAY\",\"WEDNESDAY\",\"THURSDAY\",\"FRIDAY\"]"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/member-profile/{userId}', {
  method: 'PATCH',
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/member-profile/{userId}'
headers = {
    'X-Api-Key': os.environ['CLOCKIFY_API_KEY'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
payload = {/* TODO: provide payload */}
response = requests.patch(url, headers=headers, json=payload)
response.raise_for_status()
print(response.json())
```

### Success responses
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/updateMemberProfileWithAdditionalData-200.json`
```json
{
  "email": "johndoe@example.com",
  "hasPassword": false,
  "hasPendingApprovalRequest": false,
  "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
  "name": "John Doe",
  "userCustomFieldValues": [
    {
      "$ref": "#/components/schemas/UserCustomFieldValueFullDtoV1"
    }
  ],
  "weekStart": "MONDAY",
  "workCapacity": "PT7H",
  "workingDays": "[\"MONDAY\",\"TUESDAY\",\"WEDNESDAY\",\"THURSDAY\",\"FRIDAY\"]",
  "workspaceNumber": 3
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)