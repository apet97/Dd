## GET /v1/workspaces/{workspaceId}/webhooks/{webhookId}
**Summary:** Get a specific webhook by id

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents a workspace identifier across the system. |
| `webhookId` | path | string | Yes |  | Represents a webhook identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/getWebhook-200.json`
```json
{
  "authToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2NGI3YmU3YmUwODM1Yjc2ZDYzOTY5YTciLCJtdWx0aUZhY3RvciI6dHJ1ZSwiaXNzIjoiY2xvY2tpZnkiLCJuYW1lIjoiTWFydGluIExsb3lkIiwiZXhwIjoxNjkzMzY5MzEwLCJ0eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjkzMzI2MTEwLCJqdGkiOiJZVGcxT0Raak9XTXRPRGRsWVMwME5qZ3hMVGxpTlRndE5UQmlOVEprTmpOaE",
  "enabled": false,
  "id": "76a687e29ae1f428e7ebe101",
  "name": "stripe",
  "triggerSource": [
    "54a687e29ae1f428e7ebe909",
    "87p187e29ae1f428e7ebej56"
  ],
  "triggerSourceType": {
    "$ref": "#/components/schemas/WebhookEventTriggerSourceType"
  },
  "url": "https://example-clockify.com/stripeEndpoint",
  "userId": "5a0ab5acb07987125438b60f",
  "webhookEvent": {
    "$ref": "#/components/schemas/WebhookEventType"
  },
  "workspaceId": "64a687e29ae1f428e7ebe303"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)