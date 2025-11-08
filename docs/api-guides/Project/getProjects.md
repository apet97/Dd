## GET /v1/workspaces/{workspaceId}/projects
**Summary:** Get all projects on workspace

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `name` | query | string | No |  | If provided, you'll get a filtered list of projects that contains the provided string in the project name. |
| `strict-name-search` | query | boolean | No |  | Flag to toggle on/off strict search mode. When set to true, search by name will only return projects whose name exactly matches the string value given for the 'name' parameter. When set to false, results will also include projects whose name contain the string value, but could be longer than the string value itself. For example, if there is a project with the name 'applications', and the search value is 'app', setting strict-name-search to true will not return that project in the results, whereas setting it to false will. |
| `archived` | query | boolean | No |  | If provided and set to true, you'll only get archived projects. If omitted, you'll get both archived and non-archived projects. |
| `billable` | query | boolean | No |  | If provided and set to true, you'll only get billable projects. If omitted, you'll get both billable and non-billable projects. |
| `clients` | query | array | No |  | If provided, you'll get a filtered list of projects that contain clients which match any of the provided ids. |
| `contains-client` | query | boolean | No | `True` | If set to true, you'll get a filtered list of projects that contain clients which match the provided id(s) in 'clients' field. If set to false, you'll get a filtered list of projects which do NOT contain clients that match the provided id(s) in 'clients' field. |
| `client-status` | query | string | No |  | Filters projects based on client status provided. |
| `users` | query | array | No |  | If provided, you'll get a filtered list of projects that contain users which match any of the provided ids. |
| `contains-user` | query | boolean | No | `True` | If set to true, you'll get a filtered list of projects that contain users which match the provided id(s) in 'users' field. If set to false, you'll get a filtered list of projects which do NOT contain users which match the provided id(s) in 'users' field. |
| `user-status` | query | string | No |  | Filters projects based on user status provided. |
| `is-template` | query | boolean | No |  | Filters projects based on whether they are used as a template or not. |
| `sort-column` | query | string | No |  | Sorts the results by the given column/field. |
| `sort-order` | query | string | No |  | Sorting mode. |
| `hydrated` | query | boolean | No | `False` | If set to true, results will contain additional information about the project. |
| `page` | query | integer | No | `1` | Page number. |
| `page-size` | query | integer | No | `50` | Page size. |
| `access` | query | string | No |  | Valid set of string(s). If provided, you'll get a filtered list of projects that matches the provided access. |
| `expense-limit` | query | integer | No | `20` | Represents maximum number of expenses to fetch. |
| `expense-date` | query | string | No |  | If provided, you will get expenses dated before the provided value in yyyy-MM-dd format. |
| `userGroups` | query | array | No |  | If provided, you'll get a filtered list of projects that contain groups which match any of the provided ids. |
| `contains-group` | query | boolean | No | `True` | If set to true, you'll get a filtered list of projects that contain groups which match the provided id(s) in 'userGroups' field. If set to false, you'll get a filtered list of projects which do NOT contain groups which match the provided id(s) in 'userGroups' field. |

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/projects" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/projects', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/projects'
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
- Artifact: `scripts/api-docs-runner/artifacts/getProjects-200.json`
```json
[
  {
    "$ref": "#/components/schemas/ProjectDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)