## POST /v1/workspaces/{workspaceId}/invoices/info
**Summary:** Filter out invoices

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `clients` (ref: #/components/schemas/ContainsArchivedFilterRequest, optional) 
- `companies` (ref: #/components/schemas/BaseFilterRequest, optional) 
- `exactAmount` (integer, optional) Represents an invoice amount. If provided, you'll get a filtered list of invoices that has the equal amount as specified.
- `exactBalance` (integer, optional) Represents an invoice balance. If provided, you'll get a filtered list of invoices that has the equal balance as specified.
- `greaterThanAmount` (integer, optional) Represents an invoice amount. If provided, you'll get a filtered list of invoices that has amount greater than specified.
- `greaterThanBalance` (integer, optional) Represents an invoice balance. If provided, you'll get a filtered list of invoices that has balance greater than specified.
- `invoiceNumber` (string, optional) If provided, you'll get a filtered list of invoices that contain the provided string in their invoice number.
- `issueDate` (ref: #/components/schemas/TimeRangeRequestDtoV1, optional) 
- `lessThanAmount` (integer, optional) Represents an invoice amount. If provided, you'll get a filtered list of invoices that has amount less than specified.
- `lessThanBalance` (integer, optional) Represents an invoice balance. If provided, you'll get a filtered list of invoices that has balance less than specified.
- `page` (integer, required) Page number.
- `pageSize` (integer, required) Page size.
- `sortColumn` (string, optional) Represents the column name to be used as sorting criteria.
- `sortOrder` (string, optional) Represents the sorting order.
- `statuses` (array, optional) Represents a list of invoice statuses. If provided, you'll get a filtered list of invoices that matches any of the invoice status provided.
- `strictSearch` (boolean, optional) Flag to toggle on/off strict search mode. When set to true, search by invoice number only will return invoices whose number exactly matches the string value given for the 'invoiceNumber' parameter. When set to false, results will also include invoices whose number contain the string value, but could be longer than the string value itself. For example, if there is an invoice with the number '123456', and the search value is '123', setting strict-name-search to true will not return that invoice in the results, whereas setting it to false will.
- **Minimal example:**
```json
{
  "clients": {
    "$ref": "#/components/schemas/ContainsArchivedFilterRequest"
  },
  "companies": {
    "$ref": "#/components/schemas/BaseFilterRequest"
  },
  "exactAmount": 1000,
  "exactBalance": 1000,
  "greaterThanAmount": 500,
  "greaterThanBalance": 500,
  "invoiceNumber": "Invoice-01",
  "issueDate": {
    "$ref": "#/components/schemas/TimeRangeRequestDtoV1"
  },
  "lessThanAmount": 500,
  "lessThanBalance": 500,
  "page": 1,
  "pageSize": 50,
  "sortColumn": "ID",
  "sortOrder": "ASCENDING",
  "statuses": [
    "SENT",
    "PAID",
    "PARTIALLY_PAID"
  ],
  "strictSearch": false
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/info" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"clients":{"$ref":"#/components/schemas/ContainsArchivedFilterRequest"},"companies":{"$ref":"#/components/schemas/BaseFilterRequest"},"exactAmount":1000,"exactBalance":1000,"greaterThanAmount":500,"greaterThanBalance":500,"invoiceNumber":"Invoice-01","issueDate":{"$ref":"#/components/schemas/TimeRangeRequestDtoV1"},"lessThanAmount":500,"lessThanBalance":500,"page":1,"pageSize":50,"sortColumn":"ID","sortOrder":"ASCENDING","statuses":["SENT","PAID","PARTIALLY_PAID"],"strictSearch":false}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/info', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/info'
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
- Artifact: `scripts/api-docs-runner/artifacts/getInvoicesInfo-200.json`
```json
{
  "invoices": [
    {
      "$ref": "#/components/schemas/InvoiceInfoV1"
    }
  ],
  "total": 100
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)