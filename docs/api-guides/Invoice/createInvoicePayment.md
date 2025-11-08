## POST /v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments
**Summary:** Add payment to invoice

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
- **Media type:** `application/json`
- **Required:** Yes
- **Schema summary:**
- `amount` (integer, optional) Represents an invoice payment amount as long.
- `note` (string, optional) Represents an invoice payment note.
- `paymentDate` (string, optional) Represents an invoice payment date in yyyy-MM-ddThh:mm:ssZ format.
- **Minimal example:**
```json
{
  "amount": 100,
  "note": "This is a sample note for this invoice payment.",
  "paymentDate": "2021-01-01T12:00:00Z"
}
```

### Code examples
```bash
curl -X POST "https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments" \
  -H 'X-Api-Key: <YOUR_API_KEY>' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
  -d '{"amount":100,"note":"This is a sample note for this invoice payment.","paymentDate":"2021-01-01T12:00:00Z"}'
```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments', {
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

url = 'https://developer.clockify.me/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments'
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
#### Status 201
- Media type: `application/json`
- Description: Created
- Captured example: Not executed in sandbox yet.
- Artifact: `scripts/api-docs-runner/artifacts/createInvoicePayment-201.json`
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