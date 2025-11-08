## GET /v1/workspaces/{workspaceId}/invoices/{invoiceId}
**Summary:** Get invoice by ID

### Path parameters
| Name | In | Type | Required | Default | Description |
|------|----|------|----------|---------|-------------|
| `workspaceId` | path | string | Yes |  | Represents workspace identifier across the system. |
| `invoiceId` | path | string | Yes |  | Represents invoice identifier across the system. |

### Query parameters
No parameters.

### Header parameters
No parameters.

### Request body
This operation does not accept a request body.

### Code examples
```bash
curl -X GET "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}'
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
- Artifact: `scripts/api-docs-runner/artifacts/getInvoice-200.json`
```json
{
  "amount": 100,
  "balance": 50,
  "billFrom": "Business X",
  "calculationType": {
    "$ref": "#/components/schemas/CalculationType"
  },
  "clientAddress": "Ground Floor, ABC Bldg., Palo Alto, California, USA 94020",
  "clientId": "98h687e29ae1f428e7ebe707",
  "clientName": "Client X",
  "companyId": "04g687e29ae1f428e7ebe123",
  "containsImportedExpenses": false,
  "containsImportedTimes": false,
  "currency": "USD",
  "discount": 10.5,
  "discountAmount": 11,
  "dueDate": "2020-06-01T08:00:00Z",
  "id": "78a687e29ae1f428e7ebe303",
  "issuedDate": "2020-01-01T08:00:00Z",
  "items": [
    {
      "$ref": "#/components/schemas/InvoiceItemDto"
    }
  ],
  "note": "This is a sample note for this invoice.",
  "number": "202306121129",
  "paid": 50,
  "status": "PAID",
  "subject": "January salary",
  "subtotal": 5000,
  "tax": 1.5,
  "tax2": 0,
  "tax2Amount": 0,
  "taxAmount": 1,
  "taxType": {
    "$ref": "#/components/schemas/TaxType"
  },
  "userId": "12t687e29ae1f428e7ebe202",
  "visibleZeroFields": {
    "$ref": "#/components/schemas/VisibleZeroFieldsInvoice"
  }
}
```

### Error responses
No error responses documented in the spec.

### Notes
- Servers declared in spec: /api, /pto

[Back to section](README.md) · [Back to index](../index.md)