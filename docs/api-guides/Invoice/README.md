# Invoice API

**Summary:** 

- **Base URL (sandbox):** https://developer.clockify.me
- **Authentication:**
  ```
  X-Api-Key: <YOUR_API_KEY>
  Accept: application/json
  Content-Type: application/json
  ```
- **Entity identifiers:**
- Workspace ID
- Resource IDs as described per operation
- **Prerequisites:** The automated runner has not yet provisioned fixtures. Future runs should create DOCS_TEST_* resources as needed.

## Operations
| Method | Path | Operation |
|--------|------|-----------|
| GET | `/v1/workspaces/{workspaceId}/invoices` | [getInvoices.md](getInvoices.md) |
| POST | `/v1/workspaces/{workspaceId}/invoices` | [createInvoice.md](createInvoice.md) |
| POST | `/v1/workspaces/{workspaceId}/invoices/info` | [getInvoicesInfo.md](getInvoicesInfo.md) |
| GET | `/v1/workspaces/{workspaceId}/invoices/settings` | [getInvoiceSettings.md](getInvoiceSettings.md) |
| PUT | `/v1/workspaces/{workspaceId}/invoices/settings` | [updateInvoiceSettings.md](updateInvoiceSettings.md) |
| DELETE | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}` | [deleteInvoice.md](deleteInvoice.md) |
| GET | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}` | [getInvoice.md](getInvoice.md) |
| PUT | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}` | [updateInvoice.md](updateInvoice.md) |
| POST | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/duplicate` | [duplicateInvoice.md](duplicateInvoice.md) |
| GET | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/export` | [exportInvoice.md](exportInvoice.md) |
| GET | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments` | [getPaymentsForInvoice.md](getPaymentsForInvoice.md) |
| POST | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments` | [createInvoicePayment.md](createInvoicePayment.md) |
| DELETE | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/payments/{paymentId}` | [deletePaymentById.md](deletePaymentById.md) |
| PATCH | `/v1/workspaces/{workspaceId}/invoices/{invoiceId}/status` | [changeInvoiceStatus.md](changeInvoiceStatus.md) |

## Common query parameters
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `statuses`
- `userLocale`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.
