## POST /v1/workspaces/{workspaceId}/webhooks/{webhookId}/logs
**Summary:** Get logs for a webhook

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents a workspace identifier across the system. |
| `webhookId` | path | string | Yes |  | Represents a webhook identifier across the system. |

### Query parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `page` | query | integer | No | `0` | Page number. |
| `size` | query | integer | No | `50` | Page size. |

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `from` (string, optional) Represents date and time in yyyy-MM-ddThh:mm:ssZ format. If provided, results will include logs which occurred after this value.
- `sortByNewest` (boolean, optional) If set to true, logs will be sorted with most recent first.
- `status` (string, optional) Filters logs by status.
- `to` (string, optional) Represents date and time in yyyy-MM-ddThh:mm:ssZ format. If provided, results will include logs which occurred before this value.
- **Minimal example:**
```json
{
  "from": "2023-02-01T13:00:46Z",
  "sortByNewest": false,
  "status": "ALL",
  "to": "2023-02-05T13:00:46Z"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}/logs" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"from":"2023-02-01T13:00:46Z","sortByNewest":false,"status":"ALL","to":"2023-02-05T13:00:46Z"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}/logs', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}/logs'
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
#### Status 200
- Media type: `application/json`
- Description: OK
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/getLogsForWebhook-200.json`
```json
[
  {
    "$ref": "#/components/schemas/WebhookLogDtoV1"
  }
]
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)