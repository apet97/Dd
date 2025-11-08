## GET /v1/workspaces/{workspaceId}/tags
**Summary:** Find tags on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `name` | query | string | No |  | If provided, you'll get a filtered list of tags that matches the provided string in their name. |
| `strict-name-search` | query | boolean | No |  | Flag to toggle on/off strict search mode. When set to true, search by name will only return tags whose name exactly matches the string value given for the 'name' parameter. When set to false, results will also include tags whose name contain the string value, but could be longer than the string value itself. For example, if there is a tag with the name 'applications', and the search value is 'app', setting strict-name-search to true will not return that tag in the results, whereas setting it to false will. |
| `excluded-ids` | query | string | No |  | Represents a list of excluded ids |
| `sort-column` | query | string | No |  | Represents column to be used as sorting criteria. |
| `sort-order` | query | string | No |  | Represents sorting mode. |
| `page` | query | integer | No | `1` | Page number. |
| `page-size` | query | integer | No | `50` | Page size. |
| `archived` | query | boolean | No |  | Filters the result whether tags are archived or not. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/tags" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/tags', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/tags'
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
- Artifact: `scripts/api-docs-runner/artifacts/getTags-200.json`
```json
[
  {
    "$ref": "#/components/schemas/TagDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)