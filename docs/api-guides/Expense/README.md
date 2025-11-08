# Expense API

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
| GET | `/v1/workspaces/{workspaceId}/expenses` | [getExpenses.md](getExpenses.md) |
| POST | `/v1/workspaces/{workspaceId}/expenses` | [createExpense.md](createExpense.md) |
| GET | `/v1/workspaces/{workspaceId}/expenses/categories` | [getCategories.md](getCategories.md) |
| POST | `/v1/workspaces/{workspaceId}/expenses/categories` | [createExpenseCategory.md](createExpenseCategory.md) |
| DELETE | `/v1/workspaces/{workspaceId}/expenses/categories/{categoryId}` | [deleteCategory.md](deleteCategory.md) |
| PUT | `/v1/workspaces/{workspaceId}/expenses/categories/{categoryId}` | [updateCategory.md](updateCategory.md) |
| PATCH | `/v1/workspaces/{workspaceId}/expenses/categories/{categoryId}/status` | [updateExpenseCategoryStatus.md](updateExpenseCategoryStatus.md) |
| DELETE | `/v1/workspaces/{workspaceId}/expenses/{expenseId}` | [deleteExpense.md](deleteExpense.md) |
| GET | `/v1/workspaces/{workspaceId}/expenses/{expenseId}` | [getExpense.md](getExpense.md) |
| PUT | `/v1/workspaces/{workspaceId}/expenses/{expenseId}` | [updateExpense.md](updateExpense.md) |
| GET | `/v1/workspaces/{workspaceId}/expenses/{expenseId}/files/{fileId}` | [downloadFile.md](downloadFile.md) |

## Common query parameters
- `archived`
- `name`
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `user-id`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.
