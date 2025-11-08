## PUT /v1/workspaces/{workspaceId}/webhooks/{webhookId}
**Summary:** Update a webhook

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
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `name` (string, optional) Represents a webhook name.
- `triggerSource` (array, required) Represents a list of trigger sources.
- `triggerSourceType` (string, required) Represents a webhook event trigger source type.
- `url` (string, required) Represents a workspace identifier across the system.
- `webhookEvent` (string, required) Represents a webhook event type.
- **Minimal example:**
```json
{
  "name": "Stripe",
  "triggerSource": [
    "54a687e29ae1f428e7ebe909",
    "87p187e29ae1f428e7ebej56"
  ],
  "triggerSourceType": "PROJECT_ID",
  "url": "https://example-clockify.com/stripeEndpoint",
  "webhookEvent": "NEW_PROJECT"
}
```

### Code examples
```bash
curl -X PUT "https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"name":"Stripe","triggerSource":["54a687e29ae1f428e7ebe909","87p187e29ae1f428e7ebej56"],"triggerSourceType":"PROJECT_ID","url":"https://example-clockify.com/stripeEndpoint","webhookEvent":"NEW_PROJECT"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/webhooks/{webhookId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/updateWebhook-200.json`
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