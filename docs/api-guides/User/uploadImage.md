## POST /v1/file/image
**Summary:** Add photo

### Path parameters
No parameters.

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `multipart/form-data`
- **Required:** No
- **Schema summary:**
- `file` (string, required) Image to be uploaded
- **Minimal example:**
```json
{
  "file": "string"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/file/image" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"file":"string"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/file/image', {
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

url = 'https://developer.clockify.me/v1/file/image'
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
- Artifact: `scripts/api-docs-runner/artifacts/uploadImage-200.json`
```json
{
  "name": "image-01234567.jpg",
  "url": "https://clockify.com/image-01234567.jpg"
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)