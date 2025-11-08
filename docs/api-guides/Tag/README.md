# Tag API

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
| GET | `/v1/workspaces/{workspaceId}/tags` | [getTags.md](getTags.md) |
| POST | `/v1/workspaces/{workspaceId}/tags` | [createNewTag.md](createNewTag.md) |
| DELETE | `/v1/workspaces/{workspaceId}/tags/{id}` | [deleteTag.md](deleteTag.md) |
| GET | `/v1/workspaces/{workspaceId}/tags/{id}` | [getTag.md](getTag.md) |
| PUT | `/v1/workspaces/{workspaceId}/tags/{id}` | [updateTag.md](updateTag.md) |

## Common query parameters
- `archived`
- `excluded-ids`
- `name`
- `page`
- `page-size`
- `sort-column`
- `sort-order`
- `strict-name-search`

## Error reference
No shared error patterns documented yet.

## Cleanup policy
The runner tracks all DOCS_TEST_* resources it would create and would delete them when cleanup is implemented.
