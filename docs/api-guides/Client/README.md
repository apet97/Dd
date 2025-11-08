# Client API

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
| GET | `/v1/workspaces/{workspaceId}/clients` | [getClients.md](getClients.md) |
| POST | `/v1/workspaces/{workspaceId}/clients` | [createClient.md](createClient.md) |
| DELETE | `/v1/workspaces/{workspaceId}/clients/{id}` | [deleteClient.md](deleteClient.md) |
| GET | `/v1/workspaces/{workspaceId}/clients/{id}` | [getClient.md](getClient.md) |
| PUT | `/v1/workspaces/{workspaceId}/clients/{id}` | [updateClient.md](updateClient.md) |

## Common query parameters
- `archive-projects`
- `archived`
- `mark-tasks-as-done`
- `name`
- `page`
- `page-size`
- `sort-column`
- `sort-order`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.
