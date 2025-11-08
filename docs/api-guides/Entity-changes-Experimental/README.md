# Entity changes (Experimental) API

**Summary:** For use case see [Entity Changes Use Cases](#tag/Entity-Changes-Use-Cases)

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
| GET | `/v1/workspaces/{workspaceId}/entities/created` | [getCreatedEntityInfo.md](getCreatedEntityInfo.md) |
| GET | `/v1/workspaces/{workspaceId}/entities/deleted` | [getDeletedEntityInfo.md](getDeletedEntityInfo.md) |
| GET | `/v1/workspaces/{workspaceId}/entities/updated` | [getUpdatedEntityInfo.md](getUpdatedEntityInfo.md) |

## Common query parameters
- `end`
- `limit`
- `page`
- `start`
- `type`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.
